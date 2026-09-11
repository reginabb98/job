"""
Seed of the applications table from periodic Gmail scans.

Covers reginabb98@gmail.com job-application activity: ATS confirmation/status
emails (Greenhouse, Lever, Ashby, Workday, iCIMS, Workable, Teamtailor,
SmartRecruiters, Amazon Jobs) plus explicit rejection/interview language. TA/
teaching-assistant leads are intentionally excluded per instruction, as are
LinkedIn "job alert" and "jobs similar to" emails since they're
recommendations, not applications.

As of 2026-09-02, scans also search broadly for generic "thank you for
applying"/"thank you for your interest" subjects and soft-rejection phrasing
("move forward with other candidates", "not move forward", "position has
been filled", "unfortunately", "at this time") rather than relying only on
a fixed ATS-domain list -- several real applications and rejections were
sent from a company's own domain (datadoghq.com, ogilvy.com) rather than a
known ATS platform, and several rejections were phrased too softly to match
explicit reject/not-selected keyword searches. See the 2026-09-02 scan
history entries below for what that turned up.

As of 2026-09-06 (night), applied_date is assigned from the email
timestamp converted to US Eastern time, not the raw UTC date Gmail
returns. Late-evening Eastern applications (roughly 8pm-midnight) show
up as after-midnight UTC on the *next calendar day*, which had been
silently rolling them into the wrong day -- and, worse, the wrong
week -- on the dashboard. Regina caught this when a Sunday-night batch
of applications showed up dated Monday. Every row touched in or after
that correction uses the Eastern date; earlier rows were not
retroactively audited for this.

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
  - 2026-08-25: Regina reported a batch of cold outreach emails; confirmed
    via Sent Mail and added 10 new Networking rows -- Gander/Heist (sent
    2026-08-19) and, sent 2026-08-25, four individual contacts at Meta,
    two at Wieden+Kennedy, and three at Red Antler, all reaching out about
    brand strategy roles. Logged as Networking rather than Applied since
    they're direct personal emails, not formal applications -- they count
    toward the dashboard's weekly reach-out activity but not toward Total
    Applications. The weekly-activity chart was updated to show reach-outs
    stacked on top of applications per week, so this kind of outreach is
    visible as "things done this week" without inflating the applications
    benchmark.
  - 2026-08-26: reconciled against a screenshot of Accenture's own candidate
    portal (My Applications, both already Rejected). Added job req
    R00338279 to the Senior Strategist row's title/notes, and corrected the
    Senior Designer (R00348810) applied_date from 2026-08-18 to 2026-08-17
    -- the portal's "Date Submitted" is authoritative over the confirmation
    email's timestamp. No status changes; both were already Rejected.
  - 2026-08-26 (later): incremental rescan, 1 new row (VaynerMedia,
    Relevance Strategist).
  - 2026-08-26 (evening): Regina reported two more cold outreach emails;
    confirmed via Sent Mail and added as Networking rows (Porto Rocha --
    Natalee, and Decade).
  - 2026-08-27: incremental rescan, no new rows. Two rejections: Duel's
    Advocacy Consultant application (after the recruiter screen with
    Ibrahim Thomas) and DualEntry's Brand Design Lead application (before
    the interview stage) -- DualEntry's title was also corrected from the
    earlier placeholder "Design Lead" now that the rejection email named
    it directly.
  - 2026-08-31: incremental rescan, no new rows. Flipped Mammoth Brands'
    Creative Strategist application to Rejected.
  - 2026-09-02: incremental rescan, no new rows. Flipped MUBI's
    Communications Manager, US application to Rejected.
  - 2026-09-02 (later): Regina applied directly to Monks (Associate Director,
    Comms Planning) and separately emailed a contact there the same day;
    confirmed via Gmail search and added.
  - 2026-09-02 (job-fit backfill): rated every real (non-Networking)
    application -- 66 existing plus the new Monks row, 67 total -- on fit
    against Regina's actual resume/background (five tailored resume
    versions she shared), using the real job posting where one could be
    found and confirmed via web search. Scale: Strong / Good / Fair / Weak
    / Unknown. 12 came back Unknown -- either the posting was opportunistic/
    unspecified with nothing to assess, or the exact listing couldn't be
    confirmed -- rather than guessing at a rating without real evidence.
  - 2026-09-02 (JPMC portal recheck): Regina shared an updated screenshot of
    JPMC's Candidate Experience portal. The Graphic Designer, Senior
    Associate application (210766619) is still Under Consideration, and
    Corporate Brand Marketing (210771927) was already Rejected -- no change
    to either. The Olympic & Paralympic Brand Strategist application
    (210768163), previously Under Consideration, now shows Not Selected --
    flipped to Rejected.
  - 2026-09-02 (reported directly by Regina): Superside's Lead Creative
    Strategist application was rejected -- Regina says the role requires
    being based in Mexico, which she isn't. A residency requirement, not a
    skills-based rejection. Flipped to Rejected.
  - 2026-09-02 (missed rejection, caught by Regina): Highsnobiety's
    Associate Creative application was rejected 2026-08-24, but every scan
    since then missed it -- the email's subject line was a generic "Thank
    you for your job application!" and the rejection itself was phrased
    softly ("decided to move forward with other candidates"), neither of
    which matched the more explicit rejection language prior searches
    looked for. Flipped to Rejected; future scans should also treat
    generic "thank you for applying" subjects and "moving forward with
    other candidates" phrasing as possible soft rejections, not just
    explicit "reject"/"not selected"/"unable to move forward" language.
    Also reconciled against a fresh Accenture candidate-portal screenshot --
    both Droga5 applications (Senior Designer R00348810, Senior Strategist
    R00338279) already show Rejected here, matching "No Longer Under
    Consideration" on the portal. No change needed.
  - 2026-09-02 (widened rejection search, at Regina's request): searched
    Gmail for soft-rejection phrasing ("move forward with other candidates",
    "not move forward", "position has been filled", "unfortunately", etc.)
    and generic "thank you for applying" subjects across the full inbox
    history, not just explicit reject/not-selected language. Found:
    (1) David Protein's Senior Brand Manager application was rejected
    2026-08-12 and had been sitting as Applied ever since -- flipped to
    Rejected. (2) Noom's Creative Strategist application was rejected
    2026-08-25 ("the position has been filled") and had also been sitting
    as Applied -- flipped to Rejected. (3) Two applications were missed
    entirely because their ATS domains (datadoghq.com, ogilvy.com) weren't
    in the ATS-domain search list: Datadog's Lead Designer (applied
    2026-08-18, rejected 2026-08-20 -- both added) and Ogilvy's Designer
    (applied 2026-08-17, still no response -- added as Applied).
  - 2026-09-02 (reported directly by Regina): Monks' Associate Director,
    Comms Planning application was rejected the same day it was submitted --
    Olga Gamer replied she can't hire candidates who will require visa
    sponsorship, even in the future. A visa/authorization issue, not a
    skills-based rejection. Flipped to Rejected.
  - 2026-09-03: incremental rescan, 3 new rows. Accenture (Droga5 Senior
    Strategist, R00348814) -- a distinct req ID from the earlier, already-
    rejected Droga5 Senior Strategist application, likely a reposted
    opening. Nourish (role unspecified -- generic Greenhouse confirmation
    didn't name it). Disney (Associate Manager, Brand Strategy).
  - 2026-09-03 (later): incremental rescan, 1 new row. MrBeast (role
    unspecified -- generic Greenhouse confirmation didn't name it).
  - 2026-09-05: incremental rescan, 3 new rows. Notion (Brand Designer,
    Creative Studio), PepsiCo (Graphic Designer - poppi, 2026-470592 -- a
    third, distinct PepsiCo application), and Finch (Brand and Web
    Designer).
  - 2026-09-05 (later): reconciled against a screenshot of Amazon's own My
    Applications portal. The Art Director, Elevated Shopping application
    is now Archived / "No longer under consideration" -- flipped to
    Rejected. The portal also showed 1 Active Amazon application not
    visible in the screenshot (only the Archived tab was shown) -- not yet
    identified or added.
  - 2026-09-05 (later still): identified the Active Amazon application via
    Gmail -- Regina applied to Brand Designer, Brand Innovation Lab
    (ID: 10525009), then withdrew it a few minutes later per Amazon's own
    "You've withdrawn your Amazon job application!" confirmation. Added
    with status Withdrawn to match.
  - 2026-09-05 (later still): incremental rescan, 3 more new rows. Bumble
    (Graphic Designer), Landor (role unspecified -- distinct from the
    earlier Design Bridge and Partners / Landor Senior Strategist
    application, different recruiter/ATS instance), and Gigs (role
    unspecified).
  - 2026-09-05 (final): Regina shared the actual Landor and Gigs postings
    and clarified the Amazon Brand Designer situation. Landor's role
    confirmed as "Designer" (2+ yrs, brand-focused, Strong fit). Gigs'
    role confirmed as "Senior Brand Designer" ($170K-$200K, Fair fit --
    requires motion-design skills as a core requirement, which Regina
    doesn't have evidenced). Amazon's Brand Designer, Brand Innovation Lab
    application: Regina withdrew it and then reapplied the same day, so
    it's flipped back from Withdrawn to Applied.
  - 2026-09-05 (networking backfill): Regina reported 6 networking calls
    from her own memory/calendar/LinkedIn messages -- Jennifer Passas
    (Interbrand, 07-30), Julia her SVA TA (advice, 08-04), Andrew her SVA
    instructor (advice, 08-19), Anna-Rae Morris (LinkedIn, 08-31, possible
    follow-up), and two scheduled calls not yet happened: Angel Bellon
    (independent cultural-intelligence consultant/Parsons faculty, 09-08)
    and Maggie Murphy (Strategy Director at Mother, 09-10 -- a follow-up
    from the earlier Mother Intro Call). Also corrected the existing
    Mother Intro Call's date from an approximate 08-18 to the confirmed
    calendar date, 07-30.
  - 2026-09-05 (clarified by Regina): LinkedIn cold-outreach messages are
    NOT logged as Networking rows on their own -- only once they actually
    turn into a response and a scheduled/completed call. (Cold outreach
    sent by email is a separate, already-established exception -- see the
    2026-08-25 entry above -- and continues to be logged even without a
    reply, since it's tracked as direct personal outreach rather than a
    LinkedIn message.) Anna-Rae Morris and Angel Bellon both already
    cleared this bar (a completed or scheduled call), so no changes were
    needed to what's tracked.
  - 2026-09-06: incremental rescan since 2026-09-05, 2 new rows. Bain &
    Company (Strategic Designer, Weak fit -- a UX/service-design/product-
    design discipline, not brand/graphic design) and Meta (generic
    "Designer" role, Unknown fit -- confirmation email named no team or
    seniority; a 4th, distinct Meta application from the 3 already
    tracked). Also found a same-night Ogilvy security-code verification
    step followed by a second "thank you for applying" email for the same
    Designer role already tracked (applied 2026-08-17) -- treated as a
    resubmission of that existing application, not a new row.
  - 2026-09-06 (later): incremental rescan, 2 more new rows that landed in
    the inbox after the prior pass -- Havas and City of New York, both
    "Graphic Design Intern" postings. Confirmed both postings target
    current college students (Havas: rising junior/senior/recent-grad
    pipeline; NYC: civil-service title "College Aide", experience level
    "Student"), so both rated Weak fit on seniority mismatch rather than a
    skills gap.
  - 2026-09-06 (later still): incremental rescan, 5 more new rows that
    landed after the prior pass -- Gensler (Multimedia + Graphic Designer,
    Marketing, Fair fit -- motion/video is a core requirement Regina
    doesn't have evidenced), Hypha (Visual Designer, Unknown fit --
    couldn't find the posting), Vestwell (Senior Brand Designer, Fair fit
    -- strong brand-systems overlap but requires hands-on HubSpot CMS
    experience; also resubmitted via a Greenhouse security-code step,
    treated as one application), Brick (unspecified role, Unknown fit --
    generic confirmation), and The Working Assembly (Brand Designer,
    Strong fit -- close match to Regina's agency background, applied via
    the company's own Google Form rather than an ATS).
  - 2026-09-06 (incremental rescan since prior pass): 1 new row. Meta --
    Brand Designer, Iconography & Illustration, Instagram Brand Studio
    (Fair fit -- a specialist illustration/iconography track, tool
    overlap but not a demonstrated core strength). A 5th, distinct Meta
    application, same team as the existing Strategic Initiatives role but
    a different req.
  - 2026-09-06 (evening): incremental rescan, 2 new rows. Fanatics
    Collectibles (Graphic Designer II, Good fit -- 3-5 yr Adobe CC/
    branding/print-production match) and United Legwear Company
    (unspecified role, Unknown fit -- generic ADP confirmation named no
    role).
  - 2026-09-06 (fit confirmation, real postings shared by Regina): filled
    in confirmed titles and fit for 4 rows that had gone in with generic
    confirmations or estimated fit. Hypha's role confirmed as "Visual
    Designer" (posting body calls it "Brand Designer" -- a naming
    inconsistency in Hypha's own listing), Good fit. Brick's unspecified
    role confirmed as "Growth Designer" -- flipped Unknown to Weak, since
    it's a performance-marketing/ad-creative discipline, not brand
    design. United Legwear's unspecified role confirmed as "Senior
    Designer, KIDS (Scotch & Soda)" -- flipped Unknown to Weak, an
    apparel/PLM discipline unrelated to Regina's background. Meta's
    Iconography & Illustration role's fit was downgraded from an earlier
    Fair (based on a search summary) to Weak once the full posting text
    showed an 8+ year specialist-experience minimum.
  - 2026-09-06 (pay_range backfill): populated the pay_range field for
    every row where a real posting's compensation figure had already
    been confirmed (previously only mentioned in job_fit_notes prose,
    not structured): Gigs ($170K-$200K), Havas ($18-22/hr), Gensler
    ($70K-$85K), Hypha ($80K-$100K), Brick ($90K-$110K), Meta
    Iconography & Illustration ($149K-$209K), United Legwear
    ($100K-$130K), and Moon Juice in seed_from_linkedin.py ($135K). The
    Working Assembly's $95,000 is Regina's own stated salary expectation
    on the application form, not an employer-posted range, so it was
    left out of pay_range and stays noted in prose only.
  - 2026-09-06 (night): incremental rescan, 4 new rows. Amazon (3rd
    distinct Amazon application, "Designer, Premium, Elevated Shopping",
    Unknown fit -- salary confirmed but not the exact requirements),
    Assembled (Brand Designer, Good fit, $150K-$190K), Ripple
    (unspecified role, Unknown fit -- generic confirmation and two
    plausible openings, neither confirmed), and Material (unspecified
    role, Unknown fit -- generic confirmation).
  - 2026-09-06: 1 new row, reported directly by Regina. Paramount --
    Designer, Publishing, Fair fit. She'd started this application
    earlier and left it incomplete; a "please complete your application"
    reminder landed 2026-09-06 night, and she finished submitting it
    2026-09-06.
  - 2026-09-06 (later): 1 new row, found via Gmail Sent search. Pentagram
    -- Middleweight Designer, Good fit. Direct cold-email application to
    Eddie Opara's team (eo_teamjobs@pentagram.com) with resume and
    portfolio attached; no public posting found, so this looks like a
    referral-style opportunity rather than a listed job.
  - 2026-09-06 (fit confirmation, real postings shared by Regina): filled
    in confirmed titles and fit for the 2 remaining Unknown rows from
    the 09-06 night rescan. Ripple confirmed as the New York "Brand
    Designer" opening (not the separate SF Senior role) -- Unknown to
    Good, $112K-$120K. Material confirmed as "Mid-level Brand Designer
    (Aruliden)" -- Unknown to Good, $65K-$85K; also corrected the
    location from an earlier guess of Los Angeles to the posting's
    actual New York, NY (hybrid).
  - 2026-09-06 (later still, fit confirmation): Regina shared 2 more
    real postings. Pentagram's Middleweight Designer role, previously
    rated Good on general agency-tier reasoning, was downgraded to Fair
    once the full listing showed required motion-tool proficiency
    (Figma, After Effects, Cavalry, Cinema 4D) that isn't evidenced on
    her resume -- same gap as Gigs/Gensler/Brick, but a hard requirement
    here, not a plus; salary confirmed $85K-$105K. Amazon's Designer,
    Premium, Elevated Shopping (ID: 10523835) confirmed as Good fit --
    5+ yrs premium fashion/beauty design experience matches her agency
    background well; salary corrected to $132.5K-$185K.
  - 2026-09-06 (later still, fit confirmation): confirmed Meta's generic
    "Designer" application as a Creative X / Reality Labs role (wearables/
    metaverse brand design) from the LinkedIn listing Regina shared --
    Unknown to Good, $122K-$175K.
  - 2026-09-06 (later still): incremental rescan, 6 new rows. Conveo
    (Design Lead, Fair fit -- B2B/SaaS leadership scope not evidenced),
    Figma (2nd application, Brand Designer/Product Launches, Fair fit --
    launch-storytelling/motion craft not a demonstrated specialty),
    Day One (Senior Designer, Unknown -- couldn't confirm requirements),
    Fresh (Senior Designer, Digital and Social, Good fit -- beauty-brand
    digital/social work matches Regina's background, though the exact
    posting wasn't confirmed), and two generic confirmations left as
    Unspecified role (Tory Burch, Omnicom network).
  - 2026-09-06 (reconciled against Publicis's own candidate portal):
    Regina shared a screenshot showing req 2026-152303 (Razorfish
    Health, Manager, Brand Strategy) marked "Not selected" -- flipped
    that row from Applied to Rejected.
  - 2026-09-06 (later still): incremental rescan, 2 more new rows.
    Turner Duckworth (Senior Designer, 2026-166476, Strong fit --
    packaging/brand-identity agency, a direct match to Regina's Common
    Matter background) and Posh (Brand Designer, Weak fit -- wants a
    Series B-D in-house creative *leader* with hands-on motion/film and
    nightlife-culture ties, well beyond her current level).
  - 2026-09-06 (date-correction, caught by Regina): a whole evening's
    batch of applications (Pentagram, Paramount, Conveo, Figma's 2nd app,
    Day One, Fresh, Tory Burch, Omnicom, Turner Duckworth, Posh) had been
    dated 2026-09-07 -- the raw UTC date of their Gmail confirmations --
    even though they were all submitted 8-10pm Eastern on 2026-09-06.
    Regina noticed the dashboard's weekly counter had rolled into a new
    week for a Sunday-night batch. Corrected all ten applied_date values
    to 2026-09-06 and adopted Eastern-time conversion as the standing
    rule going forward (see docstring intro).
  - 2026-09-06 (fit confirmation, more real postings shared by Regina):
    Day One's Senior Designer confirmed Good fit ($80K-$95K); Tory Burch
    confirmed as "Temporary Helper, Senior
    Graphic Designer" (Unknown to Good); Omnicom confirmed as
    "Presentation Designer, Brand Experience" under a "Design Manager"
    listing title (Unknown to Good, $50K-$95K, PowerPoint-heavy); Nourish
    confirmed as "Senior Creative Strategist" (Unknown to Fair --
    performance-data fluency not evidenced); MrBeast confirmed as
    "Senior Brand Strategist" (Unknown to Weak -- wants 8-10+ yrs at a
    top-tier digital publisher, well beyond Regina's experience).
  - 2026-09-08: incremental rescan, 2 new rows. Accenture (Work & Co)
    Designer, R00334677, Unknown fit -- a generic Work & Co/Accenture Song
    design req, distinct from the three earlier Accenture/Droga5
    applications, with no confirmable requirements beyond generic team-page
    copy. Fresh, Senior Designer, Digital and Social -- a second, distinct
    SmartRecruiters application ID for the same role Regina already applied
    to on 2026-09-06, logged as an apparent accidental duplicate
    resubmission.
  - 2026-09-08 (later): incremental rescan, 1 new row and 1 rejection.
    WITHIN, Creative Lead Fellow (Weak fit -- confirmed posting is an
    8-week performance-creative/short-form-video fellowship judged on a
    public social/spec portfolio, a different discipline from Regina's
    brand/graphic design background). Flipped VaynerMedia's Relevance
    Strategist application to Rejected per a VaynerX/Greenhouse email.
  - 2026-09-09: incremental rescan, no new rows, 2 rejections. Flipped
    Finch's Brand and Web Designer application to Rejected per a Lever
    email. Flipped the Accenture (Work & Co) Designer (R00334677)
    application to Rejected per a Workday email citing that Regina's
    application indicated she requires visa sponsorship -- flagged for
    Regina to double-check her Workday/EEO profile answers, since an
    incorrect sponsorship flag there could be silently disqualifying her
    from other US-based Workday applications too.
  - 2026-09-09 (later, reported directly by Regina): 2 new rows. DualEntry,
    Brand Designer -- a direct cold-email application to the recruiter
    since Ashby was blocking a second application tied to her earlier,
    rejected Brand Design Lead req (Good fit, $100K-$160K). Omnicom
    Network, a 2nd distinct general network application (Unspecified role,
    Unknown fit) -- separate from both the 2026-07-27 and 2026-09-06
    Omnicom applications already on file.
  - 2026-09-10 (reported directly by Regina, screenshot): 1 new row.
    Pomegranate Gallery, Part Time Book Designer -- applied via SVA's own
    career-services job board (12twenty). Confirmed posting is actually a
    combined "Film Editor/Videographer & Graphic/Book Designer" role
    (Fair fit -- film editing/videography isn't evidenced on Regina's
    resume, though the book/graphic-design half overlaps).
  - 2026-09-11: incremental rescan, no new rows, 1 rejection. Flipped the
    Accenture (Droga5) Senior Strategist (R00348814) application to
    Rejected per a Workday email.

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
        "position": "Senior Strategist (R00338279)",
        "status": "Rejected",
        "applied_date": "2026-07-22",
        "next_step": None,
        "source": "Workday",
        "notes": "Applied via Accenture's Workday portal for the Droga5 Senior Strategist role. "
                 "The 2026-08-12 follow-up emails were a bar from reapplying, not a new opportunity -- "
                 "confirmed rejection. Job req R00338279 and Jul 22 applied date confirmed 2026-08-26 "
                 "via Accenture's own candidate portal (\"No Longer Under Consideration\").",
        "job_fit": "Fair",
        "job_fit_notes": "Droga5 wants someone whose career has been in the strategist seat -- brief-writing, storytelling, owning day-to-day strategy on projects, managing AI-assisted research. Regina's briefing/storytelling/AI-research skills overlap, but her career has been design-led with a strategy overlay, not a strategy-track career, which is likely why this didn't convert.",
    },
    {
        "company": "Snapchat",
        "position": "Associate Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-07-22",
        "source": "Workday",
        "notes": None,
        "job_fit": "Strong",
        "job_fit_notes": "Entry-level bar (1+ yrs creative strategy/design/marketing, presentation-building, Google Slides/AI tools, social-first storytelling) that Regina's presentation-design, visual-storytelling, and AI-assisted research skills map to directly -- if anything she's above the seniority the posting asks for.",
    },
    {
        "company": "Mammoth Brands",
        "position": "Creative Strategist",
        "status": "Rejected",
        "applied_date": "2026-07-22",
        "source": "Greenhouse",
        "notes": "Rejected 2026-08-31: \"decided to move forward with other candidates whose experience "
                 "more closely aligns with what we're looking for at this time.\"",
        "job_fit": "Weak",
        "job_fit_notes": "Wants hands-on video editing (Premiere/CapCut/DaVinci) and direct-response/performance-ad ownership. Neither is evidenced anywhere on Regina's resume -- her design and strategy work isn't in video or performance advertising.",
    },
    {
        "company": "The New York Times",
        "position": "Designer, Marketing",
        "status": "Applied",
        "applied_date": "2026-07-22",
        "source": "Email",
        "notes": None,
        "job_fit": "Good",
        "job_fit_notes": "5+ yrs agency/in-house marketing design across social/digital/email/print with strong typography and Figma/Adobe fluency -- squarely Regina's Common Matter and Superside experience. The one clear gap is hands-on motion/animation (Jitter, After Effects), which the posting also requires and isn't on her resume.",
    },
    {
        "company": "Interbrand",
        "position": "Verbal Identity Fellow",
        "status": "Applied",
        "applied_date": "2026-07-22",
        "source": "Greenhouse",
        "notes": None,
        "job_fit": "Weak",
        "job_fit_notes": "A 0-1 yr entry-level fellowship built around copywriting/naming/verbal fields (linguistics, creative writing, English) -- Regina is 6+ yrs experienced and her core strength is visual design, not copywriting, so this is a mismatch on both seniority and discipline.",
    },
    {
        "company": "Interbrand",
        "position": "General interest (no specific opening listed)",
        "status": "Applied",
        "applied_date": "2026-07-24",
        "source": "Greenhouse",
        "notes": "Separate general-interest application, distinct from the Verbal Identity Fellow role applied to 2026-07-22.",
        "job_fit": "Unknown",
        "job_fit_notes": "This was an opportunistic general-interest application with no specific opening or job posting attached -- there's no listing to assess fit against.",
    },
    {
        "company": "Lippincott",
        "position": "Senior Consultant, Strategy (R_350484)",
        "status": "Applied",
        "applied_date": "2026-07-24",
        "source": "Workday",
        "notes": None,
        "job_fit": "Good",
        "job_fit_notes": "3+ yrs strategy/brand-consulting with heavy emphasis on synthesis, presentation, and writing -- Regina's audience/cultural/competitive research and creative-briefing skills line up well, though she comes from a design-led background rather than a consulting track, and client-interview-style stakeholder work isn't clearly evidenced on her resume.",
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
        "job_fit": "Good",
        "job_fit_notes": "Leading strategic phases, translating business challenges into creative briefs, and working closely with design teams -- a strong match given Regina's brief-writing and research skills plus her own design background giving her real fluency on the design side of that strategy hand-off. This is also the one application that actually reached an interview, consistent with a solid match.",
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
        "job_fit": "Fair",
        "job_fit_notes": "Wants B2B corporate brand-marketing experience (4+ yrs) enforcing brand guidelines across a large matrixed org. Regina's background is agency/freelance creative and strategy work, not in-house corporate brand marketing, so the day-to-day skill set doesn't line up as closely as the title suggests.",
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
        "job_fit": "Weak",
        "job_fit_notes": "Requires 9 years of brand/consumer marketing experience managing creative-agency relationships and executive stakeholders -- well above Regina's 6 years, and it's a marketing-manager career track rather than design or creative strategy.",
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
        "job_fit": "Weak",
        "job_fit_notes": "Requires 10+ years of creative experience in brand/performance marketing with a paid-social campaign portfolio -- both the years bar and the paid-social specialization are well beyond what's on Regina's resume.",
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
        "job_fit": "Good",
        "job_fit_notes": "5-8+ yrs creative strategist/account-planner experience with strong storytelling, curiosity, and a creative-brief portfolio -- Regina is at the lower end of the years range but the qualitative fit (briefs, storytelling, collaborative style) is strong. The clear gap is the named audience-research tools (Quilt.AI, Infegy, Resonate, MRI-Simmons), which aren't on her resume.",
    },
    {
        "company": "Highsnobiety",
        "position": "Associate Creative",
        "status": "Rejected",
        "applied_date": "2026-07-27",
        "source": "Teamtailor",
        "notes": "Rejected 2026-08-24: \"decided to move forward with other candidates... only the finest "
                 "of nuances which tip the balance of a decision one way or the other.\" This rejection was "
                 "missed by the 2026-08-24 and 2026-08-27 rescans -- caught late when Regina forwarded it "
                 "directly on 2026-09-02.",
        "job_fit": "Strong",
        "job_fit_notes": "1-3 yrs, deep cultural fluency in fashion/music/youth culture, concepts grounded in audience and cultural insight, visual research and moodboards, Keynote/Photoshop/Illustrator -- a close match to Regina's actual skill set and experience level.",
    },
    {
        "company": "Instrument",
        "position": "Unspecified role",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Lever",
        "notes": None,
        "job_fit": "Unknown",
        "job_fit_notes": "The confirmation email never named the specific role applied to, and no listing could be matched -- there's nothing concrete to assess fit against.",
    },
    {
        "company": "Something Special Studios",
        "position": "Senior Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Greenhouse",
        "notes": None,
        "job_fit": "Strong",
        "job_fit_notes": "Leading multidisciplinary strategy projects end-to-end (research through insight to concept and launch), narrative-driven decks, client presentations, and cultural sensibility -- this maps closely to Regina's actual day-to-day skill set.",
    },
    {
        "company": "Superside",
        "position": "Lead Creative Strategist",
        "status": "Rejected",
        "applied_date": "2026-07-27",
        "source": "Lever",
        "notes": "Rejected: Regina reported the role requires being based in Mexico, which she isn't -- a "
                 "residency requirement, not a skills-based rejection.",
        "job_fit": "Good",
        "job_fit_notes": "6+ yrs strategy roles at creative/ad/digital agencies with data-informed briefs and AI-championing -- Regina is right at the years bar and has genuine insider knowledge from her own recent Superside employment (Creative, Feb-Sept 2025). The gap is team-leading/mentoring experience, which the 'Lead' title implies but isn't clearly evidenced on her resume. Note: the actual rejection was purely a Mexico-residency requirement, not a skills mismatch -- the fit rating above reflects the role's substance, not the reason it didn't move forward.",
    },
    {
        "company": "Figma",
        "position": "Designer Advocate, Figma Weave",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Email",
        "notes": None,
        "job_fit": "Weak",
        "job_fit_notes": "Wants experience with node-based/procedural AI pipelines (ComfyUI, Houdini, TouchDesigner) and a motion-graphics/VFX/creative-automation background for teaching technical creative audiences -- none of that specific tooling is on Regina's resume, even though her general AI-assisted-research and Figma skills overlap loosely.",
    },
    {
        "company": "Buttermilk",
        "position": "Senior Creative",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Teamtailor",
        "notes": "Title filled in from LinkedIn's My Jobs list (2026-08-17).",
        "job_fit": "Fair",
        "job_fit_notes": "6-8+ yrs at a creative/social/influencer/integrated agency with mentoring and creator-marketing/internet-culture specialization -- Regina is close on years and her design/strategy/presentation background is relevant, but influencer-marketing specialization and formal mentoring aren't evidenced.",
    },
    {
        "company": "co:collective",
        "position": "Senior Strategist",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Lever",
        "notes": None,
        "job_fit": "Good",
        "job_fit_notes": "4-5+ yrs strategy/brand-planning across 2-3 strategy disciplines with qual+quant synthesis and proposal-writing -- Regina's brand strategy, research, and storytelling skills map well qualitatively; formal quant-data synthesis and business-strategy consulting experience are less evidenced.",
    },
    {
        "company": "Omnicom Network",
        "position": "General network application",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Workday",
        "notes": None,
        "job_fit": "Unknown",
        "job_fit_notes": "A general opportunistic application to the Omnicom network with no specific role attached -- there's no listing to assess fit against.",
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
        "job_fit": "Weak",
        "job_fit_notes": "Requires 8-10 years of strategist experience owning brand architecture/naming/positioning and presenting to executives -- well above Regina's 6 years.",
    },
    {
        "company": "Partiful",
        "position": "Opportunistic application (no specific opening)",
        "status": "Applied",
        "applied_date": "2026-07-27",
        "source": "Ashby",
        "notes": "Not applying to a listed opening -- reached out opportunistically.",
        "job_fit": "Unknown",
        "job_fit_notes": "Explicitly an opportunistic outreach with no listed opening -- there's no posting to assess fit against.",
    },
    {
        "company": "Wieden+Kennedy",
        "position": "Unspecified role",
        "status": "Applied",
        "applied_date": "2026-07-28",
        "source": "Greenhouse",
        "notes": None,
        "job_fit": "Unknown",
        "job_fit_notes": "The confirmation email never named the specific role applied to, and no matching listing could be found -- there's nothing concrete to assess fit against.",
    },
    {
        "company": "David Protein",
        "position": "Senior Brand Manager",
        "status": "Rejected",
        "applied_date": "2026-07-28",
        "source": "Workable",
        "notes": "Rejected 2026-08-12: \"After reviewing your application, we've decided not to move "
                 "forward at this time.\" Missed by every scan since -- caught in a 2026-09-02 widened "
                 "search for soft-rejection phrasing.",
        "job_fit": "Fair",
        "job_fit_notes": "Centers on influencer/creator partnership recruitment and negotiation and top-of-funnel growth ownership at a fast-growing CPG brand. Regina's brand strategy and creative sensibility are relevant, but the role is fundamentally a partnerships/growth-marketing operator seat, which isn't part of her evidenced experience.",
    },
    {
        "company": "AKQA",
        "position": "Freelance Senior Designer (New York)",
        "status": "Rejected",
        "applied_date": "2026-07-28",
        "source": "Email",
        "notes": "Rejected same day: \"we have identified candidates who are more closely aligned with the role.\"",
        "job_fit": "Fair",
        "job_fit_notes": "A UX-leaning design role emphasizing AI-tool proficiency and research-grounded process. Regina's design, research, and AI-assisted workflow skills overlap, but her portfolio leans brand/graphic/packaging rather than UX/product design specifically.",
    },
    {
        "company": "PepsiCo",
        "position": "Design Senior Manager - Immersive (2026-439325)",
        "status": "Applied",
        "applied_date": "2026-07-29",
        "source": "iCIMS",
        "notes": "Already in PepsiCo's talent community from an earlier signup (2026-06-16).",
        "job_fit": "Good",
        "job_fit_notes": "Leading immersive/experiential brand experiences (gaming, music, festivals) for a major CPG -- Regina's Common Matter experiential work (Parlote and Live Out music festivals) is a genuinely strong direct match. The gap is formal people-management of a design team, which this 'Senior Manager' title implies.",
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
        "job_fit": "Fair",
        "job_fit_notes": "Requires 6 years of marketing experience (brand/product/growth/social), which Regina is right at, but it's a marketing-manager career track at a huge matrixed tech org rather than a design or creative-strategy seat -- a stretch outside her core discipline despite clearing the years bar.",
    },
    {
        "company": "JPMorgan Chase & Co.",
        "position": "Olympic & Paralympic Brand Strategist (Job #210768163)",
        "status": "Rejected",
        "applied_date": "2026-07-29",
        "source": "Oracle Recruiting Cloud",
        "notes": "Second, distinct JPMorgan application from the one on 2026-07-23. Title and exact "
                 "applied date confirmed 2026-08-17 via JPMC's Candidate Experience portal -- was \"Under "
                 "Consideration\" then, now shows \"Not Selected\" per a later portal check on 2026-09-02.",
        "job_fit": "Fair",
        "job_fit_notes": "Requires 4+ yrs brand strategy plus hands-on sponsorship-activation and paid-media-campaign management for the IOC/Team USA relationship. Regina's brand-strategy and creative-brief skills partially overlap, but sponsorship activation and paid-media management aren't evidenced on her resume.",
    },
    {
        "company": "Prose",
        "position": "Manager of Design, Brand Creative",
        "status": "Rejected",
        "applied_date": "2026-07-28",
        "source": "Ashby",
        "notes": "Rejected 2026-08-03: \"we have decided to move forward with other candidates.\"",
        "job_fit": "Good",
        "job_fit_notes": "4-6 yrs of visual-design leadership end-to-end with AI tools -- a strong match on the core design-leadership skill set, though the posting specifically wants apparel/sports-industry design experience, which Regina doesn't have.",
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
        "job_fit": "Good",
        "job_fit_notes": "Social-strategy development, translating cultural trends into creative direction, Gen AI use, and briefing creative teams -- lines up closely with Regina's trend-analysis, creative-briefing, and cultural-research skill set.",
    },
    {
        "company": "Bespoke Post",
        "position": "Strategist, Growth Marketing",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "Lever",
        "notes": None,
        "job_fit": "Weak",
        "job_fit_notes": "A hands-on performance-marketing role: buying and optimizing paid Meta/Google budgets, Shopify merchandising, MMM/attribution modeling. This is a different discipline entirely from Regina's brand/creative background -- no paid-media-buying or Shopify experience is evidenced.",
    },
    {
        "company": "Inizio Evoke",
        "position": "Senior Brand Strategist",
        "status": "Rejected",
        "applied_date": "2026-08-17",
        "source": "Greenhouse",
        "notes": "Rejected 2026-08-21: \"moved ahead with other candidates who we feel are a better "
                 "match for this particular position at this time.\"",
        "job_fit": "Fair",
        "job_fit_notes": "Inizio Evoke is a healthcare/pharma communications agency and the role's stated degree preference is life sciences/marketing/comms -- Regina's degree is graphic design, a field mismatch, even though the day-to-day deck-development and creative-brief work would transfer reasonably well.",
    },
    {
        "company": "Blackstone",
        "position": "Web Strategy, Associate - Digital Marketing",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "Workday",
        "notes": None,
        "job_fit": "Weak",
        "job_fit_notes": "A web-ops/CMS role requiring hands-on WordPress, SEO/GEO, and Google Analytics experience -- none of that technical web-strategy work is evidenced anywhere in Regina's design/creative-strategy background.",
    },
    {
        "company": "NBCUniversal",
        "position": "Associate Manager, NBC & Peacock Marketing",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "ZipRecruiter",
        "notes": None,
        "job_fit": "Fair",
        "job_fit_notes": "An entertainment-marketing campaign-execution/coordination role (2+ yrs). Regina's brand and creative collaboration skills transfer reasonably, but this is more marketing-ops/coordination than the design or strategy authorship she actually does.",
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
        "job_fit": "Strong",
        "job_fit_notes": "2-5 yrs hands-on brand/packaging/graphic design with 360 brand-design experience across print, packaging, digital, environmental, and experiential -- almost exactly Regina's Common Matter experience.",
    },
    {
        "company": "Razorfish Health",
        "position": "Manager, Brand Strategy (2026-152303)",
        "status": "Rejected",
        "applied_date": "2026-08-17",
        "source": "iCIMS",
        "notes": "Publicis Groupe agency; confirmation came via Publicis Groupe's iCIMS instance. Rejected per "
                 "Publicis's own candidate portal (screenshot shared by Regina 2026-09-06) -- \"Not selected.\" "
                 "Exact rejection date not shown on the portal.",
        "job_fit": "Good",
        "job_fit_notes": "3-6 yrs strategy/research/agency experience built on qual+quant research synthesis, creative-brief development, and presentations -- Regina's research, briefing, and presentation skills map well. The one gap is the healthcare/HCP-specific research angle the posting calls out as ideal.",
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
        "job_fit": "Strong",
        "job_fit_notes": "3+ yrs brand design across disciplines, a portfolio in brand systems and multi-channel campaigns, Adobe CS + Figma, and interest in generative AI -- a very close, direct match to Regina's actual design background and tools.",
    },
    # -- 2026-08-18 early-morning rescan --
    {
        "company": "DualEntry",
        "position": "Brand Design Lead",
        "status": "Rejected",
        "applied_date": "2026-08-18",
        "source": "Ashby",
        "notes": "Confirmation email didn't name the role applied to; title confirmed 2026-08-27 by the "
                 "rejection email. Accounting/ERP software startup (recent $90M Series A). Rejected "
                 "2026-08-27: \"not able to move forward to the interview stage at this time.\"",
        "job_fit": "Weak",
        "job_fit_notes": "Wants 6+ yrs including deep motion/3D tooling (After Effects, Blender, Cinema4D) and freelancer management -- neither is evidenced on Regina's resume. Worth flagging separately: the listing itself restricts the role to candidates based in the EU or LATAM, which may not even match her eligibility.",
    },
    {
        "company": "Firefly",
        "position": "Visual Designer, Brand",
        "status": "Applied",
        "applied_date": "2026-08-18",
        "source": "Ashby",
        "notes": None,
        "job_fit": "Strong",
        "job_fit_notes": "Owning a brand's print and digital collateral -- tradeshow graphics, decks, packaging -- and being equally comfortable in print and pixels. Strong direct overlap with Regina's Common Matter packaging/print/presentation/digital-collateral work.",
    },
    {
        "company": "Accenture (Droga5)",
        "position": "Droga5 Senior Designer (R00348810)",
        "status": "Rejected",
        "applied_date": "2026-08-17",
        "source": "Workday",
        "notes": "Distinct from both the earlier Accenture (Droga5) Senior Strategist application "
                 "(rejected 2026-07-22) and the LinkedIn-sourced Accenture 'Creative Agency Senior "
                 "Designer' application -- this one carries its own reference role ID (R00348810) and "
                 "a fresh 2026-08-18 confirmation email, so it's kept separate rather than merged. "
                 "Accenture's own candidate portal (checked 2026-08-26) shows the actual submitted date "
                 "as Aug 17, one day before that confirmation email -- corrected here. "
                 "Rejected 2026-08-20: \"unable to move forward at this time.\"",
        "job_fit": "Good",
        "job_fit_notes": "6-8 yrs agency design experience -- Regina's core brand/campaign design work overlaps well. The gaps are the posting's motion-design and UX/UI requirements and formal mentoring of junior designers, none of which are clearly evidenced on her resume.",
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
        "job_fit": "Fair",
        "job_fit_notes": "Same pattern as the other Google AI Education role: 6 years of product-marketing experience (loosely met) but a partnerships/marketing-manager career track rather than design or creative strategy.",
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
        "job_fit": "Fair",
        "job_fit_notes": "This specialized 'Strategic Initiatives' track wants 8+ yrs of brand/identity design (the general Instagram Brand Designer track is 5+ yrs, which Regina's 6 would clear); motion tools like After Effects/Cinema4D are listed as preferred, not required, and are the one clear gap otherwise.",
    },
    # -- 2026-08-18: reported directly by Regina, not from any inbox scan --
    {
        "company": "Mother",
        "position": "Networking call -- no open role (Strategy)",
        "status": "Networking",
        "applied_date": "2026-07-30",
        "source": "Referral",
        "notes": "Mother Intro Call, confirmed via calendar (12:30pm, 2026-07-30) -- corrects the earlier "
                 "approximate date. Recruiter called to get to know Regina, not about a specific opening -- "
                 "she said she doesn't currently have any open roles. Regina expressed interest in Strategy. "
                 "Led to a follow-up call scheduled with Maggie Murphy, Strategy Director at Mother, on "
                 "2026-09-10 (see separate row).",
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
        "job_fit": "Strong",
        "job_fit_notes": "Same company and role family as the Greenhouse-sourced Senior Creative Strategist application -- research-to-insight-to-concept work, narrative decks, and cultural sensibility line up closely with Regina's actual skill set.",
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
        "job_fit": "Fair",
        "job_fit_notes": "5-7 yrs owning brand positioning plus a full content system and editorial calendar across channels. Regina's brand strategy and creative-briefing skills are relevant, but the role is heavy on content-strategy/editorial-calendar operations, which isn't evidenced on her resume.",
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
        "job_fit": "Fair",
        "job_fit_notes": "An early-career rotational program spanning influencer/social/performance-marketing/analytics -- Regina is well past the program's intended career stage, and most of the rotations (performance marketing, data analytics) aren't her strength, though the 'Creative Briefing & Project Management' rotation specifically would fit her well.",
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
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting (LinkedIn): 5-8+ yrs brand management/marketing (fashion/retail preferred), acting as the cross-functional connector across marketing/creative/merchandising/e-commerce/wholesale, leading brand collaborations. Regina's storytelling and trend instincts overlap qualitatively, but this is a brand-management ownership/connector role rather than design or creative-strategy execution, and her 6 years sits at the low end of the 5-8+ range.",
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
        "job_fit": "Unknown",
        "job_fit_notes": "No posting matching this exact title and company could be found -- only unrelated low-paid remote marketing-strategist gigs under a similarly named site turned up, which don't look like a genuine match. Can't confirm what the actual posting asked for.",
    },
    # -- 2026-08-19 (evening): incremental rescan --
    {
        "company": "MUBI",
        "position": "Communications Manager, US",
        "status": "Rejected",
        "applied_date": "2026-08-19",
        "source": "Ashby",
        "notes": "Rejected 2026-09-02: \"other candidates were selected whose profiles more closely "
                 "matched what we are looking for at this time.\"",
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting (Ashby): 2-3 yrs as a communications coordinator/manager, PR/publicity-focused -- awards-campaign logistics, press screenings, talent scheduling, pitching press directly, Google Docs/Adobe Suite/Mailchimp/Muck Rack. This is a press-relations discipline, not brand design or creative strategy -- outside Regina's core background even though Adobe Suite overlaps.",
    },
    {
        "company": "Tapestry",
        "position": "Associate, External Communications",
        "status": "Rejected",
        "applied_date": "2026-08-19",
        "source": "Workday",
        "notes": "Rejected 2026-08-24: application isn't progressing further.",
        "job_fit": "Weak",
        "job_fit_notes": "1-2 yrs comms/PR/journalism with a required Communications/Journalism/PR/English/Marketing degree -- a discipline mismatch against Regina's graphic design degree and visual-design core strength.",
    },
    # -- 2026-08-24: incremental rescan -- Amazon was missed by every prior
    # scan because amazon.jobs wasn't in the ATS domain list; caught by
    # widening the search after Regina asked about an interview invite.
    {
        "company": "Amazon",
        "position": "Brand Designer, Brand Innovation Lab (ID: 10525009)",
        "status": "Applied",
        "applied_date": "2026-09-05",
        "source": "Amazon Jobs",
        "notes": "Applied 2026-09-05, briefly withdrew, then reapplied the same day per Regina -- currently "
                 "a live application. Distinct from the earlier, already-rejected Art Director, Elevated "
                 "Shopping application.",
        "job_fit": "Strong",
        "job_fit_notes": "Confirmed posting (Job ID 10525009): 4+ yrs brand design at agencies or in-house "
                         "creative, Adobe Creative Suite, presentation decks, campaign work spanning film, "
                         "packaging, and social -- a strong match to Regina's Common Matter/Superside "
                         "background and tools.",
    },
    {
        "company": "Amazon",
        "position": "Art Director, Elevated Shopping (ID: 10410280)",
        "status": "Rejected",
        "applied_date": "2026-08-17",
        "source": "Amazon Jobs",
        "notes": "Online assessment completed 2026-08-18. Rejected per Amazon's own My Applications "
                 "portal (screenshot shared by Regina 2026-09-05) -- moved to Archived, \"No longer under "
                 "consideration.\" Exact rejection date not shown on the portal.",
        "job_fit": "Good",
        "job_fit_notes": "2+ yrs design, a portfolio, Adobe tools, and creative direction for premium/luxury fashion and beauty content -- Regina's design and visual-storytelling background overlaps well. On-set art direction of live photo/video shoots specifically isn't clearly evidenced on her resume, though everything else lines up and this is the application that got furthest (online assessment completed).",
    },
    # -- 2026-08-24: recruiter reached out with a meeting invite --
    {
        "company": "Duel",
        "position": "Advocacy Consultant",
        "status": "Rejected",
        "applied_date": "2026-08-18",
        "source": "Teamtailor",
        "notes": "Interviewed with recruiter Ibrahim Thomas the week of 2026-08-24. Rejected 2026-08-27: "
                 "\"we are going to move forward with other candidates for this specific role.\" He offered "
                 "to keep in touch about future openings.",
        "job_fit": "Weak",
        "job_fit_notes": "Turned out to be a sales/customer-success role (Senior Brand Advocacy Consultant, on the sales team) at a SaaS platform -- a commercial/sales discipline entirely outside Regina's brand design/creative-strategy background, which likely explains the rejection after the recruiter screen.",
    },
    # -- 2026-08-25: cold outreach emails, reported by Regina and confirmed
    # via Sent Mail -- each one a direct email to a specific person, not a
    # formal application, so logged as Networking (counts toward weekly
    # reach-out activity on the dashboard, not toward Total Applications).
    {
        "company": "Gander (Heist)",
        "position": "Design/Strategy opportunities (cold outreach)",
        "status": "Networking",
        "applied_date": "2026-08-19",
        "source": "Cold email",
        "notes": "Emailed jobs@takeagander.com and mike@takeagander.com directly, referencing the Gradience "
                 "project from Alex Center's SVA class. No reply yet.",
    },
    {
        "company": "Meta",
        "position": "Brand Strategy (cold outreach -- Heidi Keel)",
        "status": "Networking",
        "applied_date": "2026-08-25",
        "source": "Cold email",
        "notes": "Direct outreach to heidi.keel@meta.com about brand strategy work at Meta. No reply yet.",
    },
    {
        "company": "Meta",
        "position": "Brand Strategy (cold outreach -- Aisea Laungauge)",
        "status": "Networking",
        "applied_date": "2026-08-25",
        "source": "Cold email",
        "notes": "Direct outreach to aisea.laungauge@meta.com about brand strategy work at Meta. No reply yet.",
    },
    {
        "company": "Meta",
        "position": "Brand Strategy (cold outreach -- Kristina Mora)",
        "status": "Networking",
        "applied_date": "2026-08-25",
        "source": "Cold email",
        "notes": "Direct outreach to kristina.mora@meta.com about brand strategy work at Meta. No reply yet.",
    },
    {
        "company": "Meta",
        "position": "Brand Strategy (cold outreach -- Sandra Fernandez)",
        "status": "Networking",
        "applied_date": "2026-08-25",
        "source": "Cold email",
        "notes": "Direct outreach to sandra.fernandez@meta.com about brand strategy work at Meta. No reply yet.",
    },
    {
        "company": "Wieden+Kennedy",
        "position": "Brand Strategy (cold outreach -- Austin Fontenot)",
        "status": "Networking",
        "applied_date": "2026-08-25",
        "source": "Cold email",
        "notes": "Direct outreach to austin.fontenot@wk.com about a brand strategy role at W+K. No reply yet.",
    },
    {
        "company": "Wieden+Kennedy",
        "position": "Brand Strategy (cold outreach -- Lucy Truglio)",
        "status": "Networking",
        "applied_date": "2026-08-25",
        "source": "Cold email",
        "notes": "Direct outreach to lucy.truglio@wk.com about a brand strategy role at W+K. No reply yet.",
    },
    {
        "company": "Red Antler",
        "position": "Brand Strategy (cold outreach -- Brenna Ferguson)",
        "status": "Networking",
        "applied_date": "2026-08-25",
        "source": "Cold email",
        "notes": "Direct outreach to brenna.ferguson@redantler.com about a brand strategy role at Red Antler. "
                 "No reply yet.",
    },
    {
        "company": "Red Antler",
        "position": "Brand Strategy (cold outreach -- Sabrina Frometa)",
        "status": "Networking",
        "applied_date": "2026-08-25",
        "source": "Cold email",
        "notes": "Direct outreach to sabrina.frometa@redantler.com about a brand strategy role at Red Antler. "
                 "No reply yet.",
    },
    {
        "company": "Red Antler",
        "position": "Brand Strategy (cold outreach -- Deva Ferar)",
        "status": "Networking",
        "applied_date": "2026-08-25",
        "source": "Cold email",
        "notes": "Direct outreach to deva.ferar@redantler.com about a brand strategy role at Red Antler. "
                 "No reply yet.",
    },
    # -- 2026-08-26: incremental rescan --
    {
        "company": "VaynerMedia",
        "position": "Relevance Strategist",
        "status": "Rejected",
        "applied_date": "2026-08-26",
        "source": "Greenhouse",
        "notes": "Rejected via a VaynerX/Greenhouse email on 2026-09-08 (\"decided not to move forward\").",
        "job_fit": "Fair",
        "job_fit_notes": "Wants deep insider fluency in Tech/AI developer culture specifically, based in LA. Regina's cultural-research and trend-analysis skills are relevant in a general sense, but the role's specific vertical and location don't match her background or base.",
    },
    # -- 2026-08-26 (later): two more cold outreach emails, confirmed via Sent Mail --
    {
        "company": "Porto Rocha",
        "position": "Brand Strategy (cold outreach -- Natalee)",
        "status": "Networking",
        "applied_date": "2026-08-26",
        "source": "Cold email",
        "notes": "Direct outreach to natalee@portorocha.com about brand strategy work at Porto Rocha. "
                 "No reply yet.",
    },
    {
        "company": "Decade",
        "position": "Creative Strategy Opportunity (cold outreach)",
        "status": "Networking",
        "applied_date": "2026-08-26",
        "source": "Cold email",
        "notes": "Direct outreach to hello@decadenewyork.com introducing herself for creative strategy "
                 "work. No reply yet.",
    },
    # -- 2026-09-02: widened rejection-pattern search turned up 2 applications
    # that every prior scan had missed entirely (neither their confirmation nor
    # their outcome email matched the ATS-domain/explicit-rejection search) --
    {
        "company": "Datadog",
        "position": "Lead Designer",
        "status": "Rejected",
        "applied_date": "2026-08-18",
        "source": "Email",
        "notes": "Missed entirely by every prior scan -- confirmation email came from "
                 "no-reply@datadoghq.com, not a domain in the ATS search list. Rejected 2026-08-20: "
                 "\"we have decided not to move forward with your application at this time.\"",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm the exact 'Lead Designer' posting -- Datadog's design roles "
                         "found in this range (Lead UX Designer, Staff Visual/Product Designer) are all "
                         "senior UX/product-design specialist tracks (6-10+ yrs) rather than brand/graphic "
                         "design, which would be a stretch for Regina's background, but the specific listing "
                         "she applied to can't be verified.",
    },
    {
        "company": "Ogilvy",
        "position": "Designer",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "Email",
        "notes": "Missed entirely by every prior scan -- confirmation email came from no-reply@ogilvy.com, "
                 "not a domain in the ATS search list. No response yet as of 2026-09-02. Resubmitted via a "
                 "Greenhouse security-code verification step on 2026-09-05 (security-code email then a "
                 "second \"thank you for applying\" confirmation, both for the same Designer role) -- treated "
                 "as the same application, not double-counted.",
        "job_fit": "Good",
        "job_fit_notes": "The closest generalist-titled match found is a 3-5 yr Graphic Designer posting: "
                         "advanced Adobe Creative Suite, working Figma knowledge, client-branding-guideline "
                         "layout work -- a solid match for Regina's tools and design background, though the "
                         "confirmation email didn't specify a seniority level so this exact posting isn't "
                         "fully confirmed.",
    },
    # -- 2026-09-05 (later still): incremental rescan, 3 more new rows --
    {
        "company": "Bumble",
        "position": "Graphic Designer",
        "status": "Applied",
        "applied_date": "2026-09-05",
        "source": "Ashby",
        "notes": None,
        "job_fit": "Good",
        "job_fit_notes": "3+ yrs graphic design (tech sector preferred, not required), in-house creative "
                         "studio work across print/digital/social/campaign -- a good match for Regina's "
                         "Common Matter and Superside background, with tech-industry experience as the one "
                         "soft preference she doesn't have.",
    },
    {
        "company": "Landor",
        "position": "Designer",
        "status": "Applied",
        "applied_date": "2026-09-05",
        "source": "Greenhouse",
        "notes": "Generic Greenhouse confirmation didn't name the role; title confirmed from Regina's copy "
                 "of the New York posting. Distinct from the earlier Design Bridge and Partners / Landor "
                 "(WPP) Senior Strategist application (applied 2026-07-24, Interviewing) -- that one came "
                 "through a different recruiter contact and ATS instance.",
        "job_fit": "Strong",
        "job_fit_notes": "Confirmed posting: 2+ yrs brand-focused design, building brands from scratch or "
                         "refreshing them, Adobe Creative Suite, a comprehensive portfolio -- a close, "
                         "direct match to Regina's Common Matter brand-design background and tools.",
    },
    {
        "company": "Gigs",
        "position": "Senior Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-05",
        "source": "Greenhouse",
        "notes": "Generic Greenhouse auto-reply confirmation didn't name the role; title confirmed from "
                 "Regina's copy of the posting. New York, salary range $170K-$200K.",
        "pay_range": "$170K-$200K/yr",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: Figma/Adobe CS proficiency and agency/scale-up background line "
                         "up with Regina's experience, but the role explicitly requires strong motion-design "
                         "skills (After Effects, 'bring assets to life') as a core skill, not a nice-to-have "
                         "-- that isn't evidenced anywhere on her resume. Fintech familiarity is called out "
                         "as a plus, which she also doesn't have.",
    },
    # -- 2026-09-05: networking calls reported directly by Regina, backfilled
    # from her own memory/calendar/LinkedIn messages (not a Gmail scan find) --
    {
        "company": "Interbrand",
        "position": "Networking call -- Jennifer Passas",
        "status": "Networking",
        "applied_date": "2026-07-30",
        "source": "Referral",
        "notes": "Networking call with Jennifer Passas, who works at Interbrand. Not tied to a specific "
                 "open role -- general relationship-building conversation.",
    },
    {
        "company": "SVA",
        "position": "Advice call -- Julia (TA)",
        "status": "Networking",
        "applied_date": "2026-08-04",
        "source": "Referral",
        "notes": "Advice call with Julia, Regina's TA at SVA -- career/job-search advice, not a job lead.",
    },
    {
        "company": "SVA",
        "position": "Advice call -- Andrew (instructor)",
        "status": "Networking",
        "applied_date": "2026-08-19",
        "source": "Referral",
        "notes": "Advice call with Andrew, one of Regina's instructors at SVA -- career/job-search advice, "
                 "not a job lead.",
    },
    {
        "company": "Anna-Rae Morris",
        "position": "Networking call",
        "status": "Networking",
        "applied_date": "2026-08-31",
        "source": "LinkedIn",
        "notes": "Networking call with Anna-Rae Morris via LinkedIn outreach. Regina may have a follow-up "
                 "call with her -- not yet confirmed/scheduled.",
    },
    {
        "company": "Angel Bellon",
        "position": "Networking call (Cultural Intelligence + Foresight consultant, Parsons faculty)",
        "status": "Networking",
        "applied_date": "2026-09-08",
        "source": "LinkedIn",
        "notes": "Scheduled networking call with Angel Bellon -- independent cultural-intelligence/foresight "
                 "consultant and Parsons faculty. Not yet happened as of 2026-09-05.",
    },
    {
        "company": "Mother",
        "position": "Networking call -- Maggie Murphy, Strategy Director",
        "status": "Networking",
        "applied_date": "2026-09-10",
        "source": "Referral",
        "notes": "Scheduled follow-up call with Maggie Murphy, Strategy Director at Mother -- grew out of the "
                 "2026-07-30 Mother Intro Call. Not yet happened as of 2026-09-05.",
    },
    # -- 2026-09-05: incremental rescan, 3 new rows --
    {
        "company": "Notion",
        "position": "Brand Designer, Creative Studio",
        "status": "Applied",
        "applied_date": "2026-09-05",
        "source": "Greenhouse",
        "notes": None,
        "job_fit": "Good",
        "job_fit_notes": "5+ yrs agency/in-house design, strong Figma/Adobe CC, brand storytelling across "
                         "launch campaigns -- a solid match for Regina's design background and tools. "
                         "Animation/motion/illustration/coding is listed as one of several optional "
                         "'specialist skillset' additions rather than a hard requirement, and mentoring "
                         "isn't clearly evidenced on her resume.",
    },
    {
        "company": "PepsiCo",
        "position": "Graphic Designer - poppi (2026-470592)",
        "status": "Applied",
        "applied_date": "2026-09-05",
        "source": "iCIMS",
        "notes": "Third, distinct PepsiCo application, for the poppi brand specifically -- separate from "
                 "the Design Senior Manager - Immersive (applied 07-29) and Brand Designer (applied 08-17) "
                 "roles already tracked.",
        "job_fit": "Strong",
        "job_fit_notes": "3+ yrs graphic design with a strong packaging/print-production portfolio, Adobe "
                         "CS, translating brand guidelines into production-ready assets, independent project "
                         "ownership -- nearly a direct match to Regina's Common Matter packaging/print/"
                         "brand-guideline execution work.",
    },
    {
        "company": "Finch",
        "position": "Brand and Web Designer",
        "status": "Rejected",
        "applied_date": "2026-09-05",
        "source": "Lever",
        "notes": "Rejected via a Lever email on 2026-09-08 evening (\"decided to move forward with other applicants\").",
        "job_fit": "Good",
        "job_fit_notes": "6+ yrs brand/visual design with an agency background, Figma/Adobe CS, comfort "
                         "with AI-assisted design tools, systems thinking across brand/web/print -- strong "
                         "general overlap with Regina's background. Gaps: Webflow isn't evidenced on her "
                         "resume, and the role prefers B2B SaaS/tech-company experience, while her agency "
                         "work has been consumer/entertainment/food/beauty/cultural rather than tech.",
    },
    # -- 2026-09-03 (later): incremental rescan, 1 new row --
    {
        "company": "MrBeast",
        "position": "Senior Brand Strategist",
        "status": "Applied",
        "applied_date": "2026-09-03",
        "source": "Greenhouse",
        "notes": "Generic Greenhouse auto-reply confirmation didn't name the role; confirmed from the "
                 "LinkedIn listing Regina shared (same Greenhouse instance, mrbeastyoutube).",
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting ($135.7K-$170.2K target comp): 8-10+ yrs in Strategy/Planning "
                         "at a top-tier digital publisher/social platform/agency, proven leadership on "
                         "seven-figure multi-platform integrated partnership deals, deep YouTube/TikTok/"
                         "Instagram ad-format fluency. Regina's ~6-7 yrs is well under the bar, and the "
                         "digital-publisher partnership-sales scope isn't evidenced on her resume.",
    },
    # -- 2026-09-03: incremental rescan, 3 new rows --
    {
        "company": "Accenture (Droga5)",
        "position": "Senior Strategist (R00348814)",
        "status": "Rejected",
        "applied_date": "2026-09-03",
        "source": "Workday",
        "notes": "Distinct req ID from the earlier, already-rejected Droga5 Senior Strategist application "
                 "(R00338279) -- same role title/team, likely a reposted opening. Kept as a separate row "
                 "since it carries its own reference ID and confirmation email. Rejected via a Workday email "
                 "on 2026-09-11 (\"unable to move forward at this time\").",
        "job_fit": "Fair",
        "job_fit_notes": "Same role type as the earlier Droga5 Senior Strategist application (R00338279, "
                         "rejected): Droga5 wants someone whose career has been in the strategist seat, "
                         "which doesn't fully match Regina's design-led background with a strategy overlay. "
                         "Worth noting this is effectively a second shot at a role Accenture already passed "
                         "on her for once.",
    },
    {
        "company": "Nourish",
        "position": "Senior Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-09-03",
        "source": "Greenhouse",
        "notes": "Generic Greenhouse auto-reply confirmation didn't name the role; confirmed from the "
                 "LinkedIn listing Regina shared (same Greenhouse instance, usenourish).",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: 5-7 yrs creative strategy/growth marketing owning the creative "
                         "roadmap for paid channels. Regina's creative-strategy and storytelling skills "
                         "overlap, but the role is explicitly performance-marketing-driven -- \"fluent in "
                         "performance data,\" pattern-matching across ad tests, growth KPIs -- and that "
                         "data-driven growth-marketing fluency isn't evidenced on her resume.",
    },
    {
        "company": "Disney",
        "position": "Associate Manager, Brand Strategy",
        "status": "Applied",
        "applied_date": "2026-09-03",
        "source": "Workday",
        "notes": None,
        "job_fit": "Good",
        "job_fit_notes": "Couldn't confirm this exact posting, but Disney's closely related 'Marketing "
                         "Strategy Associate Manager' role wants 2+ yrs marketing strategy/content/brand "
                         "marketing, strong writing, and cross-functional collaboration with creative, PR, "
                         "and digital teams -- content/photo-video production oversight is preferred, not "
                         "required. Regina's creative-brief, presentation, and research skills line up well "
                         "with the core bar, though the exact req isn't fully confirmed.",
    },
    # -- 2026-09-02: applied directly + reached out to a team contact same day --
    {
        "company": "Monks",
        "position": "Associate Director, Comms Planning",
        "status": "Rejected",
        "applied_date": "2026-09-02",
        "source": "Email",
        "notes": "Applied through the official posting and separately emailed Olga Gamer "
                 "(olga.gamer@monks.com) directly the same day, referencing her Superside experience "
                 "and attaching a tailored CV. Confirmation email (no-reply@monks.com) titles the role "
                 "\"Associate Director, Comms Planning\"; the outreach email to Olga said \"Associate "
                 "Strategy Director, Comms Planning\" -- same role, minor title variant. Rejected same day: "
                 "Olga replied she can't hire candidates who will require visa sponsorship, even in the "
                 "future -- a visa/authorization issue, not a skills-based rejection.",
        "job_fit": "Fair",
        "job_fit_notes": "Wants 5 years in a media agency (3+ specifically in Connections/Comms Strategy) plus direct-report management. Regina's research, deck-building, and narrative-writing skills overlap qualitatively, but this is a media/comms-planning discipline rather than brand/creative design, and her 6 years are mostly design-agency rather than media-agency -- plus people-management isn't evidenced on her resume. Note: the actual rejection was a visa-sponsorship policy, not a skills mismatch -- the fit rating above reflects the role's substance, not the reason it didn't move forward.",
    },
    # -- 2026-09-06 incremental rescan --
    {
        "company": "Bain & Company",
        "position": "Strategic Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Email",
        "notes": None,
        "job_fit": "Weak",
        "job_fit_notes": "Couldn't confirm the exact posting, but Bain's Strategic Design roles (Manager/"
                         "Senior Strategic Designer family) center on UX, service design, and digital-product "
                         "design -- design thinking, prototyping, Figma/Miro/Webflow fluency, plus ~30% client "
                         "travel in a consulting environment. That's a different discipline from Regina's "
                         "brand/graphic-design background, which doesn't show UX/service-design or product "
                         "prototyping work.",
    },
    {
        "company": "Meta",
        "position": "Designer, Creative X (Reality Labs)",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Email",
        "notes": "Confirmation email didn't name a specific team or seniority -- generic \"Designer role\" "
                 "at Meta. Confirmed from the LinkedIn listing Regina shared as a Creative X / Reality Labs "
                 "role (wearables and metaverse brand design). Distinct from the 4 other Meta applications "
                 "already tracked (Creative Strategist NA team, Brand Strategist -- rejected, and the two "
                 "Instagram Brand Studio roles).",
        "pay_range": "$122K-$175K/yr",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 5+ yrs brand design (agency/in-house), multidisciplinary brand "
                         "identities/design systems/template-driven creative programs, Figma/Adobe CS, "
                         "directing external creative partners, presenting to stakeholders -- a strong match "
                         "to Regina's Common Matter agency background. Familiarity with wearables/VR is "
                         "called a plus, not required, and isn't evidenced on her resume.",
    },
    {
        "company": "Havas",
        "position": "Graphic Design Intern",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Workday",
        "notes": None,
        "pay_range": "$18-22/hr",
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting: Havas's Graphic Design Intern program targets rising juniors/"
                         "seniors/recent grads working toward a Bachelor's degree, $18-22/hr, a 4-month "
                         "structured internship. Regina's Adobe/typography/layout skills match the day-to-day "
                         "work, but the program is explicitly a student pipeline -- a seniority mismatch given "
                         "her 6 years of professional experience, not a skills gap.",
    },
    {
        "company": "City of New York",
        "position": "Graphic Design Intern (ref. 781366)",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "SmartRecruiters",
        "notes": None,
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting (NYC Jobs, ref. 781366): civil-service title \"College Aide\", "
                         "experience level \"Student\" -- this role is explicitly reserved for current college "
                         "students, not working professionals. Same seniority mismatch as the Havas "
                         "internship above, unrelated to Regina's actual design skills.",
    },
    # -- 2026-09-06 (later still): 5 more new rows found after the prior pass --
    {
        "company": "Gensler",
        "position": "Multimedia + Graphic Designer, Marketing",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Workday",
        "notes": None,
        "pay_range": "$70K-$85K/yr",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting ($70K-$85K): print production and digital-delivery design work "
                         "overlaps with Regina's background, but the role explicitly wants someone who "
                         "\"works in motion as fluently as in layout\" -- videography, video editing, and "
                         "animation are core requirements, not nice-to-haves, and that isn't evidenced on "
                         "her resume.",
    },
    {
        "company": "Hypha",
        "position": "Visual Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Ashby",
        "notes": "Confirmed posting (Regina shared the full listing): the job page's own title is "
                 "\"Visual Designer\" but the body describes it as a \"Brand Designer\" role -- a title "
                 "inconsistency in Hypha's own posting, not a separate role.",
        "pay_range": "$80K-$100K/yr",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting ($80K-$100K): 1-3 yrs brand/visual design experience (or an "
                         "exceptional portfolio in place of it), Figma fluency, launch/campaign creative, "
                         "and translating brand into product tokens/components -- a solid match for Regina's "
                         "design and systems-thinking background. The role also leans heavily on daily "
                         "generative-AI tool use and AI-assisted coding (Claude Code/Cursor/v0) to implement "
                         "designs directly, which isn't evidenced on her resume.",
    },
    {
        "company": "Vestwell",
        "position": "Senior Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Greenhouse",
        "notes": "Resubmitted via a Greenhouse security-code verification step the same session (security-"
                 "code email immediately followed by the \"thank you for applying\" confirmation) -- treated "
                 "as one application, not double-counted.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: a high-ownership role independently running brand design across "
                         "every channel and building/maintaining a design system, which lines up well with "
                         "Regina's brand-systems background -- but it explicitly requires hands-on HubSpot "
                         "CMS experience (building/deploying landing pages and emails directly in HubSpot), "
                         "which isn't evidenced on her resume, and it's a solo-owner Senior-level scope.",
    },
    {
        "company": "Brick",
        "position": "Growth Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Greenhouse",
        "notes": "Generic Greenhouse auto-reply confirmation didn't name the role, but Regina shared the "
                 "LinkedIn listing (same Greenhouse apply link) confirming it was this Growth Designer role.",
        "pay_range": "$90K-$110K/yr",
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting ($90K-$110K): 3-5 yrs growth/marketing/performance design, expert "
                         "Figma/Illustrator/Photoshop, but the role is specifically performance-marketing ad "
                         "creative -- direct-response hierarchy, paid-social testing/iteration, CTR/CPA/CVR "
                         "literacy. That's a different discipline from Regina's brand-identity/creative-"
                         "agency background; the tool overlap is real but the performance-marketing focus "
                         "and metrics fluency aren't evidenced on her resume.",
    },
    {
        "company": "The Working Assembly",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Google Form",
        "notes": "Applied via the agency's own Google Form (not an ATS) -- Regina listed $95,000 as her "
                 "salary expectation on the form.",
        "job_fit": "Strong",
        "job_fit_notes": "Confirmed posting: 3-5+ yrs at a branding/creative agency, crafting brand "
                         "identities across visual identity, packaging, and creative campaigns -- a close, "
                         "direct match to Regina's Common Matter agency background.",
    },
    {
        "company": "Meta",
        "position": "Brand Designer, Iconography & Illustration - Instagram Brand Studio",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Email",
        "pay_range": "$149K-$209K/yr",
        "notes": "5th, distinct Meta application -- same Instagram Brand Studio team as the existing "
                 "\"Brand Designer, Strategic Initiatives\" role (applied 07-26) but a different req/"
                 "specialization within it.",
        "job_fit": "Weak",
        "job_fit_notes": "Full posting text confirmed (updated from an earlier search-summary estimate): "
                         "8+ years of experience specifically in iconography/illustration/visual design with "
                         "a systematic icon program focus is a hard minimum qualification, plus a portfolio "
                         "demonstrating dedicated icon-system and illustration craft. Regina's ~6 yrs is "
                         "under the bar, and illustration/iconography isn't a demonstrated specialty on her "
                         "resume -- the earlier Fair rating undersold how senior and specialist this req is.",
    },
    # -- 2026-09-06 (evening): 2 more new rows --
    {
        "company": "Fanatics Collectibles",
        "position": "Graphic Designer II",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Greenhouse",
        "notes": None,
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 3-5 yrs graphic design, Adobe Creative Suite (Photoshop/"
                         "Illustrator/InDesign), branding/typography/layout/print-production work across "
                         "product lines -- a solid, direct match to Regina's tools and design background.",
    },
    {
        "company": "United Legwear Company",
        "position": "Senior Designer, KIDS (Scotch & Soda)",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "ADP",
        "notes": "Generic ADP-based confirmation email didn't name the role, but Regina shared the LinkedIn "
                 "listing (same ADP apply link) confirming it was this Scotch & Soda Kids design role.",
        "pay_range": "$100K-$130K/yr",
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting ($100K-$130K): 5+ yrs children's-apparel design experience, "
                         "hands-on with PLM systems and tech-pack/CAD development for garment production -- "
                         "an apparel/product-design discipline (fabric, fit, garment tech packs) entirely "
                         "distinct from Regina's brand/graphic-design background, with no PLM or apparel "
                         "production experience evidenced on her resume.",
    },
    # -- 2026-09-06 (night): 4 more new rows --
    {
        "company": "Amazon",
        "position": "Designer, Premium, Elevated Shopping (ID: 10523835)",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Amazon Jobs",
        "notes": "3rd, distinct Amazon application, same Elevated Shopping product family as the earlier "
                 "Art Director (rejected) and Brand Designer, Brand Innovation Lab (active) roles.",
        "pay_range": "$132.5K-$185K/yr",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: Bachelor's degree, 5+ yrs graphic design with proven premium "
                         "fashion/beauty sector expertise, branding guidelines/corporate identity, print and "
                         "digital layout design, email marketing and social media design -- a strong match to "
                         "Regina's 6-7 yrs agency background across consumer/beauty/cultural brands (Common "
                         "Matter, Superside). AI-tooling fluency and UX-adjacent experience are called out but "
                         "framed as a plus, not a hard requirement.",
    },
    {
        "company": "Assembled",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Ashby",
        "notes": None,
        "pay_range": "$150K-$190K/yr",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 5-8 yrs brand design, strong portfolio (opinionated brand work "
                         "plus practical conversion-driven marketing assets), full Adobe/Figma suite -- a "
                         "solid match to Regina's experience and tools. The role's framing around actively "
                         "adopting AI tools into a design workflow isn't clearly evidenced on her resume.",
    },
    {
        "company": "Ripple",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Greenhouse",
        "notes": "Generic Greenhouse auto-reply confirmation didn't name the role; confirmed as the New York "
                 "Brand Designer opening (not the separate San Francisco Senior Brand Designer role) from the "
                 "LinkedIn listing Regina shared.",
        "pay_range": "$112K-$120K/yr",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 4+ yrs brand design, a portfolio spanning graphic design/web/"
                         "motion/typography/physical builds, Figma + Adobe CS -- a solid general match to "
                         "Regina's brand-design background and tools. Motion/illustration is called a plus, "
                         "not required. The crypto/Web3 subject matter (Ripple/XRP) isn't evidenced anywhere "
                         "on her resume, though the posting doesn't require industry-specific experience.",
    },
    {
        "company": "Material",
        "position": "Mid-level Brand Designer (Aruliden)",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Workday",
        "notes": "Generic Workday auto-reply confirmation didn't name the role; confirmed from the LinkedIn "
                 "listing Regina shared. Aruliden is a Material-owned multi-disciplinary design studio "
                 "(beauty/lifestyle/wellness/tech clients), New York, NY (hybrid) -- not Los Angeles as "
                 "originally assumed from a generic web search.",
        "pay_range": "$65K-$85K/yr",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 2-5+ yrs studio/agency design, brand identity systems across "
                         "packaging/digital/physical, Adobe CS + Figma, strong typography, cultural fluency "
                         "in beauty/fashion/lifestyle -- a solid match to Regina's Common Matter background. "
                         "Motion graphics is called out twice as a required skill, which isn't evidenced on "
                         "her resume.",
    },
    # -- 2026-09-06: Regina completed a previously-abandoned application --
    {
        "company": "Paramount",
        "position": "Designer, Publishing",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "SuccessFactors",
        "notes": "Started this application earlier and left it incomplete; SuccessFactors sent a \"please "
                 "complete your application\" reminder on 2026-09-06 evening (Eastern), and Regina finished "
                 "submitting it later that same evening.",
        "pay_range": "$65K-$100K/yr",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: book-cover/interior design, typography, Adobe InDesign/"
                         "Illustrator/Photoshop, print production -- Regina's design and print-production "
                         "background overlaps well. Book-publishing-specific work (covers/interiors across "
                         "formats, art directing illustrators) isn't evidenced on her resume, which is more "
                         "brand/packaging-focused.",
    },
    {
        "company": "Pentagram",
        "position": "Middleweight Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Email",
        "notes": "Direct cold-email application to Eddie Opara's team (eo_teamjobs@pentagram.com), subject "
                 "\"Middleweight Designer Role\" -- resume and portfolio (reginabbsv.cargo.site) attached.",
        "pay_range": "$85K-$105K/yr",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting (Regina shared the full listing): BA in Graphic Design, 3+ yrs "
                         "experience, strong typography and brand-systems portfolio -- Regina clears the bar "
                         "and the brand-systems/typography overlap is strong. But required tool proficiency "
                         "explicitly includes motion (Figma, After Effects, Cavalry, Cinema 4D), and motion "
                         "design isn't evidenced anywhere on her resume -- the same gap seen on several other "
                         "roles (Gigs, Gensler, Brick), and here it's a listed requirement, not a plus.",
    },
    # -- 2026-09-06 (later still): 6 more new rows --
    {
        "company": "Conveo",
        "position": "Design Lead",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Ashby",
        "notes": None,
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: 6+ yrs design with strong B2B/SaaS exposure, owning a full "
                         "brand-identity rebuild end to end, casting/directing freelance designers and "
                         "motion/illustration partners from a funded budget. Regina's years and brand-"
                         "identity craft line up, but B2B/SaaS specialization and this leadership/directing "
                         "scope (versus being the individual executor) aren't evidenced on her resume.",
    },
    {
        "company": "Figma",
        "position": "Brand Designer, Product Launches",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Email",
        "notes": "2nd, distinct Figma application -- separate from the earlier Designer Advocate, Figma "
                 "Weave role (applied 07-27).",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: distilling a strategy brief into a single compelling idea and "
                         "driving it into execution, strong composition/color/pacing especially in motion "
                         "contexts, Figma proficiency (After Effects a plus, not required). Regina's "
                         "strategic-brief and Figma/Adobe skills overlap, but the role's core craft is launch "
                         "storytelling via styleframes/storyboards/motion, which isn't a demonstrated "
                         "specialty on her resume.",
    },
    {
        "company": "Day One",
        "position": "Senior Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Pinpoint",
        "notes": "Confirmation came from D1A (Day One Agency)'s Pinpoint ATS.",
        "pay_range": "$80K-$95K/yr",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 4+ yrs at an agency/design studio, multi-disciplinary portfolio "
                         "across digital/print/experiential, Adobe CS/Figma/Keynote/PowerPoint, strong "
                         "typography -- a solid match to Regina's Common Matter agency background. "
                         "Storyboarding/animation direction is one of several listed skills, not a hard "
                         "requirement, and isn't a demonstrated core strength on her resume.",
    },
    {
        "company": "Fresh",
        "position": "Senior Designer, Digital and Social",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "SmartRecruiters",
        "notes": None,
        "job_fit": "Good",
        "job_fit_notes": "Couldn't confirm the exact posting, but Fresh's closely related Senior Digital "
                         "Designer role ($100K-$130K) and Regina's Common Matter beauty-brand digital/social "
                         "design experience line up well -- treat as a good but not fully confirmed match.",
    },
    {
        "company": "Tory Burch",
        "position": "Temporary Helper, Senior Graphic Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Workday",
        "notes": "Generic Workday auto-reply confirmation didn't name the role; confirmed from the LinkedIn "
                 "listing Regina shared. The posting's own title says \"Temporary Helper, Senior Graphic "
                 "Designer\" but the body describes a Manager-level Designer role supporting the Senior Art "
                 "Director on digital experiences -- a title/body inconsistency in Tory Burch's own posting.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 4+ yrs relevant experience (fashion industry preferred, not "
                         "required), Photoshop/InDesign/Illustrator/Keynote, developing digital experiences "
                         "for site/email/digital ads -- a good match to Regina's digital design and Adobe "
                         "tool background. Fashion-industry specifics are the one soft preference she doesn't "
                         "have evidenced.",
    },
    {
        "company": "Omnicom",
        "position": "Presentation Designer, Brand Experience (Global Growth)",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Workday",
        "notes": "Generic \"thank you for your application to the Omnicom network\" confirmation didn't name "
                 "a specific agency, team, or role; confirmed from the LinkedIn listing Regina shared. The "
                 "listing's own title says \"Design Manager\" but the body describes a \"Presentation "
                 "Designer\" role on the Brand Experience team -- a title/body inconsistency in the posting.",
        "pay_range": "$50K-$95K/yr",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 5-7+ yrs brand/graphic/experience design, PowerPoint expertise "
                         "called an \"absolute must,\" Adobe Creative Cloud, strong typography/layout/visual "
                         "storytelling -- Regina's deck-building and presentation skills (noted elsewhere, "
                         "e.g. the Omnicom Media Senior Associate Strategy application) map directly onto "
                         "this role's core requirement.",
    },
    {
        "company": "Turner Duckworth",
        "position": "Senior Designer (2026-166476)",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "iCIMS",
        "notes": "Publicis Groupe agency; confirmation came via Publicis Groupe's iCIMS instance.",
        "job_fit": "Strong",
        "job_fit_notes": "Confirmed posting: 6+ yrs concept-driven, craft-focused brand design, reporting "
                         "to a Design Director -- Turner Duckworth is a packaging/brand-identity design "
                         "agency, a close, direct match to Regina's Common Matter background and years.",
    },
    {
        "company": "Posh",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Ashby",
        "notes": None,
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting: wants past experience as the in-house creative *leader* at a "
                         "Series B-D consumer brand (e.g. Liquid Death, Poppi, Partiful), hands-on motion/"
                         "photo/film production, and deep personal ties to music/nightlife culture. This is "
                         "a senior creative-leadership scope well beyond Regina's current level, plus real "
                         "gaps in motion/film production and the nightlife-specific cultural fit.",
    },
    {
        "company": "Accenture (Work & Co)",
        "position": "Designer (R00334677)",
        "status": "Rejected",
        "applied_date": "2026-09-07",
        "source": "Workday",
        "notes": "Distinct from the three earlier Accenture/Droga5 applications -- this one is a generic "
                 "Designer req under Work & Co, Accenture Song's design studio, not Droga5. Rejected via a "
                 "Workday email on 2026-09-09, citing that Regina's application indicated she requires visa "
                 "sponsorship -- worth double-checking whether a saved Workday/EEO profile answer is "
                 "incorrectly flagging sponsorship-required across applications.",
        "job_fit": "Unknown",
        "job_fit_notes": "Could only confirm generic team-page copy for Work & Co (\"no boundary between form "
                         "and function,\" visual design/UX/UI/branding/coding) -- no years-of-experience bar or "
                         "specific requirements available for this req to rate confidently.",
    },
    {
        "company": "Fresh",
        "position": "Senior Designer, Digital and Social",
        "status": "Applied",
        "applied_date": "2026-09-07",
        "source": "SmartRecruiters",
        "notes": "Second, distinct application submission (different SmartRecruiters application ID) for the "
                 "same role and company as the 2026-09-06 Fresh application -- appears to be an accidental "
                 "duplicate resubmission rather than a second role.",
        "job_fit": "Good",
        "job_fit_notes": "Same assessment as the first Fresh application: couldn't confirm the exact posting, "
                         "but Fresh's closely related Senior Digital Designer role ($100K-$130K) and Regina's "
                         "Common Matter beauty-brand digital/social design experience line up well.",
    },
    {
        "company": "WITHIN",
        "position": "Creative Lead Fellow",
        "status": "Applied",
        "applied_date": "2026-09-08",
        "source": "Greenhouse",
        "notes": None,
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting: an 8-week paid fellowship for short-form/performance-creative "
                         "content (TikTok-style hooks, platform mechanics, fatigue/iteration), evaluated on a "
                         "public portfolio of grown social accounts or spec campaigns rather than years of "
                         "experience. This is a social-video/performance-content discipline distinct from "
                         "Regina's brand/graphic-design background, with no comparable short-form content work "
                         "evidenced on her resume.",
    },
    {
        "company": "DualEntry",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-09",
        "source": "Cold email",
        "notes": "Direct cold-email application to the DualEntry recruiter (polinan@dualentry.com), resume "
                 "attached -- Ashby was blocking a second application because of Regina's earlier, rejected "
                 "Brand Design Lead application, so she emailed directly asking to be considered for this "
                 "distinct, more junior Brand/Visual Designer opening instead.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting ($100K-$160K): owning dualentry.com and the brand system end-to-end "
                         "across web, campaigns, print, and events -- a close match to Regina's Common Matter "
                         "brand-systems background across consumer/cultural/healthcare clients. Exact "
                         "years-of-experience bar wasn't confirmable, but the role reads as more hands-on/"
                         "individual-contributor than the earlier Brand Design Lead req she was rejected from.",
    },
    {
        "company": "Omnicom Network",
        "position": "General network application (2nd)",
        "status": "Applied",
        "applied_date": "2026-09-09",
        "source": "Workday",
        "notes": "Reported directly by Regina as a 2nd, distinct Omnicom application -- generic \"thank you for "
                 "your application to the Omnicom network\" confirmation didn't name a role, and Regina didn't "
                 "specify which listing. Distinct from both the 2026-07-27 general network application and the "
                 "2026-09-06 Presentation Designer, Brand Experience application.",
        "job_fit": "Unknown",
        "job_fit_notes": "No specific role attached to confirm a posting against.",
    },
    {
        "company": "Pomegranate Gallery",
        "position": "Part Time Book Designer",
        "status": "Applied",
        "applied_date": "2026-09-10",
        "source": "SVA Career Development (12twenty)",
        "notes": "Applied through SVA's own career-services job board (12twenty), confirmed via a "
                 "screenshot of the confirmation email.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting (listed as \"Part Time Film Editor/Videographer & Graphic/Book "
                         "Designer\"): a SoHo gallery role combining film editing/videography (InDesign + "
                         "iMovie) with graphic/book design, part time and in person, Hebrew fluency a bonus. "
                         "The book/graphic-design half overlaps with Regina's background, but film editing "
                         "and videography aren't evidenced on her resume, and it's a smaller-scope part-time "
                         "gallery role rather than her usual full-time agency work.",
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
        row.setdefault("pay_range", None)
        row.setdefault("job_fit", None)
        row.setdefault("job_fit_notes", None)
        db.execute(
            """
            INSERT INTO applications
                (company, position, status, applied_date, next_step, job_url, source, referral, notes, pay_range, job_fit, job_fit_notes, created_at, updated_at)
            VALUES (:company, :position, :status, :applied_date, :next_step, :job_url, :source, :referral, :notes, :pay_range, :job_fit, :job_fit_notes, :created_at, :updated_at)
            """,
            {**row, "created_at": now, "updated_at": now},
        )
    db.commit()
    print(f"Seeded {len(SEED_ROWS)} applications from the Gmail scan.")


if __name__ == "__main__":
    main()
