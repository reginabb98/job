import csv
import io
import os
import sqlite3
from datetime import datetime, date

from flask import Flask, g, jsonify, render_template, request

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tracker.db")

VALID_STATUSES = ["Applied", "Interviewing", "Offer", "Rejected", "Withdrawn", "Networking"]

app = Flask(__name__)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DB_PATH)
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            position TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Applied',
            applied_date TEXT,
            next_step TEXT,
            job_url TEXT,
            source TEXT,
            referral INTEGER NOT NULL DEFAULT 0,
            notes TEXT,
            pay_range TEXT,
            job_description TEXT,
            job_fit TEXT,
            job_fit_notes TEXT,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        """
    )
    existing_cols = {row[1] for row in db.execute("PRAGMA table_info(applications)")}
    for col in ("pay_range", "job_description", "job_fit", "job_fit_notes"):
        if col not in existing_cols:
            db.execute(f"ALTER TABLE applications ADD COLUMN {col} TEXT")
    db.commit()
    db.close()


def row_to_dict(row):
    d = dict(row)
    d["referral"] = bool(d["referral"])
    return d


def validate_status(status):
    if status not in VALID_STATUSES:
        raise ValueError(f"status must be one of {VALID_STATUSES}")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/applications", methods=["GET"])
def list_applications():
    db = get_db()
    rows = db.execute(
        "SELECT * FROM applications ORDER BY applied_date DESC, id DESC"
    ).fetchall()
    return jsonify([row_to_dict(r) for r in rows])


@app.route("/api/applications", methods=["POST"])
def create_application():
    data = request.get_json(force=True) or {}
    company = (data.get("company") or "").strip()
    position = (data.get("position") or "").strip()
    if not company or not position:
        return jsonify({"error": "company and position are required"}), 400

    status = data.get("status") or "Applied"
    try:
        validate_status(status)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    now = datetime.utcnow().isoformat()
    applied_date = data.get("applied_date") or date.today().isoformat()

    db = get_db()
    cur = db.execute(
        """
        INSERT INTO applications
            (company, position, status, applied_date, next_step, job_url, source, referral, notes, pay_range, job_description, job_fit, job_fit_notes, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            company,
            position,
            status,
            applied_date,
            data.get("next_step"),
            data.get("job_url"),
            data.get("source"),
            1 if data.get("referral") else 0,
            data.get("notes"),
            data.get("pay_range"),
            data.get("job_description"),
            data.get("job_fit"),
            data.get("job_fit_notes"),
            now,
            now,
        ),
    )
    db.commit()
    row = db.execute(
        "SELECT * FROM applications WHERE id = ?", (cur.lastrowid,)
    ).fetchone()
    return jsonify(row_to_dict(row)), 201


@app.route("/api/applications/<int:app_id>", methods=["PUT", "PATCH"])
def update_application(app_id):
    db = get_db()
    row = db.execute("SELECT * FROM applications WHERE id = ?", (app_id,)).fetchone()
    if row is None:
        return jsonify({"error": "not found"}), 404

    data = request.get_json(force=True) or {}
    if "status" in data:
        try:
            validate_status(data["status"])
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    fields = [
        "company",
        "position",
        "status",
        "applied_date",
        "next_step",
        "job_url",
        "source",
        "referral",
        "notes",
        "pay_range",
        "job_description",
        "job_fit",
        "job_fit_notes",
    ]
    updates = {k: data[k] for k in fields if k in data}
    if "referral" in updates:
        updates["referral"] = 1 if updates["referral"] else 0

    if updates:
        set_clause = ", ".join(f"{k} = ?" for k in updates)
        values = list(updates.values()) + [datetime.utcnow().isoformat(), app_id]
        db.execute(
            f"UPDATE applications SET {set_clause}, updated_at = ? WHERE id = ?",
            values,
        )
        db.commit()

    row = db.execute("SELECT * FROM applications WHERE id = ?", (app_id,)).fetchone()
    return jsonify(row_to_dict(row))


@app.route("/api/applications/<int:app_id>", methods=["DELETE"])
def delete_application(app_id):
    db = get_db()
    db.execute("DELETE FROM applications WHERE id = ?", (app_id,))
    db.commit()
    return "", 204


@app.route("/api/stats", methods=["GET"])
def stats():
    db = get_db()
    rows = db.execute("SELECT status, COUNT(*) as n FROM applications GROUP BY status").fetchall()
    by_status = {s: 0 for s in VALID_STATUSES}
    for r in rows:
        by_status[r["status"]] = r["n"]

    total = sum(by_status.values())
    responded = total - by_status.get("Applied", 0)
    response_rate = round((responded / total) * 100, 1) if total else 0.0
    interview_rate = (
        round((by_status.get("Interviewing", 0) + by_status.get("Offer", 0)) / total * 100, 1)
        if total
        else 0.0
    )
    offer_rate = round((by_status.get("Offer", 0) / total) * 100, 1) if total else 0.0

    return jsonify(
        {
            "total": total,
            "by_status": by_status,
            "response_rate": response_rate,
            "interview_rate": interview_rate,
            "offer_rate": offer_rate,
        }
    )


@app.route("/api/import", methods=["POST"])
def import_csv():
    if "file" not in request.files:
        return jsonify({"error": "no file uploaded, expected multipart field 'file'"}), 400

    file = request.files["file"]
    content = file.stream.read().decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(content))

    required = {"company", "position"}
    fieldnames = {(fn or "").strip().lower() for fn in (reader.fieldnames or [])}
    if not required.issubset(fieldnames):
        return (
            jsonify(
                {
                    "error": "CSV must include at least 'company' and 'position' columns. "
                    "Optional columns: status, applied_date, next_step, job_url, source, referral, notes, "
                    "pay_range, job_description, job_fit, job_fit_notes"
                }
            ),
            400,
        )

    db = get_db()
    now = datetime.utcnow().isoformat()
    inserted = 0
    skipped = []
    for i, raw_row in enumerate(reader, start=2):
        row = {(k or "").strip().lower(): (v or "").strip() for k, v in raw_row.items()}
        company = row.get("company", "")
        position = row.get("position", "")
        if not company or not position:
            skipped.append({"line": i, "reason": "missing company or position"})
            continue

        status = row.get("status") or "Applied"
        if status not in VALID_STATUSES:
            status = "Applied"

        db.execute(
            """
            INSERT INTO applications
                (company, position, status, applied_date, next_step, job_url, source, referral, notes, pay_range, job_description, job_fit, job_fit_notes, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                company,
                position,
                status,
                row.get("applied_date") or date.today().isoformat(),
                row.get("next_step") or None,
                row.get("job_url") or None,
                row.get("source") or "LinkedIn",
                1 if row.get("referral", "").lower() in ("1", "true", "yes") else 0,
                row.get("notes") or None,
                row.get("pay_range") or None,
                row.get("job_description") or None,
                row.get("job_fit") or None,
                row.get("job_fit_notes") or None,
                now,
                now,
            ),
        )
        inserted += 1

    db.commit()
    return jsonify({"inserted": inserted, "skipped": skipped})


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5050)
else:
    init_db()
