"""Memory screen for adding/editing memories."""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.garden.filebrowser import FileBrowser
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from datetime import datetime
import os
import shutil


class MemoryScreen(Screen):
    """Screen for adding and editing memories."""

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.memory_id = None
        self.selected_image = None
        self.build_ui()

    def build_ui(self):
        """Build the memory screen UI."""
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(
            text='Add/Edit Memory',
            size_hint_y=0.08,
            font_size='18sp',
            bold=True
        )
        main_layout.add_widget(header)
        
        # Scrollable content
        scroll = ScrollView(size_hint=(1, 0.8))
        content = GridLayout(cols=1, spacing=10, size_hint_y=None, padding=10)
        content.bind(minimum_height=content.setter('height'))
        
        # Title input
        title_label = Label(
            text='Memory Title:',
            size_hint_y=None,
            height=30,
            font_size='12sp'
        )
        content.add_widget(title_label)
        
        self.title_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=40,
            background_color=(1, 1, 1, 1)
        )
        content.add_widget(self.title_input)
        
        # Description input
        desc_label = Label(
            text='Description:',
            size_hint_y=None,
            height=30,
            font_size='12sp'
        )
        content.add_widget(desc_label)
        
        self.desc_input = TextInput(
            multiline=True,
            size_hint_y=None,
            height=100,
            background_color=(1, 1, 1, 1)
        )
        content.add_widget(self.desc_input)
        
        # Date picker
        date_label = Label(
            text='Date:',
            size_hint_y=None,
            height=30,
            font_size='12sp'
        )
        content.add_widget(date_label)
        
        self.date_input = TextInput(
            text=datetime.now().strftime('%Y-%m-%d'),
            multiline=False,
            size_hint_y=None,
            height=40,
            background_color=(1, 1, 1, 1)
        )
        content.add_widget(self.date_input)
        
        # Tags input
        tags_label = Label(
            text='Tags (comma-separated):',
            size_hint_y=None,
            height=30,
            font_size='12sp'
        )
        content.add_widget(tags_label)
        
        self.tags_input = TextInput(
            multiline=False,
            size_hint_y=None,
            height=40,
            background_color=(1, 1, 1, 1)
        )
        content.add_widget(self.tags_input)
        
        # Image section
        img_label = Label(
            text='Photo:',
            size_hint_y=None,
            height=30,
            font_size='12sp'
        )
        content.add_widget(img_label)
        
        btn_upload = Button(
            text='📷 Upload Photo',
            size_hint_y=None,
            height=50,
            background_color=self.app.theme_colors['secondary']
        )
        btn_upload.bind(on_press=self.show_file_chooser)
        content.add_widget(btn_upload)
        
        self.image_preview = Image(
            size_hint_y=None,
            height=100
        )
        content.add_widget(self.image_preview)
        
        scroll.add_widget(content)
        main_layout.add_widget(scroll)
        
        # Buttons footer
        footer = GridLayout(cols=2, size_hint_y=0.12, spacing=10)
        
        btn_save = Button(
            text='💾 Save',
            background_color=self.app.theme_colors['primary']
        )
        btn_save.bind(on_press=self.save_memory)
        
        btn_cancel = Button(
            text='❌ Cancel',
            background_color=self.app.theme_colors['text']
        )
        btn_cancel.bind(on_press=self.go_back)
        
        footer.add_widget(btn_save)
        footer.add_widget(btn_cancel)
        main_layout.add_widget(footer)
        
        self.add_widget(main_layout)

    def show_file_chooser(self, instance):
        """Show file chooser for image upload."""
        content = BoxLayout(orientation='vertical')
        
        filechooser = FileChooserListView(
            filters=['*.png', '*.jpg', '*.jpeg']
        )
        content.add_widget(filechooser)
        
        btn_layout = BoxLayout(size_hint_y=0.1, spacing=10)
        
        btn_select = Button(text='Select')
        btn_cancel = Button(text='Cancel')
        
        btn_layout.add_widget(btn_select)
        btn_layout.add_widget(btn_cancel)
        content.add_widget(btn_layout)
        
        popup = Popup(
            title='Select Image',
            content=content,
            size_hint=(0.9, 0.9)
        )
        
        def select_image(instance):
            if filechooser.selection:
                self.selected_image = filechooser.selection[0]
                self.image_preview.source = self.selected_image
                popup.dismiss()
        
        def close_popup(instance):
            popup.dismiss()
        
        btn_select.bind(on_press=select_image)
        btn_cancel.bind(on_press=close_popup)
        
        popup.open()

    def save_memory(self, instance):
        """Save memory to database."""
        from app.utils.helpers import validate_memory_data
        
        title = self.title_input.text
        description = self.desc_input.text
        date = self.date_input.text
        tags = self.tags_input.text
        
        # Validate
        is_valid, error_msg = validate_memory_data(title, description)
        if not is_valid:
            self.show_alert('Error', error_msg)
            return
        
        # Copy image if selected
        image_path = None
        if self.selected_image:
            # Create assets folder if not exists
            os.makedirs('app/assets/images', exist_ok=True)
            dest_path = f'app/assets/images/{os.path.basename(self.selected_image)}'
            shutil.copy(self.selected_image, dest_path)
            image_path = dest_path
        
        # Save to database
        self.app.db.add_memory(
            title=title,
            description=description,
            date_memory=date,
            image_path=image_path,
            tags=tags
        )
        
        self.show_alert('Success', 'Memory saved successfully!')
        self.clear_inputs()
        self.manager.current = 'home'

    def clear_inputs(self):
        """Clear all input fields."""
        self.title_input.text = ''
        self.desc_input.text = ''
        self.date_input.text = datetime.now().strftime('%Y-%m-%d')
        self.tags_input.text = ''
        self.selected_image = None
        self.image_preview.source = ''

    def show_alert(self, title, message):
        """Show alert popup."""
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
