#!/usr/bin/env python3
"""
OpenPIIMap Header Management Script
Provides easy commands for managing consistent headers across the site.
"""

import sys
import argparse
import subprocess
import os

def run_header_update():
    """Run the header update script"""
    print("🔄 Running header update...")
    result = subprocess.run([sys.executable, "scripts/update_headers.py"], 
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print(result.stdout)
        print("✅ Headers updated successfully!")
    else:
        print("❌ Header update failed:")
        print(result.stderr)
        return False
    return True

def run_build():
    """Run the full site build"""
    print("🚀 Running full site build...")
    result = subprocess.run([sys.executable, "scripts/build_static_site.py"], 
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print(result.stdout)
        print("✅ Site built successfully!")
    else:
        print("❌ Site build failed:")
        print(result.stderr)
        return False
    return True

def check_template():
    """Check if header template exists and show info"""
    template_path = "scripts/templates/header_template.html"
    if os.path.exists(template_path):
        print(f"✅ Header template found: {template_path}")
        with open(template_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.count('\n') + 1
            nav_items = content.count('nav-item')
            print(f"   📊 Template has {lines} lines and {nav_items} navigation items")
    else:
        print(f"❌ Header template not found: {template_path}")
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description='OpenPIIMap Header Management')
    parser.add_argument('command', choices=['update', 'build', 'check', 'help'], 
                       help='Command to execute')
    
    if len(sys.argv) == 1:
        # If no arguments, show help
        parser.print_help()
        return
        
    args = parser.parse_args()
    
    print("🛡️  OpenPIIMap Header Management")
    print("=" * 40)
    
    if args.command == 'update':
        run_header_update()
    elif args.command == 'build':
        if run_build():
            print("\n🔄 Also updating headers for consistency...")
            run_header_update()
    elif args.command == 'check':
        check_template()
    elif args.command == 'help':
        print("""
Available Commands:
  update  - Update headers in all existing pages
  build   - Build the entire site and update headers
  check   - Check header template status
  help    - Show this help message

Examples:
  python scripts/manage_headers.py update
  python scripts/manage_headers.py build
  python scripts/manage_headers.py check

Header Template Location:
  scripts/templates/header_template.html

To modify navigation:
  1. Edit scripts/templates/header_template.html
  2. Run: python scripts/manage_headers.py update
""")

if __name__ == "__main__":
    main()
