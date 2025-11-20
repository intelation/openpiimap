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
- **Description:** A more granular classification within a type. Subtypes enable precise filtering and querying of PII categories.
- **Status:** Optional but **RECOMMENDED** (54-100% coverage as of Nov 2025)
- **Documentation:** See [Subtype Taxonomy](subtype-taxonomy.md) for complete list and usage guidelines

#### Standard Subtypes

**Identity:**
- `personal_name` - Full Name, First Name, Last Name
- `government_id` - Government-issued identification numbers

**Contact:**
- `digital_contact` - Email addresses, messaging handles
- `telecom_contact` - Phone, fax, mobile numbers
- `address` - Physical/postal addresses

**Technical:**
- `network_identifier` - IP addresses, MAC addresses
- `device_id` - Cookies, device fingerprints, session IDs

**Sensitive:**
- `biometric` - Fingerprints, facial recognition, iris scans
- `health` - Health information (general)
- `medical` - Medical records and clinical data (specific)
- `genetic` - DNA, genetic test results

**Financial:**
- `financial_identifier` - Credit cards, payment info (general)
- `bank_account` - Bank account numbers, routing numbers
- `insurance_id` - Insurance policy numbers
- `tax_identifier` - Tax identification numbers

**Contextual:**
- `employment` - Employee ID, job title, employment status
- `hr_data` - Performance reviews, personnel files
- `compensation` - Salary, benefits information
- `education` - Student records, grades, transcripts
- `geolocation` - GPS coordinates, location data

**Other:**
- `personal_attributes` - Date of birth, age, physical characteristics
- `vehicle_identifier` - License plates, VIN numbers
- `digital_identity` - Usernames, account IDs

**Usage Example:**
```yaml
- name: Email Address
  type: direct_identifier
  subtype: digital_contact
  required_masking: true
  
- name: Social Security Number
  type: national_identifier
  subtype: government_id
  required_masking: true
```

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

**For complete citation format documentation, see [Citation Standard](citation-standard.md).**

#### Each citation object contains:

##### `regulation`
- **Type:** `string`
- **Required:** ✅
- **Description:** Name of the law or regulation (e.g., `"GDPR"`, `"HIPAA"`, `"LGPD"`).

##### `article`
- **Type:** `string`
- **Optional**
- **Description:** Article number from the regulation (e.g., `"4(1)"`, `"9"`). Common in European and civil law jurisdictions.

##### `section`
- **Type:** `string`
- **Optional**
- **Description:** Section reference from the regulation (e.g., `"45 CFR §164.514(b)(2)(i)(A)"` for HIPAA). Common in US and common law jurisdictions.

##### `recital`
- **Type:** `string`
- **Optional**
- **Description:** Recital number from EU-style regulations (e.g., `"30"` for GDPR Recital 30 on online identifiers).

##### `principle`
- **Type:** `string`
- **Optional**
- **Description:** Privacy principle number for principle-based frameworks (e.g., Privacy Act 2020, PIPEDA).

##### `chapter`
- **Type:** `string`
- **Optional**
- **Description:** Chapter identifier from the regulation (used in some national laws).

##### `description`
- **Type:** `string`
- **Optional**
- **Description:** Human-readable explanation of the citation's relevance (recommended for complex citations).

##### `url`
- **Type:** `string` (valid URL)
- **Optional**
- **Description:** Link to official source of the regulation or guidance. **Highly recommended** - target 80%+ coverage.

##### `national_law`
- **Type:** `string`
- **Optional**
- **Description:** Name of national implementing legislation (primarily for GDPR countries with supplementary laws).

##### `authority`
- **Type:** `string`
- **Optional**
- **Description:** Data protection authority or regulatory body (when citing guidance or decisions).

##### `guideline`
- **Type:** `string`
- **Optional**
- **Description:** Title or identifier of regulatory guidance document.

##### `decision`
- **Type:** `string`
- **Optional**
- **Description:** Regulatory decision or ruling number.

---

### `notes` (optional)
- **Type:** `string`
- **Description:** Jurisdiction-specific implementation details or clarifications (e.g., national interpretations of GDPR).

---

### `tags` (optional)
- **Type:** `list of strings`
- **Description:** Helpful tags to classify the data element (e.g., `["health", "genetic", "identifier"]`).

---

### `category_tags` (optional)
- **Type:** `list of strings`
- **Description:** Enhanced taxonomy tags for grouping and filtering PII categories. Currently used by GDPR countries and Argentina (44.7% coverage as of Nov 2025).
- **Status:** Optional enhancement feature

#### Common Category Tags

| Tag | Description | Usage |
|-----|-------------|-------|
| `core` | Fundamental identifiers (name, email, phone) | 61 occurrences |
| `sensitive` | Special category data requiring heightened protection | 69 occurrences |
| `digital` | Online/technical identifiers (IP, cookies, device IDs) | 48 occurrences |
| `identity` | Identity-related data | 35 occurrences |
| `contact` | Contact information | 34 occurrences |
| `tracking` | Tracking and behavioral data | 31 occurrences |
| `health` | Health and medical information | 19 occurrences |
| `behavioral` | Behavioral and preference data | 18 occurrences |
| `employment` | Employment-related information | 18 occurrences |
| `biometric` | Biometric data | 17 occurrences |
| `financial` | Financial information | 6 occurrences total |
| `government` | Government-related data | 3 occurrences |
| `professional` | Professional information | 2 occurrences |
| Other | `education`, `location`, `network`, `social`, `technical`, `temporal`, `transport`, `assets` | 1 each |

#### Usage Notes

- **Optional Feature**: `category_tags` is not required and should be considered an enhancement
- **Current Coverage**: 
  - All 16 GDPR countries use `category_tags`
  - Argentina uses `category_tags`
  - 21 other frameworks do not currently use `category_tags`
- **Recommendation**: May be added to non-GDPR frameworks in Phase 3 of the enhancement plan
- **Benefits**: Enables advanced filtering, taxonomy-based analysis, and improved user experience

#### Example Usage

```yaml
- name: Full Name
  type: direct_identifier
  category_tags:
    - core
    - identity
    
- name: Health Data
  type: special_category
  category_tags:
    - sensitive
    - health
    
- name: IP Address
  type: indirect_identifier
  category_tags:
    - digital
    - behavioral
    - tracking
```

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