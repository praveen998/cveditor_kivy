from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton,MDRectangleFlatButton

class HomeScreen(MDScreen):
    def __init__(self,**kwargs):
        super(HomeScreen,self).__init__(**kwargs)
        self.name="Home"
        layout=MDBoxLayout(orientation="vertical",padding=30,spacing=20)
        button1=MDRaisedButton(text="settings",pos_hint={'center_x':0.5},on_press=self.switch_to_settings)
        button2=MDRaisedButton(text="filechooser",pos_hint={'center_x':0.5},on_press=self.switch_to_filechooser)
        
        layout.add_widget(button1)
        layout.add_widget(button2)
        self.add_widget(layout)

    def switch_to_settings(self,instance):
        self.manager.current="settings"

    def switch_to_filechooser(self,instance):
        self.manager.current='filechooser'

    


