# File name: drawingspace.py
import kivy
kivy.require('2.3.1')
from kivy.uix.relativelayout import RelativeLayout

class DrawingSpace(RelativeLayout):
    def on_children(self, instance, value):
        self.status_bar.counter = len(self.children)
