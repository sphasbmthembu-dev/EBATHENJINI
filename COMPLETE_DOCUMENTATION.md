# EBATHENJINI - Complete Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Architecture](#architecture)
6. [API Reference](#api-reference)
7. [Configuration](#configuration)
8. [Troubleshooting](#troubleshooting)

## Introduction

EBATHENJINI is a comprehensive Python-based mobile application for preserving and celebrating memories. Built with Kivy, it provides a beautiful, intuitive interface for storing, searching, and sharing precious moments.

## Features

### Memory Management
- Create memories with title, description, date, and photos
- Edit and update existing memories
- Delete memories with confirmation
- Organize with custom tags

### Search & Filtering
- Real-time search by title, description, or tags
- Filter by date (Recent, Oldest, All)
- Tag-based filtering
- Advanced search options

### Export & Backup
- Export to PDF with images
- Export to CSV for data analysis
- Manual backup creation
- Automatic backup scheduling
- Restore from previous backups

### User Interface
- Beautiful, modern design
- Responsive layouts
- Multiple color themes
- Smooth screen transitions
- Intuitive navigation

## Installation

### System Requirements
- Python 3.8 or higher
- 100MB free disk space
- 512MB RAM minimum

### Step 1: Clone Repository
```bash
git clone https://github.com/sphasbmthembu-dev/EBATHENJINI.git
cd EBATHENJINI
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Application
```bash
python main.py
```

## Quick Start

### Adding Your First Memory
1. Launch the app
2. Click "➕ Add Memory" button
3. Enter memory details:
   - **Title**: Brief title for the memory
   - **Description**: Detailed description
   - **Date**: When the memory occurred
   - **Photo**: Optional photo
   - **Tags**: Comma-separated tags (e.g., "family,birthday")
4. Click "💾 Save"

### Viewing Memories
1. Click "🖼 View Gallery"
2. Browse all memories
3. Click on a memory to view full details
4. Use search bar to find specific memories
5. Use filter buttons to sort memories

### Searching
1. Go to Gallery
2. Type in search bar
3. Results update in real-time
4. Click memory to view details

### Exporting
1. Go to Gallery
2. Click "📊 Export"
3. Choose format (PDF or CSV)
4. File saved to current directory

### Backup & Restore
1. Go to Settings (⚙)
2. For backup: Click "🔄 Manual Backup"
3. For restore: Click "📥 Restore from Backup"
4. Follow prompts

## Architecture

### Project Structure
```
EBATHENJINI/
├── app/
│   ├── main_app.py          # Main application class
│   ├── screens/             # UI screens
│   ├── database/            # Database management
│   ├── utils/               # Utilities
│   └── assets/              # Media files
├── tests/                   # Test suite
├── main.py                  # Entry point
├── requirements.txt         # Dependencies
└── README.md               # Documentation
```

### Database Schema

```sql
CREATE TABLE memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_memory DATE,
    image_path TEXT,
    tags TEXT
);

CREATE TABLE settings (
    key TEXT PRIMARY KEY,
    value TEXT
);
```

### Data Flow

```
UI Layer (Screens)
      ↓
 Business Logic (Services)
      ↓
 Data Layer (Database Manager)
      ↓
SQLite Database
```

## API Reference

### DatabaseManager

```python
from app.database.db_manager import DatabaseManager

db = DatabaseManager()

# Add memory
memory_id = db.add_memory(
    title="Birthday Party",
    description="Great celebration",
    date_memory="2024-01-15",
    image_path="path/to/image.jpg",
    tags="birthday,family"
)

# Get all memories
memories = db.get_all_memories()

# Get specific memory
memory = db.get_memory(memory_id)

# Update memory
db.update_memory(
    memory_id,
    "Updated Title",
    "Updated Description",
    "2024-01-20"
)

# Delete memory
db.delete_memory(memory_id)

# Search memories
results = db.search_memories("party")

# Get memories by tag
family_memories = db.get_memories_by_tag("family")

# Get all tags
tags = db.get_all_tags()
```

### Helper Functions

```python
from app.utils.helpers import validate_memory_data, get_current_date

# Validate memory
is_valid, error_msg = validate_memory_data("Title", "Description")

# Get current date
today = get_current_date()  # Returns "YYYY-MM-DD"
```

### Export Manager

```python
from app.utils.export_manager import export_to_pdf, export_to_csv

# Export to PDF
export_to_pdf(memories, "output.pdf")

# Export to CSV
export_to_csv(memories, "output.csv")
```

## Configuration

### Settings
```python
from app.database.db_manager import DatabaseManager

db = DatabaseManager()

# Save setting
db.save_setting('theme', 'dark')

# Get setting
theme = db.get_setting('theme', default='light')
```

### Theme Colors

```python
THEME_COLORS = {
    'primary': (0.2, 0.5, 0.8, 1),      # Blue
    'secondary': (0.9, 0.5, 0.2, 1),    # Orange
    'accent': (0.8, 0.2, 0.5, 1),       # Pink
    'background': (0.95, 0.95, 0.95, 1),# Gray
    'text': (0.2, 0.2, 0.2, 1)          # Dark
}
```

### Window Configuration

```python
from kivy.core.window import Window

# Set window size
Window.size = (400, 600)

# Set title
Window.title = 'EBATHENJINI - Memories of Zenande'
```

## Troubleshooting

### App Won't Start

**Error**: `ModuleNotFoundError: No module named 'kivy'`

**Solution**:
```bash
pip install kivy
```

### Database Locked

**Error**: `sqlite3.OperationalError: database is locked`

**Solution**: Close other instances and try again

### Image Not Loading

**Issue**: Photos don't display in memories

**Solution**:
- Check file path is correct
- Verify image format is supported (JPG, PNG)
- Check file permissions

### Export Not Working

**Issue**: Export fails silently

**Solution**:
- Ensure `reportlab` is installed
- Check file write permissions
- Verify images exist if exporting to PDF

### Slow Performance

**Issue**: App is slow with many memories

**Solution**:
- Clear old memories
- Reduce image file sizes
- Restart the app

## File Formats

### Supported Image Formats
- JPG / JPEG
- PNG
- GIF (static only)

### Export Formats
- PDF (with images)
- CSV (data only)

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Esc | Go back to previous screen |
| F5 | Refresh current view |
| Ctrl+S | Save current memory |
| Ctrl+F | Open search |

## Tips & Tricks

1. **Organize with Tags**: Use consistent tag naming for better filtering
2. **Backup Regularly**: Create backups before major updates
3. **Resize Images**: Large images slow down the app; resize to 2MB max
4. **Consistent Dates**: Use YYYY-MM-DD format for better sorting
5. **Export Regularly**: Export important memories for archival

## FAQ

**Q: Can I import memories from other sources?**
A: Currently only supported via CSV files. Import feature coming soon.

**Q: How secure is my data?**
A: Data stored locally on device. Encryption available with backup feature.

**Q: Can I sync across devices?**
A: Use backup/restore feature to transfer between devices.

**Q: What happens if I delete a memory?**
A: Memory is permanently deleted unless you have a backup.

## Support

For issues or feature requests:
1. Check troubleshooting section
2. Review GitHub issues
3. Create new issue with details
4. Contact developers

## License

Personal project - All rights reserved

## Changelog

### v1.0 (Current)
- Initial release
- All core features
- Android/iOS support
- Backup system

---

**Dedicated to Zenande Mthembu** 💙
