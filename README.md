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
