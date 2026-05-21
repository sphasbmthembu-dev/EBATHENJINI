"""Main Kivy application class for EBATHENJINI."""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    """Home screen of the application."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title = Label(
            text='EBATHENJINI\nMemories of Zenande',
            size_hint_y=0.3,
            font_size='24sp'
        )
        layout.add_widget(title)
        
        # Buttons
        btn_add = Button(text='Add Memory', size_hint_y=0.2)
        btn_view = Button(text='View Memories', size_hint_y=0.2)
        btn_settings = Button(text='Settings', size_hint_y=0.2)
        
        layout.add_widget(btn_add)
        layout.add_widget(btn_view)
        layout.add_widget(btn_settings)
        
        self.add_widget(layout)


class EbathenjiniApp(App):
    """Main EBATHENJINI Application."""

    def build(self):
        """Build and return the root widget."""
        return HomeScreen()
