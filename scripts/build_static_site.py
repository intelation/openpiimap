import os
import yaml
import json
from datetime import date, datetime
from jinja2 import Environment, FileSystemLoader

"""
OpenPIIMap Static Site Builder

This script generates country pages and JSON data files while preserving
any custom homepage that exists. It will:

1. Generate HTML pages for each country/framework YAML file
2. Convert YAML data to JSON format
3. Preserve existing custom homepage (if Bootstrap-based)
4. Only generate basic homepage if none exists

Usage: python scripts/build_static_site.py
"""

# Paths
DATA_DIR = "./data"
SITE_DIR = "./site"
JSON_DIR = os.path.join(SITE_DIR, "json")
HTML_DIR = os.path.join(SITE_DIR, "countries")
TEMPLATE_DIR = "scripts/templates"
INDEX_PATH = os.path.join(SITE_DIR, "index.html")

# Helpers
def make_json_safe(obj):
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    return obj

def render_header_template(active_page="", in_country_page=False):
    """Render header template with optional active page and country page flag"""
    header_template = env.get_template("header_template.html")
    return header_template.render(active_page=active_page, in_country_page=in_country_page)

def calculate_dashboard_statistics(countries_data, frameworks_data):
    """Calculate statistics for dashboard generation"""
    from collections import defaultdict
    
    # Basic counts
    countries_count = len(countries_data)
    frameworks_count = len(frameworks_data)
    
    # Calculate total categories
    total_categories = 0
    region_counts = defaultdict(int)
    framework_counts = defaultdict(int)
    
    for country in countries_data:
        total_categories += country.get('categories', 0)
        region_counts[country.get('region', 'Other')] += 1
        framework_counts[country.get('framework', 'Unknown')] += 1
    
    # Calculate averages and insights
    avg_categories = round(total_categories / countries_count) if countries_count > 0 else 0
    
    # Find most comprehensive framework
    framework_avg_categories = {}
    for fw_name in framework_counts.keys():
        fw_countries = [c for c in countries_data if c.get('framework') == fw_name]
        if fw_countries:
            avg_cats = sum(c.get('categories', 0) for c in fw_countries) / len(fw_countries)
            framework_avg_categories[fw_name] = round(avg_cats)
    
    most_comprehensive_fw = max(framework_avg_categories.keys(), 
                               key=lambda k: framework_avg_categories[k]) if framework_avg_categories else "GDPR"
    most_comprehensive_avg = framework_avg_categories.get(most_comprehensive_fw, 15)
    
    # Best covered region
    best_region = max(region_counts.keys(), key=lambda k: region_counts[k]) if region_counts else "Europe"
    best_region_count = region_counts.get(best_region, 0)
    
    # Latest additions (Argentina and Thailand)
    latest_country = "Thailand"
    latest_framework = "PDPA Thailand"
    latest_categories = 20
    
    return {
        'countries_count': countries_count,
        'frameworks_count': frameworks_count,
        'categories_count': total_categories,
        'regions_count': len(region_counts),
        'avg_categories_per_country': avg_categories,
        'countries_added_recent': 2,  # Argentina and Thailand
        'frameworks_added_recent': 2,  # PDPA Argentina and PDPA Thailand
        'categories_added_recent': 38,  # 18 + 20
        'most_comprehensive_framework': most_comprehensive_fw,
        'most_comprehensive_avg': most_comprehensive_avg,
        'best_covered_region': best_region,
        'best_region_count': best_region_count,
        'latest_country': latest_country,
        'latest_framework': latest_framework,
        'latest_categories': latest_categories,
        'last_updated': datetime.now().strftime("%Y-%m-%d"),
        'countries_data': countries_data,
        'frameworks_data': frameworks_data,
        'regions_data': dict(region_counts)
    }

def generate_dashboard(countries_data, frameworks_data):
    """Generate dynamic dashboard page"""
    try:
        dashboard_template = env.get_template("dashboard_template.html")
        
        # Calculate statistics
        stats = calculate_dashboard_statistics(countries_data, frameworks_data)
        
        # Render header
        header_html = render_header_template(active_page="dashboard")
        stats['header'] = header_html
        
        # Prepare simplified data for JSON serialization
        countries_simple = []
        for country in countries_data:
            countries_simple.append({
                'name': str(country.get('name', '')),
                'framework': str(country.get('framework', '')),
                'region': str(country.get('region', '')),
                'categories': int(country.get('categories', 0)),
                'file': str(country.get('file', ''))
            })
        
        frameworks_simple = []
        for fw in frameworks_data:
            frameworks_simple.append({
                'id': str(fw.get('id', '')),
                'name': str(fw.get('name', '')),
                'abbreviation': str(fw.get('abbreviation', '')),
                'region': str(fw.get('region', '')),
                'countries': fw.get('countries', [])
            })
        
        stats['countries_data'] = countries_simple
        stats['frameworks_data'] = frameworks_simple
        
        # Generate dashboard HTML
        dashboard_html = dashboard_template.render(**stats)
        
        # Write dashboard file
        dashboard_path = os.path.join(SITE_DIR, "dashboard.html")
        with open(dashboard_path, "w", encoding="utf-8") as f:
            f.write(dashboard_html)
            
        print(f"✅ Generated dynamic dashboard with {stats['countries_count']} countries")
        return True
        
    except Exception as e:
        print(f"⚠️  Failed to generate dashboard: {e}")
        print("   Keeping existing dashboard.html")
        return False

def ensure_dirs():
    os.makedirs(JSON_DIR, exist_ok=True)
    os.makedirs(HTML_DIR, exist_ok=True)
    os.makedirs(TEMPLATE_DIR, exist_ok=True)

# Setup environment
ensure_dirs()
env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
template = env.get_template("country_template.html")

# Track generated pages and collect data
generated_pages = []
countries_data = []
frameworks_data = []

# 1. Convert YAML to JSON and generate country HTML pages
for framework in os.listdir(DATA_DIR):
    framework_path = os.path.join(DATA_DIR, framework)
    if not os.path.isdir(framework_path):
        continue

    for filename in os.listdir(framework_path):
        if not filename.endswith(".yaml"):
            continue

        base_name = filename.replace(".yaml", "")
        yaml_path = os.path.join(framework_path, filename)

        with open(yaml_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        # Collect country data for dashboard
        country_info = {
            'name': data.get("country", base_name),
            'framework': data.get("framework", framework),
            'region': data.get("region", "Other"),
            'categories': len(data.get("pii_categories", [])) if data.get("pii_categories") else 0,
            'last_updated': data.get("last_updated", ""),
            'file': f"{framework}-{base_name}.html"
        }
        countries_data.append(country_info)

        # Write JSON
        json_out_dir = os.path.join(JSON_DIR, framework)
        os.makedirs(json_out_dir, exist_ok=True)
        json_path = os.path.join(json_out_dir, f"{base_name}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=make_json_safe)

        # Write HTML
        html_filename = f"{framework}-{base_name}.html"
        html_path = os.path.join(HTML_DIR, html_filename)
        
        # Render header for country pages (with country page flag)
        header_html = render_header_template(in_country_page=True)
        
        html_content = template.render(
            country=data.get("country", base_name),
            framework=data.get("framework", framework),
            region=data.get("region", ""),
            language=data.get("language", ""),
            version=data.get("version", ""),
            status=data.get("status", ""),
            last_updated=data.get("last_updated", ""),
            source_verified=data.get("source_verified", False),
            authority=data.get("authority", ""),
            notes=data.get("notes", []),
            categories=data.get("categories", []),
            json_data=json.dumps(data, indent=2, ensure_ascii=False, default=make_json_safe),
            header=header_html
        )
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        generated_pages.append(html_filename)

# 2. Handle index.html - preserve custom homepage if it exists
if os.path.exists(INDEX_PATH):
    # Check if it's our custom Bootstrap homepage
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index_content = f.read()
    
    if "Bootstrap" in index_content and "Global Privacy Law Navigator" in index_content:
        print("✅ Preserving custom Bootstrap homepage")
        print(f"   Generated {len(generated_pages)} country pages")
        print(f"   Updated JSON data files")
    else:
        print("⚠️  Found basic index.html, keeping it as-is")
else:
    # Generate basic index.html only if none exists
    print("⚠️  No index.html found, generating basic version")
    html_links = ""
    for file in sorted(generated_pages):
        label = file.replace(".html", "").replace("-", " ").title()
        html_links += f'  <li><a href="countries/{file}">{label}</a></li>\n'

    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>OpenPIIMap - Country Explorer</title>
  <link rel="stylesheet" href="assets/style.css" />
</head>
<body>
  <h1>OpenPIIMap - Country Explorer</h1>
  <p>Select a country to view PII/PHI definitions:</p>
  <ul>
""" + html_links + """
  </ul>
</body>
</html>
"""

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(index_html)

# 3. Load frameworks data for dashboard
frameworks_json_path = os.path.join(JSON_DIR, "frameworks.json")
if os.path.exists(frameworks_json_path):
    with open(frameworks_json_path, "r", encoding="utf-8") as f:
        frameworks_data = json.load(f)
else:
    frameworks_data = []

# 4. Generate dynamic dashboard
generate_dashboard(countries_data, frameworks_data)

print("✅ Static site successfully generated in 'site/'")
