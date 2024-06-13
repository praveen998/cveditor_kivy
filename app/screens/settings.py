from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton,MDRectangleFlatButton

class SettingsScreen(MDScreen):
    def __init__(self,**kwargs):
        super(SettingsScreen,self).__init__(**kwargs)
        self.name="settings"
        layout=MDBoxLayout(orientation="vertical",padding=30,spacing=20)
        button=MDRaisedButton(text="main",pos_hint={'center_x':0.5},on_press=self.switch_to_main)
        layout.add_widget(button)
        self.add_widget(layout)
        
    def switch_to_main(self,instance):
        self.manager.current="Home"

       