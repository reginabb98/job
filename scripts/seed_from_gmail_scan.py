"""
One-time seed of the applications table from a manual Gmail scan.

This reflects the results of scanning rbarrerababb@sva.edu on 2026-08-13 for
job-application activity (thread searches for application/interview/offer/
rejection language and common ATS senders like Greenhouse, Lever, Workday,
iCIMS, Taleo, SmartRecruiters, Ashby, LinkedIn). No corporate ATS emails were
found in that inbox at scan time -- these three threads were the only
genuine position leads. Run again with `python scripts/seed_from_gmail_scan.py`
only if the applications table is empty; it will not create duplicates on
repeat runs.
"""
import os
import sqlite3
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tracker.db")

SEED_ROWS = [
    {
        "company": "SVA Library",
        "position": "Library Position",
        "status": "Rejected",
        "applied_date": "2025-08-04",
        "next_step": None,
        "job_url": None,
        "source": "Email",
        "referral": 0,
        "notes": "Interviewed on Zoom with Mark Roussel. Rejected 2025-08-04: "
                 "\"we've decided to move forward with other candidates\". "
                 "Invited to reapply when the department hires again.",
    },
    {
        "company": "Creative Putty (Bret Sanford)",
        "position": "TA - Business of Branding",
        "status": "Applied",
        "applied_date": "2026-06-16",
        "next_step": "Awaiting response",
        "job_url": None,
        "source": "Email",
        "referral": 0,
        "notes": "Applied via email 2026-06-16. As of 2026-07-02 still waiting "
                 "to hear back once TA budget is finalized.",
    },
    {
        "company": "Pop&Op (Sem Devillart)",
        "position": "TA Position",
        "status": "Applied",
        "applied_date": "2026-05-21",
        "next_step": "Awaiting response",
        "job_url": None,
        "source": "Email",
        "referral": 0,
        "notes": "Applied via email 2026-05-21. As of 2026-06-01 no definitive "
                 "answer yet; another candidate (AJ) also being considered.",
    },
]


def main():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    existing = db.execute("SELECT COUNT(*) AS n FROM applications").fetchone()["n"]
    if existing:
        print(f"applications table already has {existing} rows; skipping seed.")
        return

    now = datetime.utcnow().isoformat()
    for row in SEED_ROWS:
        db.execute(
            """
            INSERT INTO applications
                (company, position, status, applied_date, next_step, job_url, source, referral, notes, created_at, updated_at)
            VALUES (:company, :position, :status, :applied_date, :next_step, :job_url, :source, :referral, :notes, :created_at, :updated_at)
            """,
            {**row, "created_at": now, "updated_at": now},
        )
    db.commit()
    print(f"Seeded {len(SEED_ROWS)} applications from the Gmail scan.")


if __name__ == "__main__":
    main()
