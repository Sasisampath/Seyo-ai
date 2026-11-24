# Seyo AI project instructions

Preserve the existing Next.js frontend, FastAPI routes and deterministic ledger. Seyo AI is
an Indian merchant business-operations MVP; WhatsApp-first remains a direction with only
inbound integration hooks and a demo inbox currently implemented.

Before changes, read README.md, SKILL.md, docs/PRODUCT_SPEC.md and docs/ARCHITECTURE.md.
For providers, media or credentials read docs/INTEGRATIONS_AND_COMPLIANCE.md. For completion
criteria read docs/TEST_PLAN.md. Follow apps/web/AGENTS.md and the installed Next.js guides
in apps/web/node_modules/next/dist/docs/ before editing frontend code.

## Commands and working directories

- API: services/api; Python 3.11+; create .venv, install requirements.lock.txt.
- Apply migrations and seed: .venv/bin/python -m app.seed. Reset is destructive to the whole demo DB.
- API server: .venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000.
- API checks: .venv/bin/python -m pytest -q; .venv/bin/python -m pip check.
- Web: apps/web; Node 20.9+; npm ci; npm run typecheck; npm run build; npm run dev.
- Proxy: /api/* to API_URL (default http://localhost:8000); secrets never use NEXT_PUBLIC_ variables.
- From root: python3 scripts/check_migration.py verifies migration preservation hashes.
  Future intended feature changes may require updating the documented preservation policy.

## Invariants

- All financial amounts are integer INR paise; use Decimal for quantity multiplication.
- Due is invoice total minus net immutable allocation entries. Reverse via compensating entries.
- Promises and manual claims never count as verified receipts. LLMs cannot post to the ledger.
- Extraction creates a draft; merchant review and approval create an invoice.
- Keep tenant ownership checks, RBAC, signature verification, idempotency and audit evidence.
- Keep original tests and add meaningful coverage for future changes to financial rules.
- Demo mode must work without keys. Label simulations. Do not claim unverified provider success.
- No real WhatsApp send or outbound AI calling exists; do not imply flags alone enable them.

## Source and Git boundaries

Only push destination: https://github.com/Sasisampath/Seyo-ai.git. Never modify or push to the
original source. Do not import source Git history or configuration. Use normal non-force pushes.
The user requested test and secret-scan results before pushing; report them first.
Never commit real .env files, credentials, customer uploads, databases, caches, environments
or build output. Verify staged paths and run a redacted secret scan before committing.
Use the personal Sasisampath Git identity. Do not invent licenses or production-readiness claims.
