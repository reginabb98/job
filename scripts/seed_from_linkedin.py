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
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting (Publicis Health CoLab): 2-3 yrs strategy/digital-consulting/planning experience, heavy on presentation and creative-brief work; healthcare/pharma experience is called \"extremely helpful\" but not required. Regina's research, presentation, and briefing skills map well -- the pharma-industry specifics are the one real gap.",
    },
    {
        "company": "G&A Strategy and Design",
        "position": "Brand Strategist, Planning",
        "status": "Applied",
        "applied_date": "2026-08-03",
        "source": "LinkedIn",
        "notes": "Remote, United States. Posting no longer accepting applications. Applied date "
                 "estimated from LinkedIn's \"Applied 2w ago\" (as of 2026-08-17), not exact.",
        "job_fit": "Unknown",
        "job_fit_notes": "The posting is no longer live (per the tracker's own note) and no cached version could be found -- only generic brand-strategist job-description templates turned up, not real listing content.",
    },
    {
        "company": "Synthesis",
        "position": "Senior Foresight Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Hybrid, Brooklyn, NY. Posting no longer accepting applications. Applied date "
                 "estimated from LinkedIn's \"Applied 3w ago\" (as of 2026-08-17), not exact.",
        "job_fit": "Good",
        "job_fit_notes": "4+ yrs research/brand-strategy/consulting experience building foresight narratives, with Spanish/US-Hispanic cultural fluency called out as a plus -- Regina's research and storytelling skills are relevant, and her Monterrey, Mexico work history at Common Matter plausibly supports the Spanish/LatAm-culture angle specifically, which is a genuine, distinctive asset here.",
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
        "job_fit": "Good",
        "job_fit_notes": "Sister role to the Foresight Strategist posting at the same firm, focused on cultural narrative work for Americas-based clients -- Regina's cultural/audience research and Monterrey-MX/LatAm market experience are a genuine asset here.",
    },
    {
        "company": "Publicis Media",
        "position": "Senior Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Remote, New York, NY. Posting no longer accepting applications. Applied date "
                 "estimated from LinkedIn's \"Applied 3w ago\" (as of 2026-08-17), not exact.",
        "job_fit": "Fair",
        "job_fit_notes": "4+ yrs creative strategy centered on creator-led content and social-platform fluency, with mentoring of junior strategists. Regina's storytelling and presentation skills transfer, but creator-marketing-platform specialization and mentoring experience aren't evidenced.",
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
        "job_fit": "Fair",
        "job_fit_notes": "An entry-level media-planning associate program built around Excel/PowerPoint and data-driven media planning -- a different discipline (media buying/planning ops) from Regina's creative/brand background, though accessible as an entry point regardless of specialization.",
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
        "job_fit": "Strong",
        "job_fit_notes": "6+ yrs agency design with a concept-driven brand-identity portfolio, expert Figma/Illustrator/Photoshop/InDesign, and AI image-generation tools -- a strong direct match to Regina's brand-identity, visual-storytelling, and AI-assisted design background.",
    },
    {
        "company": "Reddit",
        "position": "Creative Strategist - App Dev",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Hybrid, New York, NY. Reposted 6d ago as of 2026-08-17. Applied date estimated "
                 "from LinkedIn's \"Applied 3w ago,\" not exact.",
        "job_fit": "Fair",
        "job_fit_notes": "4+ yrs advertising/creative-strategy experience building client pitch decks -- Regina's presentation and creative-strategy skills transfer, but the App-Dev-advertiser vertical and paid-social pitch experience the posting calls out aren't evidenced.",
    },
    {
        "company": "Moon Juice",
        "position": "Brand & Content Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "Remote, United States. Posting no longer accepting applications. Applied date "
                 "estimated from LinkedIn's \"Applied 3w ago\" (as of 2026-08-17), not exact.",
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting ($135K, remote -- matches the application LinkedIn shows submitted): 7+ yrs brand/content strategy, and the role owns copywriting across every channel plus manages a copywriter, with health & wellness industry experience called \"a must.\" Regina is under the years bar, copywriting ownership isn't a core strength on her resume, and wellness-industry experience isn't evidenced.",
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
        "job_fit": "Strong",
        "job_fit_notes": "4+ yrs branding-design experience with a strong brand-identity portfolio -- close overlap with Regina's background. Team-leading/mentoring interest is called out as a plus and is the one gap.",
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
        "job_fit": "Fair",
        "job_fit_notes": "Same core Reddit Creative Strategist bar as the App Dev role, applied to the Finance-advertiser vertical -- core creative-strategy and presentation skills transfer, but the finance-advertiser and paid-social pitch specifics aren't evidenced.",
    },
    {
        "company": "Noom",
        "position": "Creative Strategist",
        "status": "Rejected",
        "applied_date": "2026-07-27",
        "source": "LinkedIn",
        "notes": "New York, NY. Applied date estimated from LinkedIn's \"Applied 3w ago\" (as of "
                 "2026-08-17), not exact. Rejected 2026-08-25: \"the timing didn't quite line up, and the "
                 "position has been filled.\" Missed by every scan since -- caught in a 2026-09-02 widened "
                 "search for soft-rejection phrasing.",
        "job_fit": "Weak",
        "job_fit_notes": "Every level of this role (Junior through Senior) centers on hands-on direct-response/performance-creative work across Meta/TikTok/YouTube ads and UGC briefing -- none of that performance-advertising specialization is evidenced in Regina's background.",
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
        "job_fit": "Fair",
        "job_fit_notes": "3+ yrs marketing/communications with retail product-marketing operations (seasonal campaign planning, in-store asset creation, agency-relationship management). Regina's creative-briefing and brand skills partially transfer, but the retail-merchandising/product-marketing-ops specifics aren't evidenced.",
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
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: a junior strategist role supporting a Strategy Director, synthesizing culture/category/consumer insight into RFPs and presentations -- 1-2 yrs agency experience is called \"ideal\" but the posting says \"proven strategic comms ability... is most important.\" Regina's research, storytelling, and presentation-building skills line up well; the gap is the named syndicated research tools (Simmons-MRI, GWI) the role wants familiarity with.",
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
