# 🏷️ OpenPIIMap Subtype Taxonomy

**Document Version**: 1.0  
**Date**: November 20, 2025  
**Status**: Official Standard  
**Owner**: Data Architecture Team

---

## Purpose

This document defines the **standard subtype taxonomy** for OpenPIIMap. Subtypes provide granular classification within PII/PHI category types, enabling more precise filtering, querying, and compliance analysis.

---

## When to Use Subtypes

**Subtypes are OPTIONAL but RECOMMENDED** for:
- Adding granularity to broad category types
- Enabling filtering by data classification (e.g., "show me all `biometric` data")
- Supporting technical implementation (e.g., masking strategies differ by subtype)
- Improving data catalog and discovery

**Use subtypes when**:
- Multiple categories share the same `type` but have different characteristics
- You want to group related PII elements across frameworks
- The subtype adds meaningful semantic value

**Do not use subtypes when**:
- The category is already specific (e.g., "Email Address" doesn't need `subtype: email`)
- It would create redundancy with the `name` field
- No clear subtype exists in the standard taxonomy

---

## Standard Subtypes

### 🔖 Identity

Subtypes for personal identification data.

#### `personal_name`
- **Usage**: Full Name, First Name, Last Name, Maiden Name, Legal Name
- **Typical Type**: `direct_identifier`
- **Examples**: 
  - "Full Name" (GDPR)
  - "Nome Completo" (LGPD)
  - "氏名" (APPI)

#### `government_id`
- **Usage**: Government-issued identification numbers
- **Typical Types**: `direct_identifier`, `national_identifier`
- **Examples**:
  - Social Security Number (US)
  - National Insurance Number (UK)
  - CPF (Brazil)
  - Personalausweis (Germany)
  - Aadhaar (India)
  - NIE (Spain)
  - Tax File Number (Australia)

---

### 📧 Contact

Subtypes for communication and contact information.

#### `digital_contact`
- **Usage**: Email addresses, online messaging handles
- **Typical Type**: `direct_identifier`
- **Examples**:
  - Email Address
  - Instant Messaging ID
  - Social Media Handle (when used for contact)

#### `telecom_contact`
- **Usage**: Phone numbers, fax numbers, mobile numbers
- **Typical Type**: `direct_identifier`
- **Examples**:
  - Phone Number
  - Mobile Number
  - Fax Number
  - WhatsApp Number
  - Telephone Number

#### `address`
- **Usage**: Physical/postal addresses
- **Typical Types**: `direct_identifier`, `indirect_identifier`, `quasi_identifier`
- **Examples**:
  - Postal Address
  - Home Address
  - Residential Address
  - Street Address
  - Mailing Address

---

### 💻 Technical

Subtypes for technical and digital identifiers.

#### `network_identifier`
- **Usage**: Network-level identifiers
- **Typical Types**: `indirect_identifier`, `quasi_identifier`
- **Examples**:
  - IP Address
  - MAC Address
  - Network Identifier
  - Internet Protocol Address

#### `device_id`
- **Usage**: Device-level identifiers and tracking technologies
- **Typical Types**: `indirect_identifier`, `quasi_identifier`, `behavioral`
- **Examples**:
  - Cookies
  - Device Fingerprints
  - Device ID
  - Session ID
  - Advertising ID
  - Browser Fingerprint
  - Mobile Device Identifier

---

### 🔐 Sensitive Data

Subtypes for special category/sensitive personal data.

#### `biometric`
- **Usage**: Biometric data for identification
- **Typical Type**: `special_category`
- **Examples**:
  - Fingerprints
  - Facial Recognition Data
  - Iris Scans
  - Voice Recognition Data
  - Retina Scans
  - Biometric Identifiers
  - Biometric Data

#### `health`
- **Usage**: Health-related information (general)
- **Typical Type**: `special_category`
- **Examples**:
  - Health Data
  - Health Information
  - Personal Health Information
  - Medical History
  - Health Status

#### `medical`
- **Usage**: Specific medical records and clinical data
- **Typical Type**: `special_category`
- **Examples**:
  - Medical Records
  - Medical Record Numbers
  - Prescription Data
  - Treatment History
  - Clinical Notes
  - Diagnosis Information

#### `genetic`
- **Usage**: Genetic and hereditary information
- **Typical Type**: `special_category`
- **Examples**:
  - Genetic Data
  - DNA Information
  - Genetic Test Results
  - Hereditary Information
  - Genomic Data

---

### 💰 Financial

Subtypes for financial information.

#### `financial_identifier`
- **Usage**: Financial account numbers and payment identifiers (general)
- **Typical Types**: `direct_identifier`, `financial_identifier`
- **Examples**:
  - Credit Card Number
  - Debit Card Number
  - Payment Card Information
  - Account Number (when context is financial)
  - IBAN
  - Payment Information

#### `bank_account`
- **Usage**: Specific bank account identifiers
- **Typical Types**: `direct_identifier`, `financial_identifier`
- **Examples**:
  - Bank Account Number
  - Routing Number
  - Sort Code
  - SWIFT/BIC Code
  - Account and Routing Numbers

#### `insurance_id`
- **Usage**: Insurance-related identifiers
- **Typical Types**: `direct_identifier`, `financial_identifier`
- **Examples**:
  - Health Insurance Number
  - Insurance Policy Number
  - Health Plan Beneficiary Numbers
  - Social Insurance Number

#### `tax_identifier`
- **Usage**: Tax-related identification numbers
- **Typical Types**: `direct_identifier`, `national_identifier`
- **Examples**:
  - Tax Identification Number (TIN)
  - Tax File Number
  - VAT Number
  - Fiscal Code

---

### 🏢 Contextual

Subtypes for context-dependent PII.

#### `employment`
- **Usage**: Employment-related identifiers and basic information
- **Typical Type**: `contextual_identifier`
- **Examples**:
  - Employee ID
  - Employment Status
  - Job Title
  - Employer Name
  - Work Email

#### `hr_data`
- **Usage**: Human resources records and sensitive employment data
- **Typical Type**: `contextual_identifier`
- **Examples**:
  - Performance Reviews
  - Disciplinary Records
  - HR Records
  - Personnel Files
  - Background Check Results

#### `compensation`
- **Usage**: Salary and compensation information
- **Typical Type**: `contextual_identifier`
- **Examples**:
  - Salary Information
  - Compensation Details
  - Benefits Information
  - Payroll Data
  - Bonus Information

#### `education`
- **Usage**: Educational records and academic information
- **Typical Type**: `contextual_identifier`
- **Examples**:
  - Student ID
  - Education Records
  - Academic Transcripts
  - Grades
  - Enrollment Status
  - Educational History

#### `geolocation`
- **Usage**: Location and movement data
- **Typical Types**: `indirect_identifier`, `quasi_identifier`, `behavioral`
- **Examples**:
  - Geolocation Data
  - GPS Coordinates
  - Location Data
  - Movement Patterns
  - Location History
  - Precise Geolocation

---

### 📊 Other

Additional subtypes for specialized use cases.

#### `personal_attributes`
- **Usage**: Physical or demographic attributes (when not sensitive category)
- **Typical Types**: `indirect_identifier`, `quasi_identifier`
- **Examples**:
  - Date of Birth
  - Age
  - Gender (in non-sensitive contexts)
  - Physical Characteristics (height, weight)

#### `vehicle_identifier`
- **Usage**: Vehicle-related identifiers
- **Typical Types**: `indirect_identifier`, `quasi_identifier`
- **Examples**:
  - License Plate Number
  - Vehicle Registration Number
  - VIN (Vehicle Identification Number)

#### `digital_identity`
- **Usage**: Online account and digital identity information
- **Typical Type**: `direct_identifier`
- **Examples**:
  - Username
  - User ID
  - Account Number (online)
  - Member ID

---

## Usage Guidelines

### Mapping Categories to Subtypes

When adding subtypes to existing categories, follow this decision tree:

```
1. What is the category name?
   └─ Does it match a standard subtype directly? (e.g., "Email Address" → `digital_contact`)
   
2. What is the primary use case?
   └─ Identity verification? → Use `personal_name` or `government_id`
   └─ Contact/communication? → Use `digital_contact`, `telecom_contact`, or `address`
   └─ Technical tracking? → Use `network_identifier` or `device_id`
   └─ Sensitive data? → Use `biometric`, `health`, `medical`, or `genetic`
   └─ Financial transaction? → Use `financial_identifier`, `bank_account`, etc.
   └─ Employment/education? → Use `employment`, `hr_data`, `education`, etc.
   └─ Location tracking? → Use `geolocation`
   
3. Does it add meaningful value?
   └─ YES: Add the subtype
   └─ NO: Leave it blank (subtypes are optional)
```

### Examples

#### ✅ Good Subtype Usage

```yaml
# Clear benefit: Groups all email addresses across frameworks
- name: Email Address
  type: direct_identifier
  subtype: digital_contact
  
# Clear benefit: Distinguishes health data from other special categories
- name: Medical Records
  type: special_category
  subtype: medical
  
# Clear benefit: Enables querying all government IDs
- name: Social Security Number
  type: national_identifier
  subtype: government_id
```

#### ❌ Avoid Redundancy

```yaml
# Bad: Subtype duplicates the name
- name: Email Address
  type: direct_identifier
  subtype: email  # Don't do this - use "digital_contact"
  
# Bad: Subtype doesn't add value
- name: Passport Number
  type: direct_identifier
  subtype: passport  # Don't do this - use "government_id"
```

---

## Consistency Rules

### 1. Use Lowercase with Underscores
- ✅ `government_id`
- ✅ `digital_contact`
- ❌ `GovernmentID`
- ❌ `digital-contact`

### 2. Match Standard Taxonomy
- Always use one of the standard subtypes listed in this document
- If you need a new subtype, propose it for inclusion in this taxonomy
- Don't create framework-specific subtypes

### 3. Preserve Framework Naming Conventions
- If a framework uses different terminology, keep the original `name` field
- Map it to the appropriate standard `subtype`

**Example**:
```yaml
# HIPAA uses "PHI" terminology
- name: Medical Record Numbers
  type: direct_identifier
  subtype: medical
  
# GDPR uses "health data" terminology
- name: Health Data
  type: special_category
  subtype: health
```

### 4. Be Consistent Within Frameworks
- All files within the same framework should use the same subtype for similar categories
- Example: All GDPR countries use `personal_name` for "Full Name"

---

## Coverage Targets

### Current State (Nov 2025)

| Framework Category | Avg Subtype Coverage | Target |
|-------------------|---------------------|--------|
| GDPR (30 countries) | 80-100% | ✅ Complete |
| US State Laws (6 states) | 48-52% | 90%+ |
| Asian Frameworks (7 countries) | 20-30% | 90%+ |
| Latin American (3 countries) | 18-20% | 90%+ |
| African (2 countries) | 16-100% | 90%+ |
| Other (6 frameworks) | 16-38% | 90%+ |

### Enhancement Strategy

**Phase 3 (Weeks 11-12)**:
1. Identify all categories without subtypes
2. Map categories to standard subtypes using this taxonomy
3. Add subtypes to YAML files
4. Validate consistency across frameworks
5. Update schema documentation

---

## Validation

### Automated Checks

The `validate-yamls.py` script should verify:
- ✅ Subtype values match this standard taxonomy
- ✅ Subtypes are lowercase with underscores
- ✅ Subtypes are appropriate for the category type
- ⚠️ Warning if subtype coverage is low (<50%)

### Manual Review

Before approving PRs with new subtypes:
1. Check that the subtype exists in this taxonomy
2. Verify the subtype matches the category semantics
3. Ensure consistency with similar categories in other frameworks
4. Confirm the subtype adds meaningful value

---

## Standard Subtype List (Quick Reference)

### Identity
- `personal_name`
- `government_id`

### Contact
- `digital_contact`
- `telecom_contact`
- `address`

### Technical
- `network_identifier`
- `device_id`

### Sensitive
- `biometric`
- `health`
- `medical`
- `genetic`

### Financial
- `financial_identifier`
- `bank_account`
- `insurance_id`
- `tax_identifier`

### Contextual
- `employment`
- `hr_data`
- `compensation`
- `education`
- `geolocation`

### Other
- `personal_attributes`
- `vehicle_identifier`
- `digital_identity`

---

## Changelog

| Date | Version | Changes |
|------|---------|---------|
| 2025-11-20 | 1.0 | Initial taxonomy based on analysis of 34 country files and 28 frameworks |

---

## Contact

**Maintainer**: Data Architecture Team  
**Questions**: Open an issue on GitHub  
**Proposals**: Submit PR to update this document

---

*Document End*
