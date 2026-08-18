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
(Applied / Interviewing / Offer / Rejected / Withdrawn), `applied_date`,
`next_step`, `job_url`, `source`, `referral` (yes/no), `notes`, `pay_range`,
`job_description`.

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
