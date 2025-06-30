# 🧾 OpenPIIMap YAML Schema Reference

This document defines the schema used in all `*.yaml` files under the `/data/` folder in OpenPIIMap. It ensures consistency, legal clarity, and machine-readability for privacy frameworks such as **GDPR**, **HIPAA**, **CPRA**, and others.

---

## 🗺️ Top-Level Fields

### `country`
- **Type:** `string`
- **Required:** ✅
- **Description:** The official name of the country (e.g., `"Germany"`).

---

### `framework`
- **Type:** `string`
- **Required:** ✅
- **Description:** The governing privacy law or framework (e.g., `"GDPR"`, `"HIPAA"`).

---

### `categories`
- **Type:** `list of objects`
- **Required:** ✅
- **Description:** Each object in the list defines a specific PII or PHI element regulated under the law.

---

## 📦 Category Object Fields

Each item in the `categories` array contains the following fields:

### `name`
- **Type:** `string`
- **Required:** ✅
- **Description:** The common name of the data element (e.g., `"Full Name"`, `"Email Address"`).

---

### `type`
- **Type:** `enum`
- **Required:** ✅
- **Accepted Values:**
  - `direct_identifier` — Uniquely identifies an individual (e.g., passport number)
  - `indirect_identifier` — May identify an individual when combined (e.g., birthdate, ZIP code)
  - `special_category` — Sensitive categories defined by law (e.g., health, biometric, race)
  - `pseudonymized_data` — Reversible transformation of identifiers
  - `anonymized_data` — Irreversible; not considered personal data under some laws

---

### `subtype` (optional)
- **Type:** `string`
- **Description:** A more granular classification within a type (e.g., `"biometric"`, `"financial"`).

---

### `required_masking`
- **Type:** `boolean`
- **Required:** ✅
- **Description:** Indicates whether the data element must be masked, anonymized, or redacted under typical compliance scenarios.

---

### `citations`
- **Type:** `list of objects`
- **Required:** ✅
- **Description:** Legal references that justify inclusion of this data element.

#### Each citation object contains:

##### `regulation`
- **Type:** `string`
- **Required:** ✅
- **Description:** Name of the law or regulation (e.g., `"GDPR"`).

##### `article`
- **Type:** `string`
- **Required:** ✅
- **Description:** Article, section, or clause of the regulation (e.g., `"4(1)"`, `"9"`).

##### `text` (optional)
- **Type:** `string`
- **Description:** Excerpt or paraphrased explanation from the law (for clarity).

---

### `notes` (optional)
- **Type:** `string`
- **Description:** Jurisdiction-specific implementation details or clarifications (e.g., national interpretations of GDPR).

---

### `tags` (optional)
- **Type:** `list of strings`
- **Description:** Helpful tags to classify the data element (e.g., `["health", "genetic", "identifier"]`).

---

## ✅ Example

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
    tags: ["health", "sensitive"]