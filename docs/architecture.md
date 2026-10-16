# CONFERRA on SkyeConnex: architecture notes

Source: *Product Requirements Document — Project CONFERRA / Sovereign Academic Credential Engine*, v1.0 (Lean Pilot Edition), Verisset Canada Inc.

## Flow

```
UNF Registrar
      │
      ▼
Credential Engine (CONFERRA / Verisset)
      ├── CSV / HTML ingestion
      ├── PDF rendering
      ├── Wallet pass generation
      └── SHA-256 hashing
      ▼
SkyeConnex APIs
      ├── Encrypted storage
      ├── Fragmentation / sharding (Canadian nodes only)
      ├── Audit metadata (Merkle custody log)
      ├── Share links
      └── Verification services
      ▼
Graduate ── Wallet pass · ZIP evidence package · secure link
      ▼
Employer ── Verification portal: QR scan · URL validation · file upload validation
```

## Phase 1 sandbox milestones

1. **Week 2:** HTML/CSV ingestion and automated PDF generation.
2. **Week 4:** SkyeConnex sealing, Merkle logging and storage sharding.
3. **Week 6:** End-to-end demo with registrar batch issue, wallet pass receipt and public dropzone verification.

## Non-functional requirements

- Canadian data residency only (protection from the US CLOUD Act).
- Fragmented, encrypted storage to stop AI scraping.
- Zero PII during the pilot, using 5 to 10 fictional student profiles.

## Demo status vs. production

| Area | Demo | Pilot target |
| --- | --- | --- |
| Hashing | Real SHA-256 (Web Crypto) | Same, done client-side before upload |
| Merkle log | Real tree built in the browser | SkyeConnex custody log |
| Storage / sharding | Simulated | SkyeConnex REST APIs on ThinkOn nodes |
| PDFs | HTML preview with canonical text | Rendered from approved SVG/HTML templates |
| Wallet | Visual mock + real QR | `.pkpass` + Google Wallet objects |
