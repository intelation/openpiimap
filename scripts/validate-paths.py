#!/usr/bin/env python3
"""
Validate path references in country-index.json files

This script checks that all paths referenced in country-index.json files
actually exist in the filesystem.
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Tuple

def validate_country_index_paths(data_dir: Path) -> List[Tuple[str, str, str]]:
    """
    Validate all country-index.json files in the data directory.
    
    Returns:
        List of tuples (framework_dir, referenced_path, issue)
    """
    issues = []
    
    # Find all country-index.json files
    for country_index in data_dir.rglob("country-index.json"):
        framework_dir = country_index.parent.name
        
        try:
            with open(country_index, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Validate each country entry
            for country in data.get('countries', []):
                if 'path' not in country:
                    issues.append((
                        framework_dir,
                        country.get('name', 'Unknown'),
                        "Missing 'path' field"
                    ))
                    continue
                
                path = country['path']
                
                # Construct the full path (relative to project root)
                if path.startswith('data/'):
                    # Path is relative to project root
                    full_path = data_dir.parent / path
                elif path.startswith('../'):
                    # Path is relative to country-index.json location
                    full_path = (country_index.parent / path).resolve()
                else:
                    # Assume path is relative to data directory
                    full_path = data_dir / path
                
                # Check if file exists
                if not full_path.exists():
                    issues.append((
                        framework_dir,
                        path,
                        f"Referenced file does not exist: {full_path}"
                    ))
                
                # Check for common path errors
                if '/' in path and '\\' not in path:
                    # Check for hyphen vs underscore issues
                    path_parts = path.split('/')
                    if len(path_parts) >= 2:
                        dir_name = path_parts[-2]  # Get directory name
                        
                        # Check if directory with hyphen exists when path uses hyphen
                        if '-' in dir_name:
                            actual_dir = data_dir / dir_name.replace('-', '')
                            if actual_dir.exists() and not (data_dir / dir_name).exists():
                                issues.append((
                                    framework_dir,
                                    path,
                                    f"Path uses hyphen but directory without hyphen exists: {dir_name}"
                                ))
                
        except json.JSONDecodeError as e:
            issues.append((
                framework_dir,
                str(country_index),
                f"Invalid JSON: {e}"
            ))
        except Exception as e:
            issues.append((
                framework_dir,
                str(country_index),
                f"Error reading file: {e}"
            ))
    
    return issues

def main():
    """Main validation function"""
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    data_dir = project_root / "data"
    
    if not data_dir.exists():
        print(f"Error: Data directory not found: {data_dir}")
        sys.exit(1)
    
    print("=" * 80)
    print("COUNTRY INDEX PATH VALIDATION")
    print("=" * 80)
    print()
    
    # Validate paths
    issues = validate_country_index_paths(data_dir)
    
    if not issues:
        print("✅ All country index paths are valid!")
        print()
        return 0
    
    # Report issues
    print(f"❌ Found {len(issues)} issue(s):")
    print()
    
    for framework, path, issue in issues:
        print(f"Framework: {framework}")
        print(f"  Path: {path}")
        print(f"  Issue: {issue}")
        print()
    
    print("=" * 80)
    print(f"SUMMARY: {len(issues)} path validation error(s) found")
    print("=" * 80)
    
    return 1

if __name__ == "__main__":
    sys.exit(main())
