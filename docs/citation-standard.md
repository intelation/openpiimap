# Citation Format Standard

**Version**: 1.0  
**Date**: November 20, 2025  
**Status**: Official Standard

---

## Overview

This document defines the standardized format for citations in OpenPIIMap YAML files. All country/framework files should follow this schema to ensure consistency and machine-readability.

## Standardized Citation Schema

```yaml
citations:
  - regulation: string (required)
    article: string (optional)
    section: string (optional)
    recital: string (optional)
    chapter: string (optional)
    principle: string (optional)
    description: string (optional)
    url: string (optional)
    national_law: string (optional)
    authority: string (optional)
    guideline: string (optional)
    decision: string (optional)
```

## Field Definitions

### Required Fields

#### `regulation`
- **Type**: String
- **Required**: Yes
- **Description**: The name or abbreviation of the regulation/law being cited
- **Examples**:
  - `GDPR`
  - `HIPAA`
  - `LGPD`
  - `CPRA`
  - `PIPL`
  - `UK GDPR`
  - `Privacy Act 1988`

### Optional Fields

#### `article`
- **Type**: String
- **Description**: Article number or identifier from the regulation
- **Usage**: Common in European and civil law jurisdictions
- **Examples**:
  - `4(1)` - GDPR Article 4(1)
  - `Article 5, I` - LGPD Article 5, I
  - `Article 2(1) – Definition of Personal Information` - APPI
  - `Article 4 – Definition of Personal Data` - UAE DPL

#### `section`
- **Type**: String
- **Description**: Section number or identifier from the regulation
- **Usage**: Common in US and common law jurisdictions
- **Examples**:
  - `45 CFR §164.514(b)(2)(i)(A)` - HIPAA
  - `Cal. Civ. Code §1798.140(v)(1)(A)` - CPRA
  - `Section 2(1) – Definition of Personal Data` - PDPA Singapore
  - `Section 2(t) – Definition of Personal Data` - DPDPB India

#### `recital`
- **Type**: String
- **Description**: Recital number from EU-style regulations (preamble text providing context)
- **Usage**: Primarily GDPR and EU directives
- **Examples**:
  - `30` - GDPR Recital 30 (online identifiers)
  - `51` - GDPR Recital 51 (special categories of data)

#### `chapter`
- **Type**: String
- **Description**: Chapter identifier from the regulation
- **Usage**: Some national laws organized by chapters
- **Examples**:
  - `3 §` - Swedish Dataskyddslagen

#### `principle`
- **Type**: String
- **Description**: Privacy principle number or identifier
- **Usage**: Laws based on principles (e.g., Privacy Act 2020, PIPEDA)
- **Examples**:
  - `1` - Privacy Act 2020 Principle 1
  - `3` - PIPEDA Principle 3

#### `description`
- **Type**: String
- **Description**: Human-readable explanation of the citation's relevance
- **Usage**: Recommended for complex citations or to clarify application
- **Examples**:
  - `Personal data includes any identifiable information`
  - `Restricts processing of PPS numbers to lawful use only`
  - `Online identifiers such as IP addresses can lead to identifiability`

#### `url`
- **Type**: String (valid URL)
- **Description**: Link to official source of the regulation or guidance
- **Usage**: Highly recommended for all citations when available
- **Examples**:
  - `https://eur-lex.europa.eu/eli/reg/2016/679/oj`
  - `https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html`
  - `https://www.dsb.gv.at/download-links/dokumente`

#### `national_law`
- **Type**: String
- **Description**: Name of national implementing legislation (primarily GDPR countries)
- **Usage**: When a national law supplements or implements a framework regulation
- **Examples**:
  - `Bundesdatenschutzgesetz (BDSG)` - Germany
  - `Datenschutzgesetz (DSG)` - Austria
  - `Data Protection Act 2018` - Ireland/UK
  - `Legislative Decree 196/2003` - Italy

#### `authority`
- **Type**: String
- **Description**: Data protection authority or regulatory body
- **Usage**: When citing guidance or decisions from regulators
- **Examples**:
  - `DSB` - Austrian Data Protection Authority
  - `CNIL` - French Data Protection Authority
  - `HDPA` - Hellenic Data Protection Authority
  - `ICO` - UK Information Commissioner's Office

#### `guideline`
- **Type**: String
- **Description**: Title or identifier of regulatory guidance document
- **Usage**: When citing official interpretations or guidelines
- **Examples**:
  - `DSB-Empfehlung zu Cookies und Tracking`
  - `PPC Guidelines (2022)` - Japan
  - `ICO Guidance on International Transfers`

#### `decision`
- **Type**: String
- **Description**: Regulatory decision or ruling number
- **Usage**: When citing specific enforcement decisions or rulings
- **Examples**:
  - `No. 28/2019` - Greek DPA decision on biometrics

---

## Citation Patterns by Framework

### Pattern 1: Basic Regulation + Article
**Most Common** - Used by GDPR countries, APPI, LGPD, PIPL, etc.

```yaml
citations:
  - regulation: GDPR
    article: 4(1)
```

```yaml
citations:
  - regulation: LGPD
    article: Article 5, I
```

### Pattern 2: Regulation + Section
Used by US laws (HIPAA, CPRA), Asian laws (PDPA Singapore, DPDPB India)

```yaml
citations:
  - regulation: HIPAA
    section: 45 CFR §164.514(b)(2)(i)(A)
```

```yaml
citations:
  - regulation: CPRA
    section: Cal. Civ. Code §1798.140(v)(1)(A)
```

### Pattern 3: Regulation + Article/Section + Description
Recommended for clarity

```yaml
citations:
  - regulation: PIPL
    article: Article 4
    description: Definition of Personal Information
```

```yaml
citations:
  - regulation: DPDPB, 2023
    section: Section 2(t)
    description: Definition of Personal Data
```

### Pattern 4: GDPR + Recital
For GDPR interpretation guidance

```yaml
citations:
  - regulation: GDPR
    recital: 30
    description: Online identifiers such as IP addresses can lead to identifiability
```

### Pattern 5: GDPR + National Law
For national implementations

```yaml
citations:
  - regulation: GDPR
    article: 4(1)
  - national_law: Bundesdatenschutzgesetz (BDSG)
    section: Section 26
    description: Employee data requires special protection
```

### Pattern 6: Authority Guidance
For regulatory interpretations

```yaml
citations:
  - regulation: GDPR
    article: 4(1)
  - authority: DSB
    guideline: DSB-Empfehlung zu Cookies und Tracking
    url: https://www.dsb.gv.at/download-links/dokumente
```

### Pattern 7: Principle-Based (Privacy Act)
For principle-based frameworks

```yaml
citations:
  - regulation: Privacy Act 2020
    principle: 1
    description: Personal information must be collected for a lawful purpose.
```

---

## Implementation Guidelines

### 1. Always Include `regulation` Field
Every citation must have a `regulation` field. This is the minimum requirement.

### 2. Use Appropriate Structural Field
Choose the field that matches your jurisdiction's legal structure:
- **European/Civil Law**: Use `article`
- **US/Common Law**: Use `section`
- **Principle-Based**: Use `principle`
- **EU Regulations**: May also use `recital`

### 3. Add Descriptions for Clarity
When the citation's relevance isn't obvious, add a `description`:

```yaml
# Good - clear without description
citations:
  - regulation: GDPR
    article: 9(1)  # Obviously about special categories

# Better - description adds value
citations:
  - regulation: Data Protection Act 2018
    section: 46
    description: Restricts processing of PPS numbers to lawful use only
```

### 4. Include URLs When Available
Always try to include official URLs for regulations:

```yaml
citations:
  - regulation: GDPR
    article: 4(1)
    url: https://eur-lex.europa.eu/eli/reg/2016/679/oj
```

### 5. Multiple Citations for Single Category
Some categories may have multiple legal bases:

```yaml
- name: Health Data
  type: special_category
  citations:
    - regulation: GDPR
      article: 9(1)
      description: Explicit consent required for processing
    - national_law: Bundesdatenschutzgesetz (BDSG)
      section: Section 22
      description: Additional restrictions for employee health data
    - authority: BfDI
      guideline: Orientierungshilfe Gesundheitsdaten
      url: https://www.bfdi.bund.de/...
```

### 6. Maintain Consistent Formatting
- Use official abbreviations: `GDPR`, `HIPAA`, `CPRA`, `LGPD`
- For article numbers, use the official format: `4(1)`, not `4.1` or `4-1`
- For sections, include the full citation: `Cal. Civ. Code §1798.140(v)(1)(A)`
- For recitals, just use the number: `30`, not `Recital 30`

---

## Migration Guide

### For Existing Files

1. **Audit Current Citations**
   ```bash
   python scripts/analyze-citations.py
   ```

2. **Check for Missing Fields**
   - Ensure all citations have `regulation` field
   - Verify structural fields (`article`, `section`, etc.) match jurisdiction

3. **Add Descriptions** (Target: 50%+ of citations)
   - Focus on complex or non-obvious citations
   - Explain how the citation applies to the category

4. **Add URLs** (Target: 80%+ of citations)
   - Link to official regulation text
   - Use permalink/stable URLs when possible
   - Verify links are accessible

5. **Validate**
   ```bash
   python scripts/validate-yamls.py
   ```

### For New Files

Use this template:

```yaml
- name: [Category Name]
  type: [type]
  required_masking: true/false
  tags:
    - pii
  citations:
    - regulation: [Framework Name]
      article: [Article Number]  # OR section: [Section Number]
      description: [Optional explanation]
      url: [Official URL if available]
```

---

## Field Usage Statistics

Based on analysis of 22 frameworks (November 2025):

| Field | Occurrences | % of Citations |
|-------|-------------|----------------|
| `regulation` | 474 | 100% |
| `article` | 325 | 69% |
| `section` | 129 | 27% |
| `description` | 59 | 12% |
| `authority` | 46 | 10% |
| `guideline` | 45 | 9% |
| `url` | 45 | 9% |
| `recital` | 32 | 7% |
| `national_law` | 26 | 5% |
| `principle` | 13 | 3% |
| `decision` | 1 | <1% |
| `chapter` | 1 | <1% |

**Target for Phase 2**:
- `url`: Increase from 9% to 80%+
- `description`: Increase from 12% to 50%+

---

## Examples by Framework

### GDPR (Germany)
```yaml
- name: Full Name
  type: direct_identifier
  citations:
    - regulation: GDPR
      article: 4(1)
      description: Personal data includes any identifiable information
      url: https://eur-lex.europa.eu/eli/reg/2016/679/oj
    - national_law: Bundesdatenschutzgesetz (BDSG)
      section: Section 26
      description: Employee data requires special protection
```

### HIPAA (USA)
```yaml
- name: Full Name
  type: direct_identifier
  citations:
    - regulation: HIPAA
      section: 45 CFR §164.514(b)(2)(i)(A)
      url: https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html
```

### LGPD (Brazil)
```yaml
- name: Full Name
  type: direct_identifier
  citations:
    - regulation: LGPD
      article: Article 5, I
      description: Definition of personal data
      url: http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
```

### PIPL (China)
```yaml
- name: Full Name
  type: direct_identifier
  citations:
    - regulation: PIPL
      article: Article 4
      description: Definition of Personal Information
      url: http://www.npc.gov.cn/npc/c30834/202108/a8c4e3672c74491a80b53a172bb753fe.shtml
```

---

## Validation Rules

The following validation rules are enforced by `scripts/validate-yamls.py`:

1. ✓ Every citation must have a `regulation` field
2. ✓ `url` fields must be valid URLs (http/https)
3. ✓ At least one structural field (`article`, `section`, `principle`, `recital`) should be present
4. ✓ Field types must match schema (all strings)
5. ⚠ Warning if no `description` for complex citations
6. ⚠ Warning if no `url` provided (target 80%+)

---

## Questions & Support

For questions about citation formatting:
- Review this document and `docs/schema.md`
- Check examples in existing country files
- Post in GitHub Discussions: #data-quality

---

*Last Updated: November 20, 2025*
