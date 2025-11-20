# OpenPIIMap

**OpenPIIMap** is a global, open-source initiative that provides machine-readable definitions of **Personally Identifiable Information (PII)** and **Protected Health Information (PHI)** across countries, privacy frameworks, and industry verticals.

It helps privacy engineers, data scientists, and compliance teams understand and enforce what constitutes sensitive data under laws like **GDPR**, **HIPAA**, **CPRA**, and more.

---

## Why OpenPIIMap?

There is no publicly available, standardized, developer-friendly map of what qualifies as sensitive data across jurisdictions. OpenPIIMap solves that by offering:

- YAML/JSON definitions of PII and PHI covering **29 frameworks** across **59 countries**
- Legal citations, classifications, and regulatory context with authoritative URLs
- Rich metadata including subtypes, risk levels, masking techniques, and retention guidelines
- Extensible schema to support policy-as-code, data governance, anonymization, and risk analysis

---

## Coverage Index (All Frameworks)

See the full global coverage: [`coverage.json`](./data/coverage.json)

**29 Frameworks** spanning **59 countries** including:

- **GDPR** - All 30 EU/EEA countries (Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden)
- **US State Laws** - CPRA (California), VCDPA (Virginia), CPA (Colorado), CTDPA (Connecticut), UCPA (Utah), MCPA (Montana)
- **HIPAA** (United States), **UK GDPR** (United Kingdom)
- **LGPD** (Brazil), **LFPDPPP** (Mexico), **NDPR** (Nigeria), **POPIA** (South Africa)
- **PIPL** (China), **DPDPB** (India), **APPI** (Japan), **PIPA** (South Korea)
- **PDPA** (Singapore, Malaysia, Thailand, Argentina), **PIPEDA** (Canada)
- **Privacy Acts** (Australia, Bahamas, New Zealand), **PDP Law** (Indonesia), **FADP** (Switzerland), **UAE DPL** (United Arab Emirates)

---

## Recent Updates

**November 2025** - Major enhancements:
- ✅ **Complete GDPR coverage** - All 30 EU/EEA countries now included (added 14 new countries)
- ✅ **Expanded US coverage** - 5 new state privacy laws: Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Utah (UCPA), Montana (MCPA)
- ✅ **Enhanced metadata** - Risk levels, breach impact analysis, masking techniques, retention guidelines, and processing purposes
- ✅ **Comprehensive subtypes** - 81% coverage across all frameworks with 24 standardized subtypes
- ✅ **Standardized citations** - Consistent format with authoritative URLs documented
- ✅ **Framework naming** - Clarified PDPA variants with country-specific directories

See the full GDPR index: [`data/gdpr/country-index.json`](./data/gdpr/country-index.json)

---

## Project Structure

```
openpiimap/
├── data/                 # YAML definitions of PII/PHI by regulation and region
│   └── gdpr/             # GDPR country-specific YAMLs
├── api/                  # FastAPI-based API for programmatic access (WIP)
├── frontend/             # Static website for browsing definitions (WIP)
├── examples/             # Sample use cases and before/after anonymization
├── docs/                 # Format guides, contributor instructions
├── .github/              # Issue and PR templates
├── coverage.json         # Root-level summary (see data/coverage.json for latest)
├── README.md             # This file
├── LICENSE               # MIT License
└── .gitignore
```

---

## YAML Example: Enhanced Schema

```yaml
country: Germany
framework: GDPR
categories:
  - name: Email Address
    type: direct_identifier
    subtype: digital_contact
    required_masking: true
    risk_level: high
    citations:
      - regulation: GDPR
        article: 4(1)
        url: https://eur-lex.europa.eu/eli/reg/2016/679/oj
    masking_techniques:
      - method: hash
        algorithm: SHA-256
        suitability: production
    processing_purposes:
      allowed:
        - service_delivery
        - authentication
      legal_basis:
        - consent
        - contract
```

---

## Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/YOUR-ORG/openpiimap.git
   cd openpiimap
   ```

2. **Contribute a YAML file**

   - Fork the repo
   - Add a YAML file under `/data/[framework]/`
   - Submit a pull request

3. **Run the API locally (optional)**

   ```bash
   cd api
   pip install -r requirements.txt
   uvicorn app:app --reload
   ```

---

## Contributing

We welcome all contributors!

- Add new country definitions
- Improve legal citations or metadata
- Help build the web UI or API backend
- Translate definitions into other languages

See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) to get started.

---

## License

MIT License © 2025 [Intelation](https://www.intelation.com) Built for the global privacy community.

---

## Project Website

Coming soon at [https://www.openpiimap.org](https://www.openpiimap.org)
---

## Validation & Tools

Run core validation and generation commands:

```bash
python scripts/openpiimap.py validate              # Validate all YAML files
python scripts/openpiimap.py lint                  # Check field order and tags
python scripts/openpiimap.py format                # Reformat YAML files
python scripts/generate-coverage-json.py           # Update coverage.json
python scripts/generate-country-indexes.py         # Auto-generate country indexes
python scripts/validate-paths.py                   # Verify file path references
```

---

## GitHub Actions (CI)

All YAML files are continuously validated on GitHub via:

- Schema compliance checks
- Field order and tag linter
- coverage.json updates (optional)

GitHub Action file: `.github/workflows/validate.yml`

To enable:
1. Commit your scripts and workflow YAML
2. Push to GitHub
3. All PRs and pushes will trigger validation