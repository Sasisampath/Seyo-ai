# Personal integration setup and current limits

Use only credentials from your personal vendor accounts. Keep them in an ignored repository-root
`.env` (or services/api/.env), or export them in the backend shell. Do not paste keys into the
frontend, Git, screenshots or logs. `.env.example` contains empty provider placeholders and a
public simulated-webhook value only. No credentials are needed for the default demo.

Optional SDKs: in services/api, activate .venv and run
`pip install -r requirements-integrations.txt`. These code paths have not been verified against
vendor accounts. Configured credentials do not prove that an integration is working. The existing
UI uses “live” for some configured adapters; read that as configuration status, not a validation result.

## Gemini

Set GEMINI_API_KEY and optionally GEMINI_MODEL. The existing default is gemini-2.5-flash;
choose a model available to your personal account after checking current official documentation.
The adapter uses google-genai for document extraction and optional tool selection. Uploaded bill
bytes are sent to Google when extraction is enabled. Use fictional bills for initial validation.
Extraction always yields a reviewable draft, never an invoice or balance mutation. Assistant
amounts are rendered by deterministic backend tools.

## ElevenLabs

Set ELEVENLABS_API_KEY and ELEVENLABS_AGENT_ID. The backend obtains a short-lived signed
conversation URL; the browser uses @elevenlabs/client. Configure the agent's server tools to call
POST /v1/voice-tools/customer-balance, /today-promises and /today-received on an HTTPS backend.
Send the x-voice-tool-secret header matching a strong VOICE_TOOL_SECRET. Set
VOICE_TOOL_MERCHANT_ID to the intended merchant (mer_demo_a for fictional demo data).
This shared-secret configuration is pinned to one merchant and is not multi-tenant production
authentication. Browser speech remains available where the Web Speech API is supported.
No outbound calls are implemented. Neither microphone capture nor live agent audio was verified
as part of automated tests.

## Razorpay test mode

Set RAZORPAY_KEY_ID (rzp_test_ prefix), RAZORPAY_KEY_SECRET and RAZORPAY_WEBHOOK_SECRET.
Do not use live keys. Use a dedicated personal test account and HTTPS webhook URL ending in
/v1/webhooks/razorpay. Signatures are checked against the exact request body and provider event ID.
The ledger also requires a MerchantProviderAccount mapping with provider=razorpay and account_id
matching the webhook account_id. There is no settings UI for provisioning that mapping: configure
it deliberately in the dedicated test database through SQLAlchemy/admin work, not by changing seed
fixtures or inventing an account ID. Owner approval creates one independent payment link per amount;
provider notifications/reminders are disabled. Validate whether the account's webhook payment entity
retains notes.payment_request_id. Without correlation the receipt is held unallocated. Never infer
settlement from a screenshot. Partial refunds require manual review. No live payment processing
or bank settlement integration has been verified.

## Meta WhatsApp inbound

Set WHATSAPP_APP_SECRET, WHATSAPP_VERIFY_TOKEN, WHATSAPP_ACCESS_TOKEN and optionally
WHATSAPP_GRAPH_VERSION. v21.0 is the inherited default; confirm an available version for your
personal Meta app before integration testing. Configure GET/POST /v1/webhooks/whatsapp on an
HTTPS test backend. The signature uses the Meta app secret. Create a MerchantProviderAccount
mapping with provider=whatsapp and account_id equal to the test phone_number_id. For merchant
bill intake, set the merchant User.phone to the inbound sender's number. Customer text is matched
against Customer.phone. These mappings are not provisioned by the demo settings UI.

Only image/document media from a matched merchant enters the bill extraction path. Audio intake
is not built. Media download uses FastAPI BackgroundTasks; durable retry/queue and encrypted storage
remain work. Signed text fixtures are tested; real Meta delivery and media download are unverified.
No WhatsApp send code exists. OUTBOUND_POLICY_APPROVED alone enables no sending; existing message
type, opt-in, opt-out and merchant-approval gates remain in place. Existing prohibited-message rules
remain unchanged. Review current vendor terms independently before any future outbound implementation;
the historical research file is not a current policy or legal assurance.

## Data and production boundaries

Demo login is passwordless and local-only in intended use. DEMO_MODE=false disables demo login
and simulator/reset routes but does not supply production auth. Uploads, raw webhook bodies,
assistant questions and consent evidence may contain personal data; the MVP lacks encryption,
retention controls, rate limiting and hardened logging. Use fictional data until these are addressed.
Never collect UPI PINs, OTPs or customer banking credentials. Keep the deterministic ledger as the
financial source of truth. See TEST_PLAN.md and MVP_ROADMAP.md for validation and remaining work.
