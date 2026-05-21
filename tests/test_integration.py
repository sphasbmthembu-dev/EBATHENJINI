"""Integration tests for EBATHENJINI screens."""

import unittest
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from app.main_app import EbathenjiniApp
from app.database.db_manager import DatabaseManager
import tempfile
import shutil
import os


class TestScreenIntegration(unittest.TestCase):
    """Integration tests for app screens."""

    def setUp(self):
        """Set up test environment."""
        self.test_dir = tempfile.mkdtemp()
        self.db_path = os.path.join(self.test_dir, 'test_ebathenjini.db')
        # Create a simple test app
        self.app = EbathenjiniApp()
        self.app.db = DatabaseManager(self.db_path)

    def tearDown(self):
        """Clean up test environment."""
        shutil.rmtree(self.test_dir)

    def test_home_screen_creation(self):
        """Test home screen creation."""
        self.assertIsNotNone(self.app)
        self.assertEqual(self.app.title, 'EBATHENJINI - Memories of Zenande')

    def test_database_initialization(self):
        """Test database initialization."""
        self.assertIsNotNone(self.app.db)
        self.assertTrue(os.path.exists(self.db_path))

    def test_theme_colors(self):
        """Test theme colors are set."""
        self.assertIn('primary', self.app.theme_colors)
        self.assertIn('secondary', self.app.theme_colors)
        self.assertIn('accent', self.app.theme_colors)
        self.assertIn('background', self.app.theme_colors)
        self.assertIn('text', self.app.theme_colors)


if __name__ == '__main__':
    unittest.main()
