"""Home screen component."""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class HomeScreen(Screen):
    """Home screen of the application."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Welcome to EBATHENJINI')
        layout.add_widget(label)
        self.add_widget(layout)
