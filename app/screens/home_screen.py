"""Home screen component."""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from datetime import datetime


class HomeScreen(Screen):
    """Home screen of the application."""

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.build_ui()

    def build_ui(self):
        """Build the home screen UI."""
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = BoxLayout(size_hint_y=0.15, padding=10)
        header.canvas.before.clear()
        from kivy.graphics import Color, Rectangle
        with header.canvas.before:
            Color(*self.app.theme_colors['primary'])
            Rectangle(size=header.size, pos=header.pos)
        
        title = Label(
            text='EBATHENJINI\nMemories of Zenande',
            size_hint_y=1,
            font_size='20sp',
            bold=True,
            color=(1, 1, 1, 1)
        )
        header.add_widget(title)
        main_layout.add_widget(header)
        
        # Stats section
        stats_layout = GridLayout(cols=3, size_hint_y=0.15, spacing=10, padding=10)
        memories = self.app.db.get_all_memories()
        memory_count = len(memories)
        
        # Count memories by tag
        tags_count = {}
        for memory in memories:
            if memory[6]:  # tags column
                for tag in memory[6].split(','):
                    tag = tag.strip()
                    tags_count[tag] = tags_count.get(tag, 0) + 1
        
        stat1 = Label(
            text=f'Memories\n{memory_count}',
            size_hint_x=0.33,
            font_size='14sp',
            bold=True
        )
        stat2 = Label(
            text=f'Tags\n{len(tags_count)}',
            size_hint_x=0.33,
            font_size='14sp',
            bold=True
        )
        stat3 = Label(
            text='Love\n∞',
            size_hint_x=0.33,
            font_size='14sp',
            bold=True
        )
        
        stats_layout.add_widget(stat1)
        stats_layout.add_widget(stat2)
        stats_layout.add_widget(stat3)
        main_layout.add_widget(stats_layout)
        
        # Buttons section
        buttons_layout = GridLayout(cols=2, size_hint_y=0.4, spacing=10, padding=10)
        
        btn_add = Button(
            text='➕ Add Memory',
            size_hint=(0.5, 0.5),
            background_color=self.app.theme_colors['primary']
        )
        btn_add.bind(on_press=self.goto_memory)
        
        btn_gallery = Button(
            text='🖼 View Gallery',
            size_hint=(0.5, 0.5),
            background_color=self.app.theme_colors['secondary']
        )
        btn_gallery.bind(on_press=self.goto_gallery)
        
        btn_search = Button(
            text='🔍 Search',
            size_hint=(0.5, 0.5),
            background_color=self.app.theme_colors['accent']
        )
        btn_search.bind(on_press=self.goto_search)
        
        btn_settings = Button(
            text='⚙ Settings',
            size_hint=(0.5, 0.5),
            background_color=self.app.theme_colors['text']
        )
        btn_settings.bind(on_press=self.goto_settings)
        
        buttons_layout.add_widget(btn_add)
        buttons_layout.add_widget(btn_gallery)
        buttons_layout.add_widget(btn_search)
        buttons_layout.add_widget(btn_settings)
        main_layout.add_widget(buttons_layout)
        
        # Recent memories
        recent_label = Label(
            text='Recent Memories',
            size_hint_y=0.05,
            font_size='16sp',
            bold=True
        )
        main_layout.add_widget(recent_label)
        
        recent_layout = BoxLayout(orientation='vertical', size_hint_y=0.25)
        if memories:
            for memory in memories[:3]:
                memory_btn = Button(
                    text=f"{memory[1]}\n{memory[4]}",
                    size_hint_y=0.33
                )
                memory_btn.memory_id = memory[0]
                memory_btn.bind(on_press=self.view_memory_details)
                recent_layout.add_widget(memory_btn)
        else:
            empty_label = Label(
                text='No memories yet. Add one!',
                color=self.app.theme_colors['text']
            )
            recent_layout.add_widget(empty_label)
        
        main_layout.add_widget(recent_layout)
        self.add_widget(main_layout)

    def goto_memory(self, instance):
        """Navigate to memory screen."""
        self.manager.current = 'memory'

    def goto_gallery(self, instance):
        """Navigate to gallery screen."""
        self.manager.current = 'gallery'

    def goto_search(self, instance):
        """Navigate to search (gallery with search)."""
        self.manager.current = 'gallery'
        # TODO: Set search mode in gallery screen

    def goto_settings(self, instance):
        """Navigate to settings screen."""
        self.manager.current = 'settings'

    def view_memory_details(self, instance):
        """View memory details."""
        memory_id = instance.memory_id
        self.manager.get_screen('details').load_memory(memory_id)
        self.manager.current = 'details'
