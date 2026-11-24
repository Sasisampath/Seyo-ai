# Seyo AI: implemented product scope

Seyo AI assists Indian wholesalers, distributors and small businesses with reviewed billing,
partial-payment tracking, customer-stated commitments and evidence-backed cash-flow insights.

The local web MVP is implemented. The current flow is upload → reviewable extraction draft →
merchant corrections and approval → invoice → deterministic receipt allocation → reports.
Without credentials, extraction returns a fixed sample, payments are simulated signed events,
and customer messages stay in a local inbox. No real money moves.

| Area | Implemented | Limits |
| --- | --- | --- |
| Today | IST daily metrics, expected vs received, promises, pickups, mismatches | Recorded events only; no forecast model |
| Bills | PNG/JPEG/WebP/PDF intake, correction UI, duplicate warnings, approval | Demo extraction does not read input; local disk |
| Ledgers | Customers, invoices, lines, receipts, partial allocations, audit trail | No accounting export or tax-compliance certification |
| Payments | Demo events, HMAC, idempotency, manual claims, disputes, reversals | Razorpay test adapter unverified; partial refunds flagged |
| Promises | Parse proposals, explicit confirmation, evidence, edit status/date/method | No automatic posting to receipts |
| Inbox | Demo inbound/outbound, opt-in and approval gates, signed Meta inbound hook | Live outbound and AI calling absent |
| Assistant | Read-only ledger tools, evidence, rule routing, optional Gemini selection | Not Google ADK; no general autonomous actions |
| Voice | Browser speech UI and optional ElevenLabs agent session/tools | Browser support varies; no account validation |
| Roles | Demo owner/staff/viewer and two isolated tenants | No production login or account provisioning |

Current schema, endpoints, frontend journeys and tests are inherited from the authorized snapshot.
The migration preserves all original API paths and database tables. The schema's source of truth
is services/api/app/models.py and the initial Alembic migration. Planned WhatsApp-first onboarding,
voice-note intake, secure storage and production identity are outside the current MVP.
