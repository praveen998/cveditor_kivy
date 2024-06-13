from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.filechooser import FileChooserListView
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar import MDTopAppBar


class FileChooserScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "filechooser"

        # Layout
        layout = MDBoxLayout(orientation='vertical')


        # Toolbar
        toolbar = MDTopAppBar(title="File Chooser")
        toolbar.md_bg_color = self.theme_cls.primary_color
        toolbar.left_action_items = [["arrow-left", lambda x: self.switch_to_home()]]
        layout.add_widget(toolbar)


        # FileChooser
        self.filechooser = FileChooserListView()
        layout.add_widget(self.filechooser)


        # Select button
        select_button = MDRaisedButton(
            text="Select File",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=self.select_file
        )

        layout.add_widget(select_button)

        self.add_widget(layout)

    def switch_to_home(self):
        self.manager.current = "Home"


    def select_file(self, instance):
        selected = self.filechooser.selection
        if selected:
            file_path = selected[0]
            dialog = MDDialog(
                title="Selected File",
                text=f"File path: {file_path}",
                buttons=[
                    MDRaisedButton(
                        text="OK",
                        on_release=lambda x: self.dismiss_dialog()
                    )
                ],
            )
            dialog.open()


    def dismiss_dialog(self):
        MDDialog().dismiss()
