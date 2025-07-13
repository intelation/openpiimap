# Contributing to OpenPIIMap

Thank you for your interest in contributing to **OpenPIIMap** — the open-source project that maps and defines Personally Identifiable Information (PII) and Protected Health Information (PHI) across global jurisdictions and privacy frameworks.

We welcome contributions from developers, privacy professionals, legal experts, and open data enthusiasts! 🚀

---

## What You Can Contribute

### YAML Definitions
- Add a new country or jurisdiction (e.g., `brazil.yaml`, `uae.yaml`)
- Improve existing files with better:
  - Legal citations
  - Tags (`health`, `finance`, etc.)
  - Data categories

### Documentation
- Clarify format specs or examples
- Add FAQs or tooling usage notes

### Tooling & Issues
- Improve scripts under `/scripts/`
- File or comment on issues (coverage, edge cases, YAML bugs)

---

## Folder Overview

```bash
/data/                → YAMLs by framework (e.g., gdpr/, hipaa/)
/scripts/             → Validation, lint, and coverage tools
/api/                 → WIP REST API
/frontend/            → Static website frontend
/docs/                → This file, schema specs, roadmap
.github/              → GitHub Actions, issue templates
````

---

## YAML Format Guidelines

> Use an existing country like `germany.yaml` as your template.

### Required fields:

* `country`, `framework`, `categories[]`
* Each category must include:

  * `name`, `type` (e.g., `direct_identifier`, `special_category`)
  * `required_masking` (true/false)
  * `citations[]` (article, law, or national regulation)

### Format Rules:

* YAML files must use **2-space indentation**
* **No tabs**, no trailing commas
* All tags should be present and non-empty (e.g., `tags: [biometric]`)

---

## Pre-Submission Checklist

Before submitting a pull request:

1. ✔ Follow proper file naming (`data/gdpr/finland.yaml`)
2. ✔ Include **at least 3–5 categories** with legal citations
3. ✔ Run the linter and validator:

   ```bash
   python scripts/lint-yamls.py
   python scripts/validate-yamls.py
   ```
4. Reformat your file:

   ```bash
   python scripts/reformat-yamls.py --path data/gdpr/yourfile.yaml
   ```
5. Check `git diff` for clean formatting and commit only your intended file(s)

---

## Submitting a Pull Request

1. Fork the repository
2. Create a new branch:

   ```bash
   git checkout -b add-greece-yaml
   ```
3. Add or modify YAML and test with scripts
4. Commit and push:

   ```bash
   git commit -m "Add GDPR PII definitions for Greece"
   git push origin add-greece-yaml
   ```
5. Open a Pull Request to `main`

> GitHub Actions will automatically run validation checks. Please fix any errors reported in the PR before requesting review.

---

## Need Help?

* Check [`good first issue`](https://github.com/YOUR-ORG/openpiimap/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
* Ask in GitHub Discussions (coming soon)
* Open an issue with the `question` label

---

## Suggest a Region or Framework

Want to add a new law or country?

> Open an issue titled:
> `"Request: Add support for [Country/Framework]"`

We’ll help you get started.

---

## Code of Conduct

All contributors must follow our [Code of Conduct](../CODE_OF_CONDUCT.md). Be respectful, inclusive, and constructive.

---

Thank you for helping build the world’s first open-source PII/PHI definition atlas!

```
