# 🌍 OpenPIIMap

**OpenPIIMap** is a global, open-source initiative that provides machine-readable definitions of Personally Identifiable Information (PII) and Protected Health Information (PHI) across countries, privacy frameworks, and industry verticals.

It helps privacy engineers, data scientists, and compliance teams understand and enforce what constitutes sensitive data under laws like **GDPR**, **HIPAA**, **CPRA**, and more.

---

## Why OpenPIIMap?

There is no publicly available, standardized, developer-friendly map of what qualifies as sensitive data across jurisdictions. OpenPIIMap solves that by offering:

- **YAML/JSON definitions** of PII and PHI for 100+ regions
- Legal **citations and classification** for each data type
- A planned **REST API** and **interactive UI**
- Extensible structure to support your data governance, anonymization, or policy automation workflows

---

## Project Structure

```

openpiimap/
├── data/                 # YAML definitions of PII/PHI by regulation and region
├── api/                  # FastAPI-based API for programmatic access (WIP)
├── ui/frontend/          # React UI for browsing definitions (WIP)
├── examples/             # Sample use cases and before/after anonymization
├── docs/                 # Format guides, contributor instructions
├── .github/              # Issue and PR templates
├── README.md             # This file
├── LICENSE               # MIT License
└── .gitignore

````

---

## Example: GDPR – Germany

```yaml
country: Germany
framework: GDPR
categories:
  - name: Full Name
    type: direct_identifier
    required_masking: true
    citations:
      - regulation: GDPR
        article: Article 4(1)
  - name: Health Data
    type: special_category
    required_masking: true
    citations:
      - regulation: GDPR
        article: Article 9
````

---

## Getting Started

1. **Clone the repo:**

   ```bash
   git clone https://github.com/YOUR-ORG/openpiimap.git
   cd openpiimap
   ```

2. **Contribute a PII definition:**

   * Fork the repo
   * Add a YAML file under `/data`
   * Submit a pull request

3. **Run the API locally (optional):**

   ```bash
   cd api
   pip install -r requirements.txt
   uvicorn app:app --reload
   ```

---

## Contributing

We welcome contributions! You can:

* Add new regions or frameworks (e.g., Canada, Brazil, ISO 27701)
* Improve existing definitions or legal citations
* Help build the API or UI

Check out [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) for details.

---

## License

MIT License © 2025 [Intelation](https://www.intelation.com)
Built for the global privacy community.

---

## 🔗 Project Website

👉 Coming soon at [https://openpiimap.org](https://openpiimap.org)
