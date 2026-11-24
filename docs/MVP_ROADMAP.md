# Next implementation milestones

1. **Personal WhatsApp intake sandbox.** Map a personal Meta test phone and merchant sender;
   exercise signed image/document delivery with fictional bills, Gemini extraction, web review
   and invoice approval. Add durable retry/deduplication for media jobs and explicit tested status.
2. **Provider evidence.** Verify Razorpay test account correlation and refund/dispute fixtures;
   exercise ElevenLabs signed sessions and restricted read-only tools. Record results and
   pin compatible optional SDKs before claiming support.
3. **Security and reliability.** Add production identity/provisioning, PostgreSQL concurrency
   tests, encrypted object storage, upload limits/retention, rate limiting and backup/restore.
4. **Merchant workflow.** Add WhatsApp-first onboarding and voice-note review with visible
   correction. Keep invoices, money and customer-stated promises under deterministic approval rules.
5. **Permitted communications later.** Any future customer outbound capability needs provider
   approval, current-policy review, opt-in/opt-out, approved message types and merchant approval.
   Existing prohibited activity gates remain. No autonomous payments or outbound AI calls are
   included in this migration.
