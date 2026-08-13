"""
One-time seed of the applications table from a manual Gmail scan.

This reflects a scan of reginabb98@gmail.com on 2026-08-13 for job-application
activity: ATS confirmation/status emails (Greenhouse, Lever, Ashby, Workday,
iCIMS, Workable, Teamtailor) plus explicit rejection/interview language,
covering the last 12 months. TA/teaching-assistant leads were intentionally
excluded per instruction. LinkedIn "job alert" and "jobs similar to" emails
were excluded too since they're recommendations, not applications.

Run `python scripts/seed_from_gmail_scan.py` once against an empty
applications table; it will not create duplicates on repeat runs.
"""
import os
import sqlite3
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tracker.db")

SEED_ROWS = [
    {
        "company": "Accenture (Droga5)",
        "position": "Senior Strategist",
        "status": "Rejected",
        "applied_date": "2026-07-22",
        "next_step": None,
        "source": "Workday",
        "notes": "Applied via Accenture's Workday portal for the Droga5 Senior Strategist role. "
                 "The 2026-08-12 follow-up emails were a bar from reapplying, not a new opportunity -- "
                 "confirmed rejection.",
    },
    {
        "company": "Snapchat",
        "position": "Associate Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-07-22",
        "source": "Workday",
        "notes": None,
    },
    {
        "company": "Mammoth Brands",
        "position": "Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-07-22",
        "source": "Greenhouse",
        "notes": None,
    },
    {
        "company": "The New York Times",
        "position": "Designer, Marketing",
        "status": "Applied",
        "applied_date": "2026-07-22",
        "source": "Email",
        "notes": None,
    },
    {
        "company": "Interbrand",
        "position": "Verbal Identity Fellow",
        "status": "Applied",
        "applied_date": "2026-07-22",
        "source": "Greenhouse",
        "notes": None,
    },
    {
        "company": "Interbrand",
        "position": "General interest (no specific opening listed)",
        "status": "Applied",
        "applied_date": "2026-07-24",
        "source": "Greenhouse",
        "notes": "Separate general-interest application, distinct from the Verbal Identity Fellow role applied to 2026-07-22.",
    },
    {
        "company": "Lippincott",
        "position": "Senior Consultant, Strategy (R_350484)",
        "status": "Applied",
        "applied_date": "2026-07-24",
        "source": "Workday",
        "notes": None,
    },
    {
        "company": "Design Bridge and Partners / Landor (WPP)",
        "position": "Senior Strategist",
        "status": "Interviewing",
        "applied_date": "2026-07-24",
        "next_step": "Interviewed Jul 29, 2PM ET -- awaiting outcome",
        "source": "Greenhouse",
        "notes": "Recruiter Ashley Hill (wppbrandconsulting.com) referenced this role under both the "
                 "Design Bridge and Partners and Landor names -- likely the same WPP process.",
    },
    {
        "company": "JPMorgan Chase & Co.",
        "position": "Unspecified role (Job #210771927)",
        "status": "Applied",
        "applied_date": "2026-07-24",
        "source": "Oracle Recruiting Cloud",
        "notes": "Required an email verification code to complete submission.",
    },
    {
        "company": "Google",
        "position": "Unspecified role",
        "status": "Applied",
        "applied_date": "2026-07-24",
        "source": "Email",
        "notes": "Two near-identical confirmation emails same day -- possibly one application, duplicate notification.",
    },
    {
        "company": "Meta",
        "position": "Creative role (title truncated in email)",
        "status": "Applied",
        "applied_date": "2026-07-25",
        "source": "Email",
        "notes": None,
    },
    {
        "company": "Prophet",
        "position": "Unspecified role",
        "status": "Rejected",
        "applied_date": "2026-07-23",
        "next_step": None,
        "source": "Greenhouse",
        "notes": "2026-07-25: recruiter said they couldn't move forward based on work-authorization/sponsorship "
                 "answers. She replied same day clarifying she's authorized via F-1 OPT -- no response on file yet.",
    },
    {
        "company": "Highsnobiety",
        "position": "Associate Creative",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Teamtailor",
        "notes": None,
    },
    {
        "company": "Instrument",
        "position": "Unspecified role",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Lever",
        "notes": None,
    },
    {
        "company": "Something Special Studios",
        "position": "Senior Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Greenhouse",
        "notes": None,
    },
    {
        "company": "Superside",
        "position": "Lead Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Lever",
        "notes": None,
    },
    {
        "company": "Figma",
        "position": "Designer Advocate, Figma Weave",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Email",
        "notes": None,
    },
    {
        "company": "Buttermilk",
        "position": "Unspecified role",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Teamtailor",
        "notes": None,
    },
    {
        "company": "co:collective",
        "position": "Senior Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Lever",
        "notes": None,
    },
    {
        "company": "Omnicom Network",
        "position": "General network application",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Workday",
        "notes": None,
    },
    {
        "company": "Meta",
        "position": "Brand role (title truncated in email)",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Email",
        "notes": "Distinct from the Meta Creative-role application on 2026-07-25.",
    },
    {
        "company": "Partiful",
        "position": "Unspecified role",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Ashby",
        "notes": None,
    },
    {
        "company": "Wieden+Kennedy",
        "position": "Unspecified role",
        "status": "Applied",
        "applied_date": "2026-07-28",
        "source": "Greenhouse",
        "notes": None,
    },
    {
        "company": "David Protein",
        "position": "Senior Brand Manager",
        "status": "Applied",
        "applied_date": "2026-07-28",
        "source": "Workable",
        "notes": None,
    },
    {
        "company": "AKQA",
        "position": "Freelance Senior Designer (New York)",
        "status": "Rejected",
        "applied_date": "2026-07-28",
        "source": "Email",
        "notes": "Rejected same day: \"we have identified candidates who are more closely aligned with the role.\"",
    },
    {
        "company": "PepsiCo",
        "position": "Design Senior Manager - Immersive (2026-439325)",
        "status": "Applied",
        "applied_date": "2026-07-29",
        "source": "iCIMS",
        "notes": "Already in PepsiCo's talent community from an earlier signup (2026-06-16).",
    },
    {
        "company": "Google",
        "position": "Unspecified role (second application)",
        "status": "Applied",
        "applied_date": "2026-07-29",
        "source": "Email",
        "notes": "Separate confirmation from the 2026-07-24 Google application -- unclear if same or different role.",
    },
    {
        "company": "JPMorgan Chase & Co.",
        "position": "Unspecified role (Job #210768163)",
        "status": "Applied",
        "applied_date": "2026-07-30",
        "source": "Oracle Recruiting Cloud",
        "notes": "Second, distinct JPMorgan application from the one on 2026-07-24.",
    },
    {
        "company": "Prose",
        "position": "Manager of Design, Brand Creative",
        "status": "Rejected",
        "applied_date": "2026-07-28",
        "source": "Ashby",
        "notes": "Rejected 2026-08-03: \"we have decided to move forward with other candidates.\"",
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
        row.setdefault("next_step", None)
        row.setdefault("job_url", None)
        row.setdefault("referral", 0)
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
