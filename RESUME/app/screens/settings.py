from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton,MDRectangleFlatButton
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


class SettingsScreen(MDScreen):
    def __init__(self,**kwargs):
        super(SettingsScreen,self).__init__(**kwargs)
        self.theme_cls.theme_style = 'Light'
        self.name="settings"
        layout=MDBoxLayout(orientation="vertical",padding=30,spacing=20)
        button1=MDRaisedButton(text="main",pos_hint={'center_x':0.5},on_press=self.switch_to_main)
        layout.add_widget(button1)
        content=self.create_content()
        layout.add_widget(content)
        self.add_widget(layout)
    
    def create_content(self):
        content = MDBoxLayout(orientation='vertical', padding=10)

        path_label=MDLabel(text="Selected Path:")
        content.add_widget(path_label)

        # Text field for displaying selected path
        self.path_field = MDTextField(readonly=True, multiline=False)
        content.add_widget(self.path_field)

        # Button to open file manager
        choose_button = MDRaisedButton(text="Choose Path", on_release=self.show_file_chooser)
        content.add_widget(choose_button)
        return content

    def switch_to_main(self,instance):
        self.manager.current="Home"

    def show_file_chooser(self):
        from kivymd.uix.filemanager import MDFileManager

        manager=MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path
        )
        manager.show('/')
    
    def exit_manager(self, *args):
        # Function to handle closing the file manager
        pass

    def select_path(self, path):
        # Function to handle the selected path
        self.path_field.text = path  # Update the text field with the selected path


       