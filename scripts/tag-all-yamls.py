import os
import yaml

def infer_tags(cat):
    tags = set()
    t = cat.get("type", "")
    name = cat.get("name", "").lower()
    subtype = cat.get("subtype", "")

    if t == "direct_identifier":
        tags.add("pii")
    if t == "quasi_identifier":
        tags.add("pii")
    if t == "special_category":
        tags.add("sensitive")
    if "health" in name or "medical" in name:
        tags.add("phi")
    if "biometric" in name or subtype == "biometric":
        tags.add("biometric")
    if "child" in name:
        tags.add("child")
    if "criminal" in name:
        tags.add("criminal")
    if "location" in name or "ip" in name or "tracking" in name:
        tags.add("tracking")
    return sorted(tags)

RECOMMENDED_ORDER = ["name", "type", "subtype", "required_masking", "tags", "citations"]

def reorder_fields(cat):
    if "tags" not in cat or not cat["tags"]:
        cat["tags"] = infer_tags(cat)
    ordered = {k: cat[k] for k in RECOMMENDED_ORDER if k in cat}
    for k in cat:
        if k not in ordered:
            ordered[k] = cat[k]
    return ordered

def tag_all_yamls(base_path="data"):
    failures = []
    modified = 0
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".yaml"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        data = yaml.safe_load(f)

                    categories = data.get("categories", [])
                    changed = False
                    new_cats = []
                    for cat in categories:
                        old_tags = cat.get("tags", [])
                        new_cat = reorder_fields(cat)
                        if not old_tags or old_tags != new_cat["tags"]:
                            changed = True
                        new_cats.append(new_cat)
                    if changed:
                        data["categories"] = new_cats
                        with open(full_path, "w", encoding="utf-8") as f:
                            yaml.dump(data, f, sort_keys=False, allow_unicode=True)
                        modified += 1
                except Exception as e:
                    failures.append((full_path, str(e)))
    return modified, failures

if __name__ == "__main__":
    modified, failures = tag_all_yamls()
    if not failures:
        print(f"✅ All YAML files processed. {modified} file(s) modified.")
    else:
        print(f"❌ {len(failures)} file(s) failed to process:")
        for path, err in failures:
            print(f"{path}: {err}")
