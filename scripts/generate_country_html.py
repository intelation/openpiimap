import os
import json
from jinja2 import Environment, FileSystemLoader

# Paths
JSON_ROOT = "./site/json"                     # Source directory of JSON files
OUTPUT_DIR = "./site/countries"              # Output HTML directory
TEMPLATE_DIR = "scripts/templates"         # Where your Jinja template lives

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Prepare Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template("country_template.html")

# Loop through all frameworks and country JSONs
for framework in os.listdir(JSON_ROOT):
    framework_path = os.path.join(JSON_ROOT, framework)
    if not os.path.isdir(framework_path):
        continue

    for filename in os.listdir(framework_path):
        if not filename.endswith(".json"):
            continue

        base_name = filename.replace(".json", "")
        json_path = os.path.join(framework_path, filename)
        html_path = os.path.join(OUTPUT_DIR, f"{framework}-{base_name}.html")

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        html = template.render(
            country=data.get("country", base_name),
            framework=data.get("framework", framework),
            categories=data.get("categories", []),
            json_data=json.dumps(data, indent=2, ensure_ascii=False)
        )

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)

print("✅ All HTML country pages generated in 'site/countries'")