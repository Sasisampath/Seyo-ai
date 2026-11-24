# Validation plan

Run the original 26 pytest tests from services/api using `.venv/bin/python -m pytest -q`.
They cover partial payments/closure, over-allocation, overpayment, duplicate and out-of-order
webhooks, signature tampering, currencies, unverified claims, disputes/refunds, RBAC and tenancy,
bill upload/review/approval, promise parsing, reports, read-only assistant, voice-tool auth,
outbound gates, signed WhatsApp fixtures and migration/model column parity. Preserve these tests.

From apps/web run `npm ci`, `npm run typecheck` and `npm run build`. The source has no frontend
unit-test suite; build success alone does not prove browser journeys. Run `npm audit`, a backend
dependency audit and a redacted staged-file secret scan. The migration report records exact results.

## Local journey checks (fictional demo only)

1. Seed a fresh dedicated database with `python -m app.seed`; verify migration revision 0001.
2. Start FastAPI and Next.js. Sign in as owner and verify Today totals and assistant evidence.
3. Bills: add the sample, confirm warning labels, fix dal to ₹800, sugar quantity 1/total ₹2,100,
   subtotal/total ₹5,300. Save, acknowledge the tax warning, approve, inspect the new invoice.
4. INV-0001: assert total 2,000,000 paise, prior allocations 500,000 and 1,000,000, due 500,000.
   Approve a demo request for 500,000; simulate capture and duplicate delivery. Due must be zero
   with one new positive allocation. Customer balance must agree. Simulate a refund and verify
   compensating entries restore the due amount without deleting history.
5. Confirm two proposed promises from “₹3,000 on Friday, ₹2,000 on Monday”; due stays unchanged.
6. Switch to viewer and second tenant; verify write restrictions and tenant isolation.
7. Check settings labels and reset; reset affects the whole fictional database and requires login again.

PostgreSQL locking/concurrency, actual provider credentials, browser microphone/speech recognition,
ElevenLabs audio and live Meta media require separate environment/account checks. Do not report them
as passed based on SQLite or fixture tests. Never use real customer data for migration validation.
