"""Settings screen."""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
import os
import shutil
from datetime import datetime


class SettingsScreen(Screen):
    """Settings screen for app configuration."""

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.build_ui()

    def build_ui(self):
        """Build the settings screen UI."""
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(
            text='Settings',
            size_hint_y=0.08,
            font_size='18sp',
            bold=True
        )
        main_layout.add_widget(header)
        
        # Scrollable content
        scroll = ScrollView(size_hint=(1, 0.8))
        content = GridLayout(cols=1, spacing=15, size_hint_y=None, padding=10)
        content.bind(minimum_height=content.setter('height'))
        
        # Theme section
        theme_label = Label(
            text='🎨 Theme',
            size_hint_y=None,
            height=30,
            font_size='14sp',
            bold=True
        )
        content.add_widget(theme_label)
        
        theme_spinner = Spinner(
            text='Light',
            values=('Light', 'Dark'),
            size_hint_y=None,
            height=40
        )
        content.add_widget(theme_spinner)
        
        # Notifications section
        notif_label = Label(
            text='🔔 Notifications',
            size_hint_y=None,
            height=30,
            font_size='14sp',
            bold=True
        )
        content.add_widget(notif_label)
        
        notif_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        notif_layout.add_widget(Label(text='Enable Notifications'))
        notif_checkbox = CheckBox(active=True)
        notif_layout.add_widget(notif_checkbox)
        content.add_widget(notif_layout)
        
        # Auto-backup section
        backup_label = Label(
            text='💾 Auto-Backup',
            size_hint_y=None,
            height=30,
            font_size='14sp',
            bold=True
        )
        content.add_widget(backup_label)
        
        backup_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        backup_layout.add_widget(Label(text='Enable Auto-Backup'))
        backup_checkbox = CheckBox(active=True)
        backup_layout.add_widget(backup_checkbox)
        content.add_widget(backup_layout)
        
        # Data management section
        data_label = Label(
            text='📊 Data Management',
            size_hint_y=None,
            height=30,
            font_size='14sp',
            bold=True
        )
        content.add_widget(data_label)
        
        btn_backup = Button(
            text='🔄 Manual Backup',
            size_hint_y=None,
            height=50,
            background_color=self.app.theme_colors['secondary']
        )
        btn_backup.bind(on_press=self.backup_data)
        content.add_widget(btn_backup)
        
        btn_restore = Button(
            text='📥 Restore from Backup',
            size_hint_y=None,
            height=50,
            background_color=self.app.theme_colors['accent']
        )
        btn_restore.bind(on_press=self.restore_data)
        content.add_widget(btn_restore)
        
        # About section
        about_label = Label(
            text='ℹ️ About',
            size_hint_y=None,
            height=30,
            font_size='14sp',
            bold=True
        )
        content.add_widget(about_label)
        
        about_text = Label(
            text='EBATHENJINI v1.0\nA memory app dedicated to Zenande\n\n© 2024 Personal Project',
            size_hint_y=None,
            height=80,
            font_size='11sp'
        )
        content.add_widget(about_text)
        
        scroll.add_widget(content)
        main_layout.add_widget(scroll)
        
        # Footer button
        footer = BoxLayout(size_hint_y=0.12, spacing=10)
        
        btn_back = Button(
            text='🔙 Back',
            background_color=self.app.theme_colors['text']
        )
        btn_back.bind(on_press=self.go_back)
        
        footer.add_widget(btn_back)
        main_layout.add_widget(footer)
        
        self.add_widget(main_layout)

    def backup_data(self, instance):
        """Backup database and images."""
        try:
            # Create backup directory
            backup_dir = f'backups/EBATHENJINI_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
            os.makedirs(backup_dir, exist_ok=True)
            
            # Backup database
            if os.path.exists('ebathenjini.db'):
                shutil.copy('ebathenjini.db', f'{backup_dir}/ebathenjini.db')
            
            # Backup images
            if os.path.exists('app/assets/images'):
                shutil.copytree('app/assets/images', f'{backup_dir}/images')
            
            self.show_alert('Success', f'Backup created: {backup_dir}')
        except Exception as e:
            self.show_alert('Error', f'Backup failed: {str(e)}')

    def restore_data(self, instance):
        """Restore from backup."""
        self.show_alert('Info', 'Select backup folder to restore')

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
