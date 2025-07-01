import os
import yaml
 
REQUIRED_KEYS_ORDER = [
    "name", "type", "subtype", "required_masking", "tags", "citations"
]

def lint_yaml_file(file_path):
    issues = []
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
            categories = data.get("categories", [])
            for idx, category in enumerate(categories):
                keys = list(category.keys())
                # Warn if keys are out of order
                if keys != sorted(keys, key=lambda k: REQUIRED_KEYS_ORDER.index(k) if k in REQUIRED_KEYS_ORDER else 999):
                    issues.append(f"{file_path} - category {idx+1}: ⚠️ field order mismatch")
                # Warn if tags are missing or empty
                if "tags" not in category or not category["tags"]:
                    issues.append(f"{file_path} - category {idx+1}: ⚠️ missing or empty tags")
                # Warn if citations missing expected fields
                for cidx, citation in enumerate(category.get("citations", [])):
                    if not any(k in citation for k in ["regulation", "national_law", "authority"]):
                        issues.append(f"{file_path} - category {idx+1}, citation {cidx+1}: ❌ missing 'regulation' or national equivalent")
        except yaml.YAMLError as e:
            issues.append(f"{file_path} - YAML error: {str(e)}")
    return issues

def lint_all_yamls(base_path="data"):
    all_issues = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".yaml"):
                full_path = os.path.join(root, file)
                all_issues.extend(lint_yaml_file(full_path))
    return all_issues

if __name__ == "__main__":
    issues = lint_all_yamls()
    if not issues:
        print("✅ All YAML files passed lint checks.")
    else:
        print(f"❌ {len(issues)} issue(s) found:\n")
        for issue in issues:
            print(issue)
