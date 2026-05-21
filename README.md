# EBATHENJINI

A mobile application that portrays memories of my first-born son, Zenande Mthembu.

## Project Overview

EBATHENJINI is a Python-based mobile application dedicated to preserving and celebrating memories of Zenande. This app allows you to store, view, search, and reflect on precious moments and memories with a beautiful, intuitive interface.

## Tech Stack

- **Framework**: Kivy (Python mobile framework)
- **Language**: Python 3.8+
- **Database**: SQLite (for local storage)
- **Export**: ReportLab (PDF export)
- **OS Support**: iOS, Android, Windows, macOS, Linux

## Features ✨

### Core Features
- ✅ **Add Memories** - Create new memories with title, description, date, photos, and tags
- ✅ **Photo Upload** - Attach photos to memories with image preview
- ✅ **Memory Gallery** - View all memories in a beautiful gallery layout
- ✅ **Memory Details** - View full details of individual memories
- ✅ **Edit Memories** - Modify existing memories anytime
- ✅ **Delete Memories** - Remove memories (with confirmation)

### Search & Organization
- ✅ **Search Functionality** - Search memories by title, description, or content
- ✅ **Filter Options** - Filter by recent, oldest, or all memories
- ✅ **Tags System** - Organize memories with custom tags
- ✅ **Tag Filtering** - Filter memories by specific tags

### Export & Backup
- ✅ **PDF Export** - Export memories to PDF format
- ✅ **CSV Export** - Export to CSV for data analysis
- ✅ **Manual Backup** - Backup database and images
- ✅ **Auto-Backup** - Automatic backup settings
- ✅ **Data Restore** - Restore from previous backups

### UI/UX
- ✅ **Beautiful Design** - Modern, intuitive interface
- ✅ **Color Themes** - Multiple theme options
- ✅ **Smooth Navigation** - Easy screen transitions
- ✅ **Responsive Layout** - Works on all screen sizes

### Settings
- ✅ **Theme Settings** - Light/Dark mode
- ✅ **Notifications** - Enable/disable notifications
- ✅ **Data Management** - Backup and restore options
- ✅ **App Info** - Version and attribution

## Project Structure

```
EBATHENJINI/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── main.py                   # Application entry point
├── app/
│   ├── __init__.py
│   ├── main_app.py          # Main Kivy app class
│   ├── screens/             # App screens
│   │   ├── __init__.py
│   │   ├── home_screen.py
│   │   ├── memory_screen.py
│   │   ├── gallery_screen.py
│   │   ├── memory_details_screen.py
│   │   └── settings_screen.py
│   ├── database/            # Database operations
│   │   ├── __init__.py
│   │   └── db_manager.py
│   ├── assets/              # Images and media
│   │   └── images/
│   └── utils/               # Utility functions
│       ├── __init__.py
│       ├── helpers.py
│       └── export_manager.py
├── tests/                   # Unit tests
│   ├── __init__.py
│   └── test_database.py
├── backups/                 # Backup storage
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sphasbmthembu-dev/EBATHENJINI.git
   cd EBATHENJINI
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## Usage

### Adding a Memory
1. Click "➕ Add Memory" from home screen
2. Enter title, description, and date
3. Add optional photo and tags
4. Click "💾 Save"

### Viewing Memories
1. Click "🖼 View Gallery" to see all memories
2. Click on a memory to view full details
3. Use search bar to find specific memories
4. Use filter buttons to sort memories

### Editing Memories
1. Go to gallery
2. Find the memory you want to edit
3. Click "Edit" button
4. Modify the details
5. Click "💾 Save"

### Exporting Memories
1. Go to gallery
2. Click "📊 Export" button
3. Choose format (PDF or CSV)
4. File will be saved in the project directory

### Backup & Restore
1. Go to Settings (⚙)
2. Click "💾 Manual Backup" to create backup
3. Backups are saved in `backups/` folder
4. Click "📥 Restore from Backup" to restore

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Creating a new feature

1. Create a new branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and test

3. Commit your work
   ```bash
   git add .
   git commit -m "Add: description of your feature"
   ```

4. Push to GitHub
   ```bash
   git push origin feature/your-feature-name
   ```

5. Create a Pull Request

## Resources

- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Python Documentation](https://docs.python.org/)
- [SQLite Tutorial](https://www.sqlite.org/lang.html)
- [ReportLab PDF Library](https://www.reportlab.com/)

## Future Enhancements

- [ ] Cloud sync integration
- [ ] Multiple user profiles
- [ ] Video support
- [ ] Memory reminders
- [ ] Sharing via email/social media
- [ ] Timeline view
- [ ] Memory statistics and analytics
- [ ] Voice notes
- [ ] Weather info for memories

## License

Personal project - All rights reserved

---

**Dedicated to Zenande Mthembu** 💙

*"Memories are treasures of the heart"*
