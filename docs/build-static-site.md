
# 🏗️ How to Build the OpenPIIMap Static Site from YAML Files

This guide walks you through generating a fully static, self-contained website from your YAML definitions using Python. No backend server or frontend framework is required.

---

## 📁 Project Structure Overview

```
openpiimap/
├── data/                        # YAML files (by framework and country)
├── site/                        # Output site (HTML + JSON)
│   ├── index.html
│   ├── countries/
│   └── json/
├── scripts/
│   ├── export_yaml_to_json.py
│   ├── generate_country_html.py
│   ├── generate_index.py
│   └── templates/
│       └── country_template.html
```

---

## ✅ Prerequisites

Make sure you have **Python 3.7+** and the following libraries installed:

```bash
pip install pyyaml jinja2
```

---

## 🧩 Step-by-Step Build Instructions

### 1. **Convert YAML files to JSON**

Run the following script:

```bash
python scripts/export_yaml_to_json.py
```

✅ This creates JSON versions of each country YAML in:
```
site/json/[framework]/[country].json
```

---

### 2. **Generate HTML pages for each country**

```bash
python scripts/generate_country_html.py
```

✅ This creates:
```
site/countries/gdpr-austria.html
site/countries/cpra-california.html
...
```

---

### 3. **Generate the homepage (index.html)**

```bash
python scripts/generate_index.py
```

✅ This creates:
```
site/index.html
```

---

## 🌐 Deployment

You can deploy the contents of the `/site` folder to any static host:

| Option           | How to Deploy                          |
|------------------|-----------------------------------------|
| GitHub Pages     | Push `site/` to `docs/` or `gh-pages` branch |
| Netlify / Vercel | Drag-and-drop `site/` folder            |
| Intranet / Local | Open `index.html` in a browser directly |

---

## 🧰 Regenerate After YAML Edits

Any time you update a YAML file in `/data`, re-run the 3 scripts:

```bash
python scripts/export_yaml_to_json.py
python scripts/generate_country_html.py
python scripts/generate_index.py
```

---

## 📎 Notes

- YAML file structure must follow the OpenPIIMap schema.
- Date fields like `last_updated` are automatically converted to ISO 8601 in JSON.
- You can modify the HTML template in:  
  `scripts/templates/country_template.html`
