"""Main Kivy application class for EBATHENJINI."""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from app.screens.home_screen import HomeScreen
from app.screens.memory_screen import MemoryScreen
from app.screens.gallery_screen import GalleryScreen
from app.screens.memory_details_screen import MemoryDetailsScreen
from app.screens.settings_screen import SettingsScreen
from app.database.db_manager import DatabaseManager

# Set window size
Window.size = (400, 600)

# Theme colors
THEME_COLORS = {
    'primary': (0.2, 0.5, 0.8, 1),      # Blue
    'secondary': (0.9, 0.5, 0.2, 1),    # Orange
    'accent': (0.8, 0.2, 0.5, 1),       # Pink
    'background': (0.95, 0.95, 0.95, 1), # Light gray
    'text': (0.2, 0.2, 0.2, 1),         # Dark gray
}


class EbathenjiniApp(App):
    """Main EBATHENJINI Application."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'EBATHENJINI - Memories of Zenande'
        self.db = DatabaseManager()
        self.theme_colors = THEME_COLORS

    def build(self):
        """Build and return the root widget."""
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(HomeScreen(name='home', app=self))
        sm.add_widget(MemoryScreen(name='memory', app=self))
        sm.add_widget(GalleryScreen(name='gallery', app=self))
        sm.add_widget(MemoryDetailsScreen(name='details', app=self))
        sm.add_widget(SettingsScreen(name='settings', app=self))
        
        return sm
