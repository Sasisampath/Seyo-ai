# Seyo AI

Seyo AI is a WhatsApp-first, AI-assisted business operations product for Indian wholesalers,
distributors and small businesses. This repository contains the existing local web MVP:
**handwritten bill → extraction draft → merchant review → digital invoice → partial payments
→ customer commitments → cash-flow insights and a read-only merchant assistant.**

WhatsApp-first is the product direction. Today, the web application and demo inbox are the
usable default. Official inbound WhatsApp hooks exist, but have not been verified against an
account. Real WhatsApp outbound, outbound AI calls and live payment processing are not built.
This MVP is not production-ready.

## Run locally without API keys

Requires Python 3.11+ and Node 20.9+. Migration validation used Python 3.14.9 and Node 26.7.0.
Run commands from the indicated directories. Do not configure real customer data in demo mode.

```bash
# Terminal 1, from the repository root
cd services/api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.lock.txt
python -m app.seed  # applies Alembic migrations and seeds fictional demo data
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

```bash
# Terminal 2, from the repository root
cd apps/web
npm ci
npm run dev -- --hostname 127.0.0.1 --port 3000
```

Open <http://localhost:3000>; API health: <http://localhost:8000/v1/health>;
API documentation: <http://localhost:8000/docs>. Choose an owner, staff, view-only user, or
second merchant to explore permissions and tenant isolation. No environment file is required.
The backend's original `data/autopilot.db` filename and browser token key remain unchanged
for compatibility; they are internal identifiers, not product branding.

Optional: copy `.env.example` to `.env` at the repository root. The API loads that file from
`services/api`. Next.js uses its own `apps/web/.env.local` for an optional server-only `API_URL`
override; default is `http://localhost:8000`. See [personal integration setup](docs/INTEGRATIONS_AND_COMPLIANCE.md).
For PostgreSQL, use `infra/docker-compose.yml` and a local `DATABASE_URL`; the Compose
username/password are public demo defaults and must not be used for shared deployments.

## Preserved workflows

- Today dashboard: outstanding, received, promised, unverified claims, pickup availability and cash-flow comparisons.
- Photo/PDF upload, extraction review, deterministic recalculation and explicit invoice approval.
- Customer/invoice ledgers, partial payments, allocation and audit history.
- Raw-body signed webhooks, duplicate protection and out-of-order event handling.
- Manual unverified claims, owner confirmation, disputes and compensating reversal entries.
- Customer-stated promises with evidence and an editable date/method, separate from receipts.
- Demo inbox, signed inbound WhatsApp webhook and optional media retrieval adapter.
- Read-only text assistant, browser speech and optional ElevenLabs voice adapter.
- Owner/staff/view-only demo roles, two tenants, integration settings and demo reset.

Money remains integer INR paise. An LLM can propose a draft or select a read-only tool;
it cannot post verified balances. Provider-verified, merchant-confirmed, unverified,
simulated and promised amounts retain their existing distinctions.

## Five-minute demo

1. Today: ask “Who agreed to pay today?” and “How much did Murugan Stores pay?”.
2. Bills → Try a sample WhatsApp bill photo: fix the incorrect dal line total to ₹800,
   enter sugar quantity 1 and line total ₹2,100, and set subtotal/total to ₹5,300.
   Save, review the tax warning, acknowledge it, then approve.
3. Invoices → INV-0001: the ₹20,000 invoice has ₹5,000 and ₹10,000 receipts, leaving ₹5,000.
   Prepare and approve a ₹5,000 demo request; simulate paying and verify the allocation trail.
4. Promises: simulate “₹3,000 on Friday, ₹2,000 on Monday”; confirm the proposals.
   The promises do not change the balance.
5. Payments: try duplicate/forged webhooks, an unmatched payment, dispute, refund or screenshot claim.

Reset with Settings → Reset demo data or `python -m app.seed --reset` in `services/api`.
Reset deletes the entire database's business records, including both fictional tenants;
use only a dedicated demo database. It does not implement an upload-retention cleanup job.

## Validation

```bash
cd services/api
.venv/bin/python -m pytest -q
.venv/bin/python -m pip check
# From repository root
python3 scripts/check_migration.py
cd apps/web
npm run typecheck
npm run build
npm audit
```

The existing suite has 26 tests. Exact migration results and limits are in
[the migration report](docs/MIGRATION_REPORT.md), with manual steps in [the test plan](docs/TEST_PLAN.md).
`requirements.lock.txt` captures the tested core backend dependencies; the original flexible
`requirements.txt` remains available. Optional SDK dependencies are separate and unverified.

## Repository structure

| Path | Purpose |
| --- | --- |
| `apps/web/` | Existing Next.js, TypeScript and Tailwind frontend; `/api/*` proxy |
| `services/api/app/` | FastAPI routes, settings, demo auth, tenancy, models and seed |
| `services/api/domain/` | Deterministic ledger, reconciliation, review, reports and assistant |
| `services/api/adapters/` | Demo providers and optional Gemini/Razorpay/Meta/ElevenLabs adapters |
| `services/api/workers/` | Extraction and inbound media background work |
| `services/api/migrations/` | Original Alembic database structure |
| `services/api/tests/` | Original pytest suite, unchanged |
| `fixtures/` | Fictional sample bill and its generator |
| `docs/` | Architecture, product scope, integration setup, roadmap and migration evidence |
| `scripts/check_migration.py` | Verifies protected source files against the pinned snapshot |

## Limits and next milestone

Demo passwordless login is not production authentication. Uploads are unencrypted local files;
rate limiting, retention, durable job retries, production identity and PostgreSQL concurrency
validation remain work. Simulated extraction returns a fixed sample and does not read your
uploaded file. Browser speech depends on browser/device support and microphone permission.
Provider credentials must stay server-side. No real provider account was exercised during migration.

The next milestone is a personal sandbox validation of **merchant WhatsApp bill intake → Gemini
extraction → web review/approval**, with durable media retries and explicit integration status.
See [product scope](docs/PRODUCT_SPEC.md), [architecture](docs/ARCHITECTURE.md) and
[roadmap](docs/MVP_ROADMAP.md). Historical research notes are not current policy or API guarantees.

## Provenance and ownership

This is an authorized working-tree snapshot of the existing UPI Business Autopilot MVP, rebranded
as Seyo AI. The user explicitly confirmed reuse rights and absence of company-confidential
materials before import. No original Git history, remotes, credentials, branches or company
runtime configuration were imported. [Snapshot hashes](docs/SOURCE_SNAPSHOT.json) record the
76 original files. The sole Git destination is <https://github.com/Sasisampath/Seyo-ai>.
The original repository had no declared license. No new redistribution license is asserted
by this migration; third-party dependencies retain their own terms.
