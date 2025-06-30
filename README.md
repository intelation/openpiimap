# 🌍 OpenPIIMap

**OpenPIIMap** is a global, open-source initiative that provides machine-readable definitions of **Personally Identifiable Information (PII)** and **Protected Health Information (PHI)** across countries, privacy frameworks, and industry verticals.

It helps privacy engineers, data scientists, and compliance teams understand and enforce what constitutes sensitive data under laws like **GDPR**, **HIPAA**, **CPRA**, and more.

---

## ✨ Why OpenPIIMap?

There is no publicly available, standardized, developer-friendly map of what qualifies as sensitive data across jurisdictions. OpenPIIMap solves that by offering:

- ✅ YAML/JSON definitions of PII and PHI for 100+ regions
- ✅ Legal citations, classifications, and regulatory context
- ✅ A planned REST API and interactive web UI
- ✅ Extensible schema to support policy-as-code, data governance, anonymization, and risk analysis

---

## 🧭 GDPR Coverage (Live)

We currently provide full YAML definitions for the following **EU and EEA** countries:

| Country          | File Path                              |
|------------------|------------------------------------------|
| Germany          | `data/gdpr/germany.yaml`                |
| France           | `data/gdpr/france.yaml`                 |
| Ireland          | `data/gdpr/ireland.yaml`                |
| Netherlands      | `data/gdpr/netherlands.yaml`            |
| Spain            | `data/gdpr/spain.yaml`                  |
| Italy            | `data/gdpr/italy.yaml`                  |
| Belgium          | `data/gdpr/belgium.yaml`                |
| Sweden           | `data/gdpr/sweden.yaml`                 |
| Austria          | `data/gdpr/austria.yaml`                |
| Denmark          | `data/gdpr/denmark.yaml`                |
| Finland          | `data/gdpr/finland.yaml`                |
| Poland           | `data/gdpr/poland.yaml`                 |
| Greece           | `data/gdpr/greece.yaml`                 |
| Norway           | `data/gdpr/norway.yaml`                 |
| Iceland          | `data/gdpr/iceland.yaml`                |
| Liechtenstein    | `data/gdpr/liechtenstein.yaml`          |

📁 See the full index: [`country-index.json`](./country-index.json)

---

## 🗂 Project Structure

```

openpiimap/
├── data/                 # YAML definitions of PII/PHI by regulation and region
│   └── gdpr/             # GDPR country-specific YAMLs
├── api/                  # FastAPI-based API for programmatic access (WIP)
├── ui/frontend/          # React UI for browsing definitions (WIP)
├── examples/             # Sample use cases and before/after anonymization
├── docs/                 # Format guides, contributor instructions
├── .github/              # Issue and PR templates
├── country-index.json    # Current list of completed jurisdictions
├── README.md             # This file
├── LICENSE               # MIT License
└── .gitignore

````

---

## 📘 YAML Example: GDPR – Germany

```yaml
country: Germany
framework: GDPR
categories:
  - name: Full Name
    type: direct_identifier
    required_masking: true
    citations:
      - regulation: GDPR
        article: 4(1)
  - name: Health Data
    type: special_category
    required_masking: true
    citations:
      - regulation: GDPR
        article: 9
````

---

## 🚀 Getting Started

1. **Clone the repo**

   ```bash
   git clone https://github.com/YOUR-ORG/openpiimap.git
   cd openpiimap
   ```

2. **Contribute a YAML file**

   * Fork the repo
   * Add a YAML file under `/data/gdpr/`
   * Submit a pull request

3. **Run the API locally (optional)**

   ```bash
   cd api
   pip install -r requirements.txt
   uvicorn app:app --reload
   ```

---

## 🤝 Contributing

We welcome all contributors!

* Add new country definitions
* Improve legal citations or metadata
* Help build the web UI or API backend
* Translate definitions into other languages

📄 See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) to get started.

---

## 📄 License

MIT License © 2025 [Intelation](https://www.intelation.com)
Built for the global privacy community.

---

## 🔗 Project Website

🌐 Coming soon at [https://www.openpiimap.org](https://www.openpiimap.org)

