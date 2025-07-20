import os
import yaml
import json
from datetime import date, datetime

# Paths
SOURCE_ROOT = "./data"                      # Your original data folder
OUTPUT_ROOT = "./site/json"                # Output folder for JSON files

# Ensure output directory exists
os.makedirs(OUTPUT_ROOT, exist_ok=True)

def make_json_safe(obj):
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    return obj

for framework in os.listdir(SOURCE_ROOT):
    framework_path = os.path.join(SOURCE_ROOT, framework)
    if not os.path.isdir(framework_path):
        continue

    output_framework_path = os.path.join(OUTPUT_ROOT, framework)
    os.makedirs(output_framework_path, exist_ok=True)

    for filename in os.listdir(framework_path):
        if not filename.endswith(".yaml"):
            continue

        input_path = os.path.join(framework_path, filename)
        output_path = os.path.join(output_framework_path, filename.replace(".yaml", ".json"))

        with open(input_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=make_json_safe)

print("All YAML files converted to JSON under 'site/json'")
