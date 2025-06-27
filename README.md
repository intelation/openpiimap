# OpenPIIMap 🌍
> A global, open-source map of Personally Identifiable Information (PII) and Protected Health Information (PHI) definitions across jurisdictions and industries.

## What is OpenPIIMap?

OpenPIIMap is a free and open-source initiative to help developers, privacy engineers, and compliance teams understand what constitutes sensitive data — legally and operationally — across different countries and privacy frameworks.

Unlike detection libraries, this project provides **structured, machine-readable definitions** of PII/PHI with legal references and regional context.

---

## Why This Matters

- No universal reference for PII/PHI across global frameworks  
- Enables compliance-aware pipelines and anonymization  
- Powers privacy scoring, enforcement tools, and PET automation

---

## Structure

- `/data`: Definitions organized by regulation and country
- `/examples`: Sample use cases and test cases
- `/api`: Planned REST API interface (optional)
- `/ui`: (WIP) Visual dashboard and global PII map
- `/docs`: Format guides and contributor documentation

---

## Example: GDPR - Germany

```yaml
country: Germany
framework: GDPR
categories:
  - name: Name
    type: direct_identifier
    required_masking: true
    citations:
      - article: GDPR Article 4(1)
  - name: Health data
    type: special_category
    required_masking: true
    citations:
      - article: GDPR Article 9
