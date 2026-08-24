"""
Seed of the applications table from periodic Gmail scans.

Covers reginabb98@gmail.com job-application activity: ATS confirmation/status
emails (Greenhouse, Lever, Ashby, Workday, iCIMS, Workable, Teamtailor,
SmartRecruiters, Amazon Jobs) plus explicit rejection/interview language. TA/
teaching-assistant leads are intentionally excluded per instruction, as are
LinkedIn "job alert" and "jobs similar to" emails since they're
recommendations, not applications.

Scan history:
  - 2026-08-13: initial 12-month scan, 29 applications.
  - 2026-08-17 (afternoon): incremental scan since 2026-08-13, 5 new rows.
  - 2026-08-17 (evening): incremental rescan, 2 new rows (Razorfish Health,
    a second PepsiCo application).
  - 2026-08-17 (night): reconciled against a JPMC Candidate Experience
    portal (Oracle HCM) screenshot -- corrected the titles/dates on the two
    existing JPMorgan rows, flipped one to Rejected ("Not Selected"), and
    added a third, new JPMorgan application that had no Gmail confirmation
    at all.
  - 2026-08-18 (early): incremental rescan, 3 new rows (DualEntry, Firefly,
    a second Accenture/Droga5 application distinct from the earlier one).
  - 2026-08-18 (later): reconciled against a screenshot of Google's own
    candidate portal -- flipped both existing Google rows to Rejected
    ("Not proceeding"), filled in real titles for all 3, and added the
    3rd Google application that had no Gmail confirmation at all.
  - 2026-08-18 (night): reconciled against a screenshot of Meta's own
    candidate portal -- confirmed the Creative Strategist NA team
    application's date and corrected its location, flipped the Brand
    Strategist application to Rejected with a corrected applied date, and
    added a 3rd Meta application (Instagram Brand Studio) with no Gmail
    confirmation at all.
  - 2026-08-18 (later still): filled in real titles for Partiful, Inizio
    Evoke, and DualEntry from Regina's own knowledge (not any inbox/portal
    source), and added a Mother networking call reported directly by her --
    the first row to use the new "Networking" status for a contact that
    wasn't a real application (no open role existed to apply to).
  - 2026-08-18 (final): added a second PepsiCo networking contact (Hillary,
    reported directly by Regina, not found via Gmail search) and a second,
    distinct Something Special Studios application -- a direct outreach
    email to a specific strategist there, confirmed via Gmail search,
    separate from the earlier Greenhouse-sourced application.
  - 2026-08-19: incremental rescan, 1 new row (Taskrabbit, title unknown at
    the time).
  - 2026-08-19 (later): reconciled against a LinkedIn My Jobs screenshot --
    filled in Taskrabbit's real title, confirmed Blackstone and Inizio Evoke
    already tracked, added Book of the Month (from a separate LinkedIn Easy
    Apply confirmation, title partly reconstructed) and two new applications
    (Steven Madden, Inside Out Community) whose applied dates and completion
    aren't fully confirmed -- LinkedIn only showed listing repost/post dates
    and a "Did you finish applying?" prompt, not an application date.
  - 2026-08-19 (evening): incremental rescan, 2 new rows (MUBI, Tapestry).
  - 2026-08-20: incremental rescan, no new rows. Flipped the Accenture
    Droga5 Senior Designer application (R00348810) to Rejected.
  - 2026-08-21: incremental rescan, no new rows. Flipped Inizio Evoke's
    Senior Brand Strategist application to Rejected.
  - 2026-08-24: incremental rescan, 1 new row (Amazon, Art Director --
    Elevated Shopping, applied 2026-08-17). This one had been missed by
    every scan since because amazon.jobs wasn't in the ATS domain search
    list; found by widening the search after Regina asked about an
    interview invite. The domain has been added to the search going
    forward.
  - 2026-08-24 (later): Regina reported a Tapestry rejection and forwarded
    a Duel interview invite directly. Flipped Tapestry's Associate,
    External Communications application to Rejected, and added a new Duel
    row (Advocacy Consultant, applied 2026-08-18 per its Teamtailor
    confirmation email) with status Interviewing -- a recruiter reached out
    2026-08-24 to schedule a screen.

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
        "position": "Corporate Brand Marketing - Senior Associate (Job #210771927)",
        "status": "Rejected",
        "applied_date": "2026-07-23",
        "source": "Oracle Recruiting Cloud",
        "notes": "Required an email verification code to complete submission. Title, exact applied date, "
                 "and Rejected status (\"Not Selected\") confirmed 2026-08-17 via JPMC's own Candidate "
                 "Experience portal (Oracle HCM) -- resolves the earlier ambiguity about which of the "
                 "two JPMorgan applications the LinkedIn-listed title belonged to.",
    },
    {
        "company": "Google",
        "position": "Senior Brand Marketing Manager, Global Pixel Retail",
        "status": "Rejected",
        "applied_date": "2026-07-24",
        "source": "Email",
        "notes": "Two near-identical confirmation emails same day -- possibly one application, duplicate "
                 "notification. Google's own candidate portal (checked 2026-08-18) shows all 3 submitted "
                 "Google applications as \"Not proceeding\"; the portal gives no job IDs or exact dates, "
                 "so the specific title-to-application mapping across the 3 Google rows is provisional, "
                 "but the Rejected status is confirmed for all of them.",
    },
    {
        "company": "Meta",
        "position": "Creative Strategist, NA team",
        "status": "Applied",
        "applied_date": "2026-07-25",
        "source": "Email",
        "notes": "Title was truncated in the confirmation email -- filled in from LinkedIn's My Jobs list "
                 "(2026-08-17), which said Boston, MA. Meta's own candidate portal (checked 2026-08-18) "
                 "confirms the exact applied date and says New York, NY instead -- the portal's location "
                 "is treated as authoritative over LinkedIn's. Still active, \"Current stage: Application.\"",
    },
    {
        "company": "Prophet",
        "position": "Senior Creative Strategist",
        "status": "Rejected",
        "applied_date": "2026-07-23",
        "next_step": None,
        "source": "Greenhouse",
        "notes": "2026-07-25: recruiter said they couldn't move forward based on work-authorization/sponsorship "
                 "answers. She replied same day clarifying she's authorized via F-1 OPT -- no response on file yet. "
                 "Title filled in from LinkedIn's My Jobs list (2026-08-17).",
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
        "position": "Senior Creative",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Teamtailor",
        "notes": "Title filled in from LinkedIn's My Jobs list (2026-08-17).",
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
        "position": "Brand Strategist",
        "status": "Rejected",
        "applied_date": "2026-07-23",
        "source": "Email",
        "notes": "Distinct from the Meta Creative-role application on 2026-07-25. Title filled in from "
                 "LinkedIn's My Jobs list (2026-08-17). Meta's own candidate portal (checked 2026-08-18) "
                 "shows this as \"Not moving forward\" and corrects the applied date to 2026-07-23 (the "
                 "original Gmail confirmation had it as 2026-07-27).",
    },
    {
        "company": "Partiful",
        "position": "Opportunistic application (no specific opening)",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Ashby",
        "notes": "Not applying to a listed opening -- reached out opportunistically.",
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
        "position": "Brand Marketing Manager, AI Education Adoption",
        "status": "Rejected",
        "applied_date": "2026-07-29",
        "source": "Email",
        "notes": "Separate confirmation from the 2026-07-24 Google application. Status confirmed "
                 "\"Not proceeding\" via Google's candidate portal (checked 2026-08-18) -- see note on "
                 "the other Google rows re: mapping uncertainty across the 3 Google applications.",
    },
    {
        "company": "JPMorgan Chase & Co.",
        "position": "Olympic & Paralympic Brand Strategist (Job #210768163)",
        "status": "Applied",
        "applied_date": "2026-07-29",
        "source": "Oracle Recruiting Cloud",
        "notes": "Second, distinct JPMorgan application from the one on 2026-07-23. Title and exact "
                 "applied date confirmed 2026-08-17 via JPMC's Candidate Experience portal -- \"Under "
                 "Consideration.\"",
    },
    {
        "company": "Prose",
        "position": "Manager of Design, Brand Creative",
        "status": "Rejected",
        "applied_date": "2026-07-28",
        "source": "Ashby",
        "notes": "Rejected 2026-08-03: \"we have decided to move forward with other candidates.\"",
    },
    # -- 2026-08-17 incremental scan (since 2026-08-13) --
    {
        "company": "OLIVER",
        "position": "Social & Culture Strategist",
        "status": "Rejected",
        "applied_date": "2026-08-14",
        "source": "Email",
        "notes": "Rejection received 2026-08-14: \"skill sets are not exactly aligned with our "
                 "current needs,\" profile kept in talent pool for 24 months. Rejection email did "
                 "not name the role applied to (date shown is the rejection date); title filled in "
                 "from LinkedIn's My Jobs list (2026-08-17).",
    },
    {
        "company": "Bespoke Post",
        "position": "Strategist, Growth Marketing",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "Lever",
        "notes": None,
    },
    {
        "company": "Inizio Evoke",
        "position": "Senior Brand Strategist",
        "status": "Rejected",
        "applied_date": "2026-08-17",
        "source": "Greenhouse",
        "notes": "Rejected 2026-08-21: \"moved ahead with other candidates who we feel are a better "
                 "match for this particular position at this time.\"",
    },
    {
        "company": "Blackstone",
        "position": "Web Strategy, Associate - Digital Marketing",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "Workday",
        "notes": None,
    },
    {
        "company": "NBCUniversal",
        "position": "Associate Manager, NBC & Peacock Marketing",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "ZipRecruiter",
        "notes": None,
    },
    # -- 2026-08-17 evening rescan --
    {
        "company": "PepsiCo",
        "position": "Brand Designer (2026-450688)",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "iCIMS",
        "notes": "Second, distinct PepsiCo application from the Design Senior Manager - Immersive "
                 "role applied to 2026-07-29.",
    },
    {
        "company": "Razorfish Health",
        "position": "Manager, Brand Strategy (2026-152303)",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "iCIMS",
        "notes": "Publicis Groupe agency; confirmation came via Publicis Groupe's iCIMS instance.",
    },
    # -- 2026-08-17: JPMC Candidate Experience portal screenshot --
    {
        "company": "JPMorgan Chase & Co.",
        "position": "Olympic & Paralympic, Graphic Designer, Senior Associate (Job #210766619)",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "Oracle Recruiting Cloud",
        "notes": "Third, distinct JPMorgan application, found via JPMC's own Candidate Experience "
                 "portal (Oracle HCM) rather than a Gmail confirmation. \"Under Consideration.\"",
    },
    # -- 2026-08-18 early-morning rescan --
    {
        "company": "DualEntry",
        "position": "Design Lead",
        "status": "Applied",
        "applied_date": "2026-08-18",
        "source": "Ashby",
        "notes": "Confirmation email didn't name the role applied to. Accounting/ERP software startup "
                 "(recent $90M Series A).",
    },
    {
        "company": "Firefly",
        "position": "Visual Designer, Brand",
        "status": "Applied",
        "applied_date": "2026-08-18",
        "source": "Ashby",
        "notes": None,
    },
    {
        "company": "Accenture (Droga5)",
        "position": "Droga5 Senior Designer (R00348810)",
        "status": "Rejected",
        "applied_date": "2026-08-18",
        "source": "Workday",
        "notes": "Distinct from both the earlier Accenture (Droga5) Senior Strategist application "
                 "(rejected 2026-07-22) and the LinkedIn-sourced Accenture 'Creative Agency Senior "
                 "Designer' application -- this one carries its own reference role ID (R00348810) and "
                 "a fresh 2026-08-18 confirmation email, so it's kept separate rather than merged. "
                 "Rejected 2026-08-20: \"unable to move forward at this time.\"",
    },
    # -- 2026-08-18: Google candidate portal screenshot --
    {
        "company": "Google",
        "position": "Brand Marketing Manager, AI Education Brand and Partnerships",
        "status": "Rejected",
        "applied_date": "2026-07-24",
        "source": "Email",
        "notes": "Third Google application, found via Google's own candidate portal rather than a Gmail "
                 "confirmation -- \"Not proceeding.\" Exact applied date isn't shown on the portal "
                 "(just \"updated last month\"); the earliest known Google application date is used "
                 "as a placeholder here, not a confirmed date.",
    },
    # -- 2026-08-18: Meta candidate portal screenshot --
    {
        "company": "Meta",
        "position": "Brand Designer, Strategic Initiatives - Instagram Brand Studio",
        "status": "Applied",
        "applied_date": "2026-07-26",
        "source": "Email",
        "notes": "Third Meta application, found via Meta's own candidate portal rather than a Gmail "
                 "confirmation. Still active, \"Current stage: Application.\" New York, NY.",
    },
    # -- 2026-08-18: reported directly by Regina, not from any inbox scan --
    {
        "company": "Mother",
        "position": "Networking call -- no open role (Strategy)",
        "status": "Networking",
        "applied_date": "2026-08-18",
        "source": "Referral",
        "notes": "Recruiter called to get to know Regina, not about a specific opening -- she said she "
                 "doesn't currently have any open roles. Regina expressed interest in Strategy. Call date "
                 "approximate (not confirmed).",
    },
    {
        "company": "PepsiCo",
        "position": "Networking outreach -- design role (contact: Hillary)",
        "status": "Networking",
        "applied_date": "2026-08-18",
        "source": "Email",
        "notes": "Regina emailed Hillary at PepsiCo about a design role; Hillary's only reply was asking "
                 "for Regina's email address, nothing further came of it. Not found in a Gmail search "
                 "(may be on a different email thread or platform); logged from what Regina reported "
                 "directly. Exact date not confirmed.",
    },
    {
        "company": "Something Special Studios",
        "position": "Creative Strategist (direct outreach to Hope Calnan)",
        "status": "Applied",
        "applied_date": "2026-08-14",
        "source": "Email (direct outreach)",
        "notes": "Distinct from the earlier Greenhouse-sourced 'Senior Creative Strategist' application "
                 "(2026-07-27) -- this is a separate direct outreach, following up from a LinkedIn chat, "
                 "to Hope Calnan (hope.calnan@somethingspecialstudios.com) about the 'Creative Strategist' "
                 "role, with CV and portfolio (reginabbs.cargo.site) attached. No reply yet as of "
                 "2026-08-18.",
    },
    # -- 2026-08-19: incremental rescan --
    {
        "company": "Taskrabbit",
        "position": "Sr. Manager, Brand & Content",
        "status": "Applied",
        "applied_date": "2026-08-18",
        "source": "Greenhouse",
        "notes": "Confirmation email was a generic auto-reply template and didn't name the role applied "
                 "to; title filled in from LinkedIn's My Jobs list (2026-08-19). Hybrid, New York City "
                 "Metropolitan Area.",
    },
    # -- 2026-08-19: LinkedIn My Jobs list screenshot --
    {
        "company": "Book of the Month",
        "position": "Growth & Creative Rotational Program",
        "status": "Applied",
        "applied_date": "2026-08-19",
        "source": "LinkedIn",
        "notes": "Applied via LinkedIn Easy Apply, confirmed by LinkedIn's \"Your application was sent\" "
                 "screen. Exact title was cut off in the confirmation screenshot -- reconstructed from the "
                 "visible \"Growth & Creative Rotat...\" fragment, not fully confirmed. New York, NY, "
                 "on-site, full-time.",
    },
    {
        "company": "STEVEN MADDEN Ltd.",
        "position": "Brand Manager",
        "status": "Applied",
        "applied_date": "2026-08-19",
        "source": "LinkedIn",
        "notes": "New York, NY. LinkedIn shows \"Reposted 2d ago,\" which is the listing's repost date, "
                 "not Regina's applied date -- exact applied date unknown, today's scan date used as a "
                 "placeholder. LinkedIn's own \"Did you finish applying?\" prompt on this row means "
                 "completion isn't fully confirmed either.",
    },
    {
        "company": "Inside Out Community",
        "position": "Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-08-19",
        "source": "LinkedIn",
        "notes": "New York, NY. LinkedIn shows \"Posted 3w ago,\" which is the listing's post date, not "
                 "Regina's applied date -- exact applied date unknown, today's scan date used as a "
                 "placeholder. LinkedIn's own \"Did you finish applying?\" prompt on this row means "
                 "completion isn't fully confirmed either.",
    },
    # -- 2026-08-19 (evening): incremental rescan --
    {
        "company": "MUBI",
        "position": "Communications Manager, US",
        "status": "Applied",
        "applied_date": "2026-08-19",
        "source": "Ashby",
        "notes": None,
    },
    {
        "company": "Tapestry",
        "position": "Associate, External Communications",
        "status": "Rejected",
        "applied_date": "2026-08-19",
        "source": "Workday",
        "notes": "Rejected 2026-08-24: application isn't progressing further.",
    },
    # -- 2026-08-24: incremental rescan -- Amazon was missed by every prior
    # scan because amazon.jobs wasn't in the ATS domain list; caught by
    # widening the search after Regina asked about an interview invite.
    {
        "company": "Amazon",
        "position": "Art Director, Elevated Shopping (ID: 10410280)",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "Amazon Jobs",
        "notes": "Online assessment completed 2026-08-18; no interview invite yet.",
    },
    # -- 2026-08-24: recruiter reached out with a meeting invite --
    {
        "company": "Duel",
        "position": "Advocacy Consultant",
        "status": "Interviewing",
        "applied_date": "2026-08-18",
        "source": "Teamtailor",
        "next_step": "Recruiter screen with Ibrahim Thomas -- pick a time slot (invite sent 2026-08-24).",
        "notes": None,
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
