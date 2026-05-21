"""Database manager for storing and retrieving memories."""

import sqlite3
import os
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
