# 📘 Glossary: Key Terms in OpenPIIMap

This glossary defines terms and concepts used in OpenPIIMap YAML files, documentation, and schema.

---

### 🧍 PII (Personally Identifiable Information)

Any information that can directly or indirectly identify an individual.

Examples:

* Full name
* Passport number
* IP address
* Email address

---

### 🩺 PHI (Protected Health Information)

Health-related data protected under laws like HIPAA.

Examples:

* Medical history
* Diagnosis records
* Insurance details

---

### 📚 Direct Identifier

A data point that uniquely identifies an individual on its own.

Examples:

* Social Security Number
* Driver's License Number
* Biometric face scan

---

### 🔍 Indirect Identifier

A data point that becomes identifying when combined with others.

Examples:

* Date of birth
* ZIP code
* Gender

---

### 🚨 Special Category Data

Sensitive data types requiring higher protection (as defined in laws like GDPR Article 9).

Examples:

* Health data
* Biometric data
* Political opinions
* Religious beliefs

---

### 🔐 Required Masking

If set to `true`, the data must be redacted, anonymized, or obfuscated under privacy rules.

---

### 🏷️ Tags

A list of keywords to help classify and group data elements across frameworks.

Examples:

* `biometric`, `financial`, `health`, `genetic`, `phi`, `sensitive`, `child`, `tracking`, `criminal`

---

### 📖 Citation

A legal reference backing why a data type is considered sensitive.

Includes:

* Regulation name (e.g., GDPR, CPRA, PIPL)
* Article/section number (e.g., 4(1), Article 23)

---

### 🧠 Anonymized Data

Data that has been irreversibly stripped of all identifiers and is no longer considered personal data under many laws.

---

### 🕵️‍♂️ Pseudonymized Data

Data where identifiers have been replaced or hidden but could be restored using a key.

---

### 🧩 Subtype

An optional refinement of the `type` field (e.g., `biometric`, `address`, `employment`) for more specific classification.

---

### 🌍 Region

Geographical scope of the regulation or country entry (e.g., `Europe`, `Asia`, `North America`). Used in coverage and index files.

---

### 📦 Framework

The legal or regulatory system that governs the definition (e.g., GDPR, HIPAA, NDPR). Each YAML file is grouped by framework.

---

This glossary will expand as OpenPIIMap supports more frameworks and jurisdictions.
