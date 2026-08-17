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
   (Jobs → My Jobs → Applied), copy the visible rows as plain text, and
   paste them to Claude in chat. Claude parses company / role / applied
   date out of the raw text and imports it for you — no formatting required.
2. **CSV template:** copy company / role / applied date into
   [`import_template.csv`](./import_template.csv) yourself, then in the app
   click **Import CSV** and upload it.

Required columns for CSV import: `company`, `position`. Optional: `status`
(Applied / Interviewing / Offer / Rejected / Withdrawn), `applied_date`,
`next_step`, `job_url`, `source`, `referral` (yes/no), `notes`.

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
- **2026-08-17** — incremental scan covering everything since the prior
  scan. 5 new rows: 4 Applied (NBCUniversal, Blackstone, Bespoke Post,
  Inizio Evoke) and 1 Rejected (OLIVER).

LinkedIn's own "job alert" and "jobs similar to" emails were excluded from
every scan since those are recommendations, not applications you submitted.

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
