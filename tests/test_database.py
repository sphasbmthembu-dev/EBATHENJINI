"""Unit tests for database manager."""

import unittest
import os
from app.database.db_manager import DatabaseManager


class TestDatabaseManager(unittest.TestCase):
    """Test cases for DatabaseManager."""

    def setUp(self):
        """Set up test database."""
        self.db_path = 'test_ebathenjini.db'
        self.db = DatabaseManager(self.db_path)

    def tearDown(self):
        """Clean up test database."""
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_add_memory(self):
        """Test adding a memory."""
        memory_id = self.db.add_memory(
            title='First Memory',
            description='This is a test memory',
            date_memory='2024-01-01'
        )
        self.assertIsNotNone(memory_id)
        self.assertEqual(memory_id, 1)

    def test_get_all_memories(self):
        """Test retrieving all memories."""
        self.db.add_memory('Memory 1', 'Description 1', '2024-01-01')
        self.db.add_memory('Memory 2', 'Description 2', '2024-01-02')
        
        memories = self.db.get_all_memories()
        self.assertEqual(len(memories), 2)

    def test_delete_memory(self):
        """Test deleting a memory."""
        memory_id = self.db.add_memory('Test', 'Test Description', '2024-01-01')
        self.db.delete_memory(memory_id)
        
        memories = self.db.get_all_memories()
        self.assertEqual(len(memories), 0)


if __name__ == '__main__':
    unittest.main()
