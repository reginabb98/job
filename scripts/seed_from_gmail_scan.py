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
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "iCIMS",
        "notes": "Publicis Groupe agency; confirmation came via Publicis Groupe's iCIMS instance.",
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
        "position": "Art Director, Elevated Shopping (ID: 10410280)",
        "status": "Applied",
        "applied_date": "2026-08-17",
        "source": "Amazon Jobs",
        "notes": "Online assessment completed 2026-08-18; no interview invite yet.",
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
        "status": "Applied",
        "applied_date": "2026-08-26",
        "source": "Greenhouse",
        "notes": None,
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
                 "not a domain in the ATS search list. No response yet as of 2026-09-02.",
        "job_fit": "Good",
        "job_fit_notes": "The closest generalist-titled match found is a 3-5 yr Graphic Designer posting: "
                         "advanced Adobe Creative Suite, working Figma knowledge, client-branding-guideline "
                         "layout work -- a solid match for Regina's tools and design background, though the "
                         "confirmation email didn't specify a seniority level so this exact posting isn't "
                         "fully confirmed.",
    },
    # -- 2026-09-02: applied directly + reached out to a team contact same day --
    {
        "company": "Monks",
        "position": "Associate Director, Comms Planning",
        "status": "Applied",
        "applied_date": "2026-09-02",
        "source": "Email",
        "notes": "Applied through the official posting and separately emailed Olga Gamer "
                 "(olga.gamer@monks.com) directly the same day, referencing her Superside experience "
                 "and attaching a tailored CV. Confirmation email (no-reply@monks.com) titles the role "
                 "\"Associate Director, Comms Planning\"; the outreach email to Olga said \"Associate "
                 "Strategy Director, Comms Planning\" -- same role, minor title variant.",
        "job_fit": "Fair",
        "job_fit_notes": "Wants 5 years in a media agency (3+ specifically in Connections/Comms Strategy) plus direct-report management. Regina's research, deck-building, and narrative-writing skills overlap qualitatively, but this is a media/comms-planning discipline rather than brand/creative design, and her 6 years are mostly design-agency rather than media-agency -- plus people-management isn't evidenced on her resume.",
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
        row.setdefault("job_fit", None)
        row.setdefault("job_fit_notes", None)
        db.execute(
            """
            INSERT INTO applications
                (company, position, status, applied_date, next_step, job_url, source, referral, notes, job_fit, job_fit_notes, created_at, updated_at)
            VALUES (:company, :position, :status, :applied_date, :next_step, :job_url, :source, :referral, :notes, :job_fit, :job_fit_notes, :created_at, :updated_at)
            """,
            {**row, "created_at": now, "updated_at": now},
        )
    db.commit()
    print(f"Seeded {len(SEED_ROWS)} applications from the Gmail scan.")


if __name__ == "__main__":
    main()
