# Seyo AI migration and validation report

Validation began on 23 November 2026 and final packaging continued on 24 November 2026 (IST).
This report records checks actually executed; it does not assert production readiness.

## Authorization and repository boundaries

The user explicitly confirmed the necessary source reuse rights and absence of company-confidential
materials before any local source copying. Personal Git CLI login and author are Sasisampath,
with author email 101541856+Sasisampath@users.noreply.github.com. The connected GitHub plugin has
a different identity and was used only for read-only inspection; delivery uses the personal CLI.

The destination was verified empty before import and again before final packaging. The only Git
remote is origin, https://github.com/Sasisampath/Seyo-ai.git. The source repository was read only.
There was no source clone, history import, force push, source mutation or source remote added.

## Snapshot and files migrated

Imported 76 working-tree files from source commit
`55f76f306a3f85e6480eb276f65707422894c5d8` through a GitHub archive. The original file paths,
sizes and SHA-256 values are in SOURCE_SNAPSHOT.json. The archive has no source .git directory.
No real environment files, databases, customer uploads, virtual environments, caches or builds
were present in the imported snapshot. New locally generated runtime files are ignored.

Preserved directories: apps/web, services/api (app, domain, adapters, workers, migrations, tests),
fixtures and infra. The fictional bill image and generator were retained. Original database
models, migration files, API router files, financial logic, adapters, tests and all frontend
files except product labels/metadata and package setup are byte-for-byte unchanged.

`python3 scripts/check_migration.py` passed: **65 protected original files unchanged**.
The 11 intentional original-file changes are:

- .env.example: explanatory comments, empty provider placeholders and Graph version setting.
- .gitignore: broadened protection for environments, secrets, data, caches and builds.
- README.md: Seyo AI identity, reproducible setup, current capabilities and explicit limitations.
- BUILD_PROMPT.md and SKILL.md: product name; no behavioral requirements removed.
- apps/web/app/layout.tsx: page title and product description.
- apps/web/components/shell.tsx: login, desktop and mobile product text.
- apps/web/package.json: typecheck script and Node engine floor.
- apps/web/package-lock.json: root engine metadata only; dependency entries unchanged.
- services/api/app/main.py: API title only.
- docs/ARCHITECTURE.md: distinguishes architectural targets from implementation and fixes the schema reference.

New setup/evidence files include root AGENTS.md, requirements.lock.txt, the preservation-check
script, SOURCE_SNAPSHOT.json, product scope, provider setup, test plan, roadmap, dependency
inventory and this report. No new source-code redistribution license was invented. The source
has no declared license; transfer authorization is based on the user's explicit confirmation.
Dependency license metadata is inventoried, not independently legally cleared.

## Functionality preserved

Today dashboard and cash-flow comparisons; reviewed bill uploads and invoice approval; customer
and invoice ledgers; integer-paise partial payments and allocation history; signed, idempotent
reconciliation; unverified claims, disputes and reversals; customer promises with evidence;
demo WhatsApp inbox and inbound webhook; read-only text/voice tools; browser speech and optional
ElevenLabs adapter; demo roles/tenant isolation; settings, provider adapters and reset.

All 49 distinct OpenAPI paths remain present. Financial calculations and posting stay in the
existing deterministic backend. An LLM never directly changes verified balances. A promise
or screenshot remains separate from a confirmed receipt.

## Checks executed and exact results

| Check | Result |
| --- | --- |
| Original baseline, Python 3.14.9: `.venv/bin/python -m pytest -q` | 26 passed, 1 warning in 1.01s |
| Rebranded backend: same command | 26 passed, 1 warning in 0.99s |
| `.venv/bin/python -m app.seed` | Fresh SQLite migrations applied and fictional demo data seeded |
| `.venv/bin/python -m alembic current` | 0001 (head) |
| `.venv/bin/python -m pip check` | No broken requirements found |
| Node 26.7.0 / npm 11.19.0: `npm ci` | Successful |
| `npm run typecheck` | Successful route type generation and tsc --noEmit |
| `npm run build` | Next.js 16.4.6 production build successful; 10 static pages generated, dynamic routes retained |
| `npm audit --json` | Zero known vulnerabilities |
| pip-audit of all 36 fully pinned core backend packages | Zero known vulnerabilities |
| Gitleaks 8.30.1, redacted scan of original 76 files | Zero findings |
| Source-preservation hashes | 65 protected files unchanged |
| Live requests through Next.js /api proxy | 13 checks passed, zero failed |

The pytest warning is StarletteDeprecationWarning: using httpx with starlette.testclient is
deprecated in favor of httpx2. Existing tests were retained without suppressing that warning.
The backend lock captures the tested core environment; optional Python provider SDKs were not
installed or audited. Audits report known advisories at scan time, not a guarantee of security.
PostgreSQL migrations/locking and concurrent webhook delivery were not executed on PostgreSQL.

## Running-app checks

Started FastAPI on 127.0.0.1:8000 and the built Next.js app on 127.0.0.1:3000. The running
API responds healthy and Next.js successfully proxies API requests.

Browser journeys observed:

1. Owner login and Today dashboard: seeded ₹25,900 pending, ₹10,000 simulated received,
   ₹9,000 promised and ₹2,000 unverified, with simulation labels visible.
2. Assistant answered Murugan Stores payments from ledger tools: ₹15,000 paid and ₹5,000 due.
3. Sample bill review initially blocked for line conflicts/missing quantity. Entered corrections,
   saved, acknowledged the tax warning, approved INV-0004 for ₹5,300 and inspected its lines.
4. INV-0001 retained its ₹20,000 total and two prior receipts. Prepared and approved a simulated
   ₹5,000 request, then simulated capture. Invoice due reached ₹0 with the third allocation visible.
5. Customer ledger agreed: ₹25,300 invoiced, ₹20,000 provider-verified simulated receipts,
   ₹5,300 outstanding from the newly approved bill.

A screenshot outside the Git repository, outputs/seyo-ai-preview.jpg, shows the dashboard after
those demo actions: ₹26,200 pending and ₹15,000 simulated receipts for that day. It is a
23 November test-state snapshot, not a statement of real business finances.

Subsequent live API checks through the frontend proxy verified the persisted bill and invoice,
customer/assistant evidence, exactly-once duplicate delivery, a compensating refund, forged
signature rejection, two unsaved promise proposals, cross-tenant rejection, viewer write rejection,
and disabled outbound messaging/calls. All 13 passed. Local demo artifacts are not committed.

## Integration readiness and gaps

| Integration | Current evidence | Remaining validation |
| --- | --- | --- |
| Demo payments | Pytest, browser and live API checks | Simulated money only |
| Bill extraction | Simulated draft review/approval verified | Gemini account, actual image/PDF extraction |
| Assistant | Rule routing and deterministic evidence verified | Optional Gemini routing account test |
| Browser voice | UI path retained | Microphone, speech recognition and spoken output not exercised |
| ElevenLabs | Adapter/client/tools retained; secret-auth fixture tested | Signed session and actual audio account test |
| WhatsApp inbound | Signed text fixtures tested; media code retained | Personal Meta phone mapping, real webhook/media retrieval |
| Razorpay | Test-only adapter retained | Account mapping, payment-link correlation, signed test events |
| WhatsApp outbound / AI calling | Absent and disabled | Not included in this migration |

Demo authentication is passwordless. File uploads are unencrypted local files. Production identity,
rate limiting, data retention, durable job retries, secure storage and production observability
are missing. Media jobs use BackgroundTasks without durable retry. Partial refunds need manual
review. Some existing integration UI labels say “live” on configuration alone; the documentation
explicitly distinguishes configuration from account validation. No production-readiness claim is made.

## Next milestone

Validate a personal Meta test merchant's handwritten bill intake through Gemini extraction and
web review/approval using fictional data. Add durable media retries and evidence-based integration
status. Continue with PostgreSQL concurrency and production identity/storage hardening afterward.

## Final Git preflight

The final staged file-list audit and redacted Gitleaks scan are recorded below before the initial
commit. The initial commit is local and contains no source-history parents. Push is only a normal
non-force update to the personal destination main branch, after the user-facing results report.

Final staged scope: **86 files** (76 imported files, 10 new setup/evidence files). The staged
path audit found zero forbidden paths: no source .git history, real .env files, credential files,
databases, uploaded runtime data, virtual environments, node_modules, caches or builds. All
original source paths remain. Dependency metadata inventories 36 installed core Python packages
and 117 npm lock entries. Final redacted Gitleaks scan of the exact staged file contents:
**zero findings** (Gitleaks 8.30.1).

The initial full-snapshot `git diff --cached --check` reports one inherited trailing space in
services/api/migrations/versions/0001_initial_schema.py, line 4 (the `Revises:` comment). This
nonfunctional original formatting is retained to preserve the migration file byte-for-byte.
No migration SQL or schema was changed. Secret scans do not establish ownership or prove the
absence of every confidential detail; those boundaries also rely on the user's confirmation
and inspection of the fictional fixtures and source contents.
