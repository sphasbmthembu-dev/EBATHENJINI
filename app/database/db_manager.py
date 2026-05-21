"""Database manager for storing and retrieving memories."""

import sqlite3
import os
import json
from datetime import datetime


class DatabaseManager:
    """Manages SQLite database operations for memories."""

    def __init__(self, db_path='ebathenjini.db'):
        """Initialize database manager.
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Initialize database tables."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                date_memory DATE,
                image_path TEXT,
                tags TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        ''')
        
        conn.commit()
        conn.close()

    def add_memory(self, title, description, date_memory, image_path=None, tags=None):
        """Add a new memory to database.
        
        Args:
            title: Memory title
            description: Memory description
            date_memory: Date of the memory
            image_path: Path to associated image
            tags: Comma-separated tags
        
        Returns:
            Memory ID
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO memories (title, description, date_memory, image_path, tags)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, description, date_memory, image_path, tags))
        
        conn.commit()
        memory_id = cursor.lastrowid
        conn.close()
        
        return memory_id

    def get_all_memories(self):
        """Retrieve all memories from database.
        
        Returns:
            List of memory tuples
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM memories ORDER BY date_memory DESC')
        memories = cursor.fetchall()
        
        conn.close()
        return memories

    def get_memory(self, memory_id):
        """Retrieve a specific memory.
        
        Args:
            memory_id: ID of the memory
        
        Returns:
            Memory tuple or None
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM memories WHERE id = ?', (memory_id,))
        memory = cursor.fetchone()
        
        conn.close()
        return memory

    def update_memory(self, memory_id, title, description, date_memory, image_path=None, tags=None):
        """Update an existing memory.
        
        Args:
            memory_id: ID of the memory to update
            title: New title
            description: New description
            date_memory: New date
            image_path: New image path
            tags: New tags
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE memories
            SET title=?, description=?, date_memory=?, image_path=?, tags=?
            WHERE id=?
        ''', (title, description, date_memory, image_path, tags, memory_id))
        
        conn.commit()
        conn.close()

    def delete_memory(self, memory_id):
        """Delete a memory from database.
        
        Args:
            memory_id: ID of the memory to delete
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM memories WHERE id = ?', (memory_id,))
        
        conn.commit()
        conn.close()

    def search_memories(self, query):
        """Search memories by title or description.
        
        Args:
            query: Search query
        
        Returns:
            List of matching memory tuples
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM memories
            WHERE title LIKE ? OR description LIKE ? OR tags LIKE ?
            ORDER BY date_memory DESC
        ''', (f'%{query}%', f'%{query}%', f'%{query}%'))
        memories = cursor.fetchall()
        
        conn.close()
        return memories

    def get_memories_by_tag(self, tag):
        """Get memories with a specific tag.
        
        Args:
            tag: Tag to search for
        
        Returns:
            List of memory tuples
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM memories
            WHERE tags LIKE ?
            ORDER BY date_memory DESC
        ''', (f'%{tag}%',))
        memories = cursor.fetchall()
        
        conn.close()
        return memories

    def get_all_tags(self):
        """Get all unique tags.
        
        Returns:
            List of unique tags
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT DISTINCT tags FROM memories')
        rows = cursor.fetchall()
        
        conn.close()
        
        # Parse tags
        tags_set = set()
        for row in rows:
            if row[0]:
                tags_set.update([t.strip() for t in row[0].split(',')])
        
        return sorted(list(tags_set))

    def save_setting(self, key, value):
        """Save a setting.
        
        Args:
            key: Setting key
            value: Setting value
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO settings (key, value)
            VALUES (?, ?)
        ''', (key, value))
        
        conn.commit()
        conn.close()

    def get_setting(self, key, default=None):
        """Get a setting.
        
        Args:
            key: Setting key
            default: Default value if not found
        
        Returns:
            Setting value
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT value FROM settings WHERE key = ?', (key,))
        result = cursor.fetchone()
        
        conn.close()
        
        return result[0] if result else default
