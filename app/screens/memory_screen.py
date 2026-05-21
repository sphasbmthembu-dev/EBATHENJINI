"""Memory screen for adding/viewing memories."""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MemoryScreen(Screen):
    """Screen for managing memories."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Memory Manager')
        layout.add_widget(label)
        self.add_widget(layout)
