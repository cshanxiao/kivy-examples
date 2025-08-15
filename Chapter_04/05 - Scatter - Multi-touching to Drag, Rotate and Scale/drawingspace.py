# File name: drawingspace.py
import kivy
kivy.require('2.3.1')
from kivy.uix.stencilview import StencilView

class DrawingSpace(StencilView):
    def on_children(self, instance, value):
        self.status_bar.counter = len(self.children)
