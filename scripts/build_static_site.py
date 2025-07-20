import os
import yaml
import json
from datetime import date, datetime
from jinja2 import Environment, FileSystemLoader

"""
OpenPIIMap Static Site Builder

This script generates country pages and JSON data files while preserving
any custom homepage that exists. It will:

1. Generate HTML pages for each country/framework YAML file
2. Convert YAML data to JSON format
3. Preserve existing custom homepage (if Bootstrap-based)
4. Only generate basic homepage if none exists

Usage: python scripts/build_static_site.py
"""

# Paths
DATA_DIR = "./data"
SITE_DIR = "./site"
JSON_DIR = os.path.join(SITE_DIR, "json")
HTML_DIR = os.path.join(SITE_DIR, "countries")
TEMPLATE_DIR = "scripts/templates"
INDEX_PATH = os.path.join(SITE_DIR, "index.html")

# Helpers
def make_json_safe(obj):
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    return obj

def render_header_template(active_page="", in_country_page=False):
    """Render header template with optional active page and country page flag"""
    header_template = env.get_template("header_template.html")
    return header_template.render(active_page=active_page, in_country_page=in_country_page)

def ensure_dirs():
    os.makedirs(JSON_DIR, exist_ok=True)
    os.makedirs(HTML_DIR, exist_ok=True)
    os.makedirs(TEMPLATE_DIR, exist_ok=True)

# Setup environment
ensure_dirs()
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template("country_template.html")

# Track generated pages
generated_pages = []

# 1. Convert YAML to JSON and generate country HTML pages
for framework in os.listdir(DATA_DIR):
    framework_path = os.path.join(DATA_DIR, framework)
    if not os.path.isdir(framework_path):
        continue

    for filename in os.listdir(framework_path):
        if not filename.endswith(".yaml"):
            continue

        base_name = filename.replace(".yaml", "")
        yaml_path = os.path.join(framework_path, filename)

        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        # Write JSON
        json_out_dir = os.path.join(JSON_DIR, framework)
        os.makedirs(json_out_dir, exist_ok=True)
        json_path = os.path.join(json_out_dir, f"{base_name}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=make_json_safe)

        # Write HTML
        html_filename = f"{framework}-{base_name}.html"
        html_path = os.path.join(HTML_DIR, html_filename)
        
        # Render header for country pages (with country page flag)
        header_html = render_header_template(in_country_page=True)
        
        html_content = template.render(
            country=data.get("country", base_name),
            framework=data.get("framework", framework),
            region=data.get("region", ""),
            language=data.get("language", ""),
            version=data.get("version", ""),
            status=data.get("status", ""),
            last_updated=data.get("last_updated", ""),
            source_verified=data.get("source_verified", False),
            authority=data.get("authority", ""),
            notes=data.get("notes", []),
            categories=data.get("categories", []),
            json_data=json.dumps(data, indent=2, ensure_ascii=False, default=make_json_safe),
            header=header_html
        )
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        generated_pages.append(html_filename)

# 2. Handle index.html - preserve custom homepage if it exists
if os.path.exists(INDEX_PATH):
    # Check if it's our custom Bootstrap homepage
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index_content = f.read()
    
    if "Bootstrap" in index_content and "Global Privacy Law Navigator" in index_content:
        print("✅ Preserving custom Bootstrap homepage")
        print(f"   Generated {len(generated_pages)} country pages")
        print(f"   Updated JSON data files")
    else:
        print("⚠️  Found basic index.html, keeping it as-is")
else:
    # Generate basic index.html only if none exists
    print("⚠️  No index.html found, generating basic version")
    html_links = ""
    for file in sorted(generated_pages):
        label = file.replace(".html", "").replace("-", " ").title()
        html_links += f'  <li><a href="countries/{file}">{label}</a></li>\n'

    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>OpenPIIMap - Country Explorer</title>
  <link rel="stylesheet" href="assets/style.css" />
</head>
<body>
  <h1>OpenPIIMap - Country Explorer</h1>
  <p>Select a country to view PII/PHI definitions:</p>
  <ul>
""" + html_links + """
  </ul>
</body>
</html>
"""

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(index_html)

print("✅ Static site successfully generated in 'site/'")
