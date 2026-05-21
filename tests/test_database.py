"""Unit tests for EBATHENJINI application."""

import unittest
import os
import tempfile
import shutil
from app.database.db_manager import DatabaseManager
from app.utils.helpers import validate_memory_data, get_current_date
from app.utils.export_manager import export_to_pdf, export_to_csv


class TestDatabaseManager(unittest.TestCase):
    """Test cases for DatabaseManager."""

    def setUp(self):
        """Set up test database."""
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, 'test_ebathenjini.db')
        self.db = DatabaseManager(self.db_path)

    def tearDown(self):
        """Clean up test database."""
        shutil.rmtree(self.test_dir)

    def test_add_memory(self):
        """Test adding a memory."""
        memory_id = self.db.add_memory(
            title='First Memory',
            description='This is a test memory',
            date_memory='2024-01-01'
        )
        self.assertIsNotNone(memory_id)
        self.assertEqual(memory_id, 1)

    def test_add_memory_with_tags(self):
        """Test adding memory with tags."""
        memory_id = self.db.add_memory(
            title='Tagged Memory',
            description='Memory with tags',
            date_memory='2024-01-01',
            tags='family,birthday,important'
        )
        memory = self.db.get_memory(memory_id)
        self.assertEqual(memory[6], 'family,birthday,important')

    def test_get_all_memories(self):
        """Test retrieving all memories."""
        self.db.add_memory('Memory 1', 'Description 1', '2024-01-01')
        self.db.add_memory('Memory 2', 'Description 2', '2024-01-02')
        
        memories = self.db.get_all_memories()
        self.assertEqual(len(memories), 2)

    def test_get_memory(self):
        """Test retrieving a specific memory."""
        memory_id = self.db.add_memory('Test', 'Test Description', '2024-01-01')
        memory = self.db.get_memory(memory_id)
        
        self.assertIsNotNone(memory)
        self.assertEqual(memory[1], 'Test')
        self.assertEqual(memory[2], 'Test Description')

    def test_update_memory(self):
        """Test updating a memory."""
        memory_id = self.db.add_memory('Original', 'Original Description', '2024-01-01')
        self.db.update_memory(
            memory_id,
            'Updated',
            'Updated Description',
            '2024-01-02'
        )
        
        memory = self.db.get_memory(memory_id)
        self.assertEqual(memory[1], 'Updated')
        self.assertEqual(memory[2], 'Updated Description')

    def test_delete_memory(self):
        """Test deleting a memory."""
        memory_id = self.db.add_memory('Test', 'Test Description', '2024-01-01')
        self.db.delete_memory(memory_id)
        
        memories = self.db.get_all_memories()
        self.assertEqual(len(memories), 0)

    def test_search_memories(self):
        """Test searching memories."""
        self.db.add_memory('Birthday Party', 'Great celebration', '2024-01-01')
        self.db.add_memory('School Day', 'Normal day', '2024-01-02')
        
        results = self.db.search_memories('Birthday')
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1], 'Birthday Party')

    def test_get_memories_by_tag(self):
        """Test filtering memories by tag."""
        self.db.add_memory('Memory 1', 'Desc 1', '2024-01-01', tags='family')
        self.db.add_memory('Memory 2', 'Desc 2', '2024-01-02', tags='birthday')
        
        results = self.db.get_memories_by_tag('family')
        self.assertEqual(len(results), 1)

    def test_get_all_tags(self):
        """Test retrieving all tags."""
        self.db.add_memory('M1', 'D1', '2024-01-01', tags='family,birthday')
        self.db.add_memory('M2', 'D2', '2024-01-02', tags='school,birthday')
        
        tags = self.db.get_all_tags()
        self.assertIn('family', tags)
        self.assertIn('birthday', tags)
        self.assertIn('school', tags)

    def test_settings(self):
        """Test saving and retrieving settings."""
        self.db.save_setting('theme', 'dark')
        value = self.db.get_setting('theme')
        self.assertEqual(value, 'dark')

    def test_empty_database(self):
        """Test querying empty database."""
        memories = self.db.get_all_memories()
        self.assertEqual(len(memories), 0)


class TestHelperFunctions(unittest.TestCase):
    """Test cases for helper functions."""

    def test_validate_memory_data_valid(self):
        """Test validation with valid data."""
        is_valid, msg = validate_memory_data('Title', 'Description')
        self.assertTrue(is_valid)
        self.assertEqual(msg, '')

    def test_validate_memory_data_empty_title(self):
        """Test validation with empty title."""
        is_valid, msg = validate_memory_data('', 'Description')
        self.assertFalse(is_valid)
        self.assertIn('empty', msg.lower())

    def test_validate_memory_data_empty_description(self):
        """Test validation with empty description."""
        is_valid, msg = validate_memory_data('Title', '')
        self.assertFalse(is_valid)
        self.assertIn('empty', msg.lower())

    def test_validate_memory_data_long_title(self):
        """Test validation with too long title."""
        long_title = 'A' * 101
        is_valid, msg = validate_memory_data(long_title, 'Description')
        self.assertFalse(is_valid)
        self.assertIn('long', msg.lower())

    def test_get_current_date(self):
        """Test current date function."""
        date = get_current_date()
        self.assertIsNotNone(date)
        # Check format YYYY-MM-DD
        parts = date.split('-')
        self.assertEqual(len(parts), 3)


class TestExportFunctionality(unittest.TestCase):
    """Test cases for export functionality."""

    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, 'test_ebathenjini.db')
        self.db = DatabaseManager(self.db_path)

    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)

    def test_export_to_csv(self):
        """Test CSV export."""
        self.db.add_memory('Memory 1', 'Desc 1', '2024-01-01', tags='test')
        memories = self.db.get_all_memories()
        
        csv_file = os.path.join(self.test_dir, 'test_export.csv')
        export_to_csv(memories, csv_file)
        
        self.assertTrue(os.path.exists(csv_file))
        self.assertGreater(os.path.getsize(csv_file), 0)

    def test_export_empty_list(self):
        """Test exporting empty list."""
        csv_file = os.path.join(self.test_dir, 'empty_export.csv')
        export_to_csv([], csv_file)
        
        self.assertTrue(os.path.exists(csv_file))


if __name__ == '__main__':
    unittest.main()
