"""Memory details screen."""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image


class MemoryDetailsScreen(Screen):
    """Screen for viewing memory details."""

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.current_memory = None
        self.memory_id = None

    def load_memory(self, memory_id):
        """Load a memory by ID."""
        self.memory_id = memory_id
        self.current_memory = self.app.db.get_memory(memory_id)
        self.clear_widgets()
        self.build_ui()

    def build_ui(self):
        """Build the details screen UI."""
        if not self.current_memory:
            self.add_widget(Label(text='Memory not found'))
            return
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(
            text='Memory Details',
            size_hint_y=0.08,
            font_size='18sp',
            bold=True
        )
        main_layout.add_widget(header)
        
        # Scrollable content
        scroll = ScrollView(size_hint=(1, 0.8))
        content = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=10)
        content.bind(minimum_height=content.setter('height'))
        
        # Title
        title_label = Label(
            text=f"📌 {self.current_memory[1]}",
            size_hint_y=None,
            height=40,
            font_size='16sp',
            bold=True
        )
        content.add_widget(title_label)
        
        # Date
        date_label = Label(
            text=f"📅 {self.current_memory[4]}",
            size_hint_y=None,
            height=30,
            font_size='12sp'
        )
        content.add_widget(date_label)
        
        # Image
        if self.current_memory[5]:
            image = Image(
                source=self.current_memory[5],
                size_hint_y=None,
                height=200
            )
            content.add_widget(image)
        
        # Description
        desc_label = Label(
            text='Description:',
            size_hint_y=None,
            height=25,
            font_size='12sp',
            bold=True
        )
        content.add_widget(desc_label)
        
        desc_text = Label(
            text=self.current_memory[2] or 'No description',
            size_hint_y=None,
            height=100,
            font_size='11sp',
            text_size=(self.width - 20, None)
        )
        content.add_widget(desc_text)
        
        # Tags
        if self.current_memory[6]:
            tags_label = Label(
                text='Tags:',
                size_hint_y=None,
                height=25,
                font_size='12sp',
                bold=True
            )
            content.add_widget(tags_label)
            
            tags_text = Label(
                text=f"🏷 {self.current_memory[6]}",
                size_hint_y=None,
                height=40,
                font_size='11sp'
            )
            content.add_widget(tags_text)
        
        scroll.add_widget(content)
        main_layout.add_widget(scroll)
        
        # Footer buttons
        footer = BoxLayout(size_hint_y=0.12, spacing=10)
        
        btn_edit = Button(
            text='✏️ Edit',
            background_color=self.app.theme_colors['secondary']
        )
        btn_edit.bind(on_press=self.edit_memory)
        
        btn_delete = Button(
            text='🗑️ Delete',
            background_color=self.app.theme_colors['accent']
        )
        btn_delete.bind(on_press=self.delete_memory)
        
        btn_back = Button(
            text='🔙 Back',
            background_color=self.app.theme_colors['text']
        )
        btn_back.bind(on_press=self.go_back)
        
        footer.add_widget(btn_edit)
        footer.add_widget(btn_delete)
        footer.add_widget(btn_back)
        main_layout.add_widget(footer)
        
        self.add_widget(main_layout)

    def edit_memory(self, instance):
        """Edit the current memory."""
        memory_screen = self.manager.get_screen('memory')
        memory_screen.memory_id = self.memory_id
        memory_screen.title_input.text = self.current_memory[1]
        memory_screen.desc_input.text = self.current_memory[2] or ''
        memory_screen.date_input.text = self.current_memory[4] or ''
        memory_screen.tags_input.text = self.current_memory[6] or ''
        if self.current_memory[5]:
            memory_screen.image_preview.source = self.current_memory[5]
            memory_screen.selected_image = self.current_memory[5]
        self.manager.current = 'memory'

    def delete_memory(self, instance):
        """Delete the current memory."""
        self.app.db.delete_memory(self.memory_id)
        self.manager.current = 'home'

    def go_back(self, instance):
        """Go back to gallery."""
        self.manager.current = 'gallery'
