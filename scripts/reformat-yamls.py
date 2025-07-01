import os
import yaml

RECOMMENDED_ORDER = ["name", "type", "subtype", "required_masking", "tags", "citations"]

def reorder_fields(category):
    ordered = {}
    for key in RECOMMENDED_ORDER:
        if key in category:
            ordered[key] = category[key]
    for key in category:
        if key not in ordered:
            ordered[key] = category[key]
    return ordered

def reformat_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
            categories = data.get("categories", [])
            reformatted = [reorder_fields(cat) for cat in categories]
            data["categories"] = reformatted
            with open(file_path, 'w', encoding='utf-8') as out:
                yaml.dump(data, out, allow_unicode=True, sort_keys=False, width=100)
            return True, None
        except yaml.YAMLError as e:
            return False, str(e)

def reformat_all_yamls(base_path="data"):
    failures = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".yaml"):
                full_path = os.path.join(root, file)
                success, error = reformat_yaml_file(full_path)
                if not success:
                    failures.append((full_path, error))
    return failures

if __name__ == "__main__":
    failures = reformat_all_yamls()
    if not failures:
        print("✅ All YAML files reformatted successfully.")
    else:
        print(f"❌ {len(failures)} file(s) failed to reformat:")
        for path, err in failures:
            print(f"{path}: {err}")
