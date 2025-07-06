import os

COUNTRIES_DIR = "./site/countries"
OUTPUT_PATH = "./site/index.html"

# Read all HTML files in countries directory
html_files = sorted([
    f for f in os.listdir(COUNTRIES_DIR)
    if f.endswith(".html")
])

# Build list of links
html_links = ""
for file in html_files:
    label = file.replace(".html", "").replace("-", " ").title()
    html_links += f'  <li><a href="countries/{file}">{label}</a></li>\n'

# Full HTML
index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>OpenPIIMap – Country Explorer</title>
  <style>
    body {{
      font-family: sans-serif;
      padding: 2rem;
      max-width: 800px;
      margin: auto;
    }}
    h1 {{
      color: #2c3e50;
    }}
    ul {{
      line-height: 1.6;
    }}
    a {{
      text-decoration: none;
      color: #007acc;
    }}
  </style>
</head>
<body>
  <h1>OpenPIIMap – Country Explorer</h1>
  <p>Select a country to view PII/PHI definitions:</p>
  <ul>
{html_links}
  </ul>
</body>
</html>
"""

# Write to file
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(index_html)

print("✅ index.html generated in 'site/'")
