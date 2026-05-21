"""Gallery screen for viewing and searching memories."""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.garden.filechooser import FileChooserListView


class GalleryScreen(Screen):
    """Screen for viewing and searching memories."""

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.filtered_memories = []
        self.build_ui()

    def build_ui(self):
        """Build the gallery screen UI."""
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(
            text='Memory Gallery',
            size_hint_y=0.08,
            font_size='18sp',
            bold=True
        )
        main_layout.add_widget(header)
        
        # Search bar
        search_layout = BoxLayout(size_hint_y=0.08, spacing=5)
        search_label = Label(text='🔍', size_hint_x=0.1)
        self.search_input = TextInput(
            hint_text='Search memories...',
            multiline=False,
            background_color=(1, 1, 1, 1)
        )
        self.search_input.bind(text=self.on_search_text)
        search_layout.add_widget(search_label)
        search_layout.add_widget(self.search_input)
        main_layout.add_widget(search_layout)
        
        # Filter buttons
        filter_layout = BoxLayout(size_hint_y=0.08, spacing=5)
        
        btn_all = Button(text='All', background_color=self.app.theme_colors['primary'])
        btn_all.bind(on_press=self.filter_all)
        
        btn_recent = Button(text='Recent', background_color=self.app.theme_colors['secondary'])
        btn_recent.bind(on_press=self.filter_recent)
        
        btn_oldest = Button(text='Oldest', background_color=self.app.theme_colors['accent'])
        btn_oldest.bind(on_press=self.filter_oldest)
        
        filter_layout.add_widget(btn_all)
        filter_layout.add_widget(btn_recent)
        filter_layout.add_widget(btn_oldest)
        main_layout.add_widget(filter_layout)
        
        # Memories grid
        scroll = ScrollView(size_hint=(1, 0.7))
        self.memories_grid = GridLayout(
            cols=1,
            spacing=10,
            size_hint_y=None,
            padding=10
        )
        self.memories_grid.bind(minimum_height=self.memories_grid.setter('height'))
        self.load_memories()
        scroll.add_widget(self.memories_grid)
        main_layout.add_widget(scroll)
        
        # Footer buttons
        footer = BoxLayout(size_hint_y=0.08, spacing=10)
        
        btn_export = Button(
            text='📊 Export',
            background_color=self.app.theme_colors['secondary']
        )
        btn_export.bind(on_press=self.export_memories)
        
        btn_back = Button(
            text='🔙 Back',
            background_color=self.app.theme_colors['text']
        )
        btn_back.bind(on_press=self.go_back)
        
        footer.add_widget(btn_export)
        footer.add_widget(btn_back)
        main_layout.add_widget(footer)
        
        self.add_widget(main_layout)

    def load_memories(self):
        """Load and display memories."""
        self.memories_grid.clear_widgets()
        memories = self.app.db.get_all_memories()
        
        if not memories:
            self.memories_grid.add_widget(
                Label(text='No memories found. Create one!', size_hint_y=None, height=50)
            )
            return
        
        for memory in memories:
            memory_card = self.create_memory_card(memory)
            self.memories_grid.add_widget(memory_card)

    def create_memory_card(self, memory):
        """Create a memory card widget."""
        card_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=120,
            padding=10,
            spacing=5
        )
        
        # Title and date
        title_label = Label(
            text=f"📌 {memory[1]}",
            size_hint_y=0.4,
            font_size='14sp',
            bold=True
        )
        card_layout.add_widget(title_label)
        
        # Date
        date_label = Label(
            text=f"📅 {memory[4]}",
            size_hint_y=0.2,
            font_size='10sp'
        )
        card_layout.add_widget(date_label)
        
        # Tags
        if memory[6]:
            tags_label = Label(
                text=f"🏷 {memory[6]}",
                size_hint_y=0.2,
                font_size='10sp'
            )
            card_layout.add_widget(tags_label)
        
        # Buttons
        btn_layout = BoxLayout(size_hint_y=0.2, spacing=5)
        
        btn_view = Button(text='View')
        btn_view.memory_id = memory[0]
        btn_view.bind(on_press=self.view_details)
        
        btn_edit = Button(text='Edit')
        btn_edit.memory_id = memory[0]
        btn_edit.bind(on_press=self.edit_memory)
        
        btn_delete = Button(text='Delete')
        btn_delete.memory_id = memory[0]
        btn_delete.bind(on_press=self.delete_memory)
        
        btn_layout.add_widget(btn_view)
        btn_layout.add_widget(btn_edit)
        btn_layout.add_widget(btn_delete)
        card_layout.add_widget(btn_layout)
        
        return card_layout

    def on_search_text(self, instance, value):
        """Handle search text changes."""
        self.memories_grid.clear_widgets()
        memories = self.app.db.get_all_memories()
        
        search_text = value.lower()
        filtered = [
            m for m in memories
            if search_text in m[1].lower() or search_text in m[2].lower()
        ]
        
        if not filtered:
            self.memories_grid.add_widget(
                Label(text='No memories match your search.', size_hint_y=None, height=50)
            )
            return
        
        for memory in filtered:
            memory_card = self.create_memory_card(memory)
            self.memories_grid.add_widget(memory_card)

    def filter_all(self, instance):
        """Filter all memories."""
        self.search_input.text = ''
        self.load_memories()

    def filter_recent(self, instance):
        """Filter recent memories."""
        self.search_input.text = ''
        self.load_memories()

    def filter_oldest(self, instance):
        """Filter oldest memories."""
        self.search_input.text = ''
        memories = self.app.db.get_all_memories()
        self.memories_grid.clear_widgets()
        
        for memory in reversed(memories):
            memory_card = self.create_memory_card(memory)
            self.memories_grid.add_widget(memory_card)

    def view_details(self, instance):
        """View memory details."""
        self.manager.get_screen('details').load_memory(instance.memory_id)
        self.manager.current = 'details'

    def edit_memory(self, instance):
        """Edit memory."""
        memory = self.app.db.get_memory(instance.memory_id)
        if memory:
            memory_screen = self.manager.get_screen('memory')
            memory_screen.memory_id = memory[0]
            memory_screen.title_input.text = memory[1]
            memory_screen.desc_input.text = memory[2] or ''
            memory_screen.date_input.text = memory[4] or ''
            memory_screen.tags_input.text = memory[6] or ''
            if memory[5]:
                memory_screen.image_preview.source = memory[5]
                memory_screen.selected_image = memory[5]
            self.manager.current = 'memory'

    def delete_memory(self, instance):
        """Delete memory."""
        self.app.db.delete_memory(instance.memory_id)
        self.load_memories()

    def export_memories(self, instance):
        """Export memories to PDF."""
        from app.utils.export_manager import export_to_pdf
        
        memories = self.app.db.get_all_memories()
        if memories:
            try:
                export_to_pdf(memories, 'EBATHENJINI_Export.pdf')
                self.show_alert('Success', 'Exported to EBATHENJINI_Export.pdf')
            except Exception as e:
                self.show_alert('Error', f'Export failed: {str(e)}')
        else:
            self.show_alert('Info', 'No memories to export')

    def show_alert(self, title, message):
        """Show alert popup."""
        from kivy.uix.popup import Popup
        
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))
        
        btn = Button(text='OK', size_hint_y=0.3)
        content.add_widget(btn)
        
        popup = Popup(title=title, content=content, size_hint=(0.9, 0.4))
        btn.bind(on_press=popup.dismiss)
        popup.open()

    def go_back(self, instance):
        """Go back to home screen."""
        self.manager.current = 'home'
