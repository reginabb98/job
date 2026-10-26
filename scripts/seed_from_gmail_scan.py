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
  - 2026-09-11 (later): incremental rescan, no new rows, 1 rejection.
    Flipped NBCUniversal's Associate Manager, NBC & Peacock Marketing
    application to Rejected per a SmartRecruiters email.
  - 2026-09-12 (later): 1 new row, found via a rejection email and traced
    back to its confirmation. Noom, Senior Creative Strategist, Performance
    (applied 2026-08-26, rejected 2026-09-12, Weak fit -- a performance-
    marketing/media-buying leadership scope not evidenced on Regina's
    resume) -- missed entirely by every prior scan since its generic
    confirmation subject didn't match the search keywords.
  - 2026-09-14: incremental rescan, no new rows, 1 rejection. Flipped
    Disney's Associate Manager, Brand Strategy application to Rejected
    per a Workday email.
  - 2026-09-14 (later): incremental rescan, 3 new rows. Craft, Senior
    Designer / Freelance Senior Brand Designer / Brand Designer -- three
    distinct applications submitted within minutes of each other through
    Craft's own ATS. Craft is a UK/NY creative & design recruitment
    consultancy, not the hiring company itself, and runs many concurrently
    open, similarly-titled reqs, so the exact client listing for each
    couldn't be confirmed (all three Unknown fit).
  - 2026-09-15: incremental rescan, 3 more new rows from the same evening's
    application batch. The New York Times, Senior Designer, Games
    Marketing (Temporary) -- a 2nd, distinct NYT application, Fair fit
    (motion design is a required skill here, not evidenced on Regina's
    resume). Sapience AI Corporation, Brand Graphic Designer (best-guess
    title from their job board, generic confirmation didn't name it),
    Weak fit -- the one design req found prefers Seattle/Pacific time, a
    location mismatch. Unspecified (Ashby application) -- a fully generic
    Ashby confirmation with no company name, role, or any identifying
    detail at all; likely part of the same application session but the
    company couldn't be determined.
  - 2026-09-15 (later, reported directly by Regina, screenshot): 1 new
    row, found via a rejection email and traced back to its confirmation.
    DEPT, Principal, Visual Design (applied 2026-09-14, part of the same
    evening's application batch; rejected 2026-09-15, Weak fit -- a
    Principal-level design-leadership/UX scope well beyond Regina's
    brand/graphic-design background) -- missed by the prior two rescans
    since its confirmation subject ("Whoo! We've received your
    application!") didn't match the search keywords.
  - 2026-09-15 (later): incremental rescan, 1 new row. TUSHY, Creative
    Strategist, Unknown fit -- couldn't confirm the exact posting; TUSHY's
    own board only showed a differently-titled, more senior Associate
    Director, Creative req.
  - 2026-09-15 (evening): incremental rescan, 2 new rows. Compass, Senior
    Designer (Good fit -- closest match found is a Senior Graphic
    Designer role on their in-house Creative Studio, brand/campaign/print
    work with Adobe + Figma, a solid match to Regina's background). FLORA,
    Creative Generalist (Contract), Unknown fit -- couldn't confirm the
    exact posting among FLORA's differently-titled Ashby listings.
  - 2026-09-16: incremental rescan, 2 new rows from the prior evening.
    Made Thought, Senior Designer (Good fit -- confirmed posting, a
    London creative studio wanting graphic design/art direction/strategy
    craft, a strong match to Regina's agency background). Profound, Brand
    Designer (Good fit -- a well-funded AI marketing-analytics startup
    wanting a Brand Designer to define its look/feel as it scales, solid
    general match though specific requirements weren't confirmable).
  - 2026-09-16 (reported directly by Regina, screenshot): 2 new rows,
    found via a Gmail Sent search. Combo, Senior Brand Designer -- a
    direct cold-email application (jobs@combo.co), Unknown fit since no
    actual posting could be found. Saint Urbain, Senior Designer -- a
    direct cold-email application (work@sainturbain.com) in response to
    a LinkedIn post, Strong fit -- an independent branding/strategy/
    design studio, a close match to Regina's branding-studio, Superside,
    and SVA Branding Master's background.
  - 2026-09-17: incremental rescan, no new rows, 1 rejection. Flipped
    Compass's Senior Designer application to Rejected per a Greenhouse
    email.
  - 2026-09-18: logged a networking call with Andie Wexler (30-min
    Google Meet booked via Calendly), Sept 16, 2026, reported directly
    by Regina. Only a Calendly confirmation email was found in Gmail --
    company/context unconfirmed.
  - 2026-09-18 (later): incremental rescan, 2 new rows, 2 flips. New
    York Times -- Senior Strategist (3rd distinct NYT application,
    Unknown fit -- couldn't confirm which of several same-titled NYT
    postings this was). Ripple -- Senior Brand Designer, Rejected
    (distinct from the already-tracked NY Brand Designer role; likely
    the separate SF opening referenced in that row's notes, inferred
    applied_date from the original ambiguous 09-06 confirmation).
    Flipped Made Thought's Senior Designer application to Rejected.
    Flipped Day One's Senior Designer application to Interviewing --
    an external recruiter (Angela, thechangeagents.co) reached out to
    schedule a call; not yet booked.
  - 2026-09-19: 1 new row, reported directly by Regina with the full
    posting shared. Perplexity -- Brand Designer, Growth, Fair fit
    ($150K-$225K + equity; strong on brand/visual craft, but the role's
    core growth-performance-data-driven iteration isn't a demonstrated
    specialty on her resume).
  - 2026-09-19 (later): incremental rescan, no new rows. Day One's
    interview with Angela got booked -- Google Meet confirmed for
    Monday, Sept 21, 2026, 1:00-1:25pm ET.
  - 2026-09-19 (evening): 1 new row, traced back after Regina flagged
    it from a LinkedIn applicant-insight screenshot. OLIVER -- Senior
    Designer, Good fit -- a distinct 3rd OLIVER application (global
    financial-services account, in-house-agency model), missed by
    prior scans; confirmation found via targeted search.
  - 2026-09-19 (evening rescan): incremental rescan, 1 new row. OLIVER
    -- Senior Designer (2nd application), Unknown fit -- a 4th, distinct
    OLIVER confirmation for a same-titled posting, 13 days after the
    first; OLIVER runs many concurrent Senior Designer reqs, so this
    reads as a separate opening rather than a duplicate.
  - 2026-09-20: 1 new row, traced back after a rejection surfaced for
    an application prior scans had missed. BritBox International --
    Senior Designer, Fair fit (entertainment key art for BBC Studios'
    streaming brand; typography/Photoshop craft lines up, but key art
    is a niche not evidenced on her resume). Applied 09-14, rejected
    09-20.
  - 2026-09-21: incremental rescan, no new rows, 1 rejection. Flipped
    Gensler's Multimedia + Graphic Designer, Marketing application to
    Rejected.
  - 2026-09-21 (later): reconciled against a fresh Accenture candidate-
    portal screenshot (My Applications, all 4 "No Longer Under
    Consideration"). Flipped the LinkedIn-sourced Accenture "Creative
    Agency Senior Designer" application (in seed_from_linkedin.py) to
    Rejected -- the other 3 (both Droga5 Senior Strategist reqs, Droga5
    Senior Designer) were already Rejected.
  - 2026-09-21 (evening rescan): incremental rescan, 1 new row.
    Accenture -- Creative Agency Senior Designer (2nd application),
    Strong fit -- a second, distinct Workday confirmation for the same
    role she was rejected from on 07-27, likely a reposted req.
  - 2026-09-21 (later still): incremental rescan, no new rows, 1
    rejection. Flipped Figma's Designer Advocate, Figma Weave
    application to Rejected.
  - 2026-09-22: reported directly by Regina (LinkedIn message
    screenshot), not from a Gmail scan. Anna Callagher, Lead Recruiter
    @ Craft, messaged asking to book a call about one of Regina's three
    Craft applications (Senior Designer, Freelance Senior Brand
    Designer, Brand Designer -- all applied 09-14) without saying
    which. Regina doesn't know either and asked Anna to clarify -- no
    status change yet; noted on all three pending an answer.
  - 2026-09-22 (later): 1 new row, found via Gmail Sent search. The
    Collected Works -- Brand Designer, Good fit. Direct cold-email
    application to jobs@thecollectedworks.com, resume attached; no
    listed opening, general outreach to an SVA-founded NYC/New Orleans
    identity/motion/3D design studio.
  - 2026-09-22 (later still): reported directly by Regina, not from a
    Gmail scan. Flipped all three PepsiCo job applications (Design
    Senior Manager - Immersive, Brand Designer, Graphic Designer -
    poppi) to Rejected -- an HR contact told her PepsiCo likely doesn't
    sponsor visas. Left the separate PepsiCo Networking outreach row
    (contact: Hillary) untouched since it's a contact, not an
    application to reject.
  - 2026-09-22 (evening): reported directly by Regina, who shared the
    full LinkedIn posting for the NYT Senior Strategist application
    (previously Unknown fit since the exact req couldn't be pinned
    down). Confirmed as the T Brand Studio Creative Strategy team req
    (REQ-020117, $90K-$100K, 173 applicants) -- updated to Fair fit,
    same strategy-track-career gap seen on the Droga5 and Design
    Bridge/Landor Senior Strategist roles.
  - 2026-09-22 (later): 1 new row, reported directly by Regina with the
    full posting shared. BBDO -- Senior Strategist, Fair fit
    ($95K-$110K/yr; same dedicated-strategist-career gap seen on the
    other Senior Strategist rows).
  - 2026-09-22 (still later): reported directly by Regina, full
    postings shared for two previously Unknown-fit cold/generic
    applications. OLIVER's 2nd Senior Designer application (applied
    09-19) updated to Fair fit (Req 18584, $114,750-$128,250, hybrid 4
    days/wk -- a high-volume regulated-industry account with real team-
    management and budget-ownership scope beyond IC design, not fully
    confirmed as the exact req behind that confirmation email). Combo's
    Senior Brand Designer cold-email application updated to Good fit
    (6+ yrs studio/agency, brand identity/packaging/campaign/UI
    portfolio -- a strong match to her Common Matter background).
  - 2026-09-22 (evening rescan): incremental rescan, 3 new rows.
    Monster Energy -- Senior Graphic Designer, Americas, Fair fit
    (Corona, CA-based, no remote/NYC arrangement confirmed). Born
    Social -- Associate Creative Director [NYC], Unknown fit (exact
    posting not found on their board). A third row logged as "Omnicom
    Network -- General network application (3rd)" was removed after
    Regina clarified it wasn't a separate general application -- it
    was the confirmation for the same-day BBDO Senior Strategist
    application (BBDO is part of Omnicom's network and routes through
    their shared Workday ATS). Merged that confirmation detail into
    the existing BBDO row instead.
  - 2026-09-22 (later still): added a `had_interview` field, separate
    from current `status`, so an application that reached an interview
    call keeps that fact even if it's later Rejected (Regina pointed
    out the "2 Interviewing" stat undercounts real interview calls).
    Backfilled `had_interview: 1` on the 3 rows confirmed to have had
    an actual interview/screening call: Design Bridge and Partners /
    Landor (Interviewing), Day One (Interviewing), and Duel (Rejected
    after a recruiter screen).
  - 2026-09-22 (yet later): Regina booked the Craft call with Anna
    Callagher for Wednesday, Sept 23 and asked again which of the 3
    Craft applications it's for -- still unanswered. Added a
    `next_step` note to all three flagging the booked call, but
    deliberately did not set `had_interview` on any of them yet, since
    doing so on all three would triple-count a single call and picking
    just one would be a guess.
  - 2026-09-22 (rescan): incremental rescan, 1 new row, 1 rejection.
    Flipped Accenture's 2nd Creative Agency Senior Designer application
    to Rejected -- same visa-sponsorship template as the earlier Work &
    Co Designer rejection. Added a new Craft Networking row: Fionn
    Andrews, a separate Craft recruiter (freelance placement arm, not
    the same person as Anna Callagher) who already had a call with
    Regina and is onboarding her onto Craft's "Taste" freelance-project
    platform -- distinct from the still-unresolved Anna Callagher call
    about one of the 3 full-time Craft applications.
  - 2026-09-22 (later rescan): incremental rescan, 1 new row, 2
    rejections. Flipped both Fresh -- Senior Designer, Digital and
    Social applications (09-06 and its 09-07 duplicate) to Rejected --
    two separate but identical rejection emails, ~25 min apart. New
    row: Craft (Taste freelance platform) -- Senior Designer, Brand
    Guidelines and Identity, Offer status -- Regina applied to this
    Taste freelance project the same day she was onboarded by Fionn,
    submitted a design assessment, and was selected to move forward
    with a Master Freelance Agreement/Statement of Work being sent, all
    within hours. Strong fit (brand guidelines/identity is her core
    specialty). Flagged to Regina as a new Offer-status result.
  - 2026-09-22 (yet later): 1 new row, found via Gmail Sent search.
    Mischief -- Networking outreach, no open role (contact: Robyn) --
    warm-intro cold email referred by Sadia; company isn't hiring, no
    resume attached, no specific role, so logged as Networking rather
    than a job application.
  - 2026-09-22 (final): 1 new row, found via Gmail Sent search. LOS
    YORK -- Freelance Brand Strategist, Good fit. Direct cold-email
    application to katy.b@losyork.tv in response to a LinkedIn post,
    resume attached; no formal posting found, but LOS YORK is an LA/NY
    multidisciplinary creative production studio (Amazon, Netflix,
    Logitech) -- a solid general match to Regina's brand-strategy
    background, tilted more toward video/content than her usual
    identity/print work.
  - 2026-09-22 (rescan): incremental rescan, no new rows. Day One's
    interview call with Angela happened Monday, Sept 21 as scheduled --
    she followed up 09-22 asking for an updated resume, which Regina
    sent same day. Updated next_step accordingly; still Interviewing.
  - 2026-09-23 (later): 1 new row, found via Gmail -- no original
    confirmation email or Sent-mail record exists for this application.
    Canopy -- Graphic Designer, Unknown fit, status Interviewing --
    Katy Spore (Senior Graphic Designer) invited Regina directly to
    pick a time for a 30-min intro call; applied_date is a placeholder
    since the true application date couldn't be traced.
  - 2026-09-23 (correction): Anna Callagher's (Craft) call happened
    today as scheduled, but she never confirmed which of the 3 Craft
    applications it was for. Per Regina's request, picked one --
    Craft -- Senior Designer -- to hold Interviewing status and
    had_interview=1 for now; the other two Craft rows stay Applied.
    Flagged in all three rows' next_step/notes as a placeholder
    assignment to be corrected once Anna confirms the actual role.
  - 2026-09-23 (rescan): 1 new row, 2 updates. Polonsky & Friends --
    Junior Graphic Designer, Fair fit -- new internship application
    (20 hrs/week, 6-12 months) found via referral, applied same day.
    The New York Times -- Senior Designer, Games Marketing (Temporary)
    flipped to Rejected (generic decline email). Canopy's next_step
    updated: the intro call with Katy Spore is now confirmed for
    3:00-3:30pm ET today, not just requested.
  - 2026-09-23 (correction): Regina confirmed the identities behind two
    of the three Craft applications. Craft -- Senior Designer is Red
    Antler (the Anna Callagher call held today was for this one) --
    renamed to Red Antler, Good fit, stays Interviewing/had_interview=1.
    Craft -- Brand Designer is Vault 49 (the CPG-focused one) --
    renamed to Vault 49, Good fit. Craft -- Freelance Senior Brand
    Designer remains unresolved -- the one application whose client
    company is still unknown.
  - 2026-09-24 (update): Craft (Taste freelance platform) -- Senior
    Designer, Brand Guidelines and Identity next_step updated. Regina
    completed identity verification on the portal (2026-09-23) and
    checked in with Fionn Andrews about next steps; he confirmed it's
    now with Taste's own team to review and reach out directly, not
    something to chase with him. No other contact was named.
  - 2026-09-24 (rescan): no new rows, 2 next_step updates. Red Antler --
    Senior Designer: Regina sent Anna Callagher her strategy portfolio;
    the link didn't work on Anna's end, so it may need resending. Vault
    49 -- Brand Designer: Regina sent an updated design portfolio with
    a new packaging project; Anna said it looks great. Anna will follow
    up on her thoughts on both -- no calls scheduled yet for either.
  - 2026-09-24 (later): no new rows, 1 next_step update. Red Antler --
    Senior Designer: Regina resent the corrected strategy portfolio
    link (reginabbs.cargo.site) to Anna Callagher the same day, after
    the original link didn't work on her end.
  - 2026-09-24 (evening): no new rows, 2 flips. The New York Times --
    Senior Strategist (T Brand Studio, applied 09-18) rejected via a
    generic decline email. Day One -- Senior Designer rejected: Angela
    (The Change Agents, the recruiter handling this candidacy) confirmed
    Day One's internal policy doesn't allow considering candidates who
    may need future visa sponsorship -- not a fit/performance rejection.
  - 2026-09-25: 1 new row. Craft -- Graphic Designer, Unknown fit,
    status Applied -- a 4th, distinct Craft application, confirmed only
    via Craft's generic "application received" auto-reply. Which client
    req this is for is unconfirmed (separate from the already-resolved
    Red Antler and Vault 49 reqs, and the still-unresolved Freelance
    Senior Brand Designer one).
  - 2026-09-25 (later): 1 new row, 1 next_step update. Morning Brew --
    Associate, GTM Strategy, Fair fit -- new application, confirmed via
    Lever's auto-reply. Anna-Rae Morris (networking, JKR Global): a
    follow-up call is now being actively scheduled for the week of
    2026-09-28 after a reschedule.
  - 2026-09-26: no new rows, 1 flip. Gigs -- Senior Brand Designer
    rejected: position filled ("we have recently filled this
    position").
  - 2026-09-27: no new rows, 1 next_step update. Craft (Taste freelance
    platform) -- Senior Designer, Brand Guidelines and Identity: Taste
    confirmed the concrete project assignment ("GoldenStone Slides &
    Docs", role Brand Designer), rate ($85/hr, $510/deliverable), and
    start date (Thursday, Oct 1, pending ID/background check). Stays
    Offer status.
  - 2026-09-28: 8 new rows, an application sprint late on 2026-09-27.
    2x4 -- Design Intern / Branding (Fair) and Designer / Digital (Good),
    both direct cold emails to the studio. Onebrief -- Senior Brand
    Designer (Good, AI military-planning software). Meta -- Brand
    Designer, Foundations - Instagram Brand Studio (Fair, 6th distinct
    Meta application). Profound -- Brand Designer (Good, AI marketing
    platform). HappyRobot -- Brand Designer (Good, AI-worker
    infrastructure). OLIVER -- Senior Designer, 3rd application (Unknown,
    generic confirmation, client/req unconfirmed). Thyme Care -- Visual
    Designer, Marketing (Good, oncology care company). All confirmed via
    ATS auto-replies (Ashby/Greenhouse) except the two 2x4 cold emails.
  - 2026-09-28 (later): 8 more new rows, continuation of the same
    2026-09-27 application sprint (later that same night), plus 1
    next_step update. ShopMy -- Unspecified role/Design (Unknown, generic
    confirmation, multiple open design roles). Rightway -- Sr. Graphic
    Designer (Good, healthcare-navigation tech). Code and Theory --
    Unspecified role/Design (Unknown, generic confirmation, multiple
    open designer roles). SHADOW -- Designer (Good, creative agency).
    webAI -- Marketing Designer (Unknown, no posting found). The
    Farmer's Dog -- Brand Designer (Good, DTC pet food). Fanatics
    Collectibles -- Senior Graphic Designer (Fair, trading-card print
    production). Agentio -- Brand Designer (Good, creator-ads adtech).
    Craft (Taste freelance platform) next_step updated: Taste flagged an
    incoming Checkr background-check email.
  - 2026-09-28 (still later): 16 more new rows, the same 2026-09-27
    application sprint running well past midnight. OLIVER -- Digital
    Content Designer (Fair, 5th distinct OLIVER application). Digital
    Asset -- Brand Designer (Unknown). Bespoke Post -- Graphic Designer
    (Unknown, 2nd distinct Bespoke Post application). Wpromote -- Senior
    Pitch Designer (Fair). Verve -- Unspecified role/Design (Unknown,
    multiple open design roles). J.Crew -- Sr. Digital Designer (Fair).
    VaynerMedia -- Designer (Good). goop -- Unspecified role/Design
    (Unknown, most likely Senior Graphic Designer). Warner Bros.
    Discovery -- Digital Designer, CNN (Unknown, no posting found). TRM
    Labs -- Senior Brand Designer (Good). Alpaca Markets -- Senior
    Graphic Designer (Good). Red Antler -- Senior Digital Designer
    (Good, 2nd distinct Red Antler application, direct via Breezy --
    separate from the Craft-routed Interviewing req). Suno -- Senior
    Designer, Creative Studio (Good) and the contract variant of the
    same role (Good). Conduit Health -- Brand Designer (Good). FP
    Movement -- Graphic Designer (Fair, Free People/Urban Outfitters).
  - 2026-09-28 (rescan): Conveo -- Design Lead flipped Applied -> Rejected
    (generic decline, no reason given). Rejection email arrived without
    the application in the same scan; original confirmation traced back
    to 2026-09-06, already logged with the correct applied_date.
  - 2026-09-28 (later rescan): 3 status updates, no new applications.
    Bumble -- Graphic Designer flipped Applied -> Rejected (role closed,
    not a fit rejection). Vault 49 -- Brand Designer flipped Applied ->
    Interviewing: Anna Callagher (Craft) is scheduling an interview this
    week with Vault 49's own team (Laura/Operations, Nick Corey/ADD,
    Steve Baust/ADD). Canopy -- Graphic Designer next_step updated:
    Regina sent a check-in email after no word since the 2026-09-23
    intro call; had_interview backfilled to 1 since that call already
    happened.
  - 2026-09-28 (evening rescan): 2 next_step updates, no new
    applications. Vault 49 -- interview time confirmed: Wednesday,
    Oct 1 at 1:00pm ET. Craft (Taste freelance platform) -- Senior
    Designer, Brand Guidelines and Identity: Regina submitted her
    background check and flagged a discrepancy to Dave (recruiting@
    tastelabs.com) -- the confirmed project is "GoldenStone Slides &
    Docs" but she'd understood she was joining "Guidelines and
    Identity"; also hasn't received the SOW yet. Awaiting his reply on
    both -- worth watching since it could mean a different project
    scope than expected.
  - 2026-09-29 (morning rescan): 2 updates, no new applications.
    Wpromote -- Senior Pitch Designer flipped Applied -> Rejected
    (generic "moving forward with other candidates" decline; subject
    line read "Wpromote x Giant Spoon", suggesting an agency-partner
    req). Vault 49 -- next_step updated with interview format details:
    a 45-minute call presenting a couple of projects, calendar invite
    to come from Laura.
  - 2026-09-29 (afternoon rescan): 1 update, no new applications. Red
    Antler (Craft-routed Senior Designer req, Interviewing) -- Anna
    Callagher reported Red Antler came back wanting to chat again and
    asked for Regina's availability this week and early next; Regina
    hasn't replied yet -- worth a nudge since it's a live, advancing
    Interviewing thread. (Vault 49's calendar invite for Wed Sept 30,
    1:00-1:45pm ET also came through from Laura Negin -- confirms what
    was already logged, no content change.)
  - 2026-09-29 (evening rescan): 4 updates, no new applications. Craft
    -- 4th distinct application (Graphic Designer, client still
    unknown) flipped Applied -> Rejected, generic decline direct from
    Craft. Bespoke Post -- 2nd distinct application (Graphic Designer)
    flipped Applied -> Interviewing: Kate Mulcahy wants to schedule a
    phone call, Regina hasn't replied yet. Mother -- Regina's 2026-09-25
    check-in with a contact named Rachel (rachel@motherusa.com, name
    doesn't match the original Maggie Murphy contact -- not guessing if
    same person) got a reply: still quiet on the strategy side, will
    flag if something opens up. Red Antler (Craft-routed, Interviewing)
    -- Regina replied to Anna with her availability (Wed/Thu before 3pm
    or Mon/Tue next week); awaiting a locked-in time.
  - 2026-09-30 (midday rescan): 4 updates, no new applications. Red
    Antler (Craft-routed Senior Designer req) -- advanced from
    "awaiting a time" to an actual interview: Amanda Almeida (Red
    Antler EA) is coordinating a meeting with Rogerio Lionzo, Creative
    Director, offering Thu Oct 1 2:00-2:45pm or Fri Oct 2 1:00-1:45pm;
    Regina hasn't picked a slot yet -- notable since this is the
    process moving past the recruiter and into Red Antler's own
    interview loop as expected. The Collected Works -- Brand Designer
    flipped Applied -> Rejected (high volume of applicants, generic).
    Polonsky & Friends -- Junior Graphic Designer flipped Applied ->
    Rejected (explicitly overqualified -- role is for someone earlier
    in their career). Craft (Taste freelance platform) -- Senior
    Designer, Brand Guidelines and Identity: kickoff call invite
    arrived for Thu Oct 1, 1:00-1:30pm ET (large group invite, 11+
    other designers cc'd), confirming the project is proceeding on
    schedule even though the project-name discrepancy Regina flagged
    was never explicitly answered.
  - 2026-09-30 (evening rescan): 4 updates, no new applications.
    Onebrief -- Senior Brand Designer flipped Applied -> Rejected
    (generic decline). Red Antler (Craft-routed Senior Designer req)
    -- Regina confirmed Thu Oct 1, 2:00-2:45pm ET for the Rogerio
    Lionzo interview; calendar invite followed. Bespoke Post -- Graphic
    Designer: call confirmed for Thu Oct 1, 12:15-12:45pm ET (phone
    call despite an auto-generated Meet link). Polonsky & Friends --
    Regina replied to the rejection asking to be kept in mind for
    future openings (no status change).
  - 2026-10-01 (morning rescan): 1 update, no new applications. Vault
    49 -- Anna Callagher relayed positive feedback from the Sept 30
    interview: Vault 49 wants a second round with Sam (CD) and Jenn
    (DD), proposing Thu Oct 8 2pm or Fri Oct 9 11am, and asked Regina
    to present her work as a deck this time. Regina hasn't replied yet
    -- notable since the process is advancing well. (Also corrected a
    date typo on this row: the first interview happened Wed Sept 30,
    not "Oct 1" as a prior entry mistakenly said.)
  - 2026-10-01 (afternoon rescan): 2 updates, no new applications.
    Vault 49 -- Regina confirmed the second round for Thu Oct 8,
    2:00-2:45pm ET with Sam Wilkes (CD) and Jennifer Yelk (DD), and
    agreed to prepare a deck; calendar invite followed. Craft (Taste
    freelance platform) -- the SOW finally arrived via PandaDoc
    ("Regina Barrera & Taste Tech Inc. - Slides&Docs Project - Brand
    Designer"); not yet signed. (Red Antler's Rogerio Lionzo interview,
    scheduled for 2pm ET today, hadn't happened yet as of this scan.)
  - 2026-10-01 (evening rescan): 1 update, no new applications. Red
    Antler -- the Rogerio Lionzo interview happened; Regina told Anna
    it went really well -- a strong conversation about how strategy
    and design overlap at Red Antler, she clarified her hands-on-
    design-plus-strategy fit, and sent Rogerio her design portfolio as
    a follow-up. She said the role sounds well-aligned and wants to
    move forward; awaiting word from Red Antler's side.
  - 2026-10-02 (morning rescan): 1 update, no new applications. Craft
    (Taste freelance platform) -- the SOW was completed and fully
    signed by all participants. Remaining steps: set up a
    tastemaker.pro email, join the project Slack, attend the kickoff
    call (was scheduled for Thu Oct 1).
  - 2026-10-02 (evening rescan): 2 updates, no new applications. webAI
    -- Marketing Designer flipped Applied -> Interviewing: Michael Hale
    (Technical Recruiter) reached out, Regina booked an intro call for
    Mon Oct 5, 11:30am-12pm ET. Vault 49 -- the Oct 8 second-round
    interview was rescheduled to Friday, Oct 9, 11:00-11:45am ET at
    Regina's request due to a family matter (her mother having surgery,
    requiring travel to Houston).
  - 2026-10-03 (rescan): 2 updates, no new applications. JPMorgan Chase
    & Co. -- Olympic & Paralympic, Graphic Designer, Senior Associate
    (Job #210766619) flipped Applied -> Rejected (generic, high
    volume). SHADOW -- Designer flipped Applied -> Rejected (generic
    decline).
  - 2026-10-04 (rescan): 1 update, no new applications. Fanatics
    Collectibles -- Senior Graphic Designer flipped Applied -> Rejected
    (generic decline).
  - 2026-10-05 (rescan): 3 updates, no new applications. Amazon --
    Brand Designer, Brand Innovation Lab (ID: 10525009) flipped Applied
    -> Rejected (generic decline via Amazon.jobs). Suno -- the Senior
    Designer, Creative Studio & Brand Campaigns (Contract) application
    flipped Applied -> Rejected (generic decline); the distinct
    full-time Suno req remains open. webAI -- the Oct 5 recruiter
    screen happened and went well; Michael Hale passed Regina's info to
    the Hiring Manager, who wants to chat next -- awaiting Regina to
    book that call.
  - 2026-10-05 (evening rescan): 1 new row, 2 updates. Porto Rocha --
    a cold-outreach email from 2026-08-26 (resume attached, no open
    role at the time) finally got a real reply: no Associate Strategist
    opening, but a paid strategy internship was floated; Regina said
    she's open to hearing more. Bespoke Post -- the Graphic Designer
    phone call happened and went well; Kate Mulcahy wants to schedule a
    follow-up with the Associate Creative Director next. webAI --
    Regina booked the Hiring Manager call for Thursday, Oct 15,
    1:00-1:30pm ET.
  - 2026-10-06 (rescan): 1 update, no new applications. Bespoke Post --
    Regina replied to Kate Mulcahy with her availability (Wednesday and
    most of Friday) for the Associate Creative Director conversation;
    awaiting Kate to confirm a specific time.
  - 2026-10-06 (afternoon rescan): 2 updates, no new applications.
    Bespoke Post -- after some back-and-forth (the ACD was OOO), the
    Associate Creative Director conversation is confirmed for Monday,
    Oct 12, 1:30-2:00pm ET with Joelyn Dalit; Kate also mentioned she's
    researching possible TN visa support for Regina. Mother -- a
    calendar invite appeared for a Zoom call with a third, previously
    untracked contact (Veronica Thew) on Tuesday, Oct 13, 3:00-3:30pm
    ET; no explanatory email, so its connection to the earlier Maggie
    Murphy/Rachel threads is unclear.
  - 2026-10-06 (evening rescan): 1 ambiguous rejection, no new
    applications. OLIVER -- a generic rejection email arrived with no
    job title or req ID, identical boilerplate to the already-logged
    Social & Culture Strategist rejection from 08-14. With four other
    OLIVER applications still Applied (Senior Designer x3, Digital
    Content Designer), couldn't determine which one this pertains to;
    flagged a note on all four rather than guess which to flip to
    Rejected.
  - 2026-10-07 (rescan): 8 new rows, 2 updates. A late-night
    application sprint (2026-10-06, ~8:20-9:03pm ET) produced
    confirmations from Google (Unspecified role, 4th distinct Google
    application), Mammoth Brands (Junior Creative Strategist, 2nd
    distinct application), Whatnot (Lead Brand Designer), Apple Bank
    (Senior Visual Designer), WGACA (Unspecified role), Authentic
    Brands Group (Graphic Designer), and EliseAI (Graphic Designer) --
    plus a cold-outreach application to PictureStudio (Senior
    Designer, resume emailed directly). J.Crew -- Sr. Digital Designer
    flipped Applied -> Rejected (generic decline). Rightway -- a
    second, identical confirmation arrived for the same Sr. Graphic
    Designer posting; treated as a likely accidental duplicate
    re-application rather than a new row. Craft (Taste freelance
    platform) -- Checkr confirmed the background check is complete,
    report sent to Taste AI.
  - 2026-10-08: 1 new row, from a full sweep of Sent mail (not just
    inbound confirmations) at the user's request. Solomon Page -- a
    resume/portfolio sent to a staffing-agency recruiter via a
    personal referral (Michele Cilione), general introduction, no
    specific role or client. Cross-checked several other Sent-mail
    cold-outreach threads (Accenture/Monica de Armas, Mother/Rachel
    Boyle's first contact, a personal resume review with Mike
    McCulloch) against existing rows -- all were already captured.
  - 2026-10-08 (evening rescan): 1 new row, 2 updates. Salesforce --
    Communications Designer, confirmed via Workday. Red Antler --
    Regina checked in with Anna Callagher on the Senior Designer
    process; no reply yet. Mother -- found the original 2026-09-25
    cold-outreach email to Veronica Thew (a third, distinct Mother
    contact) in a Sent-mail sweep prompted by the user; this resolves
    the previously-logged "unexplained" Oct 6 calendar invite -- it
    was the downstream scheduling step of this same thread. Veronica
    replied warmly, looped in Lauren Martinovic, and the call is now
    confirmed for Tue, Oct 13, 3:00-4:00pm ET with Lauren (Veronica
    cc'd).
  - 2026-10-08 (night rescan): 1 new row, no updates. Omnicom Network
    -- a 3rd, distinct generic "thank you for your application"
    confirmation with no role named, separate from the two earlier
    general network applications and the Presentation Designer req.
  - 2026-10-08 (later): Regina confirmed directly that the 3rd Omnicom
    Network application was for an Art Supervisor role at Area 23
    (healthcare-focused creative agency, part of Omnicom's network) --
    updated the row's title and fit notes accordingly.
  - 2026-10-08 (early morning rescan): 1 new row. HarperCollins
    Publishers -- Senior Designer, Art Department (NYC Hybrid),
    confirmed via iCIMS. Morrow imprint book-cover design role; good
    match to Regina's visual-design/conceptual-branding background.
    Also added a 2nd interview_dates entry (round 2) for Bespoke Post
    -- Kate Mulcahy confirmed a follow-up call with Associate Creative
    Director Joelyn Dalit for Mon, Oct 12, scheduled ahead of this
    rescan's inbox activity but only now reflected in interview_dates.
  - 2026-10-08 (dashboard feature): added a "cold_outreach" flag,
    explicitly set (not inferred) on rows that were Regina's own
    unsolicited outbound email rather than a response to a posting --
    currently Porto Rocha, PictureStudio, and Solomon Page. None of
    the 3 are interviewing yet, so this has no visible effect until
    one of them (or a future row like them) is.
  - 2026-10-08 (reported directly by Regina): Red Antler -- Senior
    Designer flipped Interviewing -> Rejected. Anna Callagher reported
    Rogerio enjoyed meeting Regina but Red Antler is moving forward
    with another candidate with stronger technical skill. Same email:
    Anna met Vault49's Creative Director in person, who's excited to
    meet Regina and wants her to lead with personality/thinking over
    technical polish.
  - 2026-10-08 (night rescan): 1 update, no new rows. Red Antler --
    found Regina's reply to Anna (sent 2026-10-08): gracious, asked to
    stay on Red Antler's radar, and asked whether Rogerio named the
    specific technical skills she was missing -- no answer yet. Also
    confirmed she's preparing her deck for Vault 49's second round the
    next day (Fri Oct 9), already captured on the Vault 49 row.
  - 2026-10-09 (afternoon rescan): 3 updates, no new rows. Red Antler
    -- Anna answered the feedback question: the other candidate was
    more into coding/digital branding, which read as more technical,
    but that depth was never actually required by the brief. Vault 49
    -- the second-round call with Sam Wilkes and Jennifer Yelk
    happened as scheduled; Regina's own read (relayed to Anna right
    after) was mixed -- Jen warm, Sam harder to read, ran short on
    time, and she's not sure it was clear what she's best at (showed
    a wide range; her specialty is packaging/layouts/lockups/type).
    Still interested. Bespoke Post -- Regina asked to reschedule the
    Oct 12 2nd-round call to later next week due to an unexpected
    family trip; new date not yet confirmed, so the Oct 12
    interview_dates entry was pulled until a real date is set.
  - 2026-10-09 (night rescan): 1 update, no new rows. Bespoke Post --
    Kate offered Tue 10/13 3:00pm ET or Wed 10/14 1:30pm ET for the
    rescheduled 2nd round; Regina hasn't picked one yet. Confirmed the
    original Oct 12 calendar invite was canceled.
  - 2026-10-10 (morning rescan): 1 update, no new rows. goop -- the
    "Unspecified role" placeholder was resolved: a Greenhouse
    rejection named the role directly ("the Senior Graphic Designer
    position has been filled"), confirming the earlier guess. Flipped
    Applied -> Rejected and filled in the real title.
  - 2026-10-12 (afternoon rescan): 1 new row. Reddit -- Senior
    Creative Strategist, App Dev (KarmaLab, Reddit's in-house creative
    team for the Global Sales org). No original application-
    confirmation email was ever found; only a generic Greenhouse
    rejection surfaced, so logged directly as Rejected with the
    rejection date as an unconfirmed applied_date placeholder.
  - 2026-10-12 (night rescan): 2 updates, no new rows. The Farmer's
    Dog -- Brand Designer flipped Applied -> Rejected (generic
    decline). Bespoke Post -- Regina confirmed Wednesday, Oct 14,
    1:30pm ET for the rescheduled round 2 with Joelyn Dalit.
  - 2026-10-13 (afternoon rescan): 2 updates, no new rows. Mother --
    the Veronica Thew call got rescheduled twice (Veronica had
    conflicts both times) and still hasn't happened; Jack Pompe asked
    for Regina's availability next week, no new date confirmed yet.
    Vault 49 -- Anna relayed positive feedback from Laura, but said
    they're "still interviewing at first round" -- confusing phrasing
    given Regina's second round already happened; not guessing what
    it means. No concrete next step yet.
  - 2026-10-13 (night rescan): 2 updates, no new rows. Mother -- Jack
    proposed Thursday, Oct 16, 2:30-3:00pm ET for the Veronica call;
    not yet confirmed by Regina. Porto Rocha -- flipped Applied ->
    Interviewing: Regina followed up on the internship conversation,
    Natalee proposed a call to walk through her SVA projects, and it's
    now confirmed for Tuesday, Oct 27, 4:00-4:30pm ET.
  - 2026-10-14 (morning rescan): 4 new rows, surfaced from a late-
    evening application sprint on 2026-10-13 (~7:22-8:35pm ET). Tubi
    (Associate Creative Director, likely a seniority stretch), Amazon
    (Multimedia Designer, ADX, Job ID 10574195, distinct from 3 prior
    Amazon rows, job_fit Unknown -- couldn't confirm the specific
    posting), Freshine Product Inc/Wavytalk (Graphic Designer --
    Workable's auto-reply said "applied again, overwrote the previous
    application" with no earlier Freshine row on record, so it's
    unclear whether a prior scan missed one or this was a same-night
    double-submit; flagging rather than guessing), and e.l.f. Beauty
    (Sr. Packaging Designer, requires packaging-specific experience
    Regina doesn't have).
  - 2026-10-14 (midday rescan): 3 new rows, same overnight sprint,
    just past midnight ET. Ogilvy (Senior Designer, New Business --
    distinct from the existing 2026-08-17 Ogilvy Designer row -- good
    fit on pitch-deck/brand-presentation work), Cyera (Brand Designer,
    job_fit Unknown -- multiple conflicting postings found, couldn't
    confirm which one she applied to), Twigeo (Senior Designer, Paid
    Social - New York, confirmed motion-craft requirement Regina
    doesn't have).
  - 2026-10-14 (portal check): 1 update, no new rows. Material/Aruliden
    (Mid-level Brand Designer) flipped Applied -> Rejected: Regina's
    own Workday candidate portal now shows the listing under the
    "Inactive" tab rather than "Active" -- no rejection email arrived
    to go with it.
  - 2026-10-14 (afternoon rescan): 3 new rows, 1 update. Notion
    (Brand Designer, Creative Studio) flipped Applied -> Rejected
    (generic decline). New: Material (Unspecified role -- generic
    Workday confirmation, distinct from the already-rejected
    09-06 Aruliden row, job_fit Unknown), Bandit Running (Junior Art
    Director, likely underleveled for Regina's 6+ yrs), Jacob Bar Inc.
    (Senior Designer, $140K-$170K, job_fit Unknown -- couldn't confirm
    years-of-experience requirement or the company's actual business).
  - 2026-10-15 (afternoon rescan): no new rows, 1 update. webAI --
    Regina missed her second-round call (Hiring Manager chat) due to a
    calendar mix-up (Google Calendar showed 1:00pm, Ashby had it at
    12:30pm). She emailed Michael Hale and Jaslin Tonton the same day
    to apologize; rescheduled and now confirmed for Monday, Oct 19,
    12:00-12:30pm ET. Status remains Interviewing.
  - 2026-10-15 (evening rescan): 4 new rows, all job_fit Unknown --
    none of the exact live postings could be confirmed via web search.
    Big Spaceship (Designer, $105K desired salary, confirmed 3-day/wk
    hybrid Manhattan), Live Nation Entertainment (Graphic Designer),
    MSG Entertainment Holdings, LLC (Senior Designer), and Okta
    (Unspecified role -- generic confirmation didn't name it).
  - 2026-10-15 (posting detail from Regina): no new rows, 5 updates.
    Regina shared the full LinkedIn postings for 5 already-logged
    applications, resolving prior job_fit "Unknown"s: Cyera (NY Metro
    posting confirmed, Good -- 3+ yrs required), Big Spaceship
    (confirmed posting, Good -- 3+ yrs, $75K-$105K), Live Nation/Roc
    Nation (confirmed the hiring entity is actually Roc Nation, Good
    -- 3+ yrs, $70K-$80K), MSG Entertainment Holdings (confirmed
    posting, Good -- 6+ yrs, $100K-$115K), and Okta (confirmed the
    actual role is Event & Experiences Designer, not a generic design
    role -- Fair, since it requires physical/spatial fabrication
    production experience Regina doesn't have).
  - 2026-10-15 (correction from Regina): no new rows, 2 updates.
    Regina confirmed the 2026-10-14 Material application is a
    reapplication to the same Mid-level Brand Designer (Aruliden)
    posting as the existing 2026-09-06 row -- retitled and job_fit
    set to Good. Jacob Bar Inc. -- confirmed it's a food/beverage-
    adjacent consumer brand (packaging dieline work for flavor
    launches mentioned); job_fit set to Fair (7+ yrs required, just
    above Regina's 6+ yrs).
  - 2026-10-15 (correction from Regina, part 2): no new rows, 1
    update. Warner Bros. Discovery/CNN Digital Designer -- confirmed
    same req (R000107792, Turner Services Inc) as the existing
    2026-09-28 row; job_fit set to Fair (5+ yrs required, Regina
    clears it, but HTML5/motion-graphics emphasis isn't evidenced on
    her resume). Picture Studio and WGACA not yet actioned -- missing
    the Picture Studio applied date and the WGACA posting/role
    details.
  - 2026-10-15 (Gmail search for Picture Studio/WGACA): 1 new row.
    Found Regina's direct email application to PictureStudio (sent
    2026-10-06, missed by prior ATS-domain scans since it's not an
    ATS confirmation email) -- Senior Designer, job_fit Good. WGACA's
    2026-10-07 account-creation email was found too but matches the
    already-logged 2026-10-06 WGACA row exactly -- no new role/posting
    info available for it; still Unspecified role, job_fit Unknown.
  - 2026-10-15 (cold outreach): 3 new rows, all cold_outreach=1.
    Regina sent 3 cold-outreach emails with resume attached (real
    applications, not LinkedIn cold messages). Studio Freight (Senior
    Designer, Fair -- depends on which design track, if either, is
    open), Sylvain (Strategy, Good -- strategy+design consultancy
    matches her design-to-strategy pivot well; sent to 2 contacts,
    logged as 1 row), Company Policy (Unspecified role, Unknown --
    couldn't confirm any open designer role).
  - 2026-10-16 (morning rescan): no new rows, 1 update. Bespoke Post --
    the round 2 call with Joelyn Dalit (ACD) happened Oct 14 and went
    well; Kate wrote 2026-10-15 that Joelyn "really enjoyed their
    conversation," and the next step is a video meeting with Bespoke
    Post's Chief Creative Officer (round 3). Kate also asked when
    Regina's OPT expires "to understand the timing" -- as of this
    scan Regina hasn't replied to either the availability request or
    the OPT question yet.
  - 2026-10-16 (afternoon rescan): no new rows, 2 updates. Nourish --
    flipped Applied -> Rejected (generic decline, Senior Creative
    Strategist). Bespoke Post -- Regina replied with her availability
    for the week of Oct 19 and confirmed her OPT is valid through
    September 2027 (TN transition after, support letter only, no
    formal sponsorship needed); awaiting Kate's reply to confirm the
    CCO round 3 date/time.
  - 2026-10-16 (evening rescan, part 1): no new rows, 1 update. Amazon
    (Multimedia Designer, ADX, Job ID 10574195) -- flipped Applied ->
    Rejected: Amazon's status-update email said "this position is no
    longer available" (role closed, not an evaluated decline).
  - 2026-10-16 (evening rescan, part 2): 5 new rows. Taskrabbit
    (Unspecified role, distinct from the existing 08-18 application,
    job_fit Unknown), Vinson & Elkins LLP (Unspecified role, a large
    law firm -- unusual for Regina's consumer-brand background,
    job_fit Unknown, flagging as possibly a generic ATS pull),
    WITHIN (Senior Creative Lead, distinct from the existing 09-08
    Creative Lead Fellow row, Fair -- performance-marketing skew),
    Trailborn Hotel Management LLC (Visual Designer, Good -- strong
    tool/skills match, $70K-$95K), L'Oreal (Manager, Content Designer
    (Kiehl's), job_fit Unknown -- couldn't confirm the exact posting).
    Also found a Ralph Lauren "unfinished application" nudge email
    (Senior Digital Designer, Luxury Brands) -- Regina started but did
    not complete/submit this application, so it's not logged as
    Applied; flagging for her to decide whether to finish it.
  - 2026-10-17 (evening rescan): no new rows, 1 update. Porto Rocha --
    updated calendar invite moved the Oct 27 internship call from
    4:00-4:30pm ET to 3:30-4:00pm ET (same date). Also saw a generic
    L'Oreal "Get To Know Us" candidate-engagement email on the
    existing Kiehl's application -- no status change, no action taken.
  - 2026-10-18 (morning/afternoon/evening rescans): no new rows, no
    updates across all three -- nothing but promotional/personal mail
    newer than the prior scan.
  - 2026-10-19 (morning rescan): no new rows, 1 update. Mother --
    corrected a date error from the 2026-10-13 night rescan: the
    "Thursday, Oct 16" call time it logged was never actually a
    Thursday (Oct 16, 2026 is a Friday); the Google Calendar invite
    that actually followed Jack's proposal confirms the Veronica Thew
    call landed on Thursday, Oct 22, 2:30-3:00pm ET instead, confirmed/
    accepted by both sides. Also saw an Otter.ai weekly digest
    confirming the already-logged webAI second-round call today
    (Oct 19, 12:00-12:30pm ET) -- no new information, call hadn't
    happened yet as of this scan.
  - 2026-10-19 (afternoon rescan): no new rows, 2 updates. Whatnot --
    flipped Applied -> Rejected: "won't be able to invite you to the
    next round of our hiring process." webAI -- another meeting-link
    mix-up delayed today's second-round call by a few minutes but it
    happened; Ashby then sent official next steps the same afternoon,
    moving her forward to a group-interview stage (team conversation
    plus a technical problem-solving walkthrough), awaiting her
    availability submission -- no date confirmed yet.
  - 2026-10-19 (evening rescan): 1 new row, 3 updates. Savvy Studio
    (Mid-Level Brand Designer, cold outreach with resume attached,
    job_fit Good -- well-regarded NY/Mexico City branding practice,
    strong stylistic match, specific posting not confirmed). Vinson &
    Elkins LLP -- rejected, and the rejection named the actual role
    (Creative Specialist), resolving the earlier "Unspecified role"
    placeholder. webAI -- the group-interview stage from this
    afternoon is now confirmed: a calendar invite puts the team
    interview at Tuesday, Oct 20, 9:00-10:00am ET; also logged the Oct
    19 second-round call (which did happen despite the link mix-up) in
    interview_dates.
  - 2026-10-20 (morning rescan): no new rows, no updates -- nothing
    but promotional/personal mail and a job-opportunity newsletter
    (Words of Mouth, excluded like LinkedIn job-alert digests) newer
    than the prior scan.
  - 2026-10-20 (afternoon rescan): 1 new row, 3 updates. Kettle
    (Visual Designer, cold outreach with resume attached, job_fit Good
    -- real NYC creative/digital agency, exact posting/level not
    confirmed). OLIVER (Digital Content Designer) -- a second, named
    rejection explicitly for this role arrived, flipping it to
    Rejected and resolving which of the earlier generic 10-06
    rejections it belonged to. Bespoke Post -- the CCO round 3 call is
    now locked in for Wednesday, Oct 21, 3:00-3:30pm EDT with Danny
    Cohn. webAI -- noted an ambiguous backup-link message sent right
    at today's team-interview start time; no confirmation either way
    that a mix-up actually recurred, not guessing the outcome.
  - 2026-10-20 (evening rescan): no new rows, no updates -- nothing
    but promotional/personal mail newer than the prior scan.
  - 2026-10-21 (update requested by Regina): 7 new rows, 1 update,
    surfaced from a late-evening application sprint on 2026-10-20
    (~7:56-8:22pm ET). Titan (Unspecified role, job_fit Unknown),
    Raisin (Unspecified role, job_fit Unknown -- a Brand & Marketing
    Designer NY opening exists but isn't confirmed as the one applied
    to), Rillet (Brand Designer, Good), Barry's (Graphic Designer,
    Unknown -- likely Barry's Bootcamp but unconfirmed), iHeartMedia
    (Graphic Designer, Req39497, Fair), Elmwood Brand Consultancy
    (Senior Designer, Good -- strong typography/brand-identity match),
    Peloton (Senior Designer, Good). Jacob Bar Inc. -- Regina (or an
    auto-apply tool) resubmitted to the same already-logged posting;
    Workable's confirmation says it overwrote the previous submission,
    so left as one row, not counted as new.
  - 2026-10-21 (update from Regina, offer stage): 1 update. webAI --
    the Oct 20 team interview happened; Marcus (covering for Michael)
    called 2026-10-21 and moved Regina to the offer stage -- comp is
    with finance for approval, expected back today or tomorrow via
    text + call. Filled in full job context from the 2026-10-05 intro
    call (~200-person Austin AI startup, junior/mid generalist design
    role, $80K-$100K band, fully remote) and upgraded job_fit from
    Unknown to Good. Status left as Interviewing until an actual offer
    number arrives.
  - 2026-10-21 (afternoon rescan): no new rows, 2 updates. Mammoth
    Brands (Junior Creative Strategist) -- rejected, generic decline.
    Mischief -- Robyn Makinson sent a calendar invite for a follow-up
    networking call, confirmed Monday, Oct 26, 1:00-2:00pm ET; this is
    the first concrete next step out of the 09-22 warm-intro cold
    outreach.
  - 2026-10-21 (evening rescan): 1 new row, 3 updates. Substack
    (Unspecified role, job_fit Unknown). Sylvain -- Ben Cheney replied
    to the 10-15 cold outreach: not hiring, but open to a networking
    video chat; Regina sent her availability, no date confirmed yet.
    Mother -- the Oct 22 Veronica Thew call got rescheduled twice the
    same evening, landing on Friday, Oct 23, 2:00-2:30pm ET. Bespoke
    Post -- the CCO round 3 call with Danny Cohn happened (Regina
    joined a few minutes late but it went well per her own account);
    awaiting next steps.
  - 2026-10-22 (morning rescan): no new rows, 1 update. Raisin --
    rejected, and the rejection named the actual role (Digital
    Designer), resolving the earlier "Unspecified role" placeholder.
    Excluded a mass recruiting-agency solicitation (TasteMakers/Taste
    AI, freelance Figma project work) -- unsolicited outreach, not a
    response to an application.
  - 2026-10-22 (afternoon rescan, update from Regina): 2 updates.
    webAI -- flipped to Offer: formal offer call confirmed base salary
    at Regina's ask ($95,000), plus 2,800 stock options (speculative/
    illiquid value, not guaranteed), standard 4-year vesting, proposed
    start date Nov 2. Soft-offer email, DocuSign, and benefits guide
    pending; no written offer signed yet. Sylvain -- Ben Cheney's
    networking call is now locked in for Wednesday, Oct 28, 1:00-
    1:30pm ET.
  - 2026-10-22 (evening rescan): 1 new row, 4 updates. Gretel
    (Strategy Intern, via Notion form, job_fit Unknown -- couldn't
    confirm which company or posting). EliseAI -- rejected. webAI --
    the formal written offer email arrived: $95,000 salary, 2,800
    options with confirmed 4-year vesting/1-year cliff, start date
    Nov 2, and a hard deadline (offer valid 5 business days from
    10/22, roughly through 10/29); Regina negotiated benefits
    clarifications (updated list after some perks turned out outdated)
    and asked about a coworking stipend, awaiting a reply; no DocuSign
    signed yet. Vault 49 and Bespoke Post -- with the real webAI offer
    in hand, Regina emailed both Anna and Kate to flag the competing
    offer/number and ask for a status update given her decision
    timeline; no replies yet from either as of this scan.
  - 2026-10-23 (afternoon rescan): 2 updates, no new rows. Vault 49 --
    the leverage email worked: Anna confirmed the role is still open
    (team still assessing candidates), then locked in a final-round
    in-person studio visit for Tuesday, Oct 27, 1:00pm ET at Vault
    49's studio (180 Varick Street, Suite 1018), with Sam Wilkes (CD),
    Jennifer Yelk (ACD), and a new contact, Graham Erwin (DD). Regina
    disclosed her Thursday webAI deadline to Anna, who's passed it
    along so the team moves quickly. Bespoke Post -- no reply yet
    from Kate as of this scan. Mother -- the Veronica Thew call was
    rescheduled again, same day, now Friday Oct 23, 3:00-3:30pm ET.
  - 2026-10-23 (evening rescan): 1 update, no new rows. webAI --
    Marcus confirmed there's no coworking-space program, but finance
    bumped the base salary to $98,000 (from $95,000) to help cover a
    coworking membership; equity terms unchanged, no DocuSign yet.
  - 2026-10-24 (morning rescan): 1 update, no new rows. Craft (Taste
    freelance platform) -- the GoldenStone freelance project is active
    and billing (Oct 1-15 hours reported); Taste Labs is moving her
    from the wrapping-up Brand Designer role into Presentation Design
    on the same project (assessment waived), and a new PandaDoc SOW
    for the Presentation Designer role arrived 10/24, not yet signed.
    Excluded an unrelated generic "open design projects" solicitation
    from Taste's broader recruiting list (unsolicited, not tied to
    this project).
  - 2026-10-26 (afternoon rescan): 2 updates, no new rows. Craft
    (Taste freelance platform) -- the Presentation Designer SOW is now
    fully signed by all participants. Mother -- the Veronica Thew call
    happened Friday as scheduled; Regina followed up same day with a
    thank-you note and her strategy portfolio.
  - 2026-10-26 (evening rescan): 1 update, no new rows. Instrument --
    flipped Applied -> Interviewing: recruiter Kearney Fagan reached
    out out of the blue, nearly 3 months after the original Lever
    application, inviting Regina to a phone screen; booked for
    Wednesday, Oct 28, 2:00-2:30pm ET. Excluded another generic "open
    Figma design projects" solicitation from Taste's broader
    recruiting list (unsolicited, not tied to the active GoldenStone
    project).

Run `python scripts/seed_from_gmail_scan.py` once against an empty
applications table; it will not create duplicates on repeat runs.
"""
import json
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
        "had_interview": 1,
        "interview_dates": ["2026-07-29"],
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
        "status": "Interviewing",
        "applied_date": "2026-07-27",
        "had_interview": 0,
        "interview_dates": ["2026-10-28"],
        "source": "Lever",
        "next_step": "2026-10-26: out of the blue (nearly 3 months after applying), recruiter Kearney Fagan "
                     "reached out inviting Regina to a phone screen, impressed by her skills/background. Regina "
                     "booked via Kearney's scheduling link; confirmed for Wednesday, Oct 28, 2:00-2:30pm ET "
                     "(Kearney mentioned using an AI note-taking assistant on the call unless Regina objects). "
                     "Still no confirmation of which specific role this is for.",
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
        "status": "Rejected",
        "applied_date": "2026-07-27",
        "source": "Email",
        "notes": "Rejected via email on 2026-09-21 (\"decided not to move forward with your candidacy at this "
                 "time\").",
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
        "status": "Rejected",
        "applied_date": "2026-07-29",
        "source": "iCIMS",
        "notes": "Already in PepsiCo's talent community from an earlier signup (2026-06-16). Reported directly "
                 "by Regina as Rejected -- an HR contact told her PepsiCo likely doesn't sponsor visas, "
                 "applying to all of her open PepsiCo applications.",
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
        "status": "Rejected",
        "applied_date": "2026-08-17",
        "source": "ZipRecruiter",
        "notes": "Rejected via a SmartRecruiters email on 2026-09-11 (\"not be moving forward with your candidacy\").",
        "job_fit": "Fair",
        "job_fit_notes": "An entertainment-marketing campaign-execution/coordination role (2+ yrs). Regina's brand and creative collaboration skills transfer reasonably, but this is more marketing-ops/coordination than the design or strategy authorship she actually does.",
    },
    # -- 2026-08-17 evening rescan --
    {
        "company": "PepsiCo",
        "position": "Brand Designer (2026-450688)",
        "status": "Rejected",
        "applied_date": "2026-08-17",
        "source": "iCIMS",
        "notes": "Second, distinct PepsiCo application from the Design Senior Manager - Immersive "
                 "role applied to 2026-07-29. Reported directly by Regina as Rejected -- an HR contact told "
                 "her PepsiCo likely doesn't sponsor visas, applying to all of her open PepsiCo applications.",
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
        "status": "Rejected",
        "applied_date": "2026-08-17",
        "source": "Oracle Recruiting Cloud",
        "notes": "Third, distinct JPMorgan application, found via JPMC's own Candidate Experience "
                 "portal (Oracle HCM) rather than a Gmail confirmation. \"Under Consideration.\" Rejected "
                 "2026-10-03 -- high volume of applicants, generic decline.",
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
        "status": "Rejected",
        "applied_date": "2026-09-05",
        "source": "Amazon Jobs",
        "notes": "Applied 2026-09-05, briefly withdrew, then reapplied the same day per Regina. Distinct "
                 "from the earlier, already-rejected Art Director, Elevated Shopping application. Rejected "
                 "2026-10-05 -- generic decline via Amazon.jobs status update email.",
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
        "had_interview": 1,
        "interview_dates": ["2026-08-24"],
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
        "status": "Rejected",
        "applied_date": "2026-09-05",
        "source": "Ashby",
        "notes": "Rejected 2026-09-28 -- role was closed, not a fit-based rejection.",
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
        "status": "Rejected",
        "applied_date": "2026-09-05",
        "source": "Greenhouse",
        "notes": "Generic Greenhouse auto-reply confirmation didn't name the role; title confirmed from "
                 "Regina's copy of the posting. New York, salary range $170K-$200K. Rejected 2026-09-25: "
                 "position filled (\"we have recently filled this position\").",
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
        "next_step": "Follow-up call being scheduled for next week (2026-09-25) after a reschedule -- exact "
                     "time not yet confirmed.",
        "notes": "Networking call with Anna-Rae Morris via LinkedIn outreach -- she's at JKR Global "
                 "(annarae.morris@jkrglobal.com). A follow-up call was rescheduled, and Regina is now finding "
                 "a new time with her for the week of 2026-09-28.",
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
        "next_step": "Regina sent a check-in email on 2026-09-25 to a contact at Mother named Rachel "
                     "(rachel@motherusa.com), asking about strategy-side openings -- note: this name doesn't "
                     "match Maggie Murphy from the original follow-up call, so it's unclear if this is the "
                     "same contact under a different name or a separate person at Mother; not guessing which. "
                     "Rachel replied 2026-09-29: still quiet on the strategy side, will flag if anything opens "
                     "up. Separately, Regina directly cold-emailed a third Mother contact, Veronica Thew "
                     "(veronica@mothernewyork.com), on 2026-09-25, introducing herself and noting she'd "
                     "already spoken with Rachel and Maggie -- portfolio linked, no resume attached. Veronica "
                     "replied warmly on 2026-10-04 and looped in Lauren Martinovic to schedule a call; after a "
                     "few back-and-forth messages, the call is confirmed for Tuesday, Oct 13, 3:00-4:00pm ET "
                     "with Lauren (Veronica cc'd) -- this resolves the previously-logged \"unexplained\" "
                     "calendar invite from 2026-10-06, which was just the downstream scheduling step of this "
                     "same thread. 2026-10-09: Jack Pompe (Mother) said Veronica had a scheduling conflict "
                     "during the Oct 13 3:00-3:30pm slot and asked to move to 4:00-4:30pm ET the same day; "
                     "Regina agreed. 2026-10-12: Regina followed up to confirm, offering to move to the "
                     "following week instead if that was easier. 2026-10-13: Jack replied that Veronica's "
                     "calendar had gotten chaotic again and the call didn't happen a second time; he asked "
                     "Regina for her availability next week instead. Regina replied the same day saying she's "
                     "flexible next week; Jack proposed what he called \"Thursday, 2:30-3pm ET\" (sent Oct 13, "
                     "actually mislabeled -- the calendar invite that followed confirms it landed on "
                     "**Thursday, Oct 22, 2:30-3:00pm ET**, not Oct 16 as previously logged here). Regina "
                     "confirmed 2026-10-15; the Google Calendar invite (organizer Veronica Thew, Zoom link) "
                     "shows the call as confirmed/accepted by both for Oct 22. 2026-10-21: Veronica sent an "
                     "updated \"*Rescheduling*\" invite moving the call to Thursday, Oct 22, 2:30-3:00pm ET "
                     "(same day, same time as before -- just reissued), then a second updated invite the same "
                     "evening moving it again to **Friday, Oct 23, 2:00-2:30pm ET**. 2026-10-23: a further "
                     "updated invite (same Zoom link, host jack.pompe@mothernewyork.com) moved the call again, "
                     "same day, to **3:00-3:30pm ET** -- treating this as the current, authoritative time. "
                     "2026-10-26: the call with Veronica happened as scheduled Friday -- Regina followed up "
                     "same day with a thank-you note and her strategy portfolio, saying it was lovely meeting "
                     "her and getting a glimpse of what things are like on the inside. Awaiting any reply.",
        "notes": "Scheduled follow-up call with Maggie Murphy, Strategy Director at Mother -- grew out of the "
                 "2026-07-30 Mother Intro Call. Not yet happened as of 2026-09-05.",
    },
    # -- 2026-09-05: incremental rescan, 3 new rows --
    {
        "company": "Notion",
        "position": "Brand Designer, Creative Studio",
        "status": "Rejected",
        "applied_date": "2026-09-05",
        "source": "Greenhouse",
        "notes": "Flipped Applied -> Rejected 2026-10-14: generic decline, \"we will not be moving forward "
                 "with your candidacy.\"",
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
        "status": "Rejected",
        "applied_date": "2026-09-05",
        "source": "iCIMS",
        "notes": "Third, distinct PepsiCo application, for the poppi brand specifically -- separate from "
                 "the Design Senior Manager - Immersive (applied 07-29) and Brand Designer (applied 08-17) "
                 "roles already tracked. Reported directly by Regina as Rejected -- an HR contact told her "
                 "PepsiCo likely doesn't sponsor visas, applying to all of her open PepsiCo applications.",
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
        "status": "Rejected",
        "applied_date": "2026-09-03",
        "source": "Greenhouse",
        "notes": "Generic Greenhouse auto-reply confirmation didn't name the role; confirmed from the "
                 "LinkedIn listing Regina shared (same Greenhouse instance, usenourish). Flipped Applied -> "
                 "Rejected 2026-10-16: generic decline, \"we have made the decision to move forward with "
                 "other candidates whose experience more closely aligns with our team's needs.\"",
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
        "status": "Rejected",
        "applied_date": "2026-09-03",
        "source": "Workday",
        "notes": "Rejected via a Workday email on 2026-09-14 (\"already in process with candidates whose "
                 "background and experience align with our hiring needs\").",
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
        "status": "Rejected",
        "applied_date": "2026-09-06",
        "source": "Workday",
        "notes": "Rejected via email on 2026-09-21 (\"decided not to move forward with your application\").",
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
        "status": "Rejected",
        "applied_date": "2026-09-06",
        "source": "Workday",
        "notes": "Generic Workday auto-reply confirmation didn't name the role; confirmed from the LinkedIn "
                 "listing Regina shared. Aruliden is a Material-owned multi-disciplinary design studio "
                 "(beauty/lifestyle/wellness/tech clients), New York, NY (hybrid) -- not Los Angeles as "
                 "originally assumed from a generic web search. Flipped Applied -> Rejected 2026-10-14: "
                 "Regina's own Workday candidate portal now shows this listing under the \"Inactive\" tab "
                 "(moved out of \"Active\"), no explicit rejection email received -- no reply email to go "
                 "with it.",
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
        "status": "Rejected",
        "applied_date": "2026-09-06",
        "source": "Ashby",
        "notes": "Rejected 2026-09-28 -- generic decline (\"decided not to move forward at this time\"), "
                 "no specific reason given.",
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
        "status": "Rejected",
        "applied_date": "2026-09-06",
        "had_interview": 1,
        "interview_dates": ["2026-09-22"],
        "next_step": "Rejected 2026-09-24: Angela (The Change Agents, the talent agency handling this "
                     "candidacy) confirmed Day One's internal policy doesn't allow them to consider candidates "
                     "who may need future visa sponsorship -- not a fit/performance rejection.",
        "source": "Pinpoint",
        "notes": "Confirmation came from D1A (Day One Agency)'s Pinpoint ATS. Angela Boyes of The Change "
                 "Agents (thechangeagents.co) was the recruiter handling this candidacy on Day One's behalf.",
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
        "status": "Rejected",
        "applied_date": "2026-09-06",
        "source": "SmartRecruiters",
        "notes": "Rejected via email on 2026-09-22 (\"decided to pursue other candidates\").",
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
        "status": "Rejected",
        "applied_date": "2026-09-07",
        "source": "SmartRecruiters",
        "notes": "Second, distinct application submission (different SmartRecruiters application ID) for the "
                 "same role and company as the 2026-09-06 Fresh application -- appears to be an accidental "
                 "duplicate resubmission rather than a second role. Rejected via a separate email on "
                 "2026-09-22 (\"decided to pursue other candidates\"), sent ~25 min after the first Fresh "
                 "rejection.",
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
        "company": "Noom",
        "position": "Senior Creative Strategist, Performance",
        "status": "Rejected",
        "applied_date": "2026-08-26",
        "source": "Email",
        "notes": "Missed entirely by every prior scan -- the confirmation email's generic subject didn't match "
                 "the search keywords. Found via the 2026-09-12 rejection email (\"the position has been "
                 "filled\"), then traced back to the original 2026-08-26 confirmation to backfill the applied "
                 "date and role title.",
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting: 6-10 yrs total experience, 3-5+ yrs specifically in performance "
                         "creative strategy, owning bottom-of-funnel paid-social/digital creative and managing "
                         "a junior Creative Strategist, tight partnership with media buyers on creative "
                         "testing. This is a performance-marketing leadership scope -- media-buying fluency "
                         "and direct-response/paid-social optimization experience aren't evidenced on Regina's "
                         "brand/creative-agency background.",
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
    {
        "company": "Red Antler",
        "position": "Senior Designer",
        "status": "Rejected",
        "applied_date": "2026-09-14",
        "source": "Craft (recruitment agency ATS)",
        "next_step": "Had the recruiter call with Anna Callagher on Wednesday, Sept 23 -- this was confirmed "
                     "to be the Red Antler req. Regina sent her strategy portfolio (reginabbs.cargo.site) on "
                     "2026-09-24; Anna flagged the link wasn't working, and Regina resent the corrected link "
                     "the same day. 2026-09-29: Anna reported Red Antler came back wanting to chat, and asked "
                     "Regina to share her availability; Regina replied same day offering Wed/Thu before 3pm or "
                     "Mon/Tue the following week. 2026-09-30: this advanced to a real interview -- Amanda "
                     "Almeida (Red Antler EA, on behalf of Sabrina Frometa) is coordinating a meeting with "
                     "Rogerio Lionzo, Creative Director. Regina confirmed Thu Oct 1, 2:00-2:45pm ET the same "
                     "day; a calendar invite followed (link had to be re-sent after Regina couldn't find it). "
                     "2026-10-01: the interview happened -- Regina told Anna it went really well, with a "
                     "strong conversation about how strategy and design overlap at Red Antler; she clarified "
                     "she wants to stay hands-on with design while staying close to strategic/conceptual "
                     "thinking (the two separate portfolios had caused some initial confusion), and sent "
                     "Rogerio her design portfolio as a follow-up. Regina says the role sounds well-aligned "
                     "and she wants to move forward. Awaiting word from Red Antler. Confirms the process "
                     "moving past Craft into Red Antler's own team, as expected (creative director, then the "
                     "ECDs). 2026-10-07: Regina checked in with Anna asking if she's heard anything back from "
                     "Red Antler since they last spoke; no reply yet. 2026-10-08: Anna replied -- Rogerio "
                     "enjoyed meeting Regina, but Red Antler is moving forward with another candidate who had "
                     "stronger technical skill. In the same email, Anna said she'd met with Vault49 in person "
                     "the day before and their Creative Director is excited to meet Regina, loved her "
                     "enthusiasm and drive from the first stage, and that leading with personality/thinking "
                     "(not just technical polish) is the key thing to land there. Regina replied same day: "
                     "disappointed but gracious, asked to stay on Red Antler's radar for future openings, and "
                     "asked Anna whether Rogerio mentioned which specific technical skills were missing (for "
                     "her own learning) -- no answer yet. She also confirmed she's preparing her deck for the "
                     "Vault 49 second round the next day (Fri Oct 9). 2026-10-09: Anna answered the feedback "
                     "question -- the other candidate was more focused on coding/digital branding, which made "
                     "them read as more technical overall; Anna noted that depth was never actually a "
                     "requirement of the brief, Red Antler just found it interesting in that candidate's work.",
        "notes": "Applied through Craft, a UK/NY creative & design recruitment consultancy (itscraft.com), not "
                 "the hiring company itself -- one of three distinct applications Regina submitted through "
                 "their ATS within minutes of each other on 2026-09-14. Anna Callagher, Lead Recruiter @ "
                 "Craft, messaged via LinkedIn on 2026-09-22 to book a call without saying which of the three "
                 "it was for; confirmed by Regina on 2026-09-23 (after the call) that this one was Red Antler.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed via Regina/Anna: a senior (and mid-senior/lead) brand designer role, "
                         "hiring across levels due to high project volume -- large-scale branding and brand "
                         "strategy for tech brands, NY-based with flexible remote days. Key fit criteria are "
                         "strategic thinking, a strong process rationale, and confident client presentation "
                         "(they'll reject candidates who can't walk through design decisions clearly). Regina "
                         "sees the strategy angle as her differentiator here, especially relevant in the AI "
                         "era -- a strong match to her SVA Branding background.",
        "had_interview": 1,
        "interview_dates": ["2026-10-01"],
    },
    {
        "company": "Craft",
        "position": "Freelance Senior Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-14",
        "source": "Craft (recruitment agency ATS)",
        "next_step": "Still unresolved -- the other two Craft applications were confirmed as Red Antler and "
                     "Vault 49, so this is the one remaining application whose client company is unconfirmed.",
        "notes": "Craft is a UK/NY creative & design recruitment consultancy (itscraft.com), not the hiring "
                 "company itself -- one of three distinct applications Regina submitted through their ATS "
                 "within minutes of each other on 2026-09-14.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm which specific client/freelance req this was among Craft's several "
                         "open Senior Brand Designer listings.",
    },
    {
        "company": "Vault 49",
        "position": "Brand Designer",
        "status": "Interviewing",
        "applied_date": "2026-09-14",
        "had_interview": 1,
        "interview_dates": ["2026-09-30", "2026-10-09", "2026-10-27"],
        "source": "Craft (recruitment agency ATS)",
        "next_step": "Interview happened Wednesday, Sept 30 at 1:00pm ET with Laura (Operations), Nick Corey "
                     "(ADD), and Steve Baust (ADD) -- Vault 49's own team, not just Craft. Format: a 45-minute "
                     "get-to-know-you call where Regina presented a couple of projects, walking through her "
                     "thinking/process. 2026-10-01: Anna Callagher relayed positive feedback -- Vault 49 wants "
                     "a second round with Sam Wilkes (CD) and Jennifer Yelk (DD), proposing Thu Oct 8 at 2pm or "
                     "Fri Oct 9 at 11am, and asked Regina to present her work as a deck this time (deck-"
                     "building is an important part of their work). Regina confirmed Thu Oct 8, 2:00-2:45pm "
                     "ET and agreed to prepare a deck; calendar invite followed same day. 2026-10-02: Regina "
                     "asked to reschedule due to a family matter (her mother having surgery, requiring travel "
                     "to Houston) -- moved to Friday, Oct 9, 11:00-11:45am ET; calendar invite updated. "
                     "Follows the 2026-09-24 portfolio update (new packaging project) that Anna said looked "
                     "great. 2026-10-09: the second-round call with Sam and Jen happened as scheduled -- "
                     "Regina's own read, relayed to Anna right after: Jen was warm, Sam harder to read, and "
                     "they ran a little short on time at the end. They asked whether she's more drawn to big "
                     "brands or small ones; Regina suspects this came up because most of what she presented "
                     "skewed toward smaller brands and spec work, even though she's interested in big-brand "
                     "work too. She also showed a fairly wide range, so it may not have been clear what she's "
                     "best at (packaging, layouts, lockups, and type specifically). Still interested -- liked "
                     "that the team seems hands-on. Awaiting word from Anna. 2026-10-13: Anna relayed positive "
                     "feedback from Laura at Vault 49, but said they're \"still interviewing at first round\" "
                     "and will follow up with next steps -- phrasing is a little confusing given Regina's "
                     "second-round call already happened Oct 9; not guessing what it means exactly (possibly "
                     "Vault 49 still first-round-interviewing other candidates). No concrete next step yet. "
                     "2026-10-22: with a real competing offer in hand (webAI, $95K), Regina emailed Anna to "
                     "check in given the long silence since 10-13 -- mentioned the team's energy resonated with "
                     "her, that Vault 49 is genuinely her top choice, and that she now has a decision to make "
                     "soon. 2026-10-23: the leverage email worked -- Anna replied (12:52pm) that the role is "
                     "still open but they're still assessing candidates, and she'd check back in with Laura. "
                     "Regina told Anna (3:34pm) she'd received the formal offer and has until Thursday to "
                     "respond, could potentially request a short extension, and asked if Vault 49 could decide "
                     "shortly after a visit. Anna came back (4:17pm) asking if Regina could come into the "
                     "studio 1-2:30pm Tuesday; confirmed (4:39pm) at exactly 1:00pm Tuesday, Oct 27, at Vault "
                     "49's studio -- 180 Varick Street, Suite 1018 (Laura's cell for day-of issues: "
                     "609-903-7314). Regina is asked to prepare to present some work and have a conversation "
                     "with Sam Wilkes (CD), Jennifer Yelk (ACD), and Graham Erwin (one of their DDs -- new "
                     "contact, not previously on the req). Anna has let the team know about the Thursday "
                     "deadline so they move quickly if they're keen. This is now a confirmed final-round "
                     "in-person visit directly resulting from disclosing the competing offer.",
        "notes": "Applied through Craft, a UK/NY creative & design recruitment consultancy (itscraft.com), not "
                 "the hiring company itself -- one of three distinct applications Regina submitted through "
                 "their ATS within minutes of each other on 2026-09-14. Anna Callagher, Lead Recruiter @ "
                 "Craft, was working this req alongside the Red Antler one; confirmed by Regina on 2026-09-23 "
                 "as Vault 49.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed via Regina/Anna: mid-to-senior brand designer, pays up to $100K, "
                         "CPG-focused (PepsiCo, Diageo brands, food and drink, expanding beyond alcohol/beer). "
                         "Creative director Sam Wilkes (10 years at the agency). Strong craft focus, good "
                         "work-life balance, values diverse perspectives and eagerness to learn. In-office "
                         "Tue/Wed/Thu in Manhattan (can go more) -- Regina is enthusiastic about being "
                         "in-person, and her brand-identity/craft background is a solid match.",
    },
    {
        "company": "The New York Times",
        "position": "Senior Designer, Games Marketing (Temporary)",
        "status": "Rejected",
        "applied_date": "2026-09-14",
        "source": "Greenhouse",
        "notes": "2nd, distinct New York Times application -- separate from the earlier Designer, Marketing "
                 "role (applied 07-22). This one is a temporary (6-month) role reporting to the Associate "
                 "Creative Director, Marketing, Games. Rejected 2026-09-23: generic \"will not be advancing "
                 "you in the process\" email.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: concepting/producing Games marketing campaigns, refined "
                         "aesthetic, strong typography/layout/color, and motion design as a called-out core "
                         "skill. Regina's design craft and typography line up well, but motion design is a "
                         "required skill area here (not a plus), and it isn't evidenced on her resume -- the "
                         "same recurring gap seen on several other roles.",
    },
    {
        "company": "Sapience AI Corporation",
        "position": "Brand Graphic Designer",
        "status": "Applied",
        "applied_date": "2026-09-14",
        "source": "Greenhouse",
        "notes": "Generic Greenhouse confirmation didn't name the role; \"Brand Graphic Designer\" is the one "
                 "design req found on their job board, an AI company with a remote role but Seattle-area/"
                 "Pacific-time-zone preference, so the exact title isn't fully confirmed.",
        "job_fit": "Weak",
        "job_fit_notes": "The one design req found (Brand Graphic Designer) prefers candidates in the Seattle "
                         "area on Pacific time -- Regina is NYC-based and Eastern time, a location/timezone "
                         "mismatch on top of an unfamiliar AI-company industry context.",
    },
    {
        "company": "Unspecified (Ashby application)",
        "position": "Unspecified role",
        "status": "Applied",
        "applied_date": "2026-09-14",
        "source": "Ashby",
        "notes": "The confirmation email was a fully generic Ashby template signed only \"TALENT TEAM\" -- no "
                 "company name, role title, or any other identifying detail anywhere in the email. Submitted "
                 "the same evening as the Craft/NYT/Sapience AI batch, so likely part of the same application "
                 "session, but which company this was for could not be determined.",
        "job_fit": "Unknown",
        "job_fit_notes": "No company or role information available to assess fit against.",
    },
    {
        "company": "DEPT",
        "position": "Principal, Visual Design",
        "status": "Rejected",
        "applied_date": "2026-09-14",
        "source": "Greenhouse",
        "notes": "Part of the same 2026-09-14 evening application batch as Craft/NYT/Sapience AI/the "
                 "unspecified Ashby application -- missed by the 2026-09-14/09-15 rescans since the "
                 "confirmation subject (\"Whoo! We've received your application!\") didn't match the search "
                 "keywords. Found via a rejection email Regina shared (screenshot) on 2026-09-15, then traced "
                 "back to the original confirmation to backfill the applied date; the confirmation itself "
                 "didn't name the role.",
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting: a Principal-level design-leadership role setting visual/UX "
                         "direction across large, diverse teams, with a strong UX/interaction-design-system "
                         "component and executive-level presentation/stakeholder skills. This is a design-"
                         "leadership scope and seniority several levels above Regina's brand/graphic-design "
                         "agency background, and UX/interaction design isn't evidenced on her resume.",
    },
    {
        "company": "TUSHY",
        "position": "Creative Strategist",
        "status": "Applied",
        "applied_date": "2026-09-15",
        "source": "Breezy",
        "notes": None,
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm the exact Creative Strategist posting -- TUSHY's own board only "
                         "turned up a more senior, differently-titled Associate Director, Creative req. TUSHY "
                         "is a D2C bidet/personal-care brand known for irreverent, humor-driven performance "
                         "marketing, which isn't a demonstrated specialty on Regina's resume, but without the "
                         "actual listing there's nothing concrete to assess fit against.",
    },
    {
        "company": "Compass",
        "position": "Senior Designer",
        "status": "Rejected",
        "applied_date": "2026-09-15",
        "source": "Greenhouse",
        "notes": "Rejected via a Greenhouse email on 2026-09-17 (\"decided to move forward with other "
                 "candidates\") -- confirmed as the real-estate brokerage Compass International Holdings, "
                 "not a distinct company.",
        "job_fit": "Good",
        "job_fit_notes": "The closest match found is a Senior Graphic Designer role on Compass's in-house "
                         "Creative Studio (NYC, real-estate brokerage): brand identities, motion-led campaigns, "
                         "print/digital marketing collateral, Illustrator/Photoshop/Figma/InDesign (motion a "
                         "plus, not required) -- a solid match to Regina's Common Matter agency background and "
                         "tools, though 100% in-office wasn't confirmed as a hard requirement for this exact "
                         "req.",
    },
    {
        "company": "FLORA",
        "position": "Creative Generalist (Contract)",
        "status": "Applied",
        "applied_date": "2026-09-15",
        "source": "Ashby",
        "notes": None,
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm the exact Creative Generalist posting -- FLORA's Ashby board only "
                         "showed differently-titled roles (Production Coordinator, Brand & Creative; Forward "
                         "Deployed Creative), so there's nothing concrete to assess fit against.",
    },
    {
        "company": "Made Thought",
        "position": "Senior Designer",
        "status": "Rejected",
        "applied_date": "2026-09-15",
        "source": "Email",
        "notes": "Rejected via email on 2026-09-18 (\"identified candidates more closely aligned with the "
                 "role\").",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: a London creative studio (adidas, MoMA, Pinterest, Stella "
                         "McCartney) wanting graphic design/art direction/strategy craft via Adobe CS and "
                         "Keynote, driving projects concept-to-delivery and mentoring junior designers -- a "
                         "strong match to Regina's Common Matter agency background. 3D tools are also listed "
                         "among the studio's core work, which isn't evidenced on her resume.",
    },
    {
        "company": "Profound",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-15",
        "source": "Ashby",
        "notes": None,
        "job_fit": "Good",
        "job_fit_notes": "Confirmed general scope: a well-funded ($1B valuation) AI marketing-analytics "
                         "startup wants a Brand Designer to define its look/feel across campaigns, events, and "
                         "visual systems as it scales -- a solid general match to Regina's brand-systems "
                         "background, though specific years-of-experience/skill requirements weren't "
                         "confirmable from the posting summary found.",
    },
    {
        "company": "Combo",
        "position": "Senior Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-15",
        "source": "Cold email",
        "notes": "Direct cold-email application to jobs@combo.co, resume and portfolio attached -- found via "
                 "Gmail Sent search. Full posting shared directly by Regina (NY office).",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 6+ yrs studio/agency environment, leading projects "
                         "independently concept-to-delivery, delegating to and directing other designers, "
                         "Illustrator/Photoshop/InDesign/Figma, and a diverse portfolio spanning brand "
                         "identity, packaging, campaign, and UI/digital work (motion a plus, not required). "
                         "Strong direct match on portfolio breadth, tools, and years of experience with "
                         "Regina's Common Matter background; delegating/directing other designers day-to-day "
                         "isn't as clearly evidenced as the rest, but is a lighter ask than formal team "
                         "management.",
    },
    {
        "company": "Saint Urbain",
        "position": "Senior Designer",
        "status": "Applied",
        "applied_date": "2026-09-16",
        "source": "Cold email",
        "notes": "Direct cold-email application to work@sainturbain.com in response to a LinkedIn post about "
                 "the opening, resume and cover letter attached -- found via Gmail Sent search.",
        "job_fit": "Strong",
        "job_fit_notes": "Confirmed via Saint Urbain's own LinkedIn post: a Senior Designer with brand design "
                         "experience, remote and freelance-to-start. Saint Urbain is an independent branding/"
                         "strategy/design studio -- a close, direct match to Regina's branding-studio "
                         "(Mexico), Superside, and SVA Branding Master's background.",
    },
    # -- 2026-09-18: networking call reported directly by Regina --
    {
        "company": "Andie Wexler",
        "position": "Networking call",
        "status": "Networking",
        "applied_date": "2026-09-16",
        "source": "Calendly",
        "notes": "30-minute Google Meet call booked via Calendly, Sept 16, 2026, 11:00-11:30am ET. Only a "
                 "Calendly confirmation email was found in Gmail -- no other correspondence surfaced, so the "
                 "company/context behind this contact is unconfirmed.",
    },
    # -- 2026-09-18 (later): incremental rescan, 2 new rows, 2 flips --
    {
        "company": "The New York Times",
        "position": "Senior Strategist",
        "status": "Rejected",
        "applied_date": "2026-09-18",
        "source": "Greenhouse",
        "notes": "3rd, distinct New York Times application -- separate from the Designer, Marketing role "
                 "(applied 07-22) and the Senior Designer, Games Marketing role (applied 09-14). Confirmed by "
                 "Regina as the T Brand Studio Creative Strategy team req (LinkedIn posting shared directly): "
                 "REQ-020117, $90K-$100K, reporting to the Director of Strategy. Rejected 2026-09-24: generic "
                 "\"will not be advancing you in the process\" email.",
        "applicant_count": 173,
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting (REQ-020117): 6+ yrs advertising/marketing experience building "
                         "creative briefs from cultural research and audience data, producing 360-degree "
                         "proposals for advertisers, and presenting strategy directly to agency/brand contacts "
                         "-- an advertising-sales-strategy career track. Regina's audience/cultural-research "
                         "and creative-briefing skills overlap, but like the Droga5 and Design Bridge/Landor "
                         "Senior Strategist roles, this wants a dedicated strategy-track career rather than "
                         "her design-led background with a strategy overlay.",
    },
    {
        "company": "Ripple",
        "position": "Senior Brand Designer",
        "status": "Rejected",
        "applied_date": "2026-09-06",
        "source": "Greenhouse",
        "notes": "Distinct from the already-tracked Ripple Brand Designer (NY) application -- this is likely "
                 "the separate San Francisco Senior Brand Designer opening referenced in that row's notes as "
                 "the other plausible match for the original ambiguous 09-06 Greenhouse confirmation. No "
                 "distinct confirmation email for this one was ever found, only a 2026-09-18 rejection (\"Update "
                 "on Your Application\"), so the applied_date is inferred from the original 09-06 confirmation "
                 "rather than confirmed directly.",
        "job_fit": "Unknown",
        "job_fit_notes": "The Senior-level SF posting itself wasn't separately confirmed, so fit couldn't be "
                         "assessed against it directly.",
    },
    # -- 2026-09-19: reported directly by Regina, full posting shared --
    {
        "company": "Perplexity",
        "position": "Brand Designer, Growth",
        "status": "Applied",
        "applied_date": "2026-09-19",
        "source": "Ashby",
        "notes": "Full posting shared directly by Regina. San Francisco or New York, hybrid.",
        "pay_range": "$150K-$225K + equity",
        "applicant_count": 30,
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: 5+ yrs designing growth/performance creative (paid ads, social, "
                         "lifecycle email) with strong Figma/Adobe CS craft and strategic concepting -- the "
                         "visual-design and brand-system side lines up with Regina's Common Matter background. "
                         "But the core of the role is reading ad-performance data (CTR, conversion, hook rates) "
                         "and iterating creative against it in partnership with a Growth team, which isn't a "
                         "demonstrated specialty on her resume; motion design is called out as a plus, not "
                         "required.",
    },
    # -- 2026-09-19 (later): traced back via targeted search after Regina --
    # confirmed via LinkedIn's applicant-insight screenshot that she'd applied --
    {
        "company": "OLIVER",
        "position": "Senior Designer",
        "status": "Applied",
        "applied_date": "2026-09-06",
        "source": "Greenhouse",
        "notes": "Distinct from the two other already-tracked OLIVER applications (Social & Culture "
                 "Strategist, applied 07-23; and a separate role rejected 08-14). Confirmation was missed by "
                 "prior scans; found via targeted search after Regina flagged it from LinkedIn's own "
                 "applicant-insight panel (113 applicants total, 4 in the past day, per her screenshot). A "
                 "generic OLIVER rejection email arrived 2026-10-06 (\"skill sets are not exactly aligned,\" "
                 "same boilerplate as the earlier Social & Culture Strategist rejection) with no job title or "
                 "req ID -- it could pertain to this application or to any of OLIVER's three other still-open "
                 "ones (Senior Designer x2 more, Digital Content Designer); not guessing which, so this row's "
                 "status is left unchanged pending a confirmation that names the role.",
        "applicant_count": 113,
        "job_fit": "Good",
        "job_fit_notes": "Confirmed general scope: a Senior Designer role on a global financial-services "
                         "account, embedded client-side (in OLIVER's in-house-agency model) 2 days/week, "
                         "$106,250-$118,750. A solid general match to Regina's Common Matter agency background, "
                         "though the specific financial-services client industry isn't evidenced on her resume.",
    },
    # -- 2026-09-19 (evening rescan): incremental rescan, 1 new row --
    {
        "company": "OLIVER",
        "position": "Senior Designer (2nd application)",
        "status": "Applied",
        "applied_date": "2026-09-19",
        "source": "Greenhouse",
        "notes": "Second, distinct Greenhouse confirmation for a same-titled 'Senior Designer' posting, 13 "
                 "days after the first (applied 09-06) -- OLIVER runs many concurrent Senior Designer reqs "
                 "across different client accounts, so this reads as a separate opening rather than a "
                 "duplicate resubmission. Likely matches the full posting Regina later shared (Req ID: 18584, "
                 "$114,750-$128,250, hybrid onsite 4 days/wk) -- distinct pay range and onsite schedule from "
                 "the already-confirmed 09-06 application ($106,250-$118,750, 2 days/wk), though not 100% "
                 "certain which req this specific confirmation email was for. A generic OLIVER rejection "
                 "email arrived 2026-10-06 with no job title or req ID -- could pertain to this application "
                 "or to any of OLIVER's three other still-open ones; not guessing which, status left "
                 "unchanged.",
        "pay_range": "$114,750-$128,250/yr",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting (Req 18584): leading creative delivery for a high-volume "
                         "(250+ deliverables/month) regulated-industry (financial-services-adjacent) account, "
                         "with significant scope beyond IC design -- managing/delegating to junior and "
                         "production designers, mentoring, and owning project-level production budgets "
                         "(cost estimation, PO/invoicing, freelancer negotiation). Print/editorial/brand-"
                         "consistency craft lines up with Regina's Common Matter background, but formal team "
                         "management and budget ownership aren't evidenced on her resume -- the same "
                         "management-scope gap seen on other Senior-titled roles with people-leadership scope.",
    },
    # -- 2026-09-20: traced back after a rejection surfaced; confirmation --
    # was missed by prior scans (subject didn't match search keywords) --
    {
        "company": "BritBox International",
        "position": "Senior Designer",
        "status": "Rejected",
        "applied_date": "2026-09-14",
        "source": "Teamtailor",
        "notes": "Confirmation (\"We have received your application!\") was missed by prior scans; traced back "
                 "after a rejection email arrived 2026-09-20 (\"we won't be progressing further at this "
                 "stage\").",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: leading key art and marketing design for BBC Studios' BritBox "
                         "streaming brand (Direct-to-Consumer division), reporting to the Associate Art "
                         "Director, NYC. Typography and Photoshop craft line up with Regina's design "
                         "background, but entertainment key art (movie/show marketing art) is a specific "
                         "niche not evidenced on her resume, which is agency/brand-systems focused.",
    },
    # -- 2026-09-21 (later): incremental rescan, 1 new row --
    {
        "company": "Accenture",
        "position": "Creative Agency Senior Designer (2nd application)",
        "status": "Rejected",
        "applied_date": "2026-09-21",
        "source": "Workday",
        "notes": "Second, distinct Workday confirmation for the same-titled 'Creative Agency Senior Designer' "
                 "role Regina was rejected from back on 07-27 (confirmed via the Accenture candidate-portal "
                 "screenshot) -- likely a reposted/reopened req, same pattern as the earlier Droga5 Senior "
                 "Strategist reapplication. Rejected via email on 2026-09-22, citing visa sponsorship "
                 "(\"you indicated you require sponsorship and/or support for employment visa status\") -- same "
                 "template as the earlier Work & Co Designer (R00334677) visa rejection; reference role "
                 "confirmed as \"Creative Agency Senior Designer.\"",
        "job_fit": "Strong",
        "job_fit_notes": "Same role as the earlier application: 6+ yrs agency design with a concept-driven "
                         "brand-identity portfolio, expert Figma/Illustrator/Photoshop/InDesign, and AI "
                         "image-generation tools -- a strong direct match to Regina's brand-identity, "
                         "visual-storytelling, and AI-assisted design background.",
    },
    # -- 2026-09-22: reported directly by Regina, found via Gmail Sent search --
    {
        "company": "The Collected Works",
        "position": "Brand Designer",
        "status": "Rejected",
        "applied_date": "2026-09-22",
        "source": "Cold email",
        "notes": "Direct cold-email application to jobs@thecollectedworks.com, resume attached -- no listed "
                 "opening found, general outreach to their jobs inbox. Rejected 2026-09-30 -- high volume of "
                 "applicants, not a fit-specific decline.",
        "job_fit": "Good",
        "job_fit_notes": "The Collected Works is an independent NYC/New Orleans identity, motion, and 3D "
                         "design studio co-founded by two SVA grads (Nike, The National, The New York Times "
                         "among past clients) -- a close cultural/disciplinary match to Regina's SVA Branding "
                         "Master's and Common Matter identity-design background, though no specific job "
                         "posting exists to confirm exact seniority or requirements against.",
    },
    # -- 2026-09-22 (later): reported directly by Regina, full posting shared --
    {
        "company": "BBDO",
        "position": "Senior Strategist",
        "status": "Applied",
        "applied_date": "2026-09-22",
        "source": "LinkedIn",
        "notes": "Full posting shared directly by Regina. Per LinkedIn's applicant-insight panel at the time "
                 "she applied: 42 candidates had clicked apply total, all 42 within the past day. Confirmation "
                 "arrived as a generic \"thank you for your application to the Omnicom network\" email (BBDO "
                 "is part of the Omnicom network, so it routes through their shared Workday ATS rather than "
                 "naming BBDO directly) -- initially miscounted as a separate 3rd Omnicom general application "
                 "before Regina clarified it's this same BBDO application.",
        "pay_range": "$95K-$110K/yr",
        "applicant_count": 42,
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: day-to-day strategy support on assignments/brands, leading "
                         "strategy from briefing through creative development to measurement, effectiveness "
                         "writing, new-business support, leading creative-review feedback, in-office 3+ "
                         "days/week. Collaborating with creative teams and creative-review feedback overlap "
                         "with Regina's background, but 'own and lead strategy deliverables independently' "
                         "reflects the same dedicated-strategist-career gap seen on the Droga5, Design "
                         "Bridge/Landor, and NYT Senior Strategist roles.",
    },
    # -- 2026-09-22 (evening rescan): incremental rescan, 3 new rows --
    {
        "company": "Monster Energy",
        "position": "Senior Graphic Designer, Americas",
        "status": "Applied",
        "applied_date": "2026-09-22",
        "source": "Email",
        "notes": None,
        "pay_range": "$108,750-$145,000/yr",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed general posting: 5+ yrs print graphic design for large consumer brands, "
                         "creating marketing collateral/POS materials/packaging across Monster's M-Claw "
                         "brands, Adobe CS. The consumer-brand packaging/print-production overlap with "
                         "Regina's Common Matter background is strong, but the role is based in Corona, CA -- "
                         "no remote/NYC arrangement was confirmed in the posting.",
    },
    {
        "company": "Born Social",
        "position": "Associate Creative Director [NYC]",
        "status": "Applied",
        "applied_date": "2026-09-22",
        "source": "Teamtailor",
        "notes": None,
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't find or confirm the exact 'Associate Creative Director [NYC]' posting on "
                         "Born Social's own board (only an Associate Director, Client Services role and other "
                         "differently-titled reqs turned up), so there's nothing concrete to assess fit "
                         "against.",
    },
    # -- 2026-09-22 (later): found via Gmail, distinct from the Anna --
    # Callagher thread -- a separate Craft recruiter, freelance track --
    {
        "company": "Craft",
        "position": "Networking call -- Fionn Andrews, Lead Recruiter (Freelance Brand, Design & Creative)",
        "status": "Networking",
        "applied_date": "2026-09-22",
        "source": "Referral",
        "notes": "Distinct from the pending Anna Callagher call (booked for 09-23, re: one of the 3 "
                 "full-time Craft job applications) -- Fionn Andrews is a separate Craft recruiter for their "
                 "freelance placement arm. A call already happened (\"thanks for the chat!\") before this "
                 "email, exact call date unconfirmed; Fionn onboarded Regina onto Craft's 'Taste' "
                 "freelance-project platform. Same day, she completed her profile and applied to the "
                 "'Senior Designer, Brand Guidelines and Identity' project -- see the separate Craft (Taste) "
                 "row for that application's own status.",
    },
    {
        "company": "Craft (Taste freelance platform)",
        "position": "Senior Designer, Brand Guidelines and Identity",
        "status": "Offer",
        "applied_date": "2026-09-22",
        "had_interview": 1,
        "interview_dates": ["2026-09-22"],
        "pay_range": "$85/hr, paid as $510 per deliverable (6 hrs budgeted per deliverable)",
        "next_step": "2026-09-27: Confirmed in for the 'GoldenStone Slides & Docs' project as Brand Designer, "
                     "$85/hr ($510/deliverable), starting Thursday, Oct 1 -- pending ID check and background "
                     "check. Taste flagged (2026-09-27, later) that a Checkr background-check email was on its "
                     "way, requiring full legal name/DOB/SSN (or equivalent) plus employment history. "
                     "2026-09-28: Regina submitted the background check and replied to Dave flagging a "
                     "discrepancy -- the confirmed project is 'GoldenStone Slides & Docs' but she'd understood "
                     "she was joining 'Guidelines and Identity' (the position title/assessment this row is "
                     "under). Also hasn't received the SOW yet. 2026-09-30: Ceren Berk (tastemaker.pro) sent a "
                     "kickoff call invite for the 'Goldenstone Slides & Docs Project - Brand Designers' group, "
                     "Thu Oct 1, 1:00-1:30pm ET -- a large group invite (11+ other designers cc'd), confirming "
                     "the project is proceeding on schedule despite the project-name question still not "
                     "explicitly answered by Dave. 2026-10-01: the SOW arrived via PandaDoc (sent by David "
                     "Barner, 'Regina Barrera & Taste Tech Inc. - Slides&Docs Project - Brand Designer') -- "
                     "Regina hasn't signed it yet. 2026-10-01 (later): the SOW was completed by all "
                     "participants -- fully signed. Remaining steps: set up a tastemaker.pro email, get added "
                     "to the project Slack, attend the kickoff call (was scheduled for Thu Oct 1, so should "
                     "have happened by now). 2026-10-06: Checkr confirmed the background check is complete and "
                     "the report was sent to Taste AI, who will notify Regina of next steps. 2026-10-16: "
                     "active and billing -- reminder to report hours for the Oct 1-15 payment cycle via the "
                     "Payment Center, confirming the Brand Designer work is underway. 2026-10-21: Taste Labs "
                     "said Brand is almost wrapped and asked if she wants to keep going, offering to move her "
                     "from Brand into Presentation Design on the same GoldenStone project (separately, an "
                     "unrelated generic \"open design projects\" solicitation arrived the same day from Taste's "
                     "broader recruiting list -- excluded as unsolicited, not tied to this project). 2026-10-23: "
                     "approved for Presentation Design on GoldenStone with the assessment waived. 2026-10-24: "
                     "TasteMakers' own system separately flagged her as \"selected\" for a Brand Designer/Art "
                     "Director assessment (Pitch, Brand Kit, Presentation) -- likely just the same Presentation "
                     "Design move working through two different internal systems, not a distinct role; not "
                     "guessing further. Same day, a new PandaDoc SOW arrived from David Barner for \"GoldenStone "
                     "Slides & Docs Project - Presentation Designer\" -- not yet signed as of this scan. "
                     "2026-10-26: that SOW is now fully signed/completed by all participants -- the "
                     "Presentation Designer role on GoldenStone is confirmed and underway.",
        "source": "Referral",
        "notes": "Freelance project application via Craft's Taste platform (Fionn Andrews onboarded her "
                 "earlier the same day) -- submitted brand guideline samples as the design assessment. Same "
                 "day: assessment submitted, reviewed, and selected to move forward, with a Master Freelance "
                 "Agreement/Statement of Work now being sent -- treated as Offer status since a freelance "
                 "engagement contract is being extended, pending identity verification and paperwork. "
                 "2026-09-23: Regina completed identity verification and checked in with Fionn about next "
                 "steps; he confirmed it's now with Taste's team to review and reach out directly. 2026-09-27: "
                 "Taste (Dave, recruiting@tastelabs.com) confirmed the project assignment, rate, and start date.",
        "job_fit": "Strong",
        "job_fit_notes": "Brand guidelines and identity design is squarely Regina's specialty from her "
                         "Common Matter agency background and SVA Branding Master's -- a direct match, "
                         "reflected in being selected to move forward same-day.",
    },
    # -- 2026-09-22 (later still): reported directly by Regina, found via Gmail Sent search --
    {
        "company": "Mischief",
        "position": "Networking outreach -- no open role (contact: Robyn)",
        "status": "Networking",
        "applied_date": "2026-09-22",
        "source": "Cold email",
        "notes": "Warm-intro cold email to robyn@mischiefusa.com, referred by Sadia -- Mischief isn't "
                 "actively hiring, but Sadia flagged they might need extra design support as things get "
                 "busy. Portfolio linked, no resume attached, no specific role applied to. 2026-10-21: Robyn "
                 "Makinson sent a calendar invite for \"Connect w/Regina,\" confirmed for Monday, Oct 26, "
                 "1:00-2:00pm ET (Zoom) -- this follow-up networking call grew out of the cold outreach.",
    },
    {
        "company": "LOS YORK",
        "position": "Freelance Brand Strategist",
        "status": "Applied",
        "applied_date": "2026-09-22",
        "source": "Cold email",
        "notes": "Direct cold-email application to katy.b@losyork.tv in response to a LinkedIn post about the "
                 "freelance opening, resume attached and portfolio linked -- found via Gmail Sent search.",
        "job_fit": "Good",
        "job_fit_notes": "No formal job posting found, only company profile -- LOS YORK is an LA/NY "
                         "multidisciplinary creative production studio (Amazon, Netflix, Logitech) spanning "
                         "brand strategy, content, and production from strategy through execution. Regina's "
                         "SVA Branding Master's and brand-strategy/positioning/research/messaging background "
                         "is a solid general match, though the studio's focus tilts more toward video/content "
                         "production than her more identity-and-print-centric Common Matter background.",
    },
    # -- 2026-09-23: found via Gmail -- no prior confirmation email or --
    # Sent-mail record exists for the original application; picked up --
    # here directly from the interview-invite email --
    {
        "company": "Canopy",
        "position": "Graphic Designer",
        "status": "Interviewing",
        "applied_date": "2026-09-23",
        "next_step": "Intro call with Katy Spore happened as scheduled on 2026-09-23. No word since, so "
                     "Regina sent a check-in email on 2026-09-28 reaffirming interest and addressing an "
                     "experience concern Katy raised on the call. Awaiting Katy's response. Full process if "
                     "it progresses: possible assessment, team/project presentation, then an offer.",
        "source": "Email",
        "notes": "No original application-confirmation email or Sent-mail record was found for this one -- "
                 "picked up directly from the interview-invite email, so the true applied_date is unconfirmed "
                 "(using the invite date as a placeholder).",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm the exact posting or which 'Canopy' this is with certainty (a "
                         "Graphic Designer, Mid opening in the NYC Metro area turned up under the getcanopy "
                         "name, but wasn't confirmed as this exact req).",
        "had_interview": 1,
        "interview_dates": ["2026-09-23"],
    },
    {
        "company": "Polonsky & Friends",
        "position": "Junior Graphic Designer",
        "status": "Rejected",
        "applied_date": "2026-09-23",
        "source": "Jotform (direct application)",
        "notes": "Found via a friend's referral (posting was shared to her directly) -- applied via Jotform "
                 "with resume and portfolio (reginabbsv.cargo.site) attached. Confirmed via the Jotform "
                 "submission-receipt email, which includes her full application answers. Rejected 2026-09-30 -- "
                 "explicitly cited as overqualified: the role is set up for someone earlier in their career. "
                 "Regina replied same day thanking them and asking to be kept in mind for future openings.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: a food & hospitality branding studio (P&F), internship-level "
                         "role at 20 hrs/week for 6-12 months. Strong stylistic/content fit -- brand identity, "
                         "packaging, and food/hospitality work all line up with Regina's background (including "
                         "prior work with Mexican food brands) -- but it's an internship/junior title and "
                         "part-time hours, well below her 7 years of agency experience.",
    },
    {
        "company": "Craft",
        "position": "Graphic Designer",
        "status": "Rejected",
        "applied_date": "2026-09-25",
        "source": "Craft (recruitment agency ATS)",
        "notes": "4th, distinct Craft application -- separate from the earlier Red Antler (Senior Designer), "
                 "Vault 49 (Brand Designer), and still-unresolved Freelance Senior Brand Designer applications. "
                 "Confirmed only via Craft's generic \"application received\" auto-reply (applications@itscraft.com); "
                 "no Sent-mail record or client name surfaced, so which client req this was for was never "
                 "confirmed. Rejected 2026-09-29 via a generic \"not progressing\" decline, also from Craft "
                 "directly rather than naming a client -- so the underlying company is still unknown.",
        "job_fit": "Unknown",
        "job_fit_notes": "No client or posting details available -- only a generic Craft confirmation email, "
                         "with no specifics about the hiring company or the exact role requirements.",
    },
    {
        "company": "Morning Brew",
        "position": "Associate, GTM Strategy",
        "status": "Applied",
        "applied_date": "2026-09-25",
        "source": "Lever",
        "notes": "Confirmed via Lever's \"Thank you for your application\" auto-reply.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: an early-career (Associate-level) role building sales/sponsorship "
                         "decks and packages for Morning Brew's GTM/ad-sales team -- turning research and "
                         "editorial ideas into clean, persuasive slides, with some exposure to pricing/packaging "
                         "strategy. Remote-friendly, $75K-$80K per Glassdoor. Regina's storytelling and "
                         "deck/presentation craft overlap, but it's a sales-enablement function rather than "
                         "brand/design work, and an Associate title is a level down from her 7 years of agency "
                         "experience.",
    },
    {
        "company": "2x4",
        "position": "Design Intern / Branding",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Email",
        "notes": "Direct cold-email application to internships@2x4.org, resume and portfolio "
                 "(reginabbsv.cargo.site) attached -- found via Gmail Sent search.",
        "job_fit": "Fair",
        "job_fit_notes": "No formal posting found, only 2x4's internship inbox -- 2x4 is a well-known NYC "
                         "branding and design studio spanning identity, campaigns, editorial, packaging, "
                         "digital, and print. Strong stylistic overlap with Regina's Common Matter/SVA Branding "
                         "background, but an internship-level Branding-team role is well below her 7 years of "
                         "agency experience.",
    },
    {
        "company": "2x4",
        "position": "Designer / Digital",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Email",
        "notes": "Direct cold-email application to jobinquiries@2x4.org, resume attached -- found via Gmail "
                 "Sent search. Sent 5 minutes after the 2x4 Design Intern / Branding application, same studio.",
        "job_fit": "Good",
        "job_fit_notes": "No formal posting found, only 2x4's general inquiries inbox -- this is a Digital-team "
                         "role, not explicitly senior/junior. Regina's background spans brand and digital "
                         "design (identities, visual systems, websites, digital experiences, campaigns), a "
                         "solid general match, though the exact seniority/level of this specific opening "
                         "couldn't be confirmed.",
    },
    {
        "company": "Onebrief",
        "position": "Senior Brand Designer",
        "status": "Rejected",
        "applied_date": "2026-09-27",
        "source": "Ashby",
        "notes": "Confirmed via Ashby's auto-reply. Rejected 2026-09-30 -- generic \"moving forward with other "
                 "candidates\" decline.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: Onebrief builds AI-powered military-planning/collaboration "
                         "software (backed by General Catalyst, Battery, Insight, valued $2B+); this Senior "
                         "Brand Designer role shapes visual identity across marketing/sales touchpoints and "
                         "translates complex operational/technical concepts into cohesive visual design. "
                         "Remote, US. A solid match to Regina's brand-identity and visual-systems background, "
                         "though the defense/military-planning subject matter is a new domain for her.",
    },
    {
        "company": "Meta",
        "position": "Brand Designer, Foundations - Instagram Brand Studio",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Email",
        "pay_range": "$149K-$209K/yr",
        "notes": "6th, distinct Meta application -- same Instagram Brand Studio team as the existing "
                 "\"Strategic Initiatives\" (applied 07-26) and \"Iconography & Illustration\" (applied 09-06) "
                 "roles, but a different req/specialization within it.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: owns the strategic design and scaling of Instagram's visual "
                         "identity system -- typography, color, layout systems, multi-channel applications -- "
                         "translating brand strategy into scalable design systems. Overlaps with Regina's "
                         "brand-identity/systems background, but like the other Instagram Brand Studio roles, "
                         "this reads as a senior/strategic-track position, and desirable motion/creative-coding/"
                         "AI-workflow skills aren't evidenced on her resume.",
    },
    {
        "company": "Profound",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Ashby",
        "notes": "Confirmed via Ashby's auto-reply.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: Profound is an AI-era marketing platform (backed by Lightspeed, "
                         "Sequoia, Kleiner Perkins, Khosla; ~$1B valuation; NYC/SF/Buenos Aires/London). This "
                         "Brand Designer role defines and shapes how Profound looks and feels across every "
                         "channel -- campaigns, events, and the visual systems that scale the brand -- a close "
                         "match to Regina's brand-identity and visual-systems background.",
    },
    {
        "company": "HappyRobot",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Ashby",
        "pay_range": "$120K-$150K/yr",
        "notes": "Confirmed via Ashby's auto-reply.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: HappyRobot builds AI-worker infrastructure for enterprises (Y "
                         "Combinator S23, backed by a16z/Base10/Prysm/Eurazeo, $150M+ raised). This Brand "
                         "Designer role maintains and evolves the brand's visual language across a high volume "
                         "of brand/marketing work -- social, print, physical formats, OOH, merch -- a solid "
                         "match to Regina's broad brand-production background. San Francisco with a remote "
                         "option.",
    },
    {
        "company": "OLIVER",
        "position": "Senior Designer (3rd application)",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Greenhouse",
        "notes": "Third, distinct Greenhouse confirmation for a same-titled 'Senior Designer' posting -- OLIVER "
                 "runs many concurrent Senior Designer reqs across different client accounts, so this reads as "
                 "a separate opening from the 09-06 and 09-19 applications rather than a duplicate. Generic "
                 "confirmation email (\"Thank you for interest in the Senior Designer posting\") did not name "
                 "the specific client account or req. A generic OLIVER rejection email arrived 2026-10-06 with "
                 "no job title or req ID -- could pertain to this application or to any of OLIVER's three "
                 "other still-open ones; not guessing which, status left unchanged.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm which specific client account or req this confirmation was for "
                         "among OLIVER's several concurrently open Senior Designer listings.",
    },
    {
        "company": "Thyme Care",
        "position": "Visual Designer, Marketing",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Ashby",
        "pay_range": "$115K-$135K/yr",
        "notes": "Confirmed via Ashby's auto-reply.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: Thyme Care is a value-based oncology care company; this Visual "
                         "Designer role on the Marketing team owns design/production of campaigns, digital "
                         "assets, social content, presentations, and experiential materials within an "
                         "established brand system (Figma/Adobe CS/Google Workspace). 4+ yrs experience -- a "
                         "solid match to Regina's brand-production background, with healthcare/oncology as a "
                         "new industry context for her. Remote.",
    },
    {
        "company": "ShopMy",
        "position": "Unspecified role (Design)",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Greenhouse",
        "notes": "Generic Greenhouse confirmation (\"Thanks for applying to ShopMy\") did not name the role. "
                 "ShopMy (creator-commerce/influencer platform) had several open design roles at the time -- "
                 "Senior Product Designer, Associate UI Product Designer, and Senior Brand Designer -- most "
                 "likely the Senior Brand Designer given her background, but not confirmed.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm which of ShopMy's several open design roles this application was "
                         "for.",
    },
    {
        "company": "Rightway",
        "position": "Sr. Graphic Designer",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Greenhouse",
        "notes": "Confirmed via Greenhouse's auto-reply. A second, identical confirmation email arrived "
                 "2026-10-07, same title/company, no req ID or distinguishing detail -- likely an accidental "
                 "duplicate re-application during a late-night application sprint rather than a genuinely "
                 "separate posting; not logged as a second row.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: Rightway is a healthcare-navigation tech company; this Sr. "
                         "Graphic Designer role stewards the brand across marketing assets (web, email, social, "
                         "print) -- landing pages, sellsheets, presentations, posters, social graphics -- a "
                         "solid match to Regina's brand-production background, with healthcare as a new "
                         "industry context for her.",
    },
    {
        "company": "Code and Theory",
        "position": "Unspecified role (Design)",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Email",
        "notes": "Generic confirmation (\"Thank you for your interest in Code and Theory\") did not name the "
                 "role. Code and Theory is a digital-first creative agency with several open designer roles at "
                 "the time -- Senior Experience Designer, Senior Designer, and Junior Designer -- not confirmed "
                 "which one this was for.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm which of Code and Theory's several open designer roles this "
                         "application was for.",
    },
    {
        "company": "SHADOW",
        "position": "Designer",
        "status": "Rejected",
        "applied_date": "2026-09-27",
        "source": "Greenhouse",
        "notes": "Confirmed via Greenhouse's auto-reply; role title inferred from SHADOW's only open design "
                 "listing found (Creative Division). Rejected 2026-10-03 -- generic decline, not deciding to "
                 "proceed with the candidacy.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: SHADOW is a creative marketing/communications agency; this "
                         "Creative Division Designer role wants 3-5 yrs, preferably agency or consumer-brand "
                         "experience, working across print, UI, email, spatial, packaging, and merch -- a solid "
                         "match to Regina's Common Matter agency background.",
    },
    {
        "company": "webAI",
        "position": "Marketing Designer",
        "status": "Offer",
        "applied_date": "2026-09-27",
        "had_interview": 1,
        "interview_dates": ["2026-10-05", "2026-10-19"],
        "source": "Ashby",
        "next_step": "Michael Hale (Technical Recruiter) reached out 2026-10-02 to schedule an intro call; "
                     "Regina booked Monday, Oct 5, 11:30am-12pm ET via his Google Calendar link (20-30 min "
                     "video call). That recruiter screen happened; the same day, Michael emailed that he'd "
                     "shared her info with the Hiring Manager, who wants to chat next. Regina booked that "
                     "call for Thursday, Oct 15, 1:00-1:30pm ET via Ashby (Google Meet). 2026-10-15: Regina "
                     "missed this second-round call due to a calendar mix-up -- her Google Calendar showed "
                     "1:00pm but Ashby had it listed for 12:30pm. She emailed Michael and Jaslin Tonton the "
                     "same day to apologize and rescheduled; the call is now confirmed for Monday, Oct 19, "
                     "12:00-12:30pm ET. 2026-10-19: another mix-up at call time (wrong meeting link posted by "
                     "Ashby), resolved within a few minutes over email and the call happened. Same afternoon, "
                     "Ashby sent official next steps: webAI wants to move her forward to a group-interview "
                     "stage (\"meet with members of the team you'd work closely with\" plus a technical "
                     "problem-solving walkthrough) -- asked her to submit availability via an Ashby scheduling "
                     "link. 2026-10-19 evening: calendar invite arrived from Marcus Godin (webai.com) for "
                     "\"Marketing Designer @ webAI - Team Interview,\" confirmed for Tuesday, Oct 20, "
                     "9:00-10:00am ET (Google Meet). 2026-10-20, right at start time: Jaslin preemptively sent "
                     "a backup Meet link \"in case the same thing is happening again\" -- no follow-up message "
                     "either way, so whether another mix-up actually occurred or the backup link was just "
                     "precautionary isn't confirmed; not guessing the outcome. The Oct 20 group/team interview "
                     "did happen. 2026-10-21: Marcus (covering for Michael, who's out of town) texted asking "
                     "for a quick call; the call happened and webAI is moving Regina to the offer stage -- "
                     "they're submitting her comp to finance for approval and will follow up today or tomorrow "
                     "with a number, then a text and a call to discuss. Regina intends to ask for $95K (up from "
                     "the $90K she originally gave Michael on the 10/5 intro call), within the role's $80K-"
                     "$100K band. 2026-10-22: formal offer call (HR, covering for Michael) -- base salary "
                     "confirmed at Regina's ask, $95,000. Equity: 2,800 options, strike price ~$5.50, with a "
                     "hypothetical/estimated future sale price of ~$32.50 used to project a rough total equity "
                     "value of ~$70-75K over a vesting period (~$18-19K/year) -- framed by HR as bringing total "
                     "comp to a \"$113-114K\" quote-unquote figure, though this equity value is a speculative, "
                     "illiquid projection tied to an unreleased internal valuation, not guaranteed money. "
                     "Standard 4-year vesting mentioned; exact cliff/post-termination exercise window not yet "
                     "confirmed in writing. Proposed start date Nov 2, 2026 (backup option Nov 16); Regina "
                     "confirmed Nov 2 works. HR asked whether Regina had other processes in play -- she said "
                     "she has other conversations in progress but none at offer stage yet, and expressed "
                     "genuine excitement about webAI. HR is sending a soft-offer email plus a DocuSign and an "
                     "updated benefits guide; Regina has not yet signed as of this call. No written offer "
                     "confirmed yet -- treating this as Offer status based on the verbal terms given, to be "
                     "finalized once the DocuSign/written offer arrives. 2026-10-22 evening: formal written "
                     "offer email arrived from Marcus Godin -- $95,000 salary, 2,800 options with a confirmed "
                     "4-year vesting schedule and 1-year cliff, target start date Nov 2. **Offer valid for 5 "
                     "business days from 10/22** (i.e. roughly through Thu 10/29) -- a real decision deadline. "
                     "Regina asked follow-up questions: several perks from the original job posting (a $200/mo "
                     "health & wellness stipend, Function Health subscription) weren't in the attached benefits "
                     "guide -- Marcus said the guide was outdated (benefits were re-elected for next year) and "
                     "sent an updated list (HSA/FSA-based health plan, 401k match, flexible PTO, parental "
                     "leave, continuing education support (case-by-case, not a fixed stipend), life/disability "
                     "insurance, free in-office parking). Performance reviews are bi-annual (every 6 months) "
                     "with potential base/equity increases. No coworking stipend or WFH equipment budget as a "
                     "standard benefit -- Marcus is checking whether any flexibility exists after Regina asked "
                     "about partial reimbursement, given she'd be fully remote from NYC; awaiting his reply. "
                     "No DocuSign sent/signed yet as of this scan. 2026-10-23: Marcus confirmed there's still "
                     "no coworking-space program or reimbursement, but finance bumped the base salary to "
                     "**$98,000** (up from $95,000) to help cover a coworking membership instead. Equity/"
                     "options terms unchanged. Still no DocuSign sent/signed as of this scan.",
        "notes": "Confirmed via Ashby's auto-reply.",
        "pay_range": "$98K base + 2,800 stock options",
        "job_fit": "Good",
        "job_fit_notes": "Per the 2026-10-05 intro call with Michael Hale: webAI is a ~200-person Austin AI "
                         "startup (decentralized/on-device AI solutions), design team of 5-6. This is an open "
                         "junior/mid-level generalist design role spanning marketing/sales collateral, digital, "
                         "and possibly web -- a solid match for Regina's generalist brand/marketing design "
                         "background, though likely a step below her actual 6+ yrs of seniority. Fully remote "
                         "(this team doesn't require Austin relocation). Michael confirmed OPT/TN timeline "
                         "isn't a concern on their end.",
    },
    {
        "company": "The Farmer's Dog",
        "position": "Brand Designer",
        "status": "Rejected",
        "applied_date": "2026-09-27",
        "source": "Greenhouse",
        "pay_range": "$80K-$90K/yr",
        "notes": "Confirmed via Greenhouse's auto-reply. Rejected 2026-10-12 -- generic \"decided to move "
                 "forward with other candidates\" decline.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: The Farmer's Dog is a DTC fresh-pet-food subscription company; "
                         "this Brand Designer role creates marketing/digital/print creative across channels "
                         "(email, social, landing pages, print) and develops brand standards/physical touchpoints "
                         "including packaging. 3+ yrs, agency and/or client-side -- a solid match to Regina's "
                         "background.",
    },
    {
        "company": "Fanatics Collectibles",
        "position": "Senior Graphic Designer",
        "status": "Rejected",
        "applied_date": "2026-09-27",
        "source": "Email",
        "notes": "Confirmed via automated confirmation email. Rejected 2026-10-04 -- generic decline, "
                 "decided to move forward with other candidates.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed general scope: designs trading cards, branding, and marketing assets for "
                         "Fanatics Collectibles, managing projects through print production. Print-design craft "
                         "overlaps with Regina's background, but the trading-card/collectibles print-production "
                         "specialization is a narrower niche than her branding-agency experience.",
    },
    {
        "company": "Agentio",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Ashby",
        "pay_range": "$72K-$108K/yr",
        "notes": "Confirmed via Ashby's auto-reply.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: Agentio is a creator-ads adtech startup; this Brand Designer role "
                         "drives design from concept to execution across digital, print, video, and events, "
                         "wanting 3-6+ yrs in brand design with strong storytelling skills -- a solid match to "
                         "Regina's background. On-site, New York, NY.",
    },
    {
        "company": "OLIVER",
        "position": "Digital Content Designer",
        "status": "Rejected",
        "applied_date": "2026-09-27",
        "source": "Greenhouse",
        "notes": "5th, distinct OLIVER application -- a genuinely different title from the other four OLIVER "
                 "applications (Social & Culture Strategist; Senior Designer x3). Confirmed via Greenhouse's "
                 "auto-reply (\"Thank you for interest in the Digital Content Designer posting\"). A generic "
                 "OLIVER rejection email arrived 2026-10-06 with no job title or req ID -- could pertain to "
                 "this application or to any of OLIVER's three other still-open ones (Senior Designer x3); "
                 "not guessing which, status left unchanged. 2026-10-20: a second, named rejection arrived "
                 "(\"Important information about your application to The Inside Ideas Group\"), explicitly "
                 "for the Digital Content Designer role -- flipped to Rejected. The earlier 10-06 generic "
                 "rejection most likely belonged to one of the Senior Designer applications instead, since "
                 "this one got its own dedicated rejection email.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed general scope: end-to-end design and production of content for a client's "
                         "flagship digital display platform, with motion graphics/video editing/Gen AI tool "
                         "proficiency called out. Digital-production overlap with Regina's background, but "
                         "motion/video work is the recurring gap seen on several other OLIVER and Meta roles.",
    },
    {
        "company": "Digital Asset",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "HiBob",
        "notes": "Confirmed via HiBob's auto-reply, which did not include posting details.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't find the specific posting or confirm what the role required -- Digital "
                         "Asset appears to be a blockchain/DLT company, but no further detail was available.",
    },
    {
        "company": "Bespoke Post",
        "position": "Graphic Designer",
        "status": "Interviewing",
        "applied_date": "2026-09-27",
        "had_interview": 1,
        "interview_dates": ["2026-10-01", "2026-10-14", "2026-10-21"],
        "source": "Lever",
        "next_step": "Kate Mulcahy reached out 2026-09-29 to schedule a phone call; Regina replied 2026-09-30 "
                     "with her availability, and the call is now confirmed for Thursday, Oct 1, 12:15-12:45pm "
                     "ET (phone call, despite the auto-generated Google Meet link on the invite). That call "
                     "happened and went well; Kate followed up 2026-10-05 wanting to schedule a next "
                     "conversation with Bespoke Post's Associate Creative Director. After some back-and-forth "
                     "(the ACD was OOO until Monday), the call is confirmed for Monday, Oct 12, 1:30-2:00pm ET "
                     "with Joelyn Dalit (Associate Creative Director). Note: in the scheduling exchange, Kate "
                     "mentioned she's researching whether Bespoke Post could support a TN visa for Regina in "
                     "the future -- Regina said it's light on the employer side (a support letter rather than "
                     "formal sponsorship). Visa sponsorship/support may be a relevant factor for Regina's "
                     "search generally. 2026-10-09: Regina asked Kate to move the Oct 12 call to another day "
                     "next week -- she had to travel home unexpectedly for a family matter and her schedule "
                     "got tighter (unclear if related to the earlier Houston/mother's-surgery trip or a "
                     "separate one; not guessing). New date not yet confirmed; round 2 removed from "
                     "interview_dates until it actually happens. Kate replied the same evening offering Tue "
                     "10/13 at 3:00pm ET or Wed 10/14 at 1:30pm ET. The original Oct 12 calendar invite was "
                     "canceled. 2026-10-12: Regina confirmed Wednesday, Oct 14, 1:30pm ET for the rescheduled "
                     "round 2 with Joelyn Dalit. That round 2 call happened and went well -- Kate wrote "
                     "2026-10-15 that \"Joelyn really enjoyed their conversation,\" and the next step is a "
                     "video meeting with Bespoke Post's Chief Creative Officer (round 3). Kate asked for "
                     "Regina's availability next week, and separately asked when Regina's OPT expires \"to "
                     "understand the timing.\" 2026-10-16: Regina replied with a detailed week-of-Oct-19 "
                     "availability window and confirmed her OPT is valid through September 2027, after which "
                     "she'd transition to TN status -- she said she can handle that visa process herself and "
                     "would just need an employment support letter from the company. Awaiting Kate's reply to "
                     "confirm the CCO round 3 date/time. 2026-10-20: Kate proposed Wednesday, Oct 21, 3:00pm "
                     "ET; Regina confirmed the same day, and a calendar invite followed for Wed, Oct 21, "
                     "3:00-3:30pm EDT with Danny Cohn (Bespoke Post's CCO) -- round 3 now locked in. 2026-10-21: "
                     "the call happened -- Regina joined about 3 minutes late (Kate checked in mid-call asking "
                     "if everything was okay since Danny hadn't seen her join yet), but she and Danny connected "
                     "and Regina described it as \"a really great conversation.\" Awaiting next steps. "
                     "2026-10-22: with a real competing offer in hand (webAI, $95K), Regina emailed Kate -- "
                     "said she enjoyed the Danny call, flagged the offer/number, and asked where things stand "
                     "given she has a decision to make soon. No reply from Kate yet as of this scan.",
        "notes": "2nd, distinct Bespoke Post application -- separate from the earlier Strategist, Growth "
                 "Marketing application (applied 08-17, Weak fit). Confirmed via Lever's auto-reply.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't find the specific Graphic Designer posting to confirm requirements.",
    },
    {
        "company": "Wpromote",
        "position": "Senior Pitch Designer",
        "status": "Rejected",
        "applied_date": "2026-09-27",
        "source": "Lever",
        "pay_range": "$75K-$90K/yr",
        "notes": "Confirmed via Lever's auto-reply. Rejected 2026-09-29 -- generic 'moving forward with other "
                 "candidates' decline (email subject referenced 'Wpromote x Giant Spoon', suggesting this req "
                 "was a joint/agency-partner listing).",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: design lead on Wpromote's enterprise new-business pitches, turning "
                         "strategy docs, audit findings, and media plans into pitch decks, data visualizations, "
                         "and motion/video assets (PowerPoint/Google Slides, Adobe CS, Figma, Premiere, After "
                         "Effects). Overlaps with Regina's strategy-and-deck-building skills (similar to the "
                         "Morning Brew GTM Strategy role), but the motion/video tools aren't a demonstrated "
                         "strength.",
    },
    {
        "company": "Verve",
        "position": "Unspecified role (Design)",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Greenhouse",
        "notes": "Generic confirmation (\"Thank you for your interest in Verve\") did not name the role. Verve "
                 "(ad-tech company) had multiple open design roles at the time -- Visual Designer, Marketing "
                 "($75K-$85K, 2+ yrs) and Strategy & Presentation Designer -- not confirmed which.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm which of Verve's open design roles this application was for.",
    },
    {
        "company": "J.Crew",
        "position": "Sr. Digital Designer",
        "status": "Rejected",
        "applied_date": "2026-09-27",
        "source": "Workday",
        "notes": "Confirmed via Workday's auto-reply. Rejected 2026-10-07 -- generic decline, resume kept on "
                 "file.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: Senior-level, hybrid, NY HQ, wants 7+ yrs experience with Figma/"
                         "InDesign/Photoshop. The 7+ yrs bar is a bit beyond Regina's ~7 years, and retail/"
                         "fashion digital design is a different context from her branding-agency background, "
                         "though the core design skills overlap.",
    },
    {
        "company": "VaynerMedia",
        "position": "Designer",
        "status": "Applied",
        "applied_date": "2026-09-27",
        "source": "Greenhouse",
        "notes": "Confirmed via Greenhouse's auto-reply.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 2+ yrs experience, skills in motion graphics, color grading, and "
                         "Photoshop, agency environment -- a solid general match to Regina's agency background, "
                         "though motion/color-grading specifics aren't strongly evidenced on her resume.",
    },
    {
        "company": "goop",
        "position": "Senior Graphic Designer",
        "status": "Rejected",
        "applied_date": "2026-09-28",
        "source": "Greenhouse",
        "notes": "Generic confirmation (\"Thank you for your application to goop\") did not name the role. goop "
                 "had a Senior Graphic Designer opening at the time (6+ yrs, beauty/wellness/fashion/luxury, "
                 "$70K-$80K+equity) that was the most likely match -- confirmed 2026-10-09 when Greenhouse sent "
                 "a rejection naming the role directly (\"the Senior Graphic Designer position has been "
                 "filled\").",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm the specific posting's requirements before the role was filled.",
    },
    {
        "company": "Warner Bros. Discovery",
        "position": "Digital Designer, CNN",
        "status": "Applied",
        "applied_date": "2026-09-28",
        "source": "Workday",
        "notes": "Confirmed via Workday's auto-reply, which named the req (R000107792) but included no further "
                 "posting details. Posting confirmed 2026-10-15 via Regina -- same req ID (R000107792), hiring "
                 "entity is Turner Services Inc.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: hybrid (Atlanta/NYC/Burbank), $63,008-$117,016/yr, requires 5+ "
                         "yrs designing for broadcast, streaming, digital, or social-first campaigns, "
                         "Photoshop/Illustrator/InDesign/After Effects, HTML5 + motion graphics for digital "
                         "\"strongly preferred.\" Regina's 6+ yrs clears the bar, but the HTML5 and motion-"
                         "graphics emphasis aren't evidenced on her resume.",
    },
    {
        "company": "TRM Labs",
        "position": "Senior Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-28",
        "source": "Ashby",
        "notes": "Confirmed via Ashby's auto-reply.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: TRM Labs builds AI-powered blockchain-intelligence software for "
                         "public/private-sector crime investigation. This Senior Brand Designer role owns brand "
                         "design end-to-end -- campaigns, web, social, events, sales/marketing materials, "
                         "reports -- including turning data-heavy topics into infographics with AI-assisted "
                         "workflows. A solid match to Regina's brand-design and creative-briefing background; "
                         "blockchain/crime-intelligence is a new industry context for her.",
    },
    {
        "company": "Alpaca Markets",
        "position": "Senior Graphic Designer",
        "status": "Applied",
        "applied_date": "2026-09-28",
        "source": "Email",
        "notes": "Confirmed via automated confirmation email.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 7+ yrs professional graphic/visual/brand/marketing design "
                         "experience producing multi-channel go-to-market assets -- campaigns, product launches, "
                         "demand gen, sales enablement, events, corporate comms -- within an established brand "
                         "system. Seniority and production breadth line up well with Regina's background.",
    },
    {
        "company": "Red Antler",
        "position": "Senior Digital Designer",
        "status": "Applied",
        "applied_date": "2026-09-28",
        "source": "Breezy",
        "notes": "2nd, distinct Red Antler application -- separate from the Craft-routed 'Senior Designer' req "
                 "(applied 09-14, currently Interviewing via Anna Callagher) and the earlier cold-outreach "
                 "networking attempts (08-25, no replies). This was a direct application through Red Antler's "
                 "own Breezy ATS. Confirmed via Breezy's auto-reply, which did not include full posting details.",
        "job_fit": "Good",
        "job_fit_notes": "No separate posting text found, but Red Antler's confirmed hiring focus (per the "
                         "Craft/Anna Callagher req) is large-scale branding and brand strategy for tech brands, "
                         "hiring across levels -- a 'Digital Designer' title suggests more digital-execution "
                         "focus, which still overlaps well with Regina's background.",
    },
    {
        "company": "Suno",
        "position": "Senior Designer, Creative Studio",
        "status": "Applied",
        "applied_date": "2026-09-28",
        "source": "Ashby",
        "notes": "Confirmed via Ashby's auto-reply.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: Suno (AI music-creation platform) is hiring a multidisciplinary "
                         "Senior Designer for its Brand & Creative Team, working at the intersection of brand, "
                         "culture, and product -- marketing campaigns, artist partnerships, in-product brand "
                         "moments, culture-defining activations. A solid match to Regina's brand-design "
                         "background in an exciting music-tech context.",
    },
    {
        "company": "Suno",
        "position": "Senior Designer, Creative Studio & Brand Campaigns (Contract)",
        "status": "Rejected",
        "applied_date": "2026-09-28",
        "source": "Ashby",
        "notes": "2nd, distinct Suno application -- a contract variant of the same Brand & Creative Team role, "
                 "applied minutes after the full-time req. Confirmed via Ashby's auto-reply. Rejected "
                 "2026-10-05 -- \"isn't a fit at this time,\" generic decline. The full-time req (Senior "
                 "Designer, Creative Studio) remains open/unanswered as of this scan.",
        "job_fit": "Good",
        "job_fit_notes": "Same Brand & Creative Team scope as the full-time Suno req (brand/culture/product "
                         "design across campaigns, artist partnerships, and activations) but structured as a "
                         "contract engagement -- a solid match to Regina's brand-design background.",
    },
    {
        "company": "Conduit Health",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-09-28",
        "source": "Ashby",
        "notes": "Confirmed via Ashby's auto-reply.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: Conduit Health (post-acute-care/AI-powered platform) is building "
                         "its first scalable brand and creative engine -- visual identity, voice, design "
                         "systems, and creative across ads, web, landing pages, decks, and lifecycle. 3+ yrs "
                         "brand/marketing design experience -- a close match to Regina's SVA Branding Master's "
                         "and Common Matter identity-systems background. NYC, hybrid.",
    },
    {
        "company": "FP Movement",
        "position": "Graphic Designer",
        "status": "Applied",
        "applied_date": "2026-09-28",
        "source": "iCIMS",
        "notes": "Confirmed via iCIMS's auto-reply (FP Movement is a Free People/Urban Outfitters brand).",
        "job_fit": "Fair",
        "job_fit_notes": "Couldn't confirm the exact req behind this generic confirmation, but FP Movement's "
                         "design postings around this time centered on seasonal apparel/activewear graphics -- "
                         "photo- and artwork-driven design and typography overlap generally with Regina's "
                         "background, though the apparel/activewear graphics niche is a different focus from "
                         "her brand-identity work.",
    },
    # -- 2026-10-05 (evening): 1 new row --
    {
        "company": "Porto Rocha",
        "position": "Brand Strategy (cold outreach -- no open role at time of contact)",
        "status": "Interviewing",
        "applied_date": "2026-08-26",
        "source": "Email",
        "notes": "Direct cold-outreach email to Natalee Ranii-Dropcho (Strategy & Copy Director) with resume "
                 "attached; no open strategy role existed at the time. Went unanswered for over a month, "
                 "then got a real reply 2026-10-05: Natalee asked which portfolio projects were speculative "
                 "vs. real client work, then said there's no Associate Strategist opening but asked if "
                 "Regina would consider a paid strategy internship. Regina said she's open to hearing more "
                 "though she's looking for full-time strategy work; awaiting Natalee's next message. "
                 "2026-10-13: Regina followed up to confirm she's still interested in the internship; Natalee "
                 "replied the same day proposing a call Oct 27 or 28 at 4pm to walk through Regina's SVA "
                 "projects and her approach to strategy. Regina confirmed either day works; calendar invite "
                 "followed for Tuesday, Oct 27, 4:00-4:30pm ET. Flipped to Interviewing since this is "
                 "effectively a first conversation for the internship opportunity. 2026-10-17: calendar "
                 "invite updated -- call time moved to 3:30-4:00pm ET (same date, Oct 27).",
        "job_fit": "Good",
        "job_fit_notes": "Porto Rocha is a well-regarded NYC branding studio; this was a speculative intro, "
                         "not a response to a specific posting. The paid-strategy-internship path now being "
                         "discussed is a good match for Regina's design-to-strategy transition, though it's "
                         "not the full-time strategy role she's ultimately after.",
        "cold_outreach": 1,
    },
    # -- 2026-10-07 (rescan): 7 new rows from a late-night application sprint (2026-10-06, ~8:20-9:03pm ET) --
    {
        "company": "Google",
        "position": "Unspecified role",
        "status": "Applied",
        "applied_date": "2026-10-06",
        "source": "Email",
        "notes": "4th, distinct Google application -- separate from the 3 already-tracked and already-"
                 "rejected Google rows (all from July). Fully generic confirmation email with no job title, "
                 "req ID, or team named.",
        "job_fit": "Unknown",
        "job_fit_notes": "No role title or posting details available to rate fit.",
    },
    {
        "company": "Mammoth Brands",
        "position": "Junior Creative Strategist",
        "status": "Rejected",
        "applied_date": "2026-10-06",
        "source": "Greenhouse",
        "notes": "2nd, distinct Mammoth Brands application -- separate from the earlier Creative Strategist "
                 "application (applied 07-22, already Rejected). Confirmed via Greenhouse's auto-reply. "
                 "Rejected 2026-10-21: \"decided to move forward with other candidates whose experience more "
                 "closely aligns with what we're looking for.\"",
        "job_fit": "Good",
        "job_fit_notes": "A Junior Creative Strategist posting at Lume Deodorant (a Mammoth Brands company), "
                         "$90,800-$113,500, described as early-career with room to learn from senior creative "
                         "leadership and grow quickly -- a good match for Regina's design-to-strategy "
                         "transition, since it's explicitly junior-level rather than requiring years of prior "
                         "strategy experience.",
    },
    {
        "company": "Whatnot",
        "position": "Lead Brand Designer",
        "status": "Rejected",
        "applied_date": "2026-10-06",
        "source": "Ashby",
        "notes": "Confirmed via Ashby's auto-reply. Rejected 2026-10-19: \"after reviewing your application and "
                 "experience, we won't be able to invite you to the next round of our hiring process.\"",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't find a posting with this exact title -- Whatnot's other senior/lead brand "
                         "creative roles found (Lead Illustrator, Lead Motion Designer, Senior Art Director "
                         "2D Illustration) lean heavily toward illustration/motion specialties and pay "
                         "$155K-$200K, which would suggest a 'Lead' title here also implies significant "
                         "seniority and a specialist skill set beyond Regina's core brand-identity background, "
                         "but the exact Brand Designer req's requirements aren't confirmed.",
    },
    {
        "company": "Apple Bank",
        "position": "Senior Visual Designer",
        "status": "Applied",
        "applied_date": "2026-10-06",
        "source": "Workday",
        "notes": "Confirmed via Workday's auto-reply.",
        "job_fit": "Weak",
        "job_fit_notes": "Confirmed posting: $150K-$180K, NY hybrid, requires 8+ years of visual design "
                         "experience with financial-services/bank or credit-union experience required or "
                         "preferred. Regina's ~7 years is under the bar, and she has no financial-services "
                         "industry experience.",
    },
    {
        "company": "WGACA",
        "position": "Unspecified role (Design)",
        "status": "Applied",
        "applied_date": "2026-10-06",
        "source": "Excelforce (ATS)",
        "notes": "Generic account-creation email from WGACA's (What Goes Around Comes Around, luxury vintage "
                 "resale) ATS -- no job title, req ID, or team named.",
        "job_fit": "Unknown",
        "job_fit_notes": "No role title or posting details available to rate fit.",
    },
    {
        "company": "Authentic Brands Group",
        "position": "Graphic Designer",
        "status": "Applied",
        "applied_date": "2026-10-06",
        "source": "Greenhouse",
        "notes": "Confirmed via Greenhouse's auto-reply.",
        "job_fit": "Fair",
        "job_fit_notes": "Couldn't confirm the exact req, but Authentic Brands Group's other current Graphic "
                         "Designer and Junior Graphic Designer postings pay $70K-$75K and read as junior-"
                         "leaning (supporting brand storytelling for entertainment/sports licensing brands) -- "
                         "core design skills overlap with Regina's background, but the pay level and seniority "
                         "framing suggest a more junior seat than her ~7 years would typically target.",
    },
    {
        "company": "EliseAI",
        "position": "Graphic Designer",
        "status": "Rejected",
        "applied_date": "2026-10-06",
        "source": "Ashby",
        "notes": "Confirmed via Ashby's auto-reply. Rejected 2026-10-22: \"the application process is highly "
                 "competitive... we are not in the position to move forward with your application.\"",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: $125K-$160K, NYC on-site, 2-5 years as a Brand/Graphic/Marketing "
                         "Designer, driving visual identity and brand expression, building design-system "
                         "components and reusable templates, Figma/Adobe Creative Suite -- a solid match to "
                         "Regina's brand-identity and design-system background.",
    },
    {
        "company": "PictureStudio",
        "position": "Senior Designer",
        "status": "Applied",
        "applied_date": "2026-10-06",
        "source": "Email",
        "notes": "Direct cold-outreach email (resume attached) to jobs@picturestudio.ai, stating expected "
                 "salary $110,000-$130,000 and earliest start date November 1. No confirmation reply yet.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't find PictureStudio's posting or confirm the company's specific focus to "
                         "rate fit confidently.",
        "cold_outreach": 1,
    },
    # -- 2026-10-08: found via a Sent-mail sweep (checking outgoing emails, not just inbound confirmations) --
    {
        "company": "Solomon Page",
        "position": "Unspecified role (Design, via staffing agency)",
        "status": "Applied",
        "applied_date": "2026-09-25",
        "source": "Email",
        "notes": "Direct cold-outreach email (resume and portfolio attached) to Marina Monsante at Solomon "
                 "Page, a staffing agency -- contact passed along by a personal connection, Michele Cilione, "
                 "after they discussed Michele's own job search. General introduction, no specific role or "
                 "client named (\"in case anything comes up\"); per standing practice for recruitment "
                 "agencies, logged under the agency name until a specific client/role is confirmed. No reply "
                 "yet.",
        "job_fit": "Unknown",
        "job_fit_notes": "No specific role or client named to rate fit against.",
        "cold_outreach": 1,
    },
    # -- 2026-10-08 (evening rescan): 1 new row, 1 update --
    {
        "company": "Salesforce",
        "position": "Communications Designer",
        "status": "Applied",
        "applied_date": "2026-10-07",
        "source": "Workday",
        "notes": "Confirmed via Workday's auto-reply.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: the role sits on Salesforce's Professional Services team, working "
                         "like an in-house creative agency building customer-proposal decks, graphics, and "
                         "social content for Customer Success teams -- 5+ yrs graphic design/visual "
                         "communication, Adobe Creative Cloud, Figma, Google Slides. A strong match to Regina's "
                         "agency deck-building and presentation-design background. Pay varies widely by listing "
                         "($117K-$261K); office policy also varies (remote vs. 3 days/wk in-office).",
    },
    {
        "company": "Omnicom Network",
        "position": "Art Supervisor (Area 23)",
        "status": "Applied",
        "applied_date": "2026-10-07",
        "source": "Workday",
        "notes": "Generic \"thank you for your application to the Omnicom network\" confirmation didn't name a "
                 "role; Regina confirmed directly it was for an Art Supervisor opening at Area 23, a "
                 "healthcare-focused creative agency that routes through Omnicom's shared Workday ATS. "
                 "Distinct from the 2026-07-27 and 2026-09-09 general network applications and the "
                 "2026-09-06 Presentation Designer application.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't find the specific Area 23 Art Supervisor posting to confirm requirements. "
                         "Art Supervisor is typically a senior agency-hierarchy title (parallel to/above Art "
                         "Director) involving managing junior art staff on specific accounts -- Area 23's focus "
                         "is healthcare/pharma advertising, an industry Regina hasn't worked in before, and the "
                         "people-management scope is a step beyond her individual-contributor-focused resume.",
    },
    {
        "company": "HarperCollins Publishers",
        "position": "Senior Designer, Art Department (NYC Hybrid)",
        "status": "Applied",
        "applied_date": "2026-10-07",
        "source": "iCIMS",
        "notes": "Confirmed via iCIMS's auto-reply.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: sits in the Morrow imprint's Art Department designing book covers "
                         "(hardcover/paperback, fiction and nonfiction) -- conceptual thinking, typography, and "
                         "image-making, working with an Art Director and editors. A solid match to Regina's "
                         "visual-design and conceptual branding background, though she has no prior book-cover "
                         "or publishing-specific design experience.",
    },
    {
        "company": "Reddit",
        "position": "Senior Creative Strategist - App Dev",
        "status": "Rejected",
        "applied_date": "2026-10-12",
        "source": "Greenhouse",
        "notes": "No original application-confirmation email was found -- picked up directly from the "
                 "rejection, so the true applied_date is unconfirmed (using the rejection date as a "
                 "placeholder). Generic decline: \"after carefully considering your background and "
                 "qualifications we have decided not to move forward.\"",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: sits in KarmaLab, Reddit's in-house creative team for the Global "
                         "Sales org -- building campaign concepts and supporting Sales on pitches/RFPs for app "
                         "advertisers, 5-7+ yrs creative strategy/advertising experience. Overlaps with Regina's "
                         "strategy-transition background, but leans more toward ad-sales pitch support for a "
                         "specific platform vertical (app/mobile advertisers) than her brand/product-design-"
                         "rooted strategy experience.",
    },
    {
        "company": "Tubi",
        "position": "Associate Creative Director",
        "status": "Applied",
        "applied_date": "2026-10-13",
        "source": "Greenhouse",
        "notes": "Confirmed via Greenhouse's auto-reply, applied during a late-evening application sprint.",
        "job_fit": "Fair",
        "job_fit_notes": "Posting is for entertainment/streaming marketing creative, hybrid LA/NYC, "
                         "$135K-$192.8K. Couldn't confirm the exact years-of-experience requirement on the "
                         "official posting, but ACD is a senior/leadership title that typically implies "
                         "10+ yrs and prior people-management experience -- likely a seniority stretch above "
                         "Regina's current individual-contributor level.",
    },
    {
        "company": "Amazon",
        "position": "Multimedia Designer, Amazon Delivery Experience (ADX)",
        "status": "Rejected",
        "applied_date": "2026-10-13",
        "source": "Amazon Jobs",
        "notes": "Confirmed via Amazon Jobs auto-reply, Job ID 10574195. Distinct from Regina's 3 other "
                 "existing Amazon applications (Job IDs 10525009, 10410280, 10523835). Flipped Applied -> "
                 "Rejected 2026-10-16: Amazon's status-update email said \"this position is no longer "
                 "available\" -- role closed, not an evaluated decline, but no longer pursuable.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't find this specific Job ID's posting to confirm requirements. General context "
                         "found: the ADX team supports and advocates for Amazon's global network of delivery "
                         "partners and Operations professionals -- can't confirm fit without the actual "
                         "posting.",
    },
    {
        "company": "Freshine Product Inc (Wavytalk)",
        "position": "Graphic Designer",
        "status": "Applied",
        "applied_date": "2026-10-13",
        "source": "Workable",
        "notes": "Confirmed via Workable's auto-reply, which read \"You have applied again for this job. This "
                 "application has overwritten the previous one.\" No earlier Freshine/Wavytalk row exists in "
                 "this scan history, so it's unclear whether a prior application was missed by earlier scans "
                 "or this reflects an accidental double-submit tonight -- flagging rather than guessing. "
                 "Regina's application answers: $90,000 salary expectation, 6 yrs relevant graphic design "
                 "experience, 0 yrs motion graphics/video editing experience, hybrid Mon-Thu onsite/Fri remote, "
                 "Flatiron NYC commute confirmed yes.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: hybrid NYC role for the Wavytalk beauty brand, covering social/"
                         "email/website/Amazon/TikTok Shop creative. Explicitly wants motion graphics/video "
                         "editing experience, which Regina self-reported as 0 years on her application -- a "
                         "real gap. Posted salary range is $70K-$75K vs. her stated $90K expectation, a likely "
                         "mismatch.",
    },
    {
        "company": "e.l.f. Beauty",
        "position": "Sr. Packaging Designer",
        "status": "Applied",
        "applied_date": "2026-10-13",
        "source": "Lever",
        "notes": "Confirmed via Lever's auto-reply, applied during a late-evening application sprint.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: requires 5+ yrs beauty-specific packaging design experience and "
                         "Adobe Creative Suite, $80K-$110K, 3 days/week in-office minimum. Regina doesn't have "
                         "packaging-design-specific experience, so this is a stretch outside her core "
                         "digital/brand/strategy background.",
    },
    {
        "company": "Ogilvy",
        "position": "Senior Designer, New Business",
        "status": "Applied",
        "applied_date": "2026-10-14",
        "source": "Email",
        "notes": "Confirmed via auto-reply from no-reply@ogilvy.com. Distinct role, date, and source from the "
                 "existing 2026-08-17 Ogilvy Designer application already in this scan history.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: reports to the NY New Business Executive Group Director, "
                         "supporting the North America business-development/pitch team -- building pitch "
                         "decks, visual concepts, brand stories, mockups, digital assets, and landing pages "
                         "for pitches. Emphasizes visual storytelling, typography, branding, layout, "
                         "illustration, print, and \"basic motion graphics\" as a plus (not a stated hard "
                         "requirement). One NY listing shows $60K-$140K/yr. Solid match to Regina's visual/"
                         "brand design and deck-design skillset; years-of-experience requirement couldn't be "
                         "confirmed anywhere.",
    },
    {
        "company": "Cyera",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-10-14",
        "source": "Email",
        "notes": "Confirmed via Spark Hire/Comeet auto-reply from no-reply@careers.cyera.io. Posting confirmed "
                 "2026-10-15 via Comeet (NY Metro, Intermediate level, Product Management dept).",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: NY Metro, $130K-$160K/yr, 3+ yrs professional brand design "
                         "experience, strong typography/composition/visual storytelling, highly proficient in "
                         "Figma + Adobe Creative Cloud, comfortable using AI tools (Claude, ChatGPT, "
                         "image-generation) as part of the design process. Motion design/animation listed as a "
                         "nice-to-have, not required. A solid match to Regina's brand-design background and "
                         "tools; her 6+ yrs comfortably clears the 3+ yr bar.",
    },
    {
        "company": "Twigeo",
        "position": "Senior Designer, Paid Social - New York",
        "status": "Applied",
        "applied_date": "2026-10-14",
        "source": "Teamtailor",
        "notes": "Confirmed via Teamtailor auto-reply from Lisa Sandahl.",
        "job_fit": "Fair",
        "job_fit_notes": "Found via aggregator listing (unconfirmed on Twigeo's own site): Brooklyn, NY, "
                         "on-site, $90K-$115K/yr. Description explicitly calls for \"a high level of design "
                         "and motion craft\" on paid social ad creative for clients like Duolingo and "
                         "MyFitnessPal -- a confirmed gap, since Regina has no motion-graphics/video-editing "
                         "experience. Years-of-experience requirement is Unknown (aggregator-only, not "
                         "corroborated on the company site).",
    },
    {
        "company": "Material",
        "position": "Mid-level Brand Designer (Aruliden)",
        "status": "Applied",
        "applied_date": "2026-10-14",
        "source": "Workday",
        "notes": "Generic Workday auto-reply confirmation (\"Thank you for applying!\") didn't name the role; "
                 "Regina confirmed 2026-10-15 this is the same Mid-level Brand Designer (Aruliden) posting as "
                 "the existing 2026-09-06 application (already flipped to Rejected per the candidate portal) "
                 "-- a reapplication to the same role.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: 2-5+ yrs studio/agency design, brand identity systems across "
                         "packaging/digital/physical, Adobe CS + Figma, strong typography, cultural fluency "
                         "in beauty/fashion/lifestyle, NYC hybrid, $65K-$85K/yr -- a solid match to Regina's "
                         "Common Matter background. Motion graphics is called out as a required skill, which "
                         "isn't evidenced on her resume.",
    },
    {
        "company": "Bandit Running",
        "position": "Junior Art Director",
        "status": "Applied",
        "applied_date": "2026-10-14",
        "source": "Workable",
        "notes": "Confirmed via Workable's auto-reply with full application data attached.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: Brooklyn, NY, on-site, requires 3+ yrs art direction/graphic "
                         "design at a fashion/apparel/sport/lifestyle brand or agency, Adobe CS + Figma, helps "
                         "art-direct (not edit) photo/video shoots. Despite the \"Junior\" title, the actual "
                         "bar (3+ yrs, reporting to an Art Director) is genuinely junior-level -- Regina's "
                         "6+ yrs makes her likely overqualified/underleveled for the stated requirement, "
                         "though the apparel/sport brand subject matter fits her background well.",
    },
    {
        "company": "Jacob Bar Inc.",
        "position": "Senior Designer",
        "status": "Applied",
        "applied_date": "2026-10-14",
        "source": "Workable",
        "notes": "Confirmed via Workable's auto-reply with full application data attached. Role confirmed "
                 "in-person in New York City (she checked \"Yes\" to acknowledge this). Posting confirmed "
                 "2026-10-15 via Regina -- Jacob is a food/beverage-adjacent consumer brand (the posting "
                 "mentions supporting dieline/packaging work for \"flavor launches and product drops\" "
                 "alongside campaign and digital design), though it explicitly says \"we're not looking for a "
                 "classic food-and-beverage designer.\"",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting (eatjacob.workable.com): NYC, on-site 5 days/week, $140K-$170K/yr, "
                         "primary design engine of the brand's media team working directly with the founder/"
                         "creative director across campaign graphics, social, OOH, retail, and packaging "
                         "dielines. Requires 7+ yrs design experience at a brand/studio/agency -- just above "
                         "Regina's 6+ yrs. Animation/motion-graphics and photo-editing skills are listed as "
                         "pluses, not required, which suits her gap there; the generalist, multi-disciplinary "
                         "framing fits her Common Matter background well. 2026-10-20 night: Regina (or an "
                         "auto-apply tool acting on her behalf) resubmitted to this same Workable posting; "
                         "Workable's own confirmation says the new submission \"overwrote the previous one\" -- "
                         "same req, not a separate application, status/date left unchanged.",
    },
    {
        "company": "Big Spaceship",
        "position": "Designer",
        "status": "Applied",
        "applied_date": "2026-10-15",
        "source": "Workable",
        "notes": "Confirmed via Workable's auto-reply with full application data attached. Regina's answers: "
                 "$105,000 desired salary; confirmed able to comply with the 3-day/week hybrid Manhattan "
                 "office policy.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: hybrid NYC, Creative & Design dept, $75K-$105K/yr -- her $105K "
                         "ask sits at the top of the band. Requires 3+ yrs in a creative agency or similar "
                         "environment, strong Figma + Adobe tools, typography/color theory/composition. After "
                         "Effects and digital-agency experience called out as pluses, not requirements. A "
                         "solid match to Regina's agency background (Common Matter, Superside) and 6+ yrs "
                         "clears the 3+ yr bar comfortably.",
    },
    {
        "company": "Live Nation Entertainment",
        "position": "Graphic Designer",
        "status": "Applied",
        "applied_date": "2026-10-15",
        "source": "Workday",
        "notes": "Confirmed via Workday's auto-reply (\"Application Acknowledgement\"). Posting confirmed "
                 "2026-10-15: the actual hiring entity is Roc Nation (a Live Nation-affiliated label/"
                 "entertainment company, Req JR-93368) -- \"Roc Nation benefits and policies differ from Live "
                 "Nation\" per the posting.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: NYC, in-office 5 days/week, $70K-$80K/yr, requires minimum 3+ yrs "
                         "in-house work experience, BA in Graphic Design, Adobe CS, direct portfolio link "
                         "required. Music/entertainment marketing and campaign design -- overlaps with "
                         "Regina's Common Matter music/live-events client work and Superside's entertainment "
                         "campaigns. Her 6+ yrs comfortably clears the 3+ yr bar.",
    },
    {
        "company": "MSG Entertainment Holdings, LLC",
        "position": "Senior Designer",
        "status": "Applied",
        "applied_date": "2026-10-15",
        "source": "Email",
        "notes": "Confirmed via no-reply@msg.com auto-reply. Posting confirmed 2026-10-15 (Req ID 27969).",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: NYC on-site, $100K-$115K/yr, requires 6+ yrs professional graphic "
                         "design experience with a focus on brand concept/design/storytelling, print + digital "
                         "design, deck design and typography; sports/entertainment/media experience preferred. "
                         "Regina's 6+ yrs matches almost exactly, and her Superside work (OOH incl. a Times "
                         "Square billboard, event branding, entertainment-adjacent campaigns) overlaps well.",
    },
    {
        "company": "Okta",
        "position": "Event & Experiences Designer",
        "status": "Applied",
        "applied_date": "2026-10-15",
        "source": "Email",
        "notes": "Generic ATS confirmation from no-reply@okta.com didn't name the role; role confirmed 2026-10-15 "
                 "via LinkedIn (\"Application submitted\" status) as Event & Experiences Designer, NY/Remote.",
        "job_fit": "Fair",
        "job_fit_notes": "Confirmed posting: $84K-$115K/yr, requires 4+ yrs dedicated experience in "
                         "experiential design, spatial/environmental graphic design, or event production, with "
                         "hands-on production fluency preparing large-format print/environmental graphics for "
                         "physical builds (tension fabric, hardwall structures, vinyl wraps, vendor fabrication "
                         "specs, CMYK/Pantone color management) -- SketchUp/Cinema 4D/Blender a plus. This is "
                         "a notably different, specialized skillset (physical/spatial production and "
                         "fabrication) than Regina's digital/brand/print design background, and isn't "
                         "evidenced on her resume -- a real stretch despite her years of experience clearing "
                         "the bar.",
    },
    {
        "company": "PictureStudio",
        "position": "Senior Designer",
        "status": "Applied",
        "applied_date": "2026-10-06",
        "source": "Email",
        "notes": "Direct email application to jobs@picturestudio.ai (no ATS), missed by prior scans since it "
                 "doesn't match the ATS-domain search list. Regina's email: expected salary $110,000-$130,000, "
                 "earliest start date November 1st.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: PictureStudio builds image-making/editing apps for Web and macOS. "
                         "Requires 3+ yrs design work, ideally including web or app development, strong "
                         "Figma/design-systems skills, salary band $70K-$140K. Regina's 6+ yrs clears the bar "
                         "comfortably, and her brand + web design background and stated interest in AI design "
                         "tools (Krea, Midjourney) align well with the role.",
    },
    {
        "company": "Studio Freight",
        "position": "Senior Designer",
        "status": "Applied",
        "applied_date": "2026-10-15",
        "source": "Email",
        "notes": "Cold-outreach email (resume attached) to Matt@studiofreight.com, \"Senior Designer Role @SF\" "
                 "-- not a response to a specific posted req.",
        "job_fit": "Fair",
        "job_fit_notes": "Studio Freight is an independent brand & digital design studio (Columbus, OH / NYC) "
                         "doing branding, visual identity, web design/development, and art direction for "
                         "clients like Netflix and Path Robotics; also builds open-source dev tools, signaling "
                         "a design+engineering hybrid shop. They periodically post a \"Senior Brand Designer\" "
                         "role (matches Regina's background well) and a \"Senior Digital Designer\" role "
                         "(leans web/interaction/motion-heavy, which isn't her strength) -- fit depends on "
                         "which track, if either, is actually open; couldn't confirm current openings.",
        "cold_outreach": 1,
    },
    {
        "company": "Sylvain",
        "position": "Strategy (unspecified)",
        "status": "Applied",
        "applied_date": "2026-10-15",
        "source": "Email",
        "next_step": "2026-10-21: Ben Cheney (Partner, Strategy & Co-Founder) replied -- Sylvain isn't "
                     "currently hiring, but he's always open to connecting with interesting people and offered "
                     "a video chat next week or the week after. Regina replied the same day with her "
                     "availability (flexible next week except Monday 1-2pm and Tuesday afternoon ET); no "
                     "specific date/time confirmed yet. 2026-10-22: Ben proposed Wednesday at 1pm; Regina "
                     "confirmed, and a calendar invite followed for Wednesday, Oct 28, 1:00-1:30pm ET (Google "
                     "Meet) -- networking call now locked in.",
        "notes": "Cold-outreach emails (resume attached) to both ben@sylvain.co and chris@sylvain.co, \"Strategy "
                 "@Sylvain\" -- same pitch sent to two contacts at the same company, logged as one application, "
                 "not a response to a specific posted req.",
        "job_fit": "Good",
        "job_fit_notes": "Sylvain (formerly Sylvain Labs) is an NYC-based strategy and design consultancy, "
                         "part of kyu Collective, blending brand strategy/design/innovation consulting for "
                         "major clients (Google, Amex, Spotify, Nike). The company's core identity (strategy + "
                         "brand design) directly matches Regina's design-to-strategy pivot and agency "
                         "pedigree; couldn't confirm a specific open strategy-team req.",
        "cold_outreach": 1,
    },
    {
        "company": "Company Policy",
        "position": "Unspecified role (Design)",
        "status": "Applied",
        "applied_date": "2026-10-15",
        "source": "Email",
        "notes": "Cold-outreach email (resume attached) to careers@companypolicy.studio, \"Design Roles at "
                 "Company Policy\" -- not a response to a specific posted req.",
        "job_fit": "Unknown",
        "job_fit_notes": "Company Policy is a small, independent brand strategy and visual identity design "
                         "studio (Brooklyn/NYC), founded 2021 by Adam Katz (ex-Google Creative Lab, "
                         "MediaMonks) -- the work (brand strategy + visual identity) matches Regina's skills "
                         "well, but couldn't confirm any open designer role or the studio's team size, so fit "
                         "beyond thematic alignment can't be verified.",
        "cold_outreach": 1,
    },
    {
        "company": "Taskrabbit",
        "position": "Unspecified role (Design)",
        "status": "Applied",
        "applied_date": "2026-10-16",
        "source": "Greenhouse",
        "notes": "Generic Greenhouse auto-reply confirmation (\"Thanks for applying to Taskrabbit!\") didn't name "
                 "the role. Distinct from the existing 2026-08-18 Taskrabbit/Sr. Manager, Brand & Content "
                 "application -- different date.",
        "job_fit": "Unknown",
        "job_fit_notes": "Two distinct current design roles found at Taskrabbit: \"Lead Visual Designer / "
                         "Senior Visual Design Specialist\" (hybrid SF/NY, $89K-$115K, 5+ yrs creative "
                         "marketing/brand design/art direction -- a reasonable match) and a separate \"AI "
                         "Content Design Lead\" (Charlotte, requires hands-on generative-AI image/video/copy "
                         "skills Regina doesn't have). Couldn't confirm which one she applied to -- not "
                         "guessing.",
    },
    {
        "company": "Vinson & Elkins LLP",
        "position": "Creative Specialist",
        "status": "Rejected",
        "applied_date": "2026-10-16",
        "source": "Email",
        "notes": "Generic \"Application Received\" confirmation from BPRecruiting@velaw.com didn't name the "
                 "role. Vinson & Elkins is a large corporate law firm -- an unusual application for Regina's "
                 "consumer-brand/agency design background; flagging rather than guessing why she applied here. "
                 "Rejected 2026-10-19: \"we will not be moving forward with your application at this time\" -- "
                 "the rejection named the actual title, Creative Specialist (Austin/Dallas/Houston/New "
                 "York/Washington), resolving the previous \"Unspecified role\" placeholder.",
        "job_fit": "Unknown",
        "job_fit_notes": "No design, creative, or marketing job postings found at the firm at all -- its "
                         "\"business professionals\" track covers business development/communications but no "
                         "open creative role was confirmed. In-house legal-marketing teams typically want "
                         "corporate/legal-services marketing experience, not consumer-brand creative -- "
                         "possibly a stretch or an unclear/generic ATS pull rather than a genuine design "
                         "opening.",
    },
    {
        "company": "WITHIN",
        "position": "Senior Creative Lead",
        "status": "Applied",
        "applied_date": "2026-10-16",
        "source": "Greenhouse",
        "notes": "Confirmed via Greenhouse's auto-reply (\"the world's first Performance Branding company\"). "
                 "Distinct from the existing 2026-09-08 WITHIN/Creative Lead Fellow application -- different "
                 "role and date.",
        "job_fit": "Fair",
        "job_fit_notes": "Multiple current listings found (ranging 5-10 yrs depending on location) focused on "
                         "social-first, performance/paid-media creative concepting and copy oversight -- not "
                         "traditional brand design. Regina's 6+ yrs clears the experience bar, but the role's "
                         "performance-marketing/paid-social skew is a gap versus her brand-strategy/visual-"
                         "design background. Couldn't confirm a single salary figure.",
    },
    {
        "company": "Trailborn Hotel Management LLC",
        "position": "Visual Designer",
        "status": "Applied",
        "applied_date": "2026-10-16",
        "source": "ADP",
        "notes": "Confirmed via ADP-hosted auto-reply.",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: NYC, on-site, 3+ yrs experience, $70K-$95K, Adobe Suite + Figma + "
                         "Canva + Asana, covering organic social, digital ads, email, sales materials, print "
                         "collateral, partnerships, and merch for a boutique hotel brand. Tool stack and scope "
                         "line up well with Regina's skills, though the 3+ yr requirement suggests the role "
                         "may be pitched below her 6+ yrs of seniority.",
    },
    {
        "company": "L'Oreal",
        "position": "Manager, Content Designer (Kiehl's)",
        "status": "Applied",
        "applied_date": "2026-10-16",
        "source": "Avature",
        "notes": "Confirmed via L'Oreal's Avature-hosted auto-reply.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't find a posting matching this exact title. Closest confirmed Kiehl's "
                         "postings found were \"Manager, E-commerce Content,\" \"Manager, Visual "
                         "Merchandising,\" and \"Senior Manager, Global Retail Design\" -- none matched "
                         "precisely, and none showed salary or years-of-experience in what was found. Not "
                         "guessing which applies.",
    },
    {
        "company": "Savvy Studio",
        "position": "Mid-Level Brand Designer",
        "status": "Applied",
        "applied_date": "2026-10-19",
        "source": "Email",
        "notes": "Direct cold-outreach email to hola@vvstudio.net about a Mid-Level Brand Designer opening she "
                 "saw posted -- resume (ReginaBarrera_CV_B.pdf) attached, portfolio linked, no open-role "
                 "confirmation beyond her own message.",
        "job_fit": "Good",
        "job_fit_notes": "Couldn't find the specific Mid-Level Brand Designer posting to confirm its exact "
                         "requirements, but Savvy Studio is a well-regarded branding/architecture practice with "
                         "NY and Mexico City offices, known for holistic brand-identity work spanning logos, "
                         "typefaces, and physical spaces for cafes, fashion labels, bookstores, and galleries -- "
                         "a strong stylistic match for Regina's brand-identity/typography/layout focus and SVA "
                         "branding background, though the exact level/seniority bar for this specific opening "
                         "isn't confirmed.",
        "cold_outreach": 1,
    },
    {
        "company": "Kettle",
        "position": "Visual Designer",
        "status": "Applied",
        "applied_date": "2026-10-20",
        "source": "Email",
        "notes": "Direct cold-outreach email to Nicole Locklair (nicole.locklair@wearekettle.com) about a Visual "
                 "Designer opening Regina saw posted, following an initial LinkedIn message -- resume "
                 "(ReginaBarrera_CV_B.pdf) attached, portfolio linked.",
        "job_fit": "Good",
        "job_fit_notes": "Couldn't find the specific (non-senior) Visual Designer posting, but Kettle is a "
                         "real NYC-headquartered creative/digital agency; their Senior Visual Designer listings "
                         "describe concept-to-build website and digital design work for agency clients, which "
                         "lines up with Regina's agency/digital design background, though the exact level and "
                         "scope of this specific opening isn't confirmed.",
        "cold_outreach": 1,
    },
    # -- 2026-10-20 night: late-evening application sprint (~7:56-8:22pm ET), 7 new rows --
    {
        "company": "Titan",
        "position": "Unspecified role",
        "status": "Applied",
        "applied_date": "2026-10-20",
        "source": "Ashby",
        "notes": "Generic Ashby confirmation (\"Thanks for your interest in Titan!\") didn't name the role.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm which Titan this is or the specific posting. Most plausible match "
                         "found was Titan, the investing/wealth-management app (Senior Product Designer roles, "
                         "NYC) -- a16z/General Catalyst-backed -- but not guessing which Titan or which role.",
    },
    {
        "company": "Raisin",
        "position": "Digital Designer",
        "status": "Rejected",
        "applied_date": "2026-10-20",
        "source": "Email",
        "notes": "Generic confirmation from careers@raisin.com (\"Thanks for applying to Raisin\") didn't name "
                 "the role. Rejected 2026-10-22: \"decided not to move forward with your candidacy at this "
                 "time\" -- this rejection named the actual title, Digital Designer, resolving the earlier "
                 "\"Unspecified role\" placeholder.",
        "job_fit": "Unknown",
        "job_fit_notes": "Raisin is a Berlin-based fintech savings/investment marketplace with a US direct-to-"
                         "consumer platform. Couldn't find the specific Digital Designer posting to confirm its "
                         "requirements.",
    },
    {
        "company": "Rillet",
        "position": "Brand Designer",
        "status": "Applied",
        "applied_date": "2026-10-20",
        "source": "Ashby",
        "notes": "Confirmed via Ashby's auto-reply (\"Thank you for applying for the Brand Designer role at "
                 "Rillet!\").",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting context: Rillet is a well-funded startup ($100M+ raised); the Brand "
                         "Designer sits on the marketing team defining how the company shows up visually -- a "
                         "brand-identity-focused role that lines up with Regina's background, though the exact "
                         "requirements/seniority bar weren't independently confirmed.",
    },
    {
        "company": "Barry's",
        "position": "Graphic Designer",
        "status": "Applied",
        "applied_date": "2026-10-20",
        "source": "Rippling",
        "notes": "Confirmed via Rippling's auto-reply, which named the role (Graphic Designer) but not which "
                 "Barry's -- most likely Barry's Bootcamp (fitness brand) given the context, but not confirmed.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't find or confirm the specific posting behind this application.",
    },
    {
        "company": "iHeartMedia",
        "position": "Graphic Designer",
        "status": "Applied",
        "applied_date": "2026-10-20",
        "source": "Workday",
        "notes": "Confirmed via Workday's auto-reply, which named the req (Req39497 - Graphic Designer) but the "
                 "exact req's requirements couldn't be matched to a specific public posting.",
        "job_fit": "Fair",
        "job_fit_notes": "Other iHeartMedia Graphic Designer postings found (not confirmed to be this exact "
                         "req) describe a mid-level, lower-paying NYC role ($52K-65K) focused on presentations, "
                         "infographics, and brand consistency -- core design/presentation skills overlap with "
                         "Regina's background, but the pay band suggests a less senior role than her 6+ yrs.",
    },
    {
        "company": "Elmwood Brand Consultancy",
        "position": "Senior Designer",
        "status": "Applied",
        "applied_date": "2026-10-20",
        "source": "Workable",
        "notes": "Confirmed via Workable's auto-reply with full application data attached (resume: Regina "
                 "Barrera_Designer_Elmwood.pdf).",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting: NYC, hybrid, $100K-115K, owning projects from concept to execution "
                         "with client-relationship and junior-mentoring responsibilities, requiring mastery of "
                         "design systems, typography, and art direction -- a strong match for Regina's "
                         "brand-identity/typography background and 6+ yrs of experience.",
    },
    {
        "company": "Peloton",
        "position": "Senior Designer",
        "status": "Applied",
        "applied_date": "2026-10-20",
        "source": "Greenhouse",
        "notes": "Confirmed via Greenhouse's auto-reply, with a matching copy-of-application notice also sent "
                 "via Adzuna (\"We have sent your Senior Designer application to Peloton\").",
        "job_fit": "Good",
        "job_fit_notes": "Confirmed posting (via aggregator): bachelor's degree + 3 yrs experience, hybrid NYC, "
                         "covering campaign work, landing pages, brand visuals across digital channels, and "
                         "design systems -- a solid match for Regina's brand/campaign/digital design background, "
                         "though likely pitched a bit below her 6+ yrs of seniority.",
    },
    {
        "company": "Substack",
        "position": "Unspecified role",
        "status": "Applied",
        "applied_date": "2026-10-21",
        "source": "Ashby",
        "notes": "Generic Ashby confirmation (\"We're on it!\") didn't name the role.",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm which role this was for. Substack's only confirmed open design "
                         "listing found was a Product Designer role (hybrid NY/SF, 3+ yrs, $150K-$215K) -- not "
                         "guessing whether that's the one applied to.",
    },
    {
        "company": "Gretel",
        "position": "Strategy Intern",
        "status": "Applied",
        "applied_date": "2026-10-22",
        "source": "Notion form",
        "notes": "Confirmed via a Notion-hosted application form confirmation (\"Thank you for filling out "
                 "'Gretel Strategy Intern'\").",
        "job_fit": "Unknown",
        "job_fit_notes": "Couldn't confirm which company this is (common name) or find the specific posting to "
                         "assess requirements.",
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
        row.setdefault("applicant_count", None)
        row.setdefault("had_interview", 0)
        row.setdefault("interview_dates", None)
        row.setdefault("cold_outreach", 0)
        interview_dates = json.dumps(row["interview_dates"]) if row["interview_dates"] else None
        db.execute(
            """
            INSERT INTO applications
                (company, position, status, applied_date, next_step, job_url, source, referral, notes, pay_range, job_fit, job_fit_notes, applicant_count, had_interview, interview_dates, cold_outreach, created_at, updated_at)
            VALUES (:company, :position, :status, :applied_date, :next_step, :job_url, :source, :referral, :notes, :pay_range, :job_fit, :job_fit_notes, :applicant_count, :had_interview, :interview_dates, :cold_outreach, :created_at, :updated_at)
            """,
            {**row, "interview_dates": interview_dates, "created_at": now, "updated_at": now},
        )
    db.commit()
    print(f"Seeded {len(SEED_ROWS)} applications from the Gmail scan.")


if __name__ == "__main__":
    main()
