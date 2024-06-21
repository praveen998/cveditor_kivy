from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.filemanager import MDFileManager
import cv2
import numpy as np


class DrawWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.line = None
        self.shapes = []  # Store shapes coordinates here
        self.image = None

    def set_image(self, image_path):
        self.canvas.clear()
        self.shapes.clear()
        with self.canvas.before:
            self.image = Image(source=image_path, allow_stretch=True, keep_ratio=True)
            self.image.bind(texture_size=self._update_size)
            self.canvas.before.add(self.image.canvas.before)
        self.bind(size=self._update_size, pos=self._update_size)

    def _update_size(self, *args):
        if self.image:
            self.image.size = self.size
            self.image.pos = self.pos

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(1, 0, 0)  # Set the color to red
                touch.ud['line'] = Line(points=(touch.x, touch.y))
            self.shapes.append([touch.x, touch.y])
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        if 'line' in touch.ud and self.collide_point(*touch.pos):
            touch.ud['line'].points += (touch.x, touch.y)
            self.shapes[-1].extend([touch.x, touch.y])
        return super().on_touch_move(touch)

    def on_touch_up(self, touch):
        if 'line' in touch.ud and self.collide_point(*touch.pos):
            touch.ud['line'].points += (touch.x, touch.y)
            self.shapes[-1].extend([touch.x, touch.y])
        return super().on_touch_up(touch)

class DrawingApp(MDApp):
    def build(self):
        root = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.draw_widget = DrawWidget(size_hint_y=None, height=700)

        choose_file_button = MDRaisedButton(text="Choose File")
        choose_file_button.bind(on_release=self.file_manager_open)

        root.add_widget(choose_file_button)
        root.add_widget(self.draw_widget)

        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            ext=['.png', '.jpg', '.jpeg']
        )
        return root

    def file_manager_open(self, *args):
        self.file_manager.show('/')

    def select_path(self, path):
        self.exit_manager()
        self.draw_widget.set_image(path)

    def exit_manager(self, *args):
        self.file_manager.close()


if __name__ == '__main__':
    DrawingApp().run()
