#!/usr/bin/env python3
"""
Audit all type values used across YAML files
"""

import os
import yaml
from pathlib import Path
from collections import Counter, defaultdict

def audit_types():
    """Scan all YAML files and collect type usage statistics"""
    data_dir = Path(__file__).parent.parent / "data"
    
    type_counter = Counter()
    type_by_framework = defaultdict(lambda: Counter())
    files_by_type = defaultdict(list)
    
    # Scan all YAML files
    for yaml_file in data_dir.rglob("*.yaml"):
        # Skip country-index files
        if yaml_file.name == "country-index.yaml":
            continue
            
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                
            if not data or 'categories' not in data:
                continue
                
            framework = data.get('framework', 'Unknown')
            
            for category in data.get('categories', []):
                if 'type' in category:
                    type_val = category['type']
                    type_counter[type_val] += 1
                    type_by_framework[framework][type_val] += 1
                    
                    rel_path = yaml_file.relative_to(data_dir)
                    if rel_path not in files_by_type[type_val]:
                        files_by_type[type_val].append(str(rel_path))
                        
        except Exception as e:
            print(f"Error reading {yaml_file}: {e}")
            continue
    
    # Print results
    print("=" * 80)
    print("TYPE USAGE AUDIT")
    print("=" * 80)
    print()
    
    print("Total unique types found:", len(type_counter))
    print()
    
    print("Type Frequency (sorted by usage):")
    print("-" * 80)
    for type_val, count in type_counter.most_common():
        print(f"  {type_val:30s} : {count:4d} occurrences")
    print()
    
    print("=" * 80)
    print("TYPES BY FRAMEWORK")
    print("=" * 80)
    for framework in sorted(type_by_framework.keys()):
        print(f"\n{framework}:")
        for type_val, count in type_by_framework[framework].most_common():
            print(f"  {type_val:30s} : {count:4d}")
    
    print("\n" + "=" * 80)
    print("FILES USING EACH TYPE")
    print("=" * 80)
    for type_val in sorted(type_counter.keys()):
        print(f"\n{type_val}:")
        print(f"  Used in {len(files_by_type[type_val])} files")
        for file_path in sorted(files_by_type[type_val])[:5]:  # Show first 5
            print(f"    - {file_path}")
        if len(files_by_type[type_val]) > 5:
            print(f"    ... and {len(files_by_type[type_val]) - 5} more")

if __name__ == "__main__":
    audit_types()
