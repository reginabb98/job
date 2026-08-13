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
Jobs" list, and there's no way for this tool to log into LinkedIn on your
behalf. To bring that data in:

1. Open LinkedIn's applied-jobs page (Jobs → My Jobs → Applied).
2. Copy company / role / applied date into a spreadsheet, or fill in
   [`import_template.csv`](./import_template.csv).
3. In the app, click **Import CSV** and upload the file.

Required columns: `company`, `position`. Optional: `status` (Applied /
Interviewing / Offer / Rejected / Withdrawn), `applied_date`, `next_step`,
`job_url`, `source`, `referral` (yes/no), `notes`.

### Email

There's no way to give this standalone app a persistent, ongoing connection
to your inbox — that would require setting up a Google Cloud project with
Gmail API OAuth credentials and running your own auth flow, which is a
separate piece of setup outside of what's in this repo.

What *is* possible: since Claude has access to your Gmail in a chat session,
you can periodically ask Claude to scan your inbox for application
confirmations, rejections, and interview invites, and either update
`tracker.db` directly or hand you a CSV to import.

The three rows in `scripts/seed_from_gmail_scan.py` came from exactly that —
a one-time scan of rbarrerababb@sva.edu on 2026-08-13, searching for
application/interview/offer/rejection language and common ATS senders
(Greenhouse, Lever, Workday, iCIMS, Taleo, SmartRecruiters, Ashby, LinkedIn).
No corporate ATS emails turned up in that inbox at the time — the only real
leads found were an SVA Library position (rejected) and two TA-position
inquiries (pending). If most of your job-hunt email goes to a different
address, point Claude at that inbox instead next time.

## API

| Method | Path                      | Description                    |
|--------|---------------------------|---------------------------------|
| GET    | `/api/applications`       | List all applications           |
| POST   | `/api/applications`       | Create an application           |
| PUT    | `/api/applications/<id>`  | Update an application           |
| DELETE | `/api/applications/<id>`  | Delete an application            |
| GET    | `/api/stats`              | Aggregate stats                 |
| POST   | `/api/import`             | Bulk import from a CSV file      |
