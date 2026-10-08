# Job Search Tracker

A small local web app for tracking job applications: table view, kanban board,
and a stats dashboard (total applications, response rate, interview rate, offer rate).

## Setup

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5050. Data is stored in `tracker.db` (SQLite, created
automatically on first run, gitignored).

To load the applications found from the initial Gmail scan (see below), run once:

```bash
python scripts/seed_from_gmail_scan.py
```

## Getting your data in

### LinkedIn

LinkedIn does not provide an API or export button for your personal "Applied
Jobs" list, and there is no LinkedIn connector available to Claude — so
nothing (this app or Claude) can log into LinkedIn on your behalf. Bringing
that data in is a manual, one-way hand-off, in either of two forms:

1. **Paste-and-parse (recommended):** open LinkedIn's applied-jobs page
   (Jobs → My Jobs → Applied), copy the visible rows as plain text (or just
   screenshot it), and paste them to Claude in chat. Claude parses company /
   role / applied date out of the raw text, reconciles it against what's
   already tracked (filling in real titles where the Gmail scan only had a
   generic placeholder, rather than creating duplicates), and imports
   whatever's genuinely new — see `scripts/seed_from_linkedin.py`.
2. **CSV template:** copy company / role / applied date into
   [`import_template.csv`](./import_template.csv) yourself, then in the app
   click **Import CSV** and upload it.

LinkedIn only exposes relative dates ("Applied 3w ago"), so applied dates
pulled in this way are estimates, noted as such on each row. LinkedIn's own
"no longer accepting applications" flag is a posting-lifecycle signal (the
listing was taken down) — it does not mean anything about whether a
response was received, so it's never treated as a rejection.

**2026-08-17** — first paste-and-parse reconciliation, 14 new applications
added (Publicis Health, G&A Strategy and Design, Synthesis ×2, Publicis
Media ×2, Accenture Creative Agency Senior Designer, Reddit ×2, Moon Juice,
Interbrand Senior Designer, Noom, UNIQLO, Omnicom Media), plus five
existing Gmail-sourced rows had their placeholder titles filled in
(two Meta roles, Prophet, Buttermilk, OLIVER).

Required columns for CSV import: `company`, `position`. Optional: `status`
(Applied / Interviewing / Offer / Rejected / Withdrawn / Networking),
`applied_date`,
`next_step`, `job_url`, `source`, `referral` (yes/no), `notes`, `pay_range`,
`job_description`, `job_fit` (Strong / Good / Fair / Weak / Unknown),
`job_fit_notes`.

### Email

There's no way to give this standalone app a persistent, ongoing connection
to your inbox — that would require setting up a Google Cloud project with
Gmail API OAuth credentials and running your own auth flow, which is a
separate piece of setup outside of what's in this repo.

What *is* possible: since Claude has access to your Gmail in a chat session,
you can periodically ask Claude to scan your inbox for application
confirmations, rejections, and interview invites, and either update
`tracker.db` directly or hand you a CSV to import. A recurring Routine can
also be scheduled to do this automatically (see below).

The rows in `scripts/seed_from_gmail_scan.py` came from exactly that:

- **2026-08-13** — initial 12-month scan, searching for ATS
  confirmation/status emails (Greenhouse, Lever, Ashby, Workday, iCIMS,
  Workable, Teamtailor) and explicit rejection/interview language. 29 real
  applications turned up: 24 Applied, 1 Interviewing (Design Bridge and
  Partners / Landor), and 4 Rejected (Prose, AKQA, Accenture/Droga5, and
  Prophet — the last over a work-authorization concern where a clarifying
  reply is already sent).
- **2026-08-17 (afternoon)** — incremental scan covering everything since
  the prior scan. 5 new rows: 4 Applied (NBCUniversal, Blackstone, Bespoke
  Post, Inizio Evoke) and 1 Rejected (OLIVER).
- **2026-08-17 (evening)** — incremental rescan. 2 new rows, both Applied
  (PepsiCo Brand Designer — a second, distinct PepsiCo application — and
  Razorfish Health).
- **2026-08-17 (night)** — reconciled against a screenshot of JPMC's own
  Candidate Experience portal (Oracle HCM), not Gmail. Corrected the
  titles and exact applied dates on the two existing generic JPMorgan
  rows, flipped one to Rejected ("Not Selected" — Corporate Brand
  Marketing, Senior Associate), and added a third JPMorgan application
  (Olympic & Paralympic, Graphic Designer, Senior Associate) that had no
  Gmail confirmation at all.
- **2026-08-18 (early)** — incremental rescan. 3 new rows, all Applied
  (DualEntry, Firefly, and a second Accenture/Droga5 application distinct
  from the earlier rejected one).
- **2026-08-18 (later)** — reconciled against a screenshot of Google's own
  candidate portal. Both existing Google rows flipped to Rejected ("Not
  proceeding"), all 3 Google applications got real titles, and the 3rd one
  (with no Gmail confirmation at all) was added.
- **2026-08-18 (night)** — reconciled against a screenshot of Meta's own
  candidate portal. Confirmed the Creative Strategist NA team application's
  date and corrected its location, flipped the Brand Strategist application
  to Rejected with a corrected applied date, and added a 3rd Meta
  application (Instagram Brand Studio) with no Gmail confirmation at all.
- **2026-08-18 (later still)** — filled in real titles for Partiful, Inizio
  Evoke, and DualEntry from Regina's own knowledge, and logged a Mother
  networking call (recruiter reached out, no open role, interest expressed
  in Strategy) using the new `Networking` status — a category for contacts
  that aren't a real application, not something the Gmail scan detects on
  its own.
- **2026-08-18 (final)** — added a second PepsiCo networking contact
  (Hillary, reported directly by Regina) and a second, distinct Something
  Special Studios application: a direct outreach email to a specific
  strategist there, confirmed via Gmail search, separate from the earlier
  Greenhouse-sourced application.
- **2026-08-19** — incremental rescan. 1 new row, Applied (Taskrabbit, title
  unknown at the time).
- **2026-08-19 (later)** — reconciled against a LinkedIn My Jobs screenshot.
  Filled in Taskrabbit's real title, confirmed Blackstone and Inizio Evoke
  were already tracked, and added 3 new rows: Book of the Month (LinkedIn
  Easy Apply, title partly reconstructed from a cut-off confirmation
  screenshot), Steven Madden, and Inside Out Community — the latter two
  with applied dates and completion status not fully confirmed, since
  LinkedIn only showed listing repost/post dates and a "Did you finish
  applying?" prompt rather than an application date.
- **2026-08-19 (evening)** — incremental rescan. 2 new rows, both Applied
  (MUBI, Tapestry).
- **2026-08-20** — incremental rescan, no new rows. Accenture's Droga5
  Senior Designer application (R00348810) came back Rejected ("unable to
  move forward at this time").
- **2026-08-21** — incremental rescan, no new rows. Inizio Evoke's Senior
  Brand Strategist application came back Rejected.
- **2026-08-24** — incremental rescan, 1 new row (Amazon, Art Director —
  Elevated Shopping, applied 2026-08-17, online assessment completed
  2026-08-18). This one had been missed by every scan since 08-17 because
  amazon.jobs wasn't in the ATS domain search list — found by widening the
  search after Regina asked about an interview invite. The domain has been
  added to the search going forward.
- **2026-08-24 (later)** — Regina reported a Tapestry rejection and
  forwarded a Duel interview invite directly. Flipped Tapestry's Associate,
  External Communications application to Rejected, and added a new Duel
  application (Advocacy Consultant, applied 2026-08-18) with status
  Interviewing — a recruiter reached out to schedule a screen.
- **2026-08-25** — Regina reported a batch of cold outreach emails;
  confirmed via Sent Mail and added 10 new Networking rows (Gander/Heist,
  four Meta contacts, two Wieden+Kennedy contacts, three Red Antler
  contacts). The weekly-activity chart now shows reach-outs stacked on top
  of applications per week, so cold outreach counts toward visible weekly
  activity without inflating Total Applications.
- **2026-08-26** — reconciled against a screenshot of Accenture's own
  candidate portal (both applications already Rejected). Added job req
  R00338279 to the Senior Strategist row and corrected the Senior Designer
  (R00348810) applied date from Aug 18 to Aug 17 per the portal's "Date
  Submitted." No status changes.
- **2026-08-26 (later)** — incremental rescan, 1 new row (VaynerMedia,
  Relevance Strategist).
- **2026-08-26 (evening)** — Regina reported two more cold outreach
  emails; confirmed via Sent Mail and added as Networking rows (Porto
  Rocha, Decade).
- **2026-08-27** — incremental rescan, no new rows. Two rejections: Duel's
  Advocacy Consultant application (after the recruiter screen) and
  DualEntry's Brand Design Lead application (before the interview stage,
  title corrected from the earlier "Design Lead" placeholder).
- **2026-08-31** — incremental rescan, no new rows. Mammoth Brands'
  Creative Strategist application came back Rejected.
- **2026-09-02** — incremental rescan, no new rows. MUBI's Communications
  Manager, US application came back Rejected.
- **2026-09-02 (later)** — Regina applied directly to Monks (Associate
  Director, Comms Planning) and separately emailed a contact there the same
  day; confirmed via Gmail search and added.
- **2026-09-02 (job-fit backfill)** — rated every real (non-Networking)
  application (67 total) on fit against Regina's actual resume/background,
  using the real job posting where one could be found and confirmed via web
  search. 12 came back Unknown rather than guessed, where the posting was
  opportunistic/unspecified or couldn't be confirmed.
- **2026-09-02 (JPMC portal recheck)** — Regina shared an updated screenshot
  of JPMC's own candidate portal. The Graphic Designer, Senior Associate
  application is still Under Consideration and Corporate Brand Marketing was
  already Rejected — no change. The Olympic & Paralympic Brand Strategist
  application flipped from Under Consideration to Not Selected — updated to
  Rejected.
- **2026-09-02 (reported directly by Regina)** — Superside's Lead Creative
  Strategist application was rejected; she says the role requires being
  based in Mexico, which she isn't — a residency requirement, not a
  skills-based rejection. Flipped to Rejected.
- **2026-09-02 (missed rejection, caught by Regina)** — Highsnobiety's
  Associate Creative application was rejected 2026-08-24, but every scan
  since then missed it: the subject line was a generic "Thank you for your
  job application!" and the rejection was phrased softly ("decided to move
  forward with other candidates") rather than in the explicit language
  prior scans searched for. Flipped to Rejected; future scans will also
  treat generic "thank you for applying" subjects and "moving forward with
  other candidates" phrasing as possible soft rejections. Also reconciled
  against a fresh Accenture portal screenshot — both Droga5 applications
  already showed Rejected here, matching the portal. No change needed.
- **2026-09-02 (widened rejection search, at Regina's request)** — searched
  Gmail for soft-rejection phrasing ("move forward with other candidates",
  "not move forward", "position has been filled", "unfortunately", etc.) and
  generic "thank you for applying" subjects across the full inbox history,
  not just explicit reject/not-selected language. Found: David Protein's
  Senior Brand Manager application, rejected 2026-08-12 and sitting as
  Applied ever since — flipped to Rejected. Noom's Creative Strategist
  application, rejected 2026-08-25 ("the position has been filled") and
  also sitting as Applied — flipped to Rejected. Two applications missed
  entirely because their domains weren't in the ATS search list: Datadog's
  Lead Designer (applied 2026-08-18, rejected 2026-08-20 — both added) and
  Ogilvy's Designer (applied 2026-08-17, still no response — added as
  Applied).
- **2026-09-02 (reported directly by Regina)** — Monks' Associate Director,
  Comms Planning application was rejected the same day it was submitted;
  Olga Gamer replied she can't hire candidates who will require visa
  sponsorship, even in the future — a visa/authorization issue, not a
  skills-based rejection. Flipped to Rejected.
- **2026-09-03** — incremental rescan, 3 new rows: Accenture (Droga5 Senior
  Strategist, R00348814 — a distinct req ID from the earlier, already-
  rejected Droga5 Senior Strategist application, likely a reposted
  opening), Nourish (role unspecified — generic Greenhouse confirmation
  didn't name it), and Disney (Associate Manager, Brand Strategy).
- **2026-09-03 (later)** — incremental rescan, 1 new row: MrBeast (role
  unspecified — generic Greenhouse confirmation didn't name it).
- **2026-09-05** — incremental rescan, 3 new rows: Notion (Brand Designer,
  Creative Studio), PepsiCo (Graphic Designer — poppi, 2026-470592 — a
  third, distinct PepsiCo application), and Finch (Brand and Web Designer).
- **2026-09-05 (later)** — reconciled against a screenshot of Amazon's own
  My Applications portal. The Art Director, Elevated Shopping application
  is now Archived / "No longer under consideration" — flipped to Rejected.
  The portal also showed 1 Active Amazon application not visible in the
  screenshot — not yet identified or added.
- **2026-09-05 (later still)** — identified the Active Amazon application
  via Gmail: Regina applied to Brand Designer, Brand Innovation Lab
  (ID: 10525009), then withdrew it a few minutes later per Amazon's own
  "You've withdrawn your Amazon job application!" confirmation. Added with
  status Withdrawn to match.
- **2026-09-05 (later still)** — incremental rescan, 3 more new rows:
  Bumble (Graphic Designer), Landor (role unspecified — distinct from the
  earlier Design Bridge and Partners / Landor Senior Strategist
  application), and Gigs (role unspecified).
- **2026-09-05 (final)** — Regina shared the actual Landor and Gigs
  postings and clarified the Amazon Brand Designer situation. Landor's
  role confirmed as "Designer" (Strong fit). Gigs' role confirmed as
  "Senior Brand Designer" (Fair fit — requires motion-design skills as a
  core requirement). Amazon's Brand Designer, Brand Innovation Lab
  application: Regina withdrew it and then reapplied the same day, so
  it's flipped back to Applied.
- **2026-09-05 (networking backfill)** — Regina reported 6 networking
  calls from her own memory/calendar/LinkedIn messages: Jennifer Passas
  (Interbrand, Jul 30), Julia her SVA TA (advice, Aug 4), Andrew her SVA
  instructor (advice, Aug 19), Anna-Rae Morris (LinkedIn, Aug 31, possible
  follow-up), and two scheduled calls not yet happened — Angel Bellon
  (independent cultural-intelligence consultant/Parsons faculty, Sep 8)
  and Maggie Murphy (Strategy Director at Mother, Sep 10 — a follow-up
  from the earlier Mother Intro Call). Also corrected the existing Mother
  Intro Call's date from an approximate Aug 18 to the confirmed calendar
  date, Jul 30.
- **2026-09-05 (clarified by Regina)** — LinkedIn cold-outreach messages
  are not logged as Networking rows on their own; only once they actually
  turn into a response and a scheduled/completed call. (Cold outreach
  sent by email is a separate, already-established exception — see the
  Aug 25 entry above — and continues to be logged even without a reply.)
- **2026-09-06** — incremental rescan since Sep 5, 2 new rows: Bain &
  Company (Strategic Designer, Weak fit — UX/service-design discipline,
  not brand/graphic design) and Meta (generic "Designer" role, Unknown
  fit — a 4th, distinct Meta application). Also found a same-night Ogilvy
  security-code verification step re-confirming the existing Designer
  application (applied Aug 17) — treated as a resubmission, not a new row.
- **2026-09-06 (later)** — incremental rescan, 2 more new rows: Havas and
  City of New York, both "Graphic Design Intern" postings. Confirmed both
  target current college students (Havas: student/recent-grad pipeline;
  NYC: civil-service title "College Aide", experience level "Student") —
  rated Weak fit on seniority mismatch, not a skills gap.
- **2026-09-06 (later still)** — incremental rescan, 5 more new rows:
  Gensler (Multimedia + Graphic Designer, Fair fit — motion/video is a
  core requirement not evidenced on Regina's resume), Hypha (Visual
  Designer, Unknown — couldn't find the posting), Vestwell (Senior Brand
  Designer, Fair — strong brand-systems overlap but requires hands-on
  HubSpot CMS experience; resubmitted via a security-code step, treated
  as one application), Brick (unspecified role, Unknown), and The Working
  Assembly (Brand Designer, Strong fit — close agency-background match,
  applied via the company's own Google Form rather than an ATS).
- **2026-09-06 (incremental)** — 1 new row: Meta — Brand Designer,
  Iconography & Illustration, Instagram Brand Studio (Fair fit — a
  specialist illustration track, tool overlap but not a demonstrated
  core strength). A 5th, distinct Meta application on the same team as
  the existing Strategic Initiatives role.
- **2026-09-06 (evening)** — incremental rescan, 2 new rows: Fanatics
  Collectibles (Graphic Designer II, Good fit — solid Adobe CC/branding/
  print-production match) and United Legwear Company (unspecified role,
  Unknown fit — generic ADP confirmation named no role).
- **2026-09-06 (fit confirmation)** — Regina shared the real postings for
  4 rows that had gone in generic or estimated: Hypha confirmed as
  "Visual Designer" (Good fit), Brick confirmed as "Growth Designer"
  (Unknown → Weak, a performance-marketing discipline), United Legwear
  confirmed as "Senior Designer, KIDS" (Unknown → Weak, an apparel/PLM
  discipline), and Meta's Iconography & Illustration role downgraded
  Fair → Weak once the full posting showed an 8+ year minimum.
- **2026-09-06 (pay_range backfill)** — populated the structured
  pay_range field for every row with a confirmed posting salary (Gigs,
  Havas, Gensler, Hypha, Brick, Meta Iconography & Illustration, United
  Legwear, Moon Juice) — previously that figure only lived in prose
  inside job_fit_notes. The dashboard now shows it on kanban cards and
  in each row's expanded detail. The Working Assembly's $95,000 is
  Regina's own stated expectation, not a posted range, so it's excluded
  from pay_range.
- **2026-09-06 (night)** — incremental rescan, 4 new rows: Amazon (3rd
  distinct application, "Designer, Premium, Elevated Shopping", Unknown
  fit — salary confirmed but not the exact requirements), Assembled
  (Brand Designer, Good fit, $150K-$190K), Ripple (unspecified role,
  Unknown fit — two plausible openings, neither confirmed), and
  Material (unspecified role, Unknown fit — generic confirmation).
- **2026-09-06** — 1 new row, reported directly by Regina: Paramount —
  Designer, Publishing (Fair fit). She'd started this application and
  left it incomplete; after a reminder email, she finished submitting
  it.
- **2026-09-06 (later)** — 1 new row: Pentagram — Middleweight Designer
  (Good fit). Direct cold-email application to Eddie Opara's team with
  resume and portfolio attached; no public posting found, so it reads
  as a referral-style opportunity rather than a listed job.
- **2026-09-06 (fit confirmation)** — Regina shared the real postings
  for the 2 remaining Unknown rows from the 09-06 night rescan: Ripple
  confirmed as the NY "Brand Designer" role (Unknown → Good, $112K-
  $120K) and Material confirmed as "Mid-level Brand Designer (Aruliden)"
  (Unknown → Good, $65K-$85K) — also correcting its location from an
  earlier guess of Los Angeles to New York, NY (hybrid).
- **2026-09-06 (later still)** — 2 more real postings confirmed: Pentagram's
  Middleweight Designer downgraded Good → Fair once the full listing
  showed required motion-tool proficiency (After Effects, Cavalry,
  Cinema 4D) not evidenced on Regina's resume — $85K-$105K confirmed.
  Amazon's Designer, Premium, Elevated Shopping confirmed as Good fit —
  5+ yrs premium fashion/beauty design matches her agency background —
  salary corrected to $132.5K-$185K.
- **2026-09-06 (later still)** — confirmed Meta's generic "Designer"
  application as a Creative X / Reality Labs role (wearables/metaverse
  brand design) — Unknown → Good, $122K-$175K.
- **2026-09-06 (later still)** — incremental rescan, 6 new rows: Conveo
  (Design Lead, Fair fit), Figma (2nd application, Brand Designer/
  Product Launches, Fair fit), Day One (Senior Designer, Unknown),
  Fresh (Senior Designer, Digital and Social, Good fit — beauty-brand
  digital/social match, exact posting unconfirmed), and two generic
  confirmations (Tory Burch, Omnicom network).
- **2026-09-06 (portal reconciliation)** — Regina shared a Publicis
  candidate-portal screenshot showing req 2026-152303 (Razorfish
  Health, Manager, Brand Strategy) marked "Not selected" — flipped
  from Applied to Rejected.
- **2026-09-06 (later still)** — incremental rescan, 2 more new rows:
  Turner Duckworth (Senior Designer, Strong fit — packaging/brand-
  identity agency match) and Posh (Brand Designer, Weak fit — wants a
  Series B-D in-house creative leader, well beyond Regina's level).
- **2026-09-06 (date correction)** — a Sunday-evening batch of ten
  applications (Pentagram, Paramount, Conveo, Figma's 2nd app, Day One,
  Fresh, Tory Burch, Omnicom, Turner Duckworth, Posh) had been dated
  2026-09-07 — the raw UTC date of their Gmail confirmations — even
  though they were submitted 8-10pm Eastern on 2026-09-06. Regina caught
  it when the dashboard's weekly counter rolled into a new week for a
  Sunday-night batch. Corrected all ten dates and switched to Eastern-
  time conversion for applied_date going forward.
- **2026-09-06 (fit confirmation)** — more real postings shared by
  Regina: Day One (Good, $80K-$95K), Tory Burch confirmed as "Temporary
  Helper, Senior Graphic Designer" (Unknown → Good), Omnicom confirmed
  as "Presentation Designer, Brand Experience" (Unknown → Good, $50K-
  $95K), Nourish confirmed as "Senior Creative Strategist" (Unknown →
  Fair), and MrBeast confirmed as "Senior Brand Strategist" (Unknown →
  Weak — wants 8-10+ yrs, well beyond Regina's experience).
- **2026-09-08** — incremental rescan, 2 new rows: Accenture (Work & Co)
  Designer, R00334677 (Unknown fit — a generic Work & Co/Accenture Song
  design req, distinct from the three earlier Accenture/Droga5
  applications, no confirmable requirements beyond team-page copy), and
  Fresh, Senior Designer, Digital and Social — a second, distinct
  SmartRecruiters application ID for the same role Regina already applied
  to on 2026-09-06, logged as an apparent accidental duplicate
  resubmission.
- **2026-09-08 (later)** — incremental rescan, 1 new row and 1 rejection:
  WITHIN, Creative Lead Fellow (Weak fit — confirmed posting is an 8-week
  performance-creative/short-form-video fellowship judged on a public
  social/spec portfolio, a different discipline from Regina's brand/graphic
  design background). Flipped VaynerMedia's Relevance Strategist
  application to Rejected per a VaynerX/Greenhouse email.
- **2026-09-09** — incremental rescan, no new rows, 2 rejections: Finch's
  Brand and Web Designer (Lever email), and Accenture (Work & Co) Designer,
  R00334677 (Workday email citing that Regina's application indicated she
  requires visa sponsorship — flagged for her to check her Workday/EEO
  profile answers, since an incorrect sponsorship flag could be silently
  disqualifying other US-based Workday applications too).
- **2026-09-09 (later, reported directly by Regina)** — 2 new rows:
  DualEntry, Brand Designer — a direct cold-email application to the
  recruiter since Ashby was blocking a second application tied to her
  earlier, rejected Brand Design Lead req (Good fit, $100K–$160K). Omnicom
  Network, a 2nd distinct general network application (Unspecified role,
  Unknown fit) — separate from both the 2026-07-27 and 2026-09-06 Omnicom
  applications already on file.
- **2026-09-10 (reported directly by Regina, screenshot)** — 1 new row:
  Pomegranate Gallery, Part Time Book Designer — applied via SVA's own
  career-services job board (12twenty). Confirmed posting is actually a
  combined "Film Editor/Videographer & Graphic/Book Designer" role (Fair
  fit — film editing/videography isn't evidenced on Regina's resume,
  though the book/graphic-design half overlaps).
- **2026-09-11** — incremental rescan, no new rows, 1 rejection: flipped
  the Accenture (Droga5) Senior Strategist (R00348814) application to
  Rejected per a Workday email.
- **2026-09-11 (later)** — incremental rescan, no new rows, 1 rejection:
  flipped NBCUniversal's Associate Manager, NBC & Peacock Marketing
  application to Rejected per a SmartRecruiters email.
- **2026-09-12 (later)** — 1 new row, found via a rejection email and
  traced back to its confirmation: Noom, Senior Creative Strategist,
  Performance (applied 2026-08-26, rejected 2026-09-12, Weak fit — a
  performance-marketing/media-buying leadership scope not evidenced on
  Regina's resume) — missed entirely by every prior scan since its
  generic confirmation subject didn't match the search keywords.
- **2026-09-14** — incremental rescan, no new rows, 1 rejection: flipped
  Disney's Associate Manager, Brand Strategy application to Rejected per
  a Workday email.
- **2026-09-14 (later)** — incremental rescan, 3 new rows: Craft, Senior
  Designer / Freelance Senior Brand Designer / Brand Designer — three
  distinct applications submitted within minutes of each other through
  Craft's own ATS. Craft is a UK/NY creative & design recruitment
  consultancy, not the hiring company itself, and runs many concurrently
  open, similarly-titled reqs, so the exact client listing for each
  couldn't be confirmed (all three Unknown fit).
- **2026-09-15** — incremental rescan, 3 more new rows from the same
  evening's application batch: The New York Times, Senior Designer, Games
  Marketing (Temporary) — a 2nd, distinct NYT application, Fair fit
  (motion design is a required skill here, not evidenced on Regina's
  resume). Sapience AI Corporation, Brand Graphic Designer (best-guess
  title from their job board, generic confirmation didn't name it), Weak
  fit — the one design req found prefers Seattle/Pacific time, a location
  mismatch. Unspecified (Ashby application) — a fully generic Ashby
  confirmation with no company name, role, or any identifying detail at
  all; likely part of the same application session but the company
  couldn't be determined.
- **2026-09-15 (later, reported directly by Regina, screenshot)** — 1 new
  row, found via a rejection email and traced back to its confirmation:
  DEPT, Principal, Visual Design (applied 2026-09-14, part of the same
  evening's application batch; rejected 2026-09-15, Weak fit — a
  Principal-level design-leadership/UX scope well beyond Regina's
  brand/graphic-design background) — missed by the prior two rescans
  since its confirmation subject ("Whoo! We've received your
  application!") didn't match the search keywords.
- **2026-09-15 (later)** — incremental rescan, 1 new row: TUSHY, Creative
  Strategist, Unknown fit — couldn't confirm the exact posting; TUSHY's
  own board only showed a differently-titled, more senior Associate
  Director, Creative req.
- **2026-09-15 (evening)** — incremental rescan, 2 new rows: Compass,
  Senior Designer (Good fit — closest match found is a Senior Graphic
  Designer role on their in-house Creative Studio, brand/campaign/print
  work with Adobe + Figma, a solid match to Regina's background). FLORA,
  Creative Generalist (Contract), Unknown fit — couldn't confirm the
  exact posting among FLORA's differently-titled Ashby listings.
- **2026-09-16** — incremental rescan, 2 new rows from the prior evening:
  Made Thought, Senior Designer (Good fit — confirmed posting, a London
  creative studio wanting graphic design/art direction/strategy craft, a
  strong match to Regina's agency background). Profound, Brand Designer
  (Good fit — a well-funded AI marketing-analytics startup wanting a
  Brand Designer to define its look/feel as it scales, solid general
  match though specific requirements weren't confirmable).
- **2026-09-16 (reported directly by Regina, screenshot)** — 2 new rows,
  found via a Gmail Sent search: Combo, Senior Brand Designer — a direct
  cold-email application (jobs@combo.co), Unknown fit since no actual
  posting could be found. Saint Urbain, Senior Designer — a direct
  cold-email application (work@sainturbain.com) in response to a
  LinkedIn post, Strong fit — an independent branding/strategy/design
  studio, a close match to Regina's branding-studio, Superside, and SVA
  Branding Master's background.
- **2026-09-17** — incremental rescan, no new rows, 1 rejection: flipped
  Compass's Senior Designer application to Rejected per a Greenhouse
  email.
- **2026-09-18** — logged a networking call with Andie Wexler (30-min
  Google Meet booked via Calendly), Sept 16, 2026, reported directly by
  Regina. Only a Calendly confirmation email was found in Gmail —
  company/context unconfirmed.
- **2026-09-18 (later)** — incremental rescan, 2 new rows, 2 flips: New
  York Times — Senior Strategist (3rd distinct NYT application, Unknown
  fit — couldn't confirm which of several same-titled NYT postings this
  was). Ripple — Senior Brand Designer, Rejected (distinct from the
  already-tracked NY Brand Designer role; likely the separate SF opening
  referenced in that row's notes, inferred applied_date from the original
  ambiguous 09-06 confirmation). Flipped Made Thought's Senior Designer
  application to Rejected. Flipped Day One's Senior Designer application
  to Interviewing — an external recruiter (Angela, thechangeagents.co)
  reached out to schedule a call; not yet booked.
- **2026-09-19** — 1 new row, reported directly by Regina with the full
  posting shared: Perplexity — Brand Designer, Growth, Fair fit
  ($150K–$225K + equity; strong on brand/visual craft, but the role's
  core growth-performance-data-driven iteration isn't a demonstrated
  specialty on her resume).
- **2026-09-19 (later)** — incremental rescan, no new rows. Day One's
  interview with Angela got booked — Google Meet confirmed for Monday,
  Sept 21, 2026, 1:00–1:25pm ET.
- **2026-09-19 (evening)** — 1 new row, traced back after Regina flagged
  it from a LinkedIn applicant-insight screenshot: OLIVER — Senior
  Designer, Good fit — a distinct 3rd OLIVER application (global
  financial-services account, in-house-agency model), missed by prior
  scans; confirmation found via targeted search.
- **2026-09-19 (evening rescan)** — incremental rescan, 1 new row:
  OLIVER — Senior Designer (2nd application), Unknown fit — a 4th,
  distinct OLIVER confirmation for a same-titled posting, 13 days after
  the first; OLIVER runs many concurrent Senior Designer reqs, so this
  reads as a separate opening rather than a duplicate.
- **2026-09-20** — 1 new row, traced back after a rejection surfaced for
  an application prior scans had missed: BritBox International — Senior
  Designer, Fair fit (entertainment key art for BBC Studios' streaming
  brand; typography/Photoshop craft lines up, but key art is a niche
  not evidenced on her resume). Applied 09-14, rejected 09-20.
- **2026-09-21** — incremental rescan, no new rows, 1 rejection: flipped
  Gensler's Multimedia + Graphic Designer, Marketing application to
  Rejected.
- **2026-09-21 (later)** — reconciled against a fresh Accenture
  candidate-portal screenshot (My Applications, all 4 "No Longer Under
  Consideration"). Flipped the LinkedIn-sourced Accenture "Creative
  Agency Senior Designer" application to Rejected — the other 3 (both
  Droga5 Senior Strategist reqs, Droga5 Senior Designer) were already
  Rejected.
- **2026-09-21 (evening rescan)** — incremental rescan, 1 new row:
  Accenture — Creative Agency Senior Designer (2nd application), Strong
  fit — a second, distinct Workday confirmation for the same role she
  was rejected from on 07-27, likely a reposted req.
- **2026-09-21 (later still)** — incremental rescan, no new rows, 1
  rejection: flipped Figma's Designer Advocate, Figma Weave application
  to Rejected.
- **2026-09-22** — reported directly by Regina (LinkedIn message
  screenshot), not from a Gmail scan: Anna Callagher, Lead Recruiter @
  Craft, messaged asking to book a call about one of Regina's three
  Craft applications (Senior Designer, Freelance Senior Brand Designer,
  Brand Designer — all applied 09-14) without saying which. Regina
  doesn't know either and asked Anna to clarify — no status change yet;
  noted on all three pending an answer.
- **2026-09-22 (later)** — 1 new row, found via Gmail Sent search: The
  Collected Works — Brand Designer, Good fit. Direct cold-email
  application to jobs@thecollectedworks.com, resume attached; no listed
  opening, general outreach to an SVA-founded NYC/New Orleans
  identity/motion/3D design studio.
- **2026-09-22 (later still)** — reported directly by Regina, not from
  a Gmail scan: flipped all three PepsiCo job applications (Design
  Senior Manager - Immersive, Brand Designer, Graphic Designer - poppi)
  to Rejected — an HR contact told her PepsiCo likely doesn't sponsor
  visas. Left the separate PepsiCo Networking outreach row (contact:
  Hillary) untouched since it's a contact, not an application to
  reject.
- **2026-09-22 (evening)** — reported directly by Regina, who shared the
  full LinkedIn posting for the NYT Senior Strategist application
  (previously Unknown fit since the exact req couldn't be pinned down).
  Confirmed as the T Brand Studio Creative Strategy team req
  (REQ-020117, $90K–$100K, 173 applicants) — updated to Fair fit, same
  strategy-track-career gap seen on the Droga5 and Design Bridge/Landor
  Senior Strategist roles.
- **2026-09-22 (later)** — 1 new row, reported directly by Regina with
  the full posting shared: BBDO — Senior Strategist, Fair fit
  ($95K–$110K/yr; same dedicated-strategist-career gap seen on the
  other Senior Strategist rows).
- **2026-09-22 (still later)** — reported directly by Regina, full
  postings shared for two previously Unknown-fit cold/generic
  applications: OLIVER's 2nd Senior Designer application (applied
  09-19) updated to Fair fit (Req 18584, $114,750–$128,250, hybrid 4
  days/wk — a high-volume regulated-industry account with real
  team-management and budget-ownership scope beyond IC design, not
  fully confirmed as the exact req behind that confirmation email).
  Combo's Senior Brand Designer cold-email application updated to Good
  fit (6+ yrs studio/agency, brand identity/packaging/campaign/UI
  portfolio — a strong match to her Common Matter background).
- **2026-09-22 (evening rescan)** — incremental rescan, 3 new rows:
  Monster Energy — Senior Graphic Designer, Americas, Fair fit (Corona,
  CA-based, no remote/NYC arrangement confirmed). Born Social —
  Associate Creative Director [NYC], Unknown fit (exact posting not
  found on their board). A third row logged as "Omnicom Network —
  General network application (3rd)" was removed after Regina
  clarified it wasn't a separate general application — it was the
  confirmation for the same-day BBDO Senior Strategist application
  (BBDO is part of Omnicom's network and routes through their shared
  Workday ATS). Merged that confirmation detail into the existing BBDO
  row instead.
- **2026-09-22 (later still)** — added a `had_interview` field, separate
  from current `status`, so an application that reached an interview
  call keeps that fact even if it's later Rejected (Regina pointed out
  the "2 Interviewing" stat undercounts real interview calls).
  Backfilled `had_interview: 1` on the 3 rows confirmed to have had an
  actual interview/screening call: Design Bridge and Partners / Landor
  (Interviewing), Day One (Interviewing), and Duel (Rejected after a
  recruiter screen).
- **2026-09-22 (yet later)** — Regina booked the Craft call with Anna
  Callagher for Wednesday, Sept 23 and asked again which of the 3 Craft
  applications it's for — still unanswered. Added a `next_step` note to
  all three flagging the booked call, but deliberately did not set
  `had_interview` on any of them yet, since doing so on all three would
  triple-count a single call and picking just one would be a guess.
- **2026-09-22 (rescan)** — incremental rescan, 1 new row, 1 rejection:
  flipped Accenture's 2nd Creative Agency Senior Designer application to
  Rejected — same visa-sponsorship template as the earlier Work & Co
  Designer rejection. Added a new Craft Networking row: Fionn Andrews,
  a separate Craft recruiter (freelance placement arm, not the same
  person as Anna Callagher) who already had a call with Regina and is
  onboarding her onto Craft's "Taste" freelance-project platform —
  distinct from the still-unresolved Anna Callagher call about one of
  the 3 full-time Craft applications.
- **2026-09-22 (later rescan)** — incremental rescan, 1 new row, 2
  rejections: flipped both Fresh — Senior Designer, Digital and Social
  applications (09-06 and its 09-07 duplicate) to Rejected — two
  separate but identical rejection emails, ~25 min apart. New row:
  Craft (Taste freelance platform) — Senior Designer, Brand Guidelines
  and Identity, **Offer** status — Regina applied to this Taste
  freelance project the same day she was onboarded by Fionn, submitted
  a design assessment, and was selected to move forward with a Master
  Freelance Agreement/Statement of Work being sent, all within hours.
  Strong fit (brand guidelines/identity is her core specialty).
- **2026-09-22 (yet later)** — 1 new row, found via Gmail Sent search:
  Mischief — Networking outreach, no open role (contact: Robyn) —
  warm-intro cold email referred by Sadia; company isn't hiring, no
  resume attached, no specific role, so logged as Networking rather
  than a job application.
- **2026-09-22 (final)** — 1 new row, found via Gmail Sent search: LOS
  YORK — Freelance Brand Strategist, Good fit. Direct cold-email
  application to katy.b@losyork.tv in response to a LinkedIn post,
  resume attached; no formal posting found, but LOS YORK is an LA/NY
  multidisciplinary creative production studio (Amazon, Netflix,
  Logitech) — a solid general match to Regina's brand-strategy
  background, tilted more toward video/content than her usual
  identity/print work.
- **2026-09-22 (rescan)** — incremental rescan, no new rows: Day One's
  interview call with Angela happened Monday, Sept 21 as scheduled —
  she followed up 09-22 asking for an updated resume, which Regina
  sent same day. Updated next_step accordingly; still Interviewing.
- **2026-09-23 (later)** — 1 new row, found via Gmail — no original
  confirmation email or Sent-mail record exists for this application:
  Canopy — Graphic Designer, Unknown fit, status Interviewing — Katy
  Spore (Senior Graphic Designer) invited Regina directly to pick a
  time for a 30-min intro call; applied_date is a placeholder since
  the true application date couldn't be traced.
- **2026-09-23 (correction)** — Anna Callagher's (Craft) call happened
  today as scheduled, but she never confirmed which of the 3 Craft
  applications it was for. Per Regina's request, picked one — Craft —
  Senior Designer — to hold Interviewing status and `had_interview=1`
  for now; the other two Craft rows stay Applied. Flagged in all three
  rows' next_step/notes as a placeholder assignment to be corrected
  once Anna confirms the actual role.
- **2026-09-23 (rescan)** — 1 new row, 2 updates: Polonsky & Friends —
  Junior Graphic Designer, Fair fit — new internship application (20
  hrs/week, 6-12 months) found via referral, applied same day. The New
  York Times — Senior Designer, Games Marketing (Temporary) flipped to
  Rejected (generic decline email). Canopy's next_step updated: the
  intro call with Katy Spore is now confirmed for 3:00-3:30pm ET today,
  not just requested.
- **2026-09-23 (correction)** — Regina confirmed the identities behind
  two of the three Craft applications. Craft — Senior Designer is Red
  Antler (the Anna Callagher call held today was for this one) —
  renamed to Red Antler, Good fit, stays Interviewing/`had_interview=1`.
  Craft — Brand Designer is Vault 49 (the CPG-focused one) — renamed to
  Vault 49, Good fit. Craft — Freelance Senior Brand Designer remains
  unresolved — the one application whose client company is still
  unknown.
- **2026-09-24 (update)** — Craft (Taste freelance platform) — Senior
  Designer, Brand Guidelines and Identity next_step updated. Regina
  completed identity verification on the portal (2026-09-23) and
  checked in with Fionn Andrews about next steps; he confirmed it's now
  with Taste's own team to review and reach out directly, not something
  to chase with him. No other contact was named.
- **2026-09-24 (rescan)** — no new rows, 2 next_step updates: Red
  Antler — Senior Designer: Regina sent Anna Callagher her strategy
  portfolio; the link didn't work on Anna's end, so it may need
  resending. Vault 49 — Brand Designer: Regina sent an updated design
  portfolio with a new packaging project; Anna said it looks great.
  Anna will follow up on her thoughts on both — no calls scheduled yet
  for either.
- **2026-09-24 (later)** — no new rows, 1 next_step update: Red Antler
  — Senior Designer: Regina resent the corrected strategy portfolio
  link (reginabbs.cargo.site) to Anna Callagher the same day, after
  the original link didn't work on her end.
- **2026-09-24 (evening)** — no new rows, 2 flips: The New York Times —
  Senior Strategist (T Brand Studio, applied 09-18) rejected via a
  generic decline email. Day One — Senior Designer rejected: Angela
  (The Change Agents, the recruiter handling this candidacy) confirmed
  Day One's internal policy doesn't allow considering candidates who
  may need future visa sponsorship — not a fit/performance rejection.
- **2026-09-25** — 1 new row: Craft — Graphic Designer, Unknown fit,
  status Applied — a 4th, distinct Craft application, confirmed only
  via Craft's generic "application received" auto-reply. Which client
  req this is for is unconfirmed (separate from the already-resolved
  Red Antler and Vault 49 reqs, and the still-unresolved Freelance
  Senior Brand Designer one).
- **2026-09-25 (later)** — 1 new row, 1 next_step update: Morning Brew
  — Associate, GTM Strategy, Fair fit — new application, confirmed via
  Lever's auto-reply. Anna-Rae Morris (networking, JKR Global): a
  follow-up call is now being actively scheduled for the week of
  2026-09-28 after a reschedule.
- **2026-09-26** — no new rows, 1 flip: Gigs — Senior Brand Designer
  rejected: position filled ("we have recently filled this position").
- **2026-09-27** — no new rows, 1 next_step update: Craft (Taste
  freelance platform) — Senior Designer, Brand Guidelines and Identity:
  Taste confirmed the concrete project assignment ("GoldenStone Slides
  & Docs", role Brand Designer), rate ($85/hr, $510/deliverable), and
  start date (Thursday, Oct 1, pending ID/background check). Stays
  Offer status.
- **2026-09-28** — 8 new rows, an application sprint late on 2026-09-27:
  2x4 — Design Intern / Branding (Fair) and Designer / Digital (Good),
  both direct cold emails to the studio. Onebrief — Senior Brand
  Designer (Good, AI military-planning software). Meta — Brand
  Designer, Foundations - Instagram Brand Studio (Fair, 6th distinct
  Meta application). Profound — Brand Designer (Good, AI marketing
  platform). HappyRobot — Brand Designer (Good, AI-worker
  infrastructure). OLIVER — Senior Designer, 3rd application (Unknown,
  generic confirmation, client/req unconfirmed). Thyme Care — Visual
  Designer, Marketing (Good, oncology care company). All confirmed via
  ATS auto-replies (Ashby/Greenhouse) except the two 2x4 cold emails.
- **2026-09-28 (later)** — 8 more new rows, continuation of the same
  2026-09-27 application sprint (later that same night), plus 1
  next_step update: ShopMy — Unspecified role/Design (Unknown, generic
  confirmation, multiple open design roles). Rightway — Sr. Graphic
  Designer (Good, healthcare-navigation tech). Code and Theory —
  Unspecified role/Design (Unknown, generic confirmation, multiple open
  designer roles). SHADOW — Designer (Good, creative agency). webAI —
  Marketing Designer (Unknown, no posting found). The Farmer's Dog —
  Brand Designer (Good, DTC pet food). Fanatics Collectibles — Senior
  Graphic Designer (Fair, trading-card print production). Agentio —
  Brand Designer (Good, creator-ads adtech). Craft (Taste freelance
  platform) next_step updated: Taste flagged an incoming Checkr
  background-check email.
- **2026-09-28 (still later)** — 16 more new rows, the same 2026-09-27
  application sprint running well past midnight: OLIVER — Digital
  Content Designer (Fair, 5th distinct OLIVER application). Digital
  Asset — Brand Designer (Unknown). Bespoke Post — Graphic Designer
  (Unknown, 2nd distinct Bespoke Post application). Wpromote — Senior
  Pitch Designer (Fair). Verve — Unspecified role/Design (Unknown,
  multiple open design roles). J.Crew — Sr. Digital Designer (Fair).
  VaynerMedia — Designer (Good). goop — Unspecified role/Design
  (Unknown, most likely Senior Graphic Designer). Warner Bros.
  Discovery — Digital Designer, CNN (Unknown, no posting found). TRM
  Labs — Senior Brand Designer (Good). Alpaca Markets — Senior Graphic
  Designer (Good). Red Antler — Senior Digital Designer (Good, 2nd
  distinct Red Antler application, direct via Breezy — separate from
  the Craft-routed Interviewing req). Suno — Senior Designer, Creative
  Studio (Good) and the contract variant of the same role (Good).
  Conduit Health — Brand Designer (Good). FP Movement — Graphic
  Designer (Fair, Free People/Urban Outfitters).
- **2026-09-28 (rescan)** — Conveo — Design Lead flipped Applied →
  Rejected (generic decline, no reason given). The rejection email
  arrived without the application in the same scan; original
  confirmation traced back to 2026-09-06, already logged with the
  correct applied_date.
- **2026-09-28 (later rescan)** — 3 status updates, no new applications.
  Bumble — Graphic Designer flipped Applied → Rejected (role closed, not
  a fit rejection). Vault 49 — Brand Designer flipped Applied →
  Interviewing: Anna Callagher (Craft) is scheduling an interview this
  week with Vault 49's own team (Laura/Operations, Nick Corey/ADD, Steve
  Baust/ADD). Canopy — Graphic Designer next_step updated: Regina sent a
  check-in email after no word since the 2026-09-23 intro call;
  had_interview backfilled to 1 since that call already happened.
- **2026-09-28 (evening rescan)** — 2 next_step updates, no new
  applications. Vault 49 — interview time confirmed: Wednesday, Oct 1 at
  1:00pm ET. Craft (Taste freelance platform) — Senior Designer, Brand
  Guidelines and Identity: Regina submitted her background check and
  flagged a discrepancy to Dave (recruiting@tastelabs.com) — the
  confirmed project is "GoldenStone Slides & Docs" but she'd understood
  she was joining "Guidelines and Identity"; also hasn't received the
  SOW yet. Awaiting his reply on both — worth watching since it could
  mean a different project scope than expected.
- **2026-09-29 (morning rescan)** — 2 updates, no new applications.
  Wpromote — Senior Pitch Designer flipped Applied → Rejected (generic
  "moving forward with other candidates" decline; subject line read
  "Wpromote x Giant Spoon", suggesting an agency-partner req). Vault 49
  — next_step updated with interview format details: a 45-minute call
  presenting a couple of projects, calendar invite to come from Laura.
- **2026-09-29 (afternoon rescan)** — 1 update, no new applications. Red
  Antler (Craft-routed Senior Designer req, Interviewing) — Anna
  Callagher reported Red Antler came back wanting to chat again and
  asked for Regina's availability this week and early next; Regina
  hasn't replied yet — worth a nudge since it's a live, advancing
  Interviewing thread. (Vault 49's calendar invite for Wed Sept 30,
  1:00–1:45pm ET also came through from Laura Negin — confirms what was
  already logged, no content change.)
- **2026-09-29 (evening rescan)** — 4 updates, no new applications.
  Craft — 4th distinct application (Graphic Designer, client still
  unknown) flipped Applied → Rejected, generic decline direct from
  Craft. Bespoke Post — 2nd distinct application (Graphic Designer)
  flipped Applied → Interviewing: Kate Mulcahy wants to schedule a
  phone call, Regina hasn't replied yet. Mother — Regina's 2026-09-25
  check-in with a contact named Rachel (rachel@motherusa.com, name
  doesn't match the original Maggie Murphy contact — not guessing if
  same person) got a reply: still quiet on the strategy side, will flag
  if something opens up. Red Antler (Craft-routed, Interviewing) —
  Regina replied to Anna with her availability (Wed/Thu before 3pm or
  Mon/Tue next week); awaiting a locked-in time.
- **2026-09-30 (midday rescan)** — 4 updates, no new applications. Red
  Antler (Craft-routed Senior Designer req) — advanced from "awaiting a
  time" to an actual interview: Amanda Almeida (Red Antler EA) is
  coordinating a meeting with Rogerio Lionzo, Creative Director,
  offering Thu Oct 1 2:00–2:45pm or Fri Oct 2 1:00–1:45pm; Regina hasn't
  picked a slot yet — notable since this is the process moving past the
  recruiter and into Red Antler's own interview loop as expected. The
  Collected Works — Brand Designer flipped Applied → Rejected (high
  volume of applicants, generic). Polonsky & Friends — Junior Graphic
  Designer flipped Applied → Rejected (explicitly overqualified — role
  is for someone earlier in their career). Craft (Taste freelance
  platform) — Senior Designer, Brand Guidelines and Identity: kickoff
  call invite arrived for Thu Oct 1, 1:00–1:30pm ET (large group invite,
  11+ other designers cc'd), confirming the project is proceeding on
  schedule even though the project-name discrepancy Regina flagged was
  never explicitly answered.
- **2026-09-30 (evening rescan)** — 4 updates, no new applications.
  Onebrief — Senior Brand Designer flipped Applied → Rejected (generic
  decline). Red Antler (Craft-routed Senior Designer req) — Regina
  confirmed Thu Oct 1, 2:00–2:45pm ET for the Rogerio Lionzo interview;
  calendar invite followed. Bespoke Post — Graphic Designer: call
  confirmed for Thu Oct 1, 12:15–12:45pm ET (phone call despite an
  auto-generated Meet link). Polonsky & Friends — Regina replied to the
  rejection asking to be kept in mind for future openings (no status
  change).
- **2026-10-01 (morning rescan)** — 1 update, no new applications.
  Vault 49 — Anna Callagher relayed positive feedback from the Sept 30
  interview: Vault 49 wants a second round with Sam (CD) and Jenn (DD),
  proposing Thu Oct 8 2pm or Fri Oct 9 11am, and asked Regina to
  present her work as a deck this time. Regina hasn't replied yet —
  notable since the process is advancing well. (Also corrected a date
  typo on this row: the first interview happened Wed Sept 30, not "Oct
  1" as a prior entry mistakenly said.)
- **2026-10-01 (afternoon rescan)** — 2 updates, no new applications.
  Vault 49 — Regina confirmed the second round for Thu Oct 8,
  2:00–2:45pm ET with Sam Wilkes (CD) and Jennifer Yelk (DD), and
  agreed to prepare a deck; calendar invite followed. Craft (Taste
  freelance platform) — the SOW finally arrived via PandaDoc ("Regina
  Barrera & Taste Tech Inc. - Slides&Docs Project - Brand Designer");
  not yet signed. (Red Antler's Rogerio Lionzo interview, scheduled for
  2pm ET today, hadn't happened yet as of this scan.)
- **2026-10-01 (evening rescan)** — 1 update, no new applications. Red
  Antler — the Rogerio Lionzo interview happened; Regina told Anna it
  went really well — a strong conversation about how strategy and
  design overlap at Red Antler, she clarified her hands-on-design-
  plus-strategy fit, and sent Rogerio her design portfolio as a
  follow-up. She said the role sounds well-aligned and wants to move
  forward; awaiting word from Red Antler's side.
- **2026-10-02 (morning rescan)** — 1 update, no new applications.
  Craft (Taste freelance platform) — the SOW was completed and fully
  signed by all participants. Remaining steps: set up a tastemaker.pro
  email, join the project Slack, attend the kickoff call (was
  scheduled for Thu Oct 1).
- **2026-10-02 (evening rescan)** — 2 updates, no new applications.
  webAI — Marketing Designer flipped Applied → Interviewing: Michael
  Hale (Technical Recruiter) reached out, Regina booked an intro call
  for Mon Oct 5, 11:30am–12pm ET. Vault 49 — the Oct 8 second-round
  interview was rescheduled to Friday, Oct 9, 11:00–11:45am ET at
  Regina's request due to a family matter (her mother having surgery,
  requiring travel to Houston).
- **2026-10-03 (rescan)** — 2 updates, no new applications. JPMorgan
  Chase & Co. — Olympic & Paralympic, Graphic Designer, Senior
  Associate (Job #210766619) flipped Applied → Rejected (generic, high
  volume). SHADOW — Designer flipped Applied → Rejected (generic
  decline).
- **2026-10-04 (rescan)** — 1 update, no new applications. Fanatics
  Collectibles — Senior Graphic Designer flipped Applied → Rejected
  (generic decline).
- **2026-10-05 (rescan)** — 3 updates, no new applications. Amazon —
  Brand Designer, Brand Innovation Lab (ID: 10525009) flipped Applied
  → Rejected (generic decline via Amazon.jobs). Suno — the Senior
  Designer, Creative Studio & Brand Campaigns (Contract) application
  flipped Applied → Rejected (generic decline); the distinct full-time
  Suno req remains open. webAI — the Oct 5 recruiter screen happened
  and went well; Michael Hale passed Regina's info to the Hiring
  Manager, who wants to chat next — awaiting Regina to book that call.
- **2026-10-05 (evening rescan)** — 1 new row, 2 updates. Porto Rocha —
  a cold-outreach email from 2026-08-26 (resume attached, no open role
  at the time) finally got a real reply: no Associate Strategist
  opening, but a paid strategy internship was floated; Regina said
  she's open to hearing more. Bespoke Post — the Graphic Designer phone
  call happened and went well; Kate Mulcahy wants to schedule a
  follow-up with the Associate Creative Director next. webAI — Regina
  booked the Hiring Manager call for Thursday, Oct 15, 1:00–1:30pm ET.
- **2026-10-06 (rescan)** — 1 update, no new applications. Bespoke
  Post — Regina replied to Kate Mulcahy with her availability
  (Wednesday and most of Friday) for the Associate Creative Director
  conversation; awaiting Kate to confirm a specific time.
- **2026-10-06 (afternoon rescan)** — 2 updates, no new applications.
  Bespoke Post — after some back-and-forth (the ACD was OOO), the
  Associate Creative Director conversation is confirmed for Monday,
  Oct 12, 1:30–2:00pm ET with Joelyn Dalit; Kate also mentioned she's
  researching possible TN visa support for Regina. Mother — a calendar
  invite appeared for a Zoom call with a third, previously untracked
  contact (Veronica Thew) on Tuesday, Oct 13, 3:00–3:30pm ET; no
  explanatory email, so its connection to the earlier Maggie
  Murphy/Rachel threads is unclear.
- **2026-10-06 (evening rescan)** — 1 ambiguous rejection, no new
  applications. OLIVER — a generic rejection email arrived with no job
  title or req ID, identical boilerplate to the already-logged Social
  & Culture Strategist rejection from 08-14. With four other OLIVER
  applications still Applied (Senior Designer x3, Digital Content
  Designer), couldn't determine which one this pertains to; flagged a
  note on all four rather than guess which to flip to Rejected.
- **2026-10-07 (rescan)** — 8 new rows, 2 updates. A late-night
  application sprint (2026-10-06, ~8:20–9:03pm ET) produced
  confirmations from Google (Unspecified role, 4th distinct Google
  application), Mammoth Brands (Junior Creative Strategist, 2nd
  distinct application), Whatnot (Lead Brand Designer), Apple Bank
  (Senior Visual Designer), WGACA (Unspecified role), Authentic Brands
  Group (Graphic Designer), and EliseAI (Graphic Designer) — plus a
  cold-outreach application to PictureStudio (Senior Designer, resume
  emailed directly). J.Crew — Sr. Digital Designer flipped Applied →
  Rejected (generic decline). Rightway — a second, identical
  confirmation arrived for the same Sr. Graphic Designer posting;
  treated as a likely accidental duplicate re-application rather than
  a new row. Craft (Taste freelance platform) — Checkr confirmed the
  background check is complete, report sent to Taste AI.
- **2026-10-08** — 1 new row, from a full sweep of Sent mail (not just
  inbound confirmations) at the user's request. Solomon Page — a
  resume/portfolio sent to a staffing-agency recruiter via a personal
  referral (Michele Cilione), general introduction, no specific role
  or client. Cross-checked several other Sent-mail cold-outreach
  threads (Accenture/Monica de Armas, Mother/Rachel Boyle's first
  contact, a personal resume review with Mike McCulloch) against
  existing rows — all were already captured.
- **2026-10-08 (evening rescan)** — 1 new row, 2 updates. Salesforce —
  Communications Designer, confirmed via Workday. Red Antler — Regina
  checked in with Anna Callagher on the Senior Designer process; no
  reply yet. Mother — found the original 2026-09-25 cold-outreach
  email to Veronica Thew (a third, distinct Mother contact) in a
  Sent-mail sweep prompted by the user; this resolves the
  previously-logged "unexplained" Oct 6 calendar invite — it was the
  downstream scheduling step of this same thread. Veronica replied
  warmly, looped in Lauren Martinovic, and the call is now confirmed
  for Tue, Oct 13, 3:00–4:00pm ET with Lauren (Veronica cc'd).

LinkedIn's own "job alert" and "jobs similar to" emails were excluded from
every scan since those are recommendations, not applications you submitted.
Employer candidate portals (like JPMC's above) are the most authoritative
source when they conflict with an email confirmation or LinkedIn's own
tracking — pasting a screenshot of one works the same way as the
paste-and-parse LinkedIn flow.

An automated Routine reruns this same scan three times a day (roughly
8am / 1pm / 6pm ET) and pushes any new rows straight to this branch.

## API

| Method | Path                      | Description                    |
|--------|---------------------------|---------------------------------|
| GET    | `/api/applications`       | List all applications           |
| POST   | `/api/applications`       | Create an application           |
| PUT    | `/api/applications/<id>`  | Update an application           |
| DELETE | `/api/applications/<id>`  | Delete an application            |
| GET    | `/api/stats`              | Aggregate stats                 |
| POST   | `/api/import`             | Bulk import from a CSV file      |
