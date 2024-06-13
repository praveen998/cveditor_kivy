from kivymd.app import MDApp
from kivy.lang import Builder
from app.screens.homescreen import HomeScreen
from app.screens.settings import SettingsScreen
from kivy.uix.screenmanager import ScreenManager
from app.screens.filechooser_screen import FileChooserScreen

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        sm=ScreenManager()
        sm.add_widget(HomeScreen(name="Home"))
        sm.add_widget(SettingsScreen(name="settings"))
        sm.add_widget(FileChooserScreen(name="filechooser"))
        return sm

if __name__ == '__main__':
    MyApp().run()