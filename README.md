# EBATHENJINI

A mobile application that portrays memories of my first-born son, Zenande Mthembu.

## Project Overview

EBATHENJINI is a Python-based mobile application dedicated to preserving and celebrating memories of Zenande. This app allows you to store, view, and reflect on precious moments and memories.

## Tech Stack

- **Framework**: Kivy (Python mobile framework)
- **Language**: Python 3.8+
- **Database**: SQLite (for local storage)
- **OS Support**: iOS, Android, Windows, macOS, Linux

## Project Structure

```
EBATHENJINI/
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── main.py                   # Application entry point
├── app/
│   ├── __init__.py
│   ├── main_app.py          # Main Kivy app class
│   ├── screens/             # Different app screens
│   │   ├── __init__.py
│   │   ├── home_screen.py
│   │   └── memory_screen.py
│   ├── database/            # Database operations
│   │   ├── __init__.py
│   │   └── db_manager.py
│   ├── assets/              # Images, icons, fonts
│   │   └── images/
│   └── utils/               # Utility functions
│       ├── __init__.py
│       └── helpers.py
├── tests/                   # Unit tests
│   ├── __init__.py
│   └── test_database.py
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

## Features (Planned)

- [ ] Create and store memories (text, photos, dates)
- [ ] View memory gallery
- [ ] Search and filter memories
- [ ] Add tags to memories
- [ ] Beautiful UI with intuitive navigation
- [ ] Local data storage with SQLite

## Development

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

## License

Personal project - All rights reserved

---

**Dedicated to Zenande Mthembu** 💙
