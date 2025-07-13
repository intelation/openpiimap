# Header Management System

This document explains how to maintain consistent headers across all pages in the OpenPIIMap static site.

## 🎯 Problem Solved

Before this system, updating navigation required manually editing headers in multiple HTML files. Now you have a **single source of truth** for headers with automatic updates across all pages.

## 📁 File Structure

```
scripts/
├── templates/
│   └── header_template.html     # Single header template
├── update_headers.py            # Updates existing pages
├── manage_headers.py            # Convenient management script
└── build_static_site.py         # Updated to use header template
```

## 🚀 Quick Start

### Update All Headers
```bash
python scripts/manage_headers.py update
```

### Build Site + Update Headers
```bash
python scripts/manage_headers.py build
```

### Check Template Status
```bash
python scripts/manage_headers.py check
```

## 🛠️ How It Works

### 1. Header Template
- **Location**: `scripts/templates/header_template.html`
- **Features**: 
  - Jinja2 template with active page highlighting
  - Automatic path adjustment for country pages
  - Consistent navigation structure

### 2. Active Page Highlighting
The template automatically highlights the current page:
```html
<a class="nav-link{% if active_page == 'home' %} active{% endif %}" href="index.html">
```

### 3. Path Resolution
Country pages get different paths automatically:
```html
<a href="{% if in_country_page %}../{% endif %}index.html">
```

## 📝 Making Changes

### To Add/Remove Navigation Items:

1. **Edit the template**:
   ```bash
   # Edit the header template
   notepad scripts/templates/header_template.html
   ```

2. **Update all pages**:
   ```bash
   python scripts/manage_headers.py update
   ```

### Example: Adding a New Page

1. Add to `PAGE_CONFIGS` in `scripts/update_headers.py`:
   ```python
   PAGE_CONFIGS = {
       "index.html": "home",
       "map.html": "map", 
       "compare.html": "compare",
       "dashboard.html": "dashboard",
       "integration.html": "integration",
       "new-page.html": "newpage"  # Add this
   }
   ```

2. Add navigation item to `header_template.html`:
   ```html
   <li class="nav-item">
       <a class="nav-link{% if active_page == 'newpage' %} active{% endif %}" href="new-page.html">
           <i class="bi bi-star me-1"></i>New Page
       </a>
   </li>
   ```

3. Update all pages:
   ```bash
   python scripts/manage_headers.py update
   ```

## 🏗️ Technical Details

### Header Template Variables
- `active_page`: Highlights current page navigation
- `in_country_page`: Adjusts paths for country subdirectory

### Build Integration
The `build_static_site.py` script automatically:
- Generates headers for country pages with correct paths
- Passes the header HTML to country templates
- Maintains consistency during build process

### Update Process
The `update_headers.py` script:
- Uses regex to find and replace existing headers
- Handles both main pages and country pages
- Provides detailed feedback on success/failure

## 🎨 Customization

### Changing Navigation Structure
Edit `scripts/templates/header_template.html` to:
- Add/remove navigation items
- Change icons (Bootstrap Icons)
- Modify dropdown menus
- Update branding

### Changing Active States
Modify the active page logic:
```html
{% if active_page == 'your-page' %} active{% endif %}
```

## 🔧 Troubleshooting

### Header Not Updating
```bash
# Check template exists
python scripts/manage_headers.py check

# Force update
python scripts/manage_headers.py update
```

### Country Page Navigation Broken
Ensure `in_country_page=True` is passed in build script:
```python
header_html = render_header_template(in_country_page=True)
```

### Build Process Integration
After modifying the header template, always run:
```bash
python scripts/manage_headers.py update
```

## ✅ Benefits

1. **Single Source of Truth**: One template file controls all headers
2. **Automatic Updates**: Change once, update everywhere
3. **Consistent Navigation**: No more manual sync issues
4. **Build Integration**: New pages get consistent headers automatically
5. **Easy Maintenance**: Simple commands for all operations

## 🎯 Best Practices

1. Always test changes with `check` command first
2. Use the management script instead of running update_headers.py directly
3. Update headers after any navigation changes
4. Keep the template clean and well-commented
5. Test country page navigation after major changes

---

*This system eliminates the tedious process of manually updating headers across multiple files and ensures consistency across the entire OpenPIIMap site.*
