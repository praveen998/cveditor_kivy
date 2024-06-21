
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivymd.uix.filemanager import MDFileManager

from kivymd.uix.screen import MDScreen
from kivy.uix.image import Image


from app.services.main import file_to_png,convert_to_frames



class FileChooserScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "filechooser"
        self.layout=  BoxLayout(orientation='vertical',spacing=10,padding=10)
        
        self.file_manager= MDFileManager(
            exit_manager= self.exit_manager,
            select_path= self.select_path,
            ext= ['.png','.pdf','.jpg']
        )
        

        # Create the main layout     
        # Label for displaying selected file path
        # path_label = Label(text="Selected File Path: ", size_hint_y=None, height=40)
        #layout.add_widget(path_label)
        # Button to open file manager

        self.choose_button = Button(text="Choose File", size_hint_y=None, height=40,
                             on_release=self.file_manager_open)   
        

        self.image=Image(
            size_hint_y=None,
            height=700,
            keep_ratio=True,
            allow_stretch=True
        )    

        self.layout.add_widget(self.choose_button)
        self.layout.add_widget(self.image)
        self.add_widget(self.layout)

       # self.layout.add_widget(image)

    def file_manager_open(self, *args):
        # Create and show file manager
        self.file_manager.show('/')  # Start with '/' (root directory)

    def exit_manager(self, *args):
        self.file_manager.close()
        # Function to handle closing the file manager
        #self.manager.current="Home"

    def select_path(self, path):
        self.exit_manager()
        # Function to handle the selected file path
        print('imagepath:',path)
        path=path.replace("\\","/")
        type=file_to_png(path)
        print('type:',type)
        convert_to_frames(type)        
        #self.image.source=path
