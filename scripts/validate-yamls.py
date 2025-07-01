import os
import yaml
import json
from jsonschema import validate, ValidationError
from yaml.loader import SafeLoader

# Disable PyYAML date parsing
class NoDatesSafeLoader(SafeLoader):
    pass

for first_letter, resolvers in list(NoDatesSafeLoader.yaml_implicit_resolvers.items()):
    NoDatesSafeLoader.yaml_implicit_resolvers[first_letter] = [
        (tag, regexp) for tag, regexp in resolvers
        if tag != 'tag:yaml.org,2002:timestamp'
    ]

# Citation entry must include at least one of: regulation, national_law, authority
citation_schema = {
    "type": "object",
    "properties": {
        "regulation": {"type": "string"},
        "national_law": {"type": "string"},
        "authority": {"type": "string"},
        "article": {"type": "string"},
        "section": {"type": "string"},
        "url": {"type": "string"},
        "description": {"type": "string"},
        "guideline": {"type": "string"}
    },
    "anyOf": [
        {"required": ["regulation"]},
        {"required": ["national_law"]},
        {"required": ["authority"]}
    ]
}

# Category schema
category_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "type": {"type": "string"},
        "subtype": {"type": "string"},
        "required_masking": {"type": "boolean"},
        "tags": {
            "type": "array",
            "items": {"type": "string"}
        },
        "citations": {
            "type": "array",
            "items": citation_schema
        }
    },
    "required": ["name", "type", "required_masking", "citations"]
}

# File-level schema
file_schema = {
    "type": "object",
    "properties": {
        "country": {"type": "string"},
        "framework": {"type": "string"},
        "region": {"type": "string"},
        "language": {"type": "string"},
        "version": {"type": "string"},
        "status": {"type": "string"},
        "last_updated": {"type": "string"},
        "source_verified": {"type": "boolean"},
        "authority": {"type": "string"},
        "notes": {"type": "array", "items": {"type": "string"}},
        "categories": {
            "type": "array",
            "items": category_schema
        }
    },
    "required": ["country", "framework", "categories"]
}

def validate_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            content = yaml.load(f, Loader=NoDatesSafeLoader)
            validate(instance=content, schema=file_schema)
            return True, None
        except (yaml.YAMLError, ValidationError) as e:
            return False, str(e)

def scan_and_validate_all_yamls(base_path='data'):
    failures = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".yaml"):
                full_path = os.path.join(root, file)
                valid, error = validate_yaml_file(full_path)
                if not valid:
                    failures.append((full_path, error))
    return failures

# Execute
if __name__ == '__main__':
    failures = scan_and_validate_all_yamls()
    if not failures:
        print("✅ All YAML files passed schema validation.")
    else:
        print(f"❌ {len(failures)} file(s) failed validation:\n")
        for path, error in failures:
            print(f"{path}:\n  {error}\n")
