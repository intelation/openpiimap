#!/usr/bin/env python3
"""
Header Update Script for OpenPIIMap Static Site
Updates all HTML pages with consistent header from template.
"""

import os
import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Paths
SITE_DIR = "./site"
TEMPLATE_DIR = "scripts/templates"

# Page configurations - maps file to active page identifier
PAGE_CONFIGS = {
    "index.html": "home",
    "map.html": "map", 
    "compare.html": "compare",
    "dashboard.html": "dashboard",
    "integration.html": "integration"
}

def setup_jinja():
    """Setup Jinja2 environment"""
    return Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def render_header(active_page="", in_country_page=False):
    """Render header template with active page and country page flag"""
    env = setup_jinja()
    template = env.get_template("header_template.html")
    return template.render(active_page=active_page, in_country_page=in_country_page)

def update_header_in_file(file_path, new_header):
    """Update header section in HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to match header section (more flexible)
        header_pattern = r'(<header class="site-header">.*?</header>)'
        
        # Check if header exists
        if re.search(header_pattern, content, re.DOTALL):
            # Replace existing header
            updated_content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
        else:
            # If no header found, try to insert after <body> tag
            body_pattern = r'(<body[^>]*>)'
            if re.search(body_pattern, content):
                updated_content = re.sub(
                    body_pattern, 
                    r'\1\n    <!-- Header -->\n    ' + new_header + '\n', 
                    content
                )
            else:
                print(f"Could not find header or body tag in {file_path}")
                return False
        
        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        return True
        
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def update_all_headers():
    """Update headers in all configured pages"""
    print("Updating headers in all pages...")
    
    updated_count = 0
    failed_count = 0
    
    for filename, active_page in PAGE_CONFIGS.items():
        file_path = os.path.join(SITE_DIR, filename)
        
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
            
        # Render header for this page
        header_html = render_header(active_page)
        
        # Update file
        if update_header_in_file(file_path, header_html):
            print(f"Updated header in {filename} (active: {active_page})")
            updated_count += 1
        else:
            print(f"Failed to update header in {filename}")
            failed_count += 1
    
    print(f"\nHeader Update Summary:")
    print(f"   Successfully updated: {updated_count} files")
    print(f"   Failed to update: {failed_count} files")
    
    if failed_count == 0:
        print("All headers updated successfully!")
    
    return updated_count, failed_count

def update_country_pages():
    """Update headers in generated country pages"""
    countries_dir = os.path.join(SITE_DIR, "countries")
    if not os.path.exists(countries_dir):
        print("Countries directory not found")
        return 0, 0
    
    print("Updating headers in country pages...")
    
    updated_count = 0
    failed_count = 0
    
    # Render header with country page flag for country pages
    header_html = render_header(in_country_page=True)
    
    for filename in os.listdir(countries_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(countries_dir, filename)
            
            if update_header_in_file(file_path, header_html):
                updated_count += 1
            else:
                failed_count += 1
    
    print(f"Country Pages Update Summary:")
    print(f"   Successfully updated: {updated_count} files")
    print(f"   Failed to update: {failed_count} files")
    
    return updated_count, failed_count

def main():
    """Main function"""
    print("OpenPIIMap Header Update Tool")
    print("=" * 50)
    
    # Check if template exists
    template_path = os.path.join(TEMPLATE_DIR, "header_template.html")
    if not os.path.exists(template_path):
        print(f"Header template not found: {template_path}")
        return
    
    # Update main pages
    main_updated, main_failed = update_all_headers()
    
    print("\n" + "-" * 50)
    
    # Update country pages
    country_updated, country_failed = update_country_pages()
    
    print("\n" + "=" * 50)
    print(f"Total Summary:")
    print(f"   Total updated: {main_updated + country_updated} files")
    print(f"   Total failed: {main_failed + country_failed} files")

if __name__ == "__main__":
    main()
