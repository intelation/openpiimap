#!/usr/bin/env python3
"""
Generate country-index.json files for all framework directories.

This script automatically creates or updates country-index.json files by scanning
all YAML files in framework directories and extracting metadata.

The script intelligently determines status based on:
- Category count (10+ for complete, 5-9 for in-progress, <5 for draft)
- Citation completeness (80%+ coverage required for complete status)

Usage:
    # Generate all country indexes
    python scripts/generate-country-indexes.py

    # Preview changes without writing files
    python scripts/generate-country-indexes.py --dry-run

    # Generate for specific framework only
    python scripts/generate-country-indexes.py --framework gdpr

    # Verify existing indexes match generated ones
    python scripts/generate-country-indexes.py --verify

Options:
    --dry-run          Show what would be generated without writing files
    --framework NAME   Only generate index for specific framework directory
    --verify           Verify existing indexes match generated ones

Output Structure:
    {
      "framework": "GDPR",
      "region": "EU + EEA",
      "last_updated": "2025-11-20",
      "countries": [
        {
          "name": "Germany",
          "slug": "germany",
          "path": "data/gdpr/germany.yaml",
          "status": "complete"
        }
      ]
    }

Author: OpenPIIMap Team
Date: November 20, 2025
"""

import os
import sys
import json
import yaml
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
from collections import defaultdict


def load_yaml_file(file_path: Path) -> Dict[str, Any]:
    """Load and parse a YAML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"❌ Error loading {file_path}: {e}")
        return None


def generate_slug(country_name: str, filename: str) -> str:
    """
    Generate a slug from country name or filename.
    
    Args:
        country_name: Name from the YAML file
        filename: The YAML filename without extension
    
    Returns:
        A slug suitable for URLs and identifiers
    """
    # Use filename without extension as slug
    slug = filename.replace('.yaml', '').replace('.yml', '')
    return slug


def extract_metadata_from_yaml(yaml_path: Path) -> Dict[str, Any]:
    """
    Extract relevant metadata from a YAML file for country index.
    
    Args:
        yaml_path: Path to the YAML file
    
    Returns:
        Dictionary with country metadata or None if invalid
    """
    data = load_yaml_file(yaml_path)
    if not data:
        return None
    
    # Extract required fields
    country_name = data.get('country')
    framework = data.get('framework')
    
    if not country_name or not framework:
        print(f"⚠️  Skipping {yaml_path}: missing 'country' or 'framework' field")
        return None
    
    # Generate slug from filename
    slug = generate_slug(country_name, yaml_path.stem)
    
    # Determine status based on categories count and completeness
    categories = data.get('categories', [])
    category_count = len(categories)
    
    # Status logic:
    # - complete: 10+ categories with proper citations and structure
    # - in-progress: 5-9 categories
    # - draft: < 5 categories or missing critical fields
    status = "draft"
    if category_count >= 10:
        # Check if most categories have proper citations
        categories_with_citations = sum(1 for cat in categories if cat.get('citations'))
        citation_percentage = categories_with_citations / category_count if category_count > 0 else 0
        
        if citation_percentage >= 0.8:  # 80% or more have citations
            status = "complete"
        else:
            status = "in-progress"
    elif category_count >= 5:
        status = "in-progress"
    
    # Convert path to relative from repository root with data/ prefix
    # yaml_path.parent is the framework directory (e.g., data/hipaa)
    # yaml_path.parent.name is the framework name (e.g., hipaa)
    framework_name = yaml_path.parent.name
    filename = yaml_path.name
    path_str = f"data/{framework_name}/{filename}"
    
    return {
        "name": country_name,
        "slug": slug,
        "path": path_str,
        "status": status,
        "category_count": category_count
    }


def scan_framework_directory(framework_dir: Path) -> List[Dict[str, Any]]:
    """
    Scan a framework directory for YAML files and extract metadata.
    
    Args:
        framework_dir: Path to framework directory (e.g., data/gdpr/)
    
    Returns:
        List of country metadata dictionaries
    """
    countries = []
    
    # Find all YAML files in the directory (excluding country-index.json)
    yaml_files = list(framework_dir.glob("*.yaml")) + list(framework_dir.glob("*.yml"))
    
    for yaml_file in yaml_files:
        metadata = extract_metadata_from_yaml(yaml_file)
        if metadata:
            countries.append(metadata)
    
    # Sort by country name
    countries.sort(key=lambda x: x['name'])
    
    return countries


def determine_region(framework: str, countries: List[Dict[str, Any]]) -> str:
    """
    Determine the region for a framework based on framework name and countries.
    
    Args:
        framework: Framework name
        countries: List of countries in the framework
    
    Returns:
        Region string
    """
    # Framework-specific regions
    region_map = {
        'GDPR': 'EU + EEA',
        'UK GDPR': 'United Kingdom',
        'HIPAA': 'USA',
        'CPRA': 'United States',
        'CCPA': 'United States',
        'VCDPA': 'United States',
        'CPA': 'United States',
        'CTDPA': 'United States',
        'UCPA': 'United States',
        'MCPA': 'United States',
        'LGPD': 'Brazil',
        'PIPL': 'China',
        'APPI': 'Japan',
        'PIPA': 'South Korea',
        'POPI': 'South Africa',
        'POPIA': 'South Africa',
        'PDPA': 'Southeast Asia',
        'PIPEDA': 'Canada',
        'Privacy Act': 'Australia/New Zealand',
        'DPDPB': 'India',
        'NDPR': 'Nigeria',
        'UAE DPL': 'United Arab Emirates',
        'FADP': 'Switzerland',
        'DPA': 'Various',
    }
    
    # Check if framework has a specific region
    for key, region in region_map.items():
        if key.lower() in framework.lower():
            return region
    
    # If multiple countries, use "Various" or try to infer
    if len(countries) > 1:
        return "Various"
    elif len(countries) == 1:
        # Use the country name as region
        return countries[0]['name']
    
    return "Global"


def generate_country_index(framework_dir: Path, framework_name: str = None) -> Dict[str, Any]:
    """
    Generate a country-index.json structure for a framework directory.
    
    Args:
        framework_dir: Path to framework directory
        framework_name: Optional framework name override
    
    Returns:
        Dictionary representing the country index
    """
    # Scan directory for countries
    countries = scan_framework_directory(framework_dir)
    
    if not countries:
        print(f"⚠️  No valid YAML files found in {framework_dir}")
        return None
    
    # Get framework name from first country file or directory name
    if framework_name:
        framework = framework_name
    else:
        # Try to get from first YAML file
        first_yaml = list(framework_dir.glob("*.yaml"))[0]
        data = load_yaml_file(first_yaml)
        framework = data.get('framework', framework_dir.name.upper())
    
    # Determine region
    region = determine_region(framework, countries)
    
    # Remove category_count from output (used only for status determination)
    for country in countries:
        if 'category_count' in country:
            del country['category_count']
    
    # Generate index structure
    index = {
        "framework": framework,
        "region": region,
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "countries": countries
    }
    
    return index


def write_country_index(framework_dir: Path, index_data: Dict[str, Any], dry_run: bool = False):
    """
    Write country-index.json to framework directory.
    
    Args:
        framework_dir: Path to framework directory
        index_data: Index data to write
        dry_run: If True, don't actually write files
    """
    output_path = framework_dir / "country-index.json"
    
    if dry_run:
        print(f"\n📄 Would write to: {output_path}")
        print(json.dumps(index_data, indent=2))
        return
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)
            f.write('\n')  # Add trailing newline
        print(f"✅ Generated: {output_path}")
    except Exception as e:
        print(f"❌ Error writing {output_path}: {e}")


def verify_country_index(framework_dir: Path, generated_index: Dict[str, Any]) -> bool:
    """
    Verify that existing country-index.json matches generated one.
    
    Args:
        framework_dir: Path to framework directory
        generated_index: Newly generated index data
    
    Returns:
        True if matches, False otherwise
    """
    index_path = framework_dir / "country-index.json"
    
    if not index_path.exists():
        print(f"⚠️  No existing index at {index_path}")
        return False
    
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            existing_index = json.load(f)
        
        # Compare (ignoring last_updated field)
        gen_copy = generated_index.copy()
        exist_copy = existing_index.copy()
        
        gen_copy.pop('last_updated', None)
        exist_copy.pop('last_updated', None)
        
        if gen_copy == exist_copy:
            print(f"✅ Verified: {framework_dir.name} index matches")
            return True
        else:
            print(f"❌ Mismatch: {framework_dir.name} index differs")
            print(f"   Generated: {len(gen_copy.get('countries', []))} countries")
            print(f"   Existing:  {len(exist_copy.get('countries', []))} countries")
            return False
    except Exception as e:
        print(f"❌ Error verifying {index_path}: {e}")
        return False


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Generate country-index.json files for framework directories"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help="Show what would be generated without writing files"
    )
    parser.add_argument(
        '--framework',
        type=str,
        help="Only generate index for specific framework directory"
    )
    parser.add_argument(
        '--verify',
        action='store_true',
        help="Verify existing indexes match generated ones"
    )
    
    args = parser.parse_args()
    
    # Get data directory
    script_dir = Path(__file__).parent
    data_dir = script_dir.parent / "data"
    
    if not data_dir.exists():
        print(f"❌ Data directory not found: {data_dir}")
        sys.exit(1)
    
    print("🔍 Scanning framework directories...")
    
    # Get all framework directories
    if args.framework:
        framework_dirs = [data_dir / args.framework]
        if not framework_dirs[0].exists():
            print(f"❌ Framework directory not found: {framework_dirs[0]}")
            sys.exit(1)
    else:
        framework_dirs = [d for d in data_dir.iterdir() if d.is_dir()]
    
    # Process each framework directory
    success_count = 0
    error_count = 0
    verified_count = 0
    
    for framework_dir in sorted(framework_dirs):
        print(f"\n📁 Processing: {framework_dir.name}")
        
        # Generate index
        index_data = generate_country_index(framework_dir)
        
        if not index_data:
            error_count += 1
            continue
        
        if args.verify:
            # Verify mode
            if verify_country_index(framework_dir, index_data):
                verified_count += 1
            else:
                error_count += 1
        else:
            # Generate mode
            write_country_index(framework_dir, index_data, args.dry_run)
            success_count += 1
    
    # Summary
    print("\n" + "=" * 60)
    if args.verify:
        print(f"✅ Verified: {verified_count} indexes match")
        print(f"❌ Errors:   {error_count} indexes differ or missing")
    else:
        print(f"✅ Generated: {success_count} country indexes")
        print(f"❌ Errors:    {error_count}")
    
    if args.dry_run:
        print("\n💡 This was a dry run. Use without --dry-run to write files.")
    
    sys.exit(0 if error_count == 0 else 1)


if __name__ == "__main__":
    main()
