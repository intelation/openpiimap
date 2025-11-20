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

### `risk_level` (optional)
- **Type:** `enum`
- **Accepted Values:** `critical`, `high`, `medium`, `low`
- **Description:** Indicates the risk level associated with exposure or breach of this data element. Used for risk assessment and prioritization.
- **Status:** Optional enhancement feature (Phase 4)

#### Risk Level Definitions

| Level | Description | Examples |
|-------|-------------|----------|
| `critical` | Highest risk; direct identity theft or severe harm possible | SSN, Passport Number, National ID, Financial Account Numbers |
| `high` | Significant risk; serious harm or fraud possible | Health Data, Biometric Data, Genetic Data, Credit Card Numbers |
| `medium` | Moderate risk; harm possible when combined with other data | Phone Number, Email Address, IP Address, Date of Birth |
| `low` | Lower risk; minimal harm in isolation | ZIP Code, Gender, Job Title, General Demographic Data |

---

### `breach_impact` (optional)
- **Type:** `list of strings`
- **Description:** Potential consequences or harms that could result from unauthorized disclosure, loss, or breach of this data element.
- **Status:** Optional enhancement feature (Phase 4)

#### Common Breach Impact Categories

- `identity_theft` - Can be used to steal or impersonate identity
- `financial_fraud` - Can lead to unauthorized financial transactions
- `account_takeover` - Can be used to gain unauthorized access to accounts
- `discrimination` - Can lead to unfair treatment or bias
- `reputational_harm` - Can damage personal or professional reputation
- `physical_harm` - Can lead to physical safety risks (e.g., stalking, harassment)
- `emotional_distress` - Can cause psychological harm or distress
- `privacy_violation` - Intrusive disclosure of personal information
- `regulatory_penalties` - Non-compliance leading to fines or sanctions
- `medical_fraud` - Misuse of health information for fraud
- `insurance_discrimination` - Unfair insurance decisions based on health/genetic data

---

### `gdpr_penalty_tier` (optional)
- **Type:** `enum`
- **Accepted Values:** `high`, `medium`, `low`
- **Description:** Indicates the potential penalty tier under GDPR for violations related to this data category. Relevant for GDPR-regulated jurisdictions.
- **Status:** Optional enhancement feature (Phase 4)

#### GDPR Penalty Tiers

| Tier | Maximum Fine | Violation Types | Examples |
|------|-------------|-----------------|----------|
| `high` | Up to €20M or 4% of annual global turnover | Article 9 violations (special category data), consent violations, data transfer violations | Health Data, Biometric Data, Genetic Data, Racial/Ethnic Origin |
| `medium` | Up to €10M or 2% of annual global turnover | Other GDPR principle violations, security violations | General PII processing violations, inadequate security measures |
| `low` | Administrative measures or warnings | Minor violations, first-time offenders with corrective action | Technical compliance issues, documentation gaps |

**Note:** Actual penalties depend on multiple factors including intent, severity, prior violations, and cooperation with authorities.

---

### `masking_techniques` (optional)
- **Type:** `list of objects`
- **Description:** Recommended techniques for anonymizing, pseudonymizing, or masking this data element. Provides practical guidance for data protection implementation.
- **Status:** Optional enhancement feature (Phase 4)

#### Each masking technique object contains:

##### `method`
- **Type:** `enum`
- **Required:** ✅
- **Accepted Values:**
  - `hash` - One-way cryptographic hashing
  - `encryption` - Reversible encryption with key management
  - `pseudonymization` - Replacing identifiers with pseudonyms
  - `tokenization` - Replacing sensitive data with non-sensitive tokens
  - `partial_mask` - Partially obscuring data (e.g., `***-**-1234`)
  - `generalization` - Reducing precision (e.g., age ranges instead of exact age)
  - `suppression` - Complete removal of data
  - `noise_addition` - Adding statistical noise to numerical data
  - `aggregation` - Combining individual records into aggregates

##### `algorithm` (optional)
- **Type:** `string`
- **Description:** Specific algorithm or technique used (e.g., `"SHA-256"`, `"AES-256"`, `"k-anonymity"`).

##### `suitability`
- **Type:** `enum`
- **Required:** ✅
- **Accepted Values:**
  - `production` - Suitable for production data storage and processing
  - `analytics` - Suitable for analytical and research purposes
  - `testing` - Suitable for testing and development environments
  - `display` - Suitable for displaying to end users or in logs
  - `archival` - Suitable for long-term archival storage
  - `sharing` - Suitable for sharing with third parties

##### `reversible` (optional)
- **Type:** `boolean`
- **Description:** Whether the masking can be reversed to recover original data.

##### `notes` (optional)
- **Type:** `string`
- **Description:** Additional implementation notes or considerations.

#### Example Usage

```yaml
- name: Email Address
  type: direct_identifier
  masking_techniques:
    - method: hash
      algorithm: SHA-256
      suitability: production
      reversible: false
    - method: pseudonymization
      algorithm: tokenization
      suitability: analytics
      reversible: true
      notes: Maintain token mapping in secure vault
    - method: partial_mask
      algorithm: "us***@example.com"
      suitability: display
      reversible: false
```

---

### `retention` (optional)
- **Type:** `object`
- **Description:** Guidelines for data retention and deletion of this data element. Helps implement data lifecycle management and comply with regulatory requirements.
- **Status:** Optional enhancement feature (Phase 4)

#### Retention Object Fields

##### `legal_minimum`
- **Type:** `string`
- **Description:** Minimum retention period required by law (e.g., `"5 years"`, `"7 years"`, `"until consent withdrawn"`).

##### `recommended`
- **Type:** `string`
- **Description:** Recommended retention period that balances legal requirements with privacy principles (e.g., `"7 years"`, `"3 years after account closure"`).

##### `maximum` (optional)
- **Type:** `string`
- **Description:** Maximum retention period allowed under data minimization principles.

##### `basis`
- **Type:** `string`
- **Description:** Legal or business basis for the retention period (e.g., `"Tax law + GDPR Article 17"`, `"SOX compliance"`, `"Statute of limitations"`).

##### `deletion_trigger`
- **Type:** `list of strings`
- **Description:** Events or conditions that trigger data deletion (e.g., `"account_closure"`, `"consent_withdrawal"`, `"contract_termination"`).

##### `exceptions` (optional)
- **Type:** `list of strings`
- **Description:** Circumstances where normal retention rules don't apply (e.g., `"ongoing legal proceedings"`, `"regulatory investigation"`, `"fraud prevention"`).

##### `archival_allowed` (optional)
- **Type:** `boolean`
- **Description:** Whether data can be moved to archival storage with restricted access instead of deletion.

##### `notes` (optional)
- **Type:** `string`
- **Description:** Additional implementation guidance or jurisdiction-specific requirements.

#### Example Usage

```yaml
- name: Financial Transaction Data
  type: special_category
  retention:
    legal_minimum: "5 years"
    recommended: "7 years"
    maximum: "10 years"
    basis: "Tax law (IRC Section 6001) + GDPR Article 17"
    deletion_trigger:
      - "account_closure + 7 years"
      - "consent_withdrawal (unless legal obligation applies)"
    exceptions:
      - "ongoing audit or legal proceedings"
      - "fraud investigation"
    archival_allowed: true
    notes: "Financial institutions may have extended retention requirements under AML regulations"
```

---

### `processing_purposes` (optional)
- **Type:** `object`
- **Description:** Defines the lawful purposes for which this data element can be processed, including allowed, restricted, and prohibited uses. Helps enforce purpose limitation principle (GDPR Article 5(1)(b)) and supports consent management and compliance automation.
- **Status:** Optional enhancement feature (Phase 4)

#### Processing Purposes Object Fields

##### `allowed`
- **Type:** `list of strings`
- **Description:** Processing purposes that are permitted under the applicable legal framework, either with explicit consent, under legitimate interest, or by legal obligation.

**Common Allowed Purposes:**
- `service_delivery` - Providing the core service or product to the user
- `account_management` - Managing user accounts and authentication
- `authentication` - Verifying user identity and access control
- `communication` - Sending transactional or service-related communications
- `password_reset` - Account recovery and security features
- `billing` - Payment processing and invoicing
- `fraud_prevention` - Detecting and preventing fraudulent activity
- `security` - Protecting systems and data security
- `legal_compliance` - Meeting legal and regulatory obligations
- `contract_fulfillment` - Performing contractual obligations
- `customer_support` - Providing customer service and support
- `analytics_with_consent` - Data analysis with explicit user consent
- `marketing_with_consent` - Marketing communications with explicit consent
- `research_with_consent` - Research purposes with explicit consent
- `personalization_with_consent` - Personalizing user experience with consent

##### `restricted`
- **Type:** `list of strings`
- **Description:** Processing purposes that require additional safeguards, explicit consent, or specific legal basis. May be subject to heightened scrutiny or regulatory oversight.

**Common Restricted Purposes:**
- `profiling_without_consent` - Creating user profiles without explicit consent
- `automated_decision_making` - Automated decisions significantly affecting individuals (GDPR Article 22)
- `sensitive_inference` - Inferring sensitive attributes from non-sensitive data
- `behavioral_advertising` - Targeted advertising based on behavior tracking
- `cross_context_tracking` - Tracking across websites or services
- `third_party_sharing` - Sharing data with third parties (requires disclosure)
- `data_enrichment` - Combining with external data sources
- `predictive_analytics` - Predicting future behavior or characteristics
- `ai_training` - Using data to train artificial intelligence models
- `location_tracking` - Continuous or frequent location monitoring
- `biometric_processing` - Processing biometric data for identification
- `secondary_use` - Using data for purposes beyond original collection

##### `prohibited`
- **Type:** `list of strings`
- **Description:** Processing purposes that are explicitly forbidden under the applicable legal framework, regardless of consent or other legal basis.

**Common Prohibited Purposes:**
- `sale_without_consent` - Selling personal data without explicit consent
- `third_party_sale_without_consent` - Selling data to third parties without consent
- `discrimination` - Using data to discriminate or cause harm
- `surveillance` - Unauthorized surveillance or monitoring
- `manipulation` - Manipulating vulnerable individuals or children
- `credit_scoring_protected_classes` - Using protected characteristics for credit decisions
- `employment_discrimination` - Using data for discriminatory hiring practices
- `insurance_discrimination` - Denying coverage based on health/genetic data
- `law_enforcement_without_warrant` - Sharing with law enforcement without legal process
- `unauthorized_access` - Any access not authorized by law or consent
- `data_breach_negligence` - Inadequate security measures
- `deceptive_collection` - Collecting data through deception or misrepresentation

##### `legal_basis` (optional)
- **Type:** `list of strings`
- **Description:** Legal justifications under which processing is permitted (particularly relevant for GDPR).

**GDPR Legal Bases:**
- `consent` - GDPR Article 6(1)(a) - Explicit consent from data subject
- `contract` - GDPR Article 6(1)(b) - Necessary for contract performance
- `legal_obligation` - GDPR Article 6(1)(c) - Required by law
- `vital_interests` - GDPR Article 6(1)(d) - Protecting life or physical safety
- `public_interest` - GDPR Article 6(1)(e) - Public interest or official authority
- `legitimate_interest` - GDPR Article 6(1)(f) - Legitimate interests of controller

##### `consent_required` (optional)
- **Type:** `boolean`
- **Description:** Whether explicit consent is required for any processing of this data element.

##### `opt_out_available` (optional)
- **Type:** `boolean`
- **Description:** Whether users can opt out of certain processing purposes while still using the service.

##### `notes` (optional)
- **Type:** `string`
- **Description:** Additional context or jurisdiction-specific guidance on processing purposes.

#### Example Usage

```yaml
- name: Email Address
  type: direct_identifier
  subtype: digital_contact
  required_masking: true
  processing_purposes:
    allowed:
      - service_delivery
      - authentication
      - password_reset
      - account_management
      - communication
      - customer_support
      - fraud_prevention
      - marketing_with_consent
    restricted:
      - third_party_sharing
      - profiling_without_consent
      - automated_decision_making
      - behavioral_advertising
    prohibited:
      - sale_without_consent
      - third_party_sale_without_consent
      - surveillance
      - discrimination
    legal_basis:
      - consent
      - contract
      - legitimate_interest
    consent_required: false
    opt_out_available: true
    notes: "Marketing communications require explicit opt-in consent under GDPR. Transactional emails are permitted under contract basis."
  citations:
    - regulation: GDPR
      article: 5(1)(b)
      description: Purpose limitation principle
      url: https://gdpr-info.eu/art-5-gdpr/

- name: Health Data
  type: special_category
  subtype: health
  required_masking: true
  processing_purposes:
    allowed:
      - service_delivery
      - medical_treatment
      - health_monitoring
      - emergency_care
      - legal_compliance
      - research_with_consent
    restricted:
      - insurance_underwriting
      - employment_screening
      - third_party_sharing
      - ai_training
      - predictive_analytics
    prohibited:
      - sale_without_consent
      - discrimination
      - insurance_discrimination
      - employment_discrimination
      - unauthorized_access
      - public_disclosure
    legal_basis:
      - explicit_consent
      - vital_interests
      - medical_treatment
      - public_health
    consent_required: true
    opt_out_available: false
    notes: "GDPR Article 9 requires explicit consent for health data processing. Medical treatment and public health may proceed under other legal bases."
  citations:
    - regulation: GDPR
      article: 9
      description: Processing of special categories of personal data
      url: https://gdpr-info.eu/art-9-gdpr/

- name: Location Data
  type: behavioral
  subtype: geolocation
  required_masking: true
  processing_purposes:
    allowed:
      - service_delivery
      - navigation
      - location_based_services
      - emergency_services
      - fraud_prevention_with_consent
    restricted:
      - behavioral_advertising
      - cross_context_tracking
      - third_party_sharing
      - location_tracking
      - data_enrichment
    prohibited:
      - surveillance
      - sale_without_consent
      - stalking
      - unauthorized_tracking
    legal_basis:
      - consent
      - legitimate_interest
    consent_required: true
    opt_out_available: true
    notes: "Continuous location tracking requires explicit consent. One-time location requests may proceed under legitimate interest for service delivery."
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

## ✅ Example (Basic)

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
 
 
 
 - - - 
 
 
 
 # #   � x �   E x a m p l e   ( W i t h   A d v a n c e d   F e a t u r e s   -   P h a s e   4 ) 
 
 
 
 ` ` ` y a m l 
 
 c o u n t r y :   U n i t e d   S t a t e s 
 
 f r a m e w o r k :   H I P A A 
 
 c a t e g o r i e s : 
 
     -   n a m e :   S o c i a l   S e c u r i t y   N u m b e r 
 
         t y p e :   n a t i o n a l _ i d e n t i f i e r 
 
         s u b t y p e :   g o v e r n m e n t _ i d 
 
         r e q u i r e d _ m a s k i n g :   t r u e 
 
         r i s k _ l e v e l :   c r i t i c a l 
 
         b r e a c h _ i m p a c t : 
 
             -   i d e n t i t y _ t h e f t 
 
             -   f i n a n c i a l _ f r a u d 
 
             -   a c c o u n t _ t a k e o v e r 
 
         m a s k i n g _ t e c h n i q u e s : 
 
             -   m e t h o d :   h a s h 
 
                 a l g o r i t h m :   S H A - 2 5 6 
 
                 s u i t a b i l i t y :   p r o d u c t i o n 
 
                 r e v e r s i b l e :   f a l s e 
 
                 n o t e s :   O n e - w a y   h a s h   f o r   v e r i f i c a t i o n   p u r p o s e s   o n l y 
 
             -   m e t h o d :   e n c r y p t i o n 
 
                 a l g o r i t h m :   A E S - 2 5 6 
 
                 s u i t a b i l i t y :   a r c h i v a l 
 
                 r e v e r s i b l e :   t r u e 
 
                 n o t e s :   U s e   H S M - b a c k e d   k e y   m a n a g e m e n t 
 
             -   m e t h o d :   p a r t i a l _ m a s k 
 
                 a l g o r i t h m :   " * * * - * * - 1 2 3 4 " 
 
                 s u i t a b i l i t y :   d i s p l a y 
 
                 r e v e r s i b l e :   f a l s e 
 
         r e t e n t i o n : 
 
             l e g a l _ m i n i m u m :   " 7   y e a r s " 
 
             r e c o m m e n d e d :   " 7   y e a r s   a f t e r   l a s t   s e r v i c e   d a t e " 
 
             b a s i s :   " H I P A A   r e t e n t i o n   r e q u i r e m e n t s   +   I R S   r e g u l a t i o n s " 
 
             d e l e t i o n _ t r i g g e r : 
 
                 -   " p a t i e n t _ d e a t h   +   7   y e a r s " 
 
                 -   " a c c o u n t _ c l o s u r e   +   7   y e a r s " 
 
             e x c e p t i o n s : 
 
                 -   " o n g o i n g   l i t i g a t i o n   o r   a u d i t " 
 
                 -   " m i n o r   r e c o r d s   ( r e t a i n   u n t i l   a g e   2 5 ) " 
 
             a r c h i v a l _ a l l o w e d :   t r u e 
 
         c i t a t i o n s : 
 
             -   r e g u l a t i o n :   H I P A A 
 
                 s e c t i o n :   4 5   C F R   � � 1 6 4 . 5 1 4 ( b ) ( 2 ) ( i ) ( A ) 
 
                 u r l :   h t t p s : / / w w w . e c f r . g o v / c u r r e n t / t i t l e - 4 5 / s u b t i t l e - A / s u b c h a p t e r - C / p a r t - 1 6 4 
 
         t a g s :   [ " i d e n t i f i e r " ,   " n a t i o n a l _ i d " ,   " s e n s i t i v e " ] 
 
         
 
     -   n a m e :   M e d i c a l   R e c o r d   N u m b e r 
 
         t y p e :   d i r e c t _ i d e n t i f i e r 
 
         s u b t y p e :   m e d i c a l 
 
         r e q u i r e d _ m a s k i n g :   t r u e 
 
         r i s k _ l e v e l :   h i g h 
 
         b r e a c h _ i m p a c t : 
 
             -   m e d i c a l _ f r a u d 
 
             -   p r i v a c y _ v i o l a t i o n 
 
             -   i d e n t i t y _ t h e f t 
 
         g d p r _ p e n a l t y _ t i e r :   h i g h 
 
         m a s k i n g _ t e c h n i q u e s : 
 
             -   m e t h o d :   p s e u d o n y m i z a t i o n 
 
                 a l g o r i t h m :   t o k e n i z a t i o n 
 
                 s u i t a b i l i t y :   a n a l y t i c s 
 
                 r e v e r s i b l e :   t r u e 
 
                 n o t e s :   M a i n t a i n   s e c u r e   t o k e n   v a u l t   w i t h   a c c e s s   c o n t r o l s 
 
             -   m e t h o d :   p a r t i a l _ m a s k 
 
                 a l g o r i t h m :   " M R N - * * * - 4 5 6 " 
 
                 s u i t a b i l i t y :   d i s p l a y 
 
                 r e v e r s i b l e :   f a l s e 
 
         r e t e n t i o n : 
 
             l e g a l _ m i n i m u m :   " 6   y e a r s " 
 
             r e c o m m e n d e d :   " 1 0   y e a r s " 
 
             m a x i m u m :   " 5 0   y e a r s " 
 
             b a s i s :   " H I P A A   � �   1 6 4 . 3 1 6 ( b ) ( 2 )   +   s t a t e   m e d i c a l   r e c o r d s   l a w s " 
 
             d e l e t i o n _ t r i g g e r : 
 
                 -   " p a t i e n t _ r e q u e s t   ( R i g h t   t o   E r a s u r e ) " 
 
                 -   " e n d _ o f _ r e t e n t i o n _ p e r i o d " 
 
             e x c e p t i o n s : 
 
                 -   " p u b l i c   h e a l t h   r e p o r t i n g   r e q u i r e m e n t s " 
 
                 -   " q u a l i t y   i m p r o v e m e n t   p r o g r a m s " 
 
             a r c h i v a l _ a l l o w e d :   t r u e 
 
             n o t e s :   " S o m e   s t a t e s   r e q u i r e   l o n g e r   r e t e n t i o n   f o r   m i n o r s " 
 
         c i t a t i o n s : 
 
             -   r e g u l a t i o n :   H I P A A 
 
                 s e c t i o n :   4 5   C F R   � � 1 6 4 . 5 1 4 ( b ) ( 2 ) ( i ) ( B ) 
 
                 d e s c r i p t i o n :   M e d i c a l   r e c o r d   n u m b e r s   m u s t   b e   r e m o v e d   f o r   d e - i d e n t i f i c a t i o n 
 
                 u r l :   h t t p s : / / w w w . e c f r . g o v / c u r r e n t / t i t l e - 4 5 / s u b t i t l e - A / s u b c h a p t e r - C / p a r t - 1 6 4 
 
         t a g s :   [ " m e d i c a l " ,   " i d e n t i f i e r " ,   " p h i " ] 
 
 ` ` ` 
 
 

---

## �Y"� Example (With Advanced Features - Phase 4)

```yaml
country: United States
framework: HIPAA
categories:
  - name: Social Security Number
    type: national_identifier
    subtype: government_id
    required_masking: true
    risk_level: critical
    breach_impact:
      - identity_theft
      - financial_fraud
      - account_takeover
    masking_techniques:
      - method: hash
        algorithm: SHA-256
        suitability: production
        reversible: false
        notes: One-way hash for verification purposes only
      - method: encryption
        algorithm: AES-256
        suitability: archival
        reversible: true
        notes: Use HSM-backed key management
      - method: partial_mask
        algorithm: "***-**-1234"
        suitability: display
        reversible: false
    retention:
      legal_minimum: "7 years"
      recommended: "7 years after last service date"
      basis: "HIPAA retention requirements + IRS regulations"
      deletion_trigger:
        - "patient_death + 7 years"
        - "account_closure + 7 years"
      exceptions:
        - "ongoing litigation or audit"
        - "minor records (retain until age 25)"
      archival_allowed: true
    citations:
      - regulation: HIPAA
        section: 45 CFR §164.514(b)(2)(i)(A)
        url: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164
    tags: ["identifier", "national_id", "sensitive"]
    
  - name: Medical Record Number
    type: direct_identifier
    subtype: medical
    required_masking: true
    risk_level: high
    breach_impact:
      - medical_fraud
      - privacy_violation
      - identity_theft
    gdpr_penalty_tier: high
    masking_techniques:
      - method: pseudonymization
        algorithm: tokenization
        suitability: analytics
        reversible: true
        notes: Maintain secure token vault with access controls
      - method: partial_mask
        algorithm: "MRN-***-456"
        suitability: display
        reversible: false
    retention:
      legal_minimum: "6 years"
      recommended: "10 years"
      maximum: "50 years"
      basis: "HIPAA § 164.316(b)(2) + state medical records laws"
      deletion_trigger:
        - "patient_request (Right to Erasure)"
        - "end_of_retention_period"
      exceptions:
        - "public health reporting requirements"
        - "quality improvement programs"
      archival_allowed: true
      notes: "Some states require longer retention for minors"
    citations:
      - regulation: HIPAA
        section: 45 CFR §164.514(b)(2)(i)(B)
        description: Medical record numbers must be removed for de-identification
        url: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164
    tags: ["medical", "identifier", "phi"]
```
