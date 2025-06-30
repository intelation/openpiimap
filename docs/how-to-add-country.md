Here are two fully written documents for your `/docs` folder:

---

## `docs/how-to-add-country.md`

````markdown
# 🌍 How to Add a New Country to OpenPIIMap

This guide walks you through contributing a new YAML definition file for a country or jurisdiction under a privacy framework like **GDPR**, **PIPEDA**, **HIPAA**, or **CPRA**.

---

## Step-by-Step Instructions

### 1. Fork and Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/openpiimap.git
cd openpiimap
````

---

### 2. Create the YAML File

* Navigate to the correct framework folder inside `/data/` (e.g., `/data/gdpr/`, `/data/pipeda/`)
* Create a new file using the lowercase English country name:

  * Example: `data/gdpr/france.yaml`

Use the schema defined in [`docs/schema.md`](./schema.md).

---

### 3. Add Required Fields

Each YAML file must include the following top-level fields:

```yaml
country: France
framework: GDPR
categories:
  - name: Email Address
    type: direct_identifier
    required_masking: true
    citations:
      - regulation: GDPR
        article: 4(1)
```

Use real legal citations (articles/sections) from the relevant privacy law. Add `tags`, `notes`, and `subtype` if helpful.

---

### 4. Validate the File

Before committing, run local checks (or rely on GitHub Actions):

```bash
yamllint data/gdpr/france.yaml
# or use a schema validation tool like pykwalify or jsonschema
```

---

### 5. Update `country-index.json`

Find and edit the central index file:

```json
{
  "name": "France",
  "slug": "france",
  "path": "data/gdpr/france.yaml",
  "status": "complete"
}
```

---

### 6. Commit and Push

```bash
git add data/gdpr/france.yaml country-index.json
git commit -m "Add France YAML under GDPR"
git push origin your-branch-name
```

---

### 7. Open a Pull Request

On GitHub, open a PR with:

* Link to relevant laws
* Summary of included categories
* Mention if it's partial or complete

---

### Tips

* Read [`docs/schema.md`](./schema.md) for valid field values
* Use consistent naming, indentation (2 spaces), and order of fields
* Check existing files (e.g., `germany.yaml`) for examples

---

Thanks for contributing to OpenPIIMap! 🌐

````