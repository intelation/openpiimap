# Framework Naming Standard

**Version**: 1.0  
**Date**: November 20, 2025  
**Status**: Proposed Standard

---

## Overview

This document proposes standardized naming conventions for privacy frameworks in OpenPIIMap. The goal is to create consistent, clear, and concise framework names while maintaining recognizability.

---

## Current vs. Proposed Framework Names

| Current Name | Proposed Name | Countries | Rationale |
|--------------|---------------|-----------|-----------|
| APPI | APPI | Japan | ✓ Already good - well-known acronym |
| CPRA | CPRA | California | ✓ Already good - standard US abbreviation |
| DPA | DPA 2012 | Philippines | Add year to distinguish from generic "Data Protection Act" |
| DPDPB | DPDPB | India | ✓ Already good - official acronym (Digital Personal Data Protection Bill) |
| FADP | FADP | Switzerland | ✓ Already good - official Swiss abbreviation |
| GDPR | GDPR | 16 EU countries | ✓ Already good - globally recognized |
| HIPAA | HIPAA | United States | ✓ Already good - standard US healthcare privacy law |
| LFPDPPP | LFPDPPP | Mexico | ✓ Already good - official Mexican law abbreviation |
| LGPD | LGPD | Brazil | ✓ Already good - widely recognized |
| NDPR | NDPR | Nigeria | ✓ Already good - official Nigerian abbreviation |
| PDP Law | PDP Law | Indonesia | ✓ Already good - commonly used name |
| PDPA | PDPA | Malaysia, Singapore | ⚠️ **Issue**: Multiple countries under one name |
| PDPA Argentina | PDPA (Argentina) | Argentina | Standardize format with parentheses |
| PDPA Thailand | PDPA (Thailand) | Thailand | Standardize format with parentheses |
| PIPA | PIPA | South Korea | ✓ Already good - official Korean abbreviation |
| PIPEDA | PIPEDA | Canada | ✓ Already good - standard Canadian law |
| PIPL | PIPL | China | ✓ Already good - official Chinese law abbreviation |
| POPIA | POPIA | South Africa | ✓ Already good - official South African abbreviation |
| Privacy Act | Privacy Act (Australia) | Australia | ⚠️ **Issue**: Too generic - needs country qualifier |
| Privacy Act | Privacy Act (Bahamas) | Bahamas | Add country qualifier |
| Privacy Act 2020 | Privacy Act 2020 (New Zealand) | New Zealand | Add country qualifier for clarity |
| UAE Federal Data Protection Law (Law No. 45/2021) | UAE DPL | United Arab Emirates | Shorten while maintaining clarity |
| UK GDPR + DPA 2018 | UK GDPR | United Kingdom | Simplify - UK GDPR is commonly understood to include DPA 2018 |

---

## Naming Principles

### 1. Use Official Acronyms When Available
**Preferred**: `GDPR`, `HIPAA`, `LGPD`, `PIPL`  
**Why**: These are globally recognized and SEO-friendly

### 2. Add Country Qualifiers for Generic Names
**Pattern**: `[Law Name] ([Country])`  
**Examples**: 
- `Privacy Act (Australia)`
- `Privacy Act (Bahamas)`
- `PDPA (Argentina)`

**Why**: Prevents ambiguity and improves searchability

### 3. Use Short Forms for Verbose Names
**Preferred**: `UAE DPL` instead of `UAE Federal Data Protection Law (Law No. 45/2021)`  
**Why**: Improves readability while maintaining clarity

### 4. Include Year When It Distinguishes Different Versions
**Examples**:
- `DPA 2012` (Philippines)
- `Privacy Act 2020` (New Zealand) - when needed to distinguish from prior versions

**Why**: Helps identify which version of the law applies

### 5. Keep Established Abbreviations Even If Long
**Examples**: `LFPDPPP`, `PIPEDA`, `DPDPB`  
**Why**: These are official government abbreviations used in their jurisdictions

---

## Proposed Changes Summary

### High Priority Changes (Breaking/Clarity Issues)

#### 1. Split PDPA Directory (Task 2.5)
**Current Issue**: Multiple countries grouped under single "PDPA" name

**Current Structure**:
```
PDPA -> [Malaysia, Singapore]
PDPA Argentina -> [Argentina]
PDPA Thailand -> [Thailand]
```

**Proposed Structure**:
```
PDPA (Malaysia) -> [Malaysia]
PDPA (Singapore) -> [Singapore]
PDPA (Argentina) -> [Argentina]
PDPA (Thailand) -> [Thailand]
```

**Action Required**:
- Rename directories (covered in Task 2.5)
- Update coverage.json
- Update all documentation and website references

#### 2. Clarify Generic "Privacy Act"
**Current**: One entry for three different laws

**Current**:
```json
"Privacy Act": ["Australia", "Bahamas", "New Zealand"]
```

**Proposed**:
```json
"Privacy Act (Australia)": ["Australia"],
"Privacy Act (Bahamas)": ["Bahamas"],
"Privacy Act 2020 (New Zealand)": ["New Zealand"]
```

**Action Required**:
- Update country-index.json files in `data/privacyact/`
- Split into separate framework names in coverage.json
- Update YAML files' `framework` field
- Update documentation

### Medium Priority Changes (Clarity Improvements)

#### 3. Simplify UAE Name
**Current**: `UAE Federal Data Protection Law (Law No. 45/2021)`  
**Proposed**: `UAE DPL`

**Rationale**: 
- Much shorter and easier to use
- `DPL` is commonly understood as "Data Protection Law"
- Law number can be in documentation/notes

#### 4. Simplify UK GDPR Name
**Current**: `UK GDPR + DPA 2018`  
**Proposed**: `UK GDPR`

**Rationale**:
- UK GDPR inherently includes DPA 2018 provisions
- Common usage just says "UK GDPR"
- Can note DPA 2018 in documentation

### Low Priority Changes (Optional)

#### 5. Add Year to Philippines DPA
**Current**: `DPA`  
**Proposed**: `DPA 2012`

**Rationale**: Distinguishes from other "Data Protection Acts"

---

## Implementation Plan

### Phase 1: Update coverage.json Format (Non-Breaking)
1. Update framework names in coverage.json
2. Split "Privacy Act" into three separate entries
3. Update "UAE DPL" and "UK GDPR" entries

**Expected coverage.json after Phase 1**:
```json
{
  "APPI": ["Japan"],
  "CPRA": ["California"],
  "DPA 2012": ["Philippines"],
  "DPDPB": ["India"],
  "FADP": ["Switzerland"],
  "GDPR": [16 EU countries],
  "HIPAA": ["United States"],
  "LFPDPPP": ["Mexico"],
  "LGPD": ["Brazil"],
  "NDPR": ["Nigeria"],
  "PDP Law": ["Indonesia"],
  "PDPA (Malaysia)": ["Malaysia"],
  "PDPA (Singapore)": ["Singapore"],
  "PDPA (Argentina)": ["Argentina"],
  "PDPA (Thailand)": ["Thailand"],
  "PIPA": ["South Korea"],
  "PIPEDA": ["Canada"],
  "PIPL": ["China"],
  "POPIA": ["South Africa"],
  "Privacy Act (Australia)": ["Australia"],
  "Privacy Act (Bahamas)": ["Bahamas"],
  "Privacy Act 2020 (New Zealand)": ["New Zealand"],
  "UAE DPL": ["United Arab Emirates"],
  "UK GDPR": ["United Kingdom"]
}
```

### Phase 2: Update YAML Files
Update `framework` field in each affected YAML file:
- `data/dpa/philippines.yaml`: `DPA` → `DPA 2012`
- `data/privacyact/australia.yaml`: `Privacy Act` → `Privacy Act (Australia)`
- `data/privacyact/bahamas.yaml`: `Data Protection (Privacy of Personal Data) Act` → `Privacy Act (Bahamas)`
- `data/privacyact/new-zealand.yaml`: `Privacy Act 2020` → `Privacy Act 2020 (New Zealand)`
- `data/uae-dpl/united-arab-emirates.yaml`: `UAE Federal Data Protection Law (Law No. 45/2021)` → `UAE DPL`
- `data/uk-gdpr/united-kingdom.yaml`: `UK GDPR + DPA 2018` → `UK GDPR`

### Phase 3: Update country-index.json Files
Update `framework` field in each country-index.json file to match.

### Phase 4: Update Documentation & Website
- Update README.md
- Update all docs/ files
- Update site/ HTML files
- Update any API documentation

### Phase 5: Directory Restructure (Breaking Change - Task 2.5)
See separate task for PDPA directory split.

---

## Validation Rules

After implementation, enforce these rules:

1. Framework names should not contain countries with commas (e.g., "Privacy Act" covering "Australia, Bahamas")
2. If a framework applies to multiple countries from different frameworks, use country qualifier pattern
3. Framework names in coverage.json must match `framework` field in YAML files
4. Framework names in coverage.json must match `framework` field in country-index.json files

---

## Migration Path for API Consumers

### For coverage.json Consumers

**Before**:
```javascript
const australiaFramework = coverage["Privacy Act"];
// Returns: ["Australia", "Bahamas", "New Zealand"]
```

**After**:
```javascript
const australiaFramework = coverage["Privacy Act (Australia)"];
// Returns: ["Australia"]
```

**Migration Strategy**:
- Provide 2-week notice before change
- Document all name changes
- Consider providing a mapping file for API consumers
- Update API documentation with examples

### For Direct File Consumers

Files will have updated `framework` field:
```yaml
# Old
framework: Privacy Act

# New
framework: Privacy Act (Australia)
```

**Impact**: Medium - affects filtering and grouping logic

---

## SEO & Discoverability Considerations

### Positive Impacts
1. ✓ More specific names improve search results
2. ✓ Country qualifiers help users find relevant frameworks
3. ✓ Standardized naming improves documentation clarity

### Potential Concerns
1. ⚠️ URL changes may require redirects
2. ⚠️ Some loss of generic search traffic (e.g., "Privacy Act")
3. ⚠️ External links may need updating

### Mitigation
- Implement proper redirects for changed URLs
- Add all name variations to documentation
- Use semantic search-friendly descriptions
- Maintain backward compatibility where possible

---

## Questions & Feedback

Please provide feedback on:
1. Do the proposed names improve clarity?
2. Are there any naming conventions that conflict with official usage?
3. Should we include additional metadata (year, region) in names?
4. Are there any SEO concerns we haven't addressed?

---

*Last Updated: November 20, 2025*
