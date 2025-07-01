import os
import json

def collect_country_indexes(base_path='data'):
    coverage = {}
    for root, _, files in os.walk(base_path):
        if "country-index.json" in files:
            framework = os.path.basename(root)
            with open(os.path.join(root, "country-index.json"), "r", encoding="utf-8") as f:
                index = json.load(f)
                if "countries" in index and "framework" in index:
                    countries = [c["name"] for c in index["countries"]]
                    coverage[index["framework"]] = sorted(countries)
    return coverage

def write_coverage_file(output_path="coverage.json"):
    coverage = collect_country_indexes()
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(coverage, f, indent=2, ensure_ascii=False)
    print(f"✅ coverage.json written with {len(coverage)} frameworks.")

if __name__ == "__main__":
    write_coverage_file()
