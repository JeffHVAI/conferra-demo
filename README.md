# CONFERRA Credential Demo

Front-end sandbox demo of **Project CONFERRA**, the Sovereign Academic Credential Engine built by Verisset Canada for the Global University Systems / University of Niagara Falls Canada (UNF) pilot. SkyeConnex provides the sovereignty and custody layer.

> **Sandbox only.** Every student record is fictional and SkyeConnex API responses are simulated in the browser. The SHA-256 fingerprints and Merkle inclusion proofs are computed for real with Web Crypto. Documents carry a "SPECIMEN · SANDBOX" watermark.

## What the demo shows

| Tab | Persona | PRD feature set |
| --- | --- | --- |
| 1 · Registrar console | Campus registrar | CSV / SIS HTML ingestion, batch issuance, pipeline log, 500-package capacity check |
| 2 · Sealing & custody | Backend (SkyeConnex) | Package contents, custody record JSON, RS(6,3) shard placement on Canadian nodes with a node-outage simulation, Merkle inclusion proof |
| 3 · Graduate wallet | Graduate | Apple / Google Wallet pass with live QR, ZIP evidence package, expiring read-only share links |
| 4 · Employer verification | Employer, licensing board, WES | Verify by link/code, simulated QR scan, or file drop (hashed locally, never uploaded); green / red / revoked / expired results; tamper lab |
| Audit & reconciliation | Registrar, finance | KPIs, revoke/reinstate, custody log, verification log, monthly $60 fee / $5 dividend report with CSV export, tenancy roles and scoped API keys, activity audit log |

It also covers the platform features in SkyeConnex's *CONFERRA on SkyeConnex* brief (16 Oct 2026): a Platform fit table (Exists / Partial / Build), REST API / S3 gateway / MCP ingestion channels, re-hash on receipt, worker-queue batches, shards dealt across Canadian vendors with a legal-order test, signed Merkle checkpoints (ML-DSA-87 + Ed25519, simulated) with an RFC 3161 anchor, the issuance record linked to its custody entry, a live self-hosted pass with native passes pending issuer approval, share links with expiry, view cap and password, a custody proof in the evidence ZIP, and an "Acting as" role switcher.

## Architecture (as demoed)

```
CONFERRA  = credential business logic   (ingestion, rendering, hashing, wallet, sharing, reporting)
SkyeConnex = sovereign trust infrastructure (encrypted storage, sharding, Merkle custody log, verification, CA residency)
```

The demo is a single static file, `index.html`. It has no build step, and its only external dependencies are Google Fonts and `qrcodejs` from cdnjs.

## Run locally

Open `index.html` in a browser, or serve the folder:

```bash
python -m http.server 8765
```

Then visit http://localhost:8765.

## Sample data

`samples/unf-graduating-class-fall-2026.csv` is a fictional 50-graduate Fall 2026 class laid out like a registrar's SIS export: 22 MSc Data Analytics, 16 MBA and 12 BBA graduates, with email, faculty, level, citizenship, honours, standing and course grades. Upload it in the Registrar console to issue a full batch. The demo ignores the extra columns. To regenerate it (the seed is fixed):

```bash
python scripts/generate_sample_cohort.py
```

## Deploy

`.github/workflows/static.yml` deploys the repository to GitHub Pages on every push to `main`. In the GitHub repo, set **Settings → Pages → Source** to **GitHub Actions**.

## Next steps toward the Phase 1 pilot

- Replace the simulated SkyeConnex calls with a connector service (store asset, retrieve asset, retrieve custody record).
- Real PDF rendering from approved institutional templates, plus `.pkpass` and Google Wallet object generation.
- Back end: .NET 8 or Node.js with PostgreSQL. Front end: React + Tailwind.

See `docs/` for the source PRD notes.
