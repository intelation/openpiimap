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
  - `direct_identifier` — Uniquely identifies an individual on its own (e.g., full name, email address, passport number, social security number)
  - `indirect_identifier` — May identify an individual when combined with other data (e.g., birthdate, ZIP code, gender). Also known as `quasi_identifier` in some frameworks
  - `quasi_identifier` — Alternative term for `indirect_identifier` used in HIPAA and some other frameworks. May identify an individual when combined with other data
  - `special_category` — Sensitive categories requiring heightened protection under law (e.g., health data, biometric data, genetic data, racial or ethnic origin, religious beliefs, sexual orientation)
  - `national_identifier` — Government-issued identification numbers specific to a country (e.g., Social Security Number in US, National Insurance Number in UK, CPF in Brazil, Aadhaar in India)
  - `financial_identifier` — Financial account or transaction information (e.g., bank account numbers, credit card numbers, IBAN, payment history)
  - `contextual_identifier` — Data that becomes PII in specific contexts such as employment or education (e.g., employee ID, salary information, performance reviews, student ID, grades)
  - `behavioral` — Information about actions, preferences, or patterns of behavior (e.g., browsing history, location data, purchase history, search queries, app usage patterns)
  - `meta` — Metadata about data processing, compliance, or governance (e.g., consent records, processing purposes, retention periods, data lineage)
  - `pseudonymized_data` — Reversible transformation of identifiers (reserved for future use)
  - `anonymized_data` — Irreversible transformation; not considered personal data under some laws (reserved for future use)

**Note:** The terms `indirect_identifier` and `quasi_identifier` are used interchangeably across different frameworks. GDPR countries typically use `indirect_identifier`, while HIPAA and CPRA use `quasi_identifier`. Both refer to the same concept.

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

## 📋 Type Taxonomy Decision

### `indirect_identifier` vs `quasi_identifier`

**Status:** Both terms are **officially accepted** and considered equivalent.

**Rationale:**
- Different privacy frameworks use different terminology for the same concept
- GDPR countries typically use `indirect_identifier`
- HIPAA, CPRA, and many Asian frameworks use `quasi_identifier`
- Both refer to data that may identify an individual when combined with other information

**Implementation:**
- Both terms are valid in the schema
- Use `indirect_identifier` for GDPR-based frameworks
- Use `quasi_identifier` for HIPAA, CPRA, and other non-GDPR frameworks
- Validation and querying tools treat both as equivalent
- No migration required; maintaining framework-specific conventions

**Current Usage:**
- `indirect_identifier`: 34 occurrences (primarily GDPR countries)
- `quasi_identifier`: 51 occurrences (HIPAA, CPRA, and other frameworks)

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