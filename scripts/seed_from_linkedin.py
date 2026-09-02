"""
Seed of additional applications pasted directly from LinkedIn's "My Jobs >
Applied" list (screenshots pasted to Claude in chat on 2026-08-17), since
LinkedIn offers no export or API for that list -- see the "Paste-and-parse"
workflow in the README.

Reconciled against the Gmail-derived seed in seed_from_gmail_scan.py: rows
that clearly matched an existing application (by company, and a title that
was previously just "Unspecified role" or a truncated email subject) were
used to fill in the real title over there instead of being duplicated here.
These are the rows that didn't match anything already tracked.

Two LinkedIn-only signals to note:
  - "No longer accepting applications" is a posting-lifecycle flag (the
    listing was taken down) -- it says nothing about whether a response was
    received, so it is never treated as a rejection here.
  - LinkedIn only gives relative dates ("Applied 3w ago"), so applied_date
    below is estimated from that offset relative to 2026-08-17, not exact.

Run `python scripts/seed_from_linkedin.py` any time; each row is only
inserted if a matching (company, position) pair isn't already present.
"""
import os
import sqlite3
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tracker.db")

NEW_ROWS = [
    {
        "company": "Publicis Health",
        "position": "Senior Strategist",
        "status": "Applied",
        "applied_date": "2026-08-03",
        "source": "LinkedIn",
        "notes": "Hybrid, New York, NY. Applied date estimated from LinkedIn's \"Applied 2w ago\" "
                 "(as of 2026-08-17), not exact.",
    },
    {
        "company": "G&A Strategy and Design",
        "position": "Brand Strategist, Planning",
        "status": "Applied",
        "applied_date": "2026-08-03",
        "source": "LinkedIn",
        "notes": "Remote, United States. Posting no longer accepting applications. Applied date "
                 "estimated from LinkedIn's \"Applied 2w ago\" (as of 2026-08-17), not exact.",
    },
    {
        "company": "Synthesis",
        "position": "Senior Foresight Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Hybrid, Brooklyn, NY. Posting no longer accepting applications. Applied date "
                 "estimated from LinkedIn's \"Applied 3w ago\" (as of 2026-08-17), not exact.",
    },
    {
        "company": "Synthesis",
        "position": "Senior Cultural Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Hybrid, Brooklyn, NY. Posting no longer accepting applications. Distinct role from "
                 "the Senior Foresight Strategist application at the same company. Applied date "
                 "estimated from LinkedIn's \"Applied 3w ago\" (as of 2026-08-17), not exact.",
    },
    {
        "company": "Publicis Media",
        "position": "Senior Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Remote, New York, NY. Posting no longer accepting applications. Applied date "
                 "estimated from LinkedIn's \"Applied 3w ago\" (as of 2026-08-17), not exact.",
    },
    {
        "company": "Publicis Media",
        "position": "Associate - New York City",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "On-site, New York, NY. Reposted 5d ago as of 2026-08-17. Distinct role from the "
                 "Senior Creative Strategist application at the same company. Applied date estimated "
                 "from LinkedIn's \"Applied 3w ago,\" not exact.",
    },
    {
        "company": "Accenture",
        "position": "Creative Agency Senior Designer",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "New York, NY. Posting no longer accepting applications. Distinct from the "
                 "Accenture (Droga5) Senior Strategist application, which was rejected. Applied date "
                 "estimated from LinkedIn's \"Applied 3w ago\" (as of 2026-08-17), not exact.",
    },
    {
        "company": "Reddit",
        "position": "Creative Strategist - App Dev",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Hybrid, New York, NY. Reposted 6d ago as of 2026-08-17. Applied date estimated "
                 "from LinkedIn's \"Applied 3w ago,\" not exact.",
    },
    {
        "company": "Moon Juice",
        "position": "Brand & Content Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Remote, United States. Posting no longer accepting applications. Applied date "
                 "estimated from LinkedIn's \"Applied 3w ago\" (as of 2026-08-17), not exact.",
    },
    {
        "company": "Interbrand",
        "position": "Senior Designer",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Hybrid, New York City Metropolitan Area. Posting no longer accepting applications. "
                 "Third distinct Interbrand application alongside the Verbal Identity Fellow and "
                 "general-interest ones already tracked. Applied date estimated from LinkedIn's "
                 "\"Applied 3w ago,\" not exact.",
    },
    {
        "company": "Reddit",
        "position": "Creative Strategist - Finance",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Hybrid, New York, NY. Posting no longer accepting applications. Distinct role from "
                 "the Creative Strategist - App Dev application at the same company. Applied date "
                 "estimated from LinkedIn's \"Applied 3w ago\" (as of 2026-08-17), not exact.",
    },
    {
        "company": "Noom",
        "position": "Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "New York, NY. Applied date estimated from LinkedIn's \"Applied 3w ago\" (as of "
                 "2026-08-17), not exact.",
    },
    {
        "company": "UNIQLO",
        "position": "Product Marketing Manager",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Hybrid, New York City Metropolitan Area. Reposted 3w ago as of 2026-08-17. Marked "
                 "\"haven't heard back\" in LinkedIn's own follow-up tracker -- still pending, not a "
                 "rejection. Applied date estimated, not exact.",
    },
    {
        "company": "Omnicom Media",
        "position": "Senior Associate, Strategy",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Hybrid, New York, NY. \"Application viewed\" per LinkedIn. Posting no longer "
                 "accepting applications. Distinct from the earlier general Omnicom Network "
                 "application. Applied date estimated from LinkedIn's \"Applied 3w ago,\" not exact.",
    },
]


def main():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    now = datetime.utcnow().isoformat()
    inserted = 0
    for row in NEW_ROWS:
        exists = db.execute(
            "SELECT 1 FROM applications WHERE company = ? AND position = ?",
            (row["company"], row["position"]),
        ).fetchone()
        if exists:
            continue
        row.setdefault("next_step", None)
        row.setdefault("job_url", None)
        row.setdefault("referral", 0)
        row.setdefault("pay_range", None)
        row.setdefault("job_description", None)
        row.setdefault("job_fit", None)
        row.setdefault("job_fit_notes", None)
        db.execute(
            """
            INSERT INTO applications
                (company, position, status, applied_date, next_step, job_url, source, referral, notes, pay_range, job_description, job_fit, job_fit_notes, created_at, updated_at)
            VALUES (:company, :position, :status, :applied_date, :next_step, :job_url, :source, :referral, :notes, :pay_range, :job_description, :job_fit, :job_fit_notes, :created_at, :updated_at)
            """,
            {**row, "created_at": now, "updated_at": now},
        )
        inserted += 1
    db.commit()
    print(f"Inserted {inserted} new LinkedIn-sourced applications ({len(NEW_ROWS) - inserted} already present).")


if __name__ == "__main__":
    main()
