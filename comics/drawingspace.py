# File name: drawingspace.py
import kivy
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
kivy.require('1.9.0')


class DrawingSpace(RelativeLayout):
    def on_children(self, instance, value):
        """
        Called every time we add or remove widgets from the
        children list (which is a kivy property) in DrawingSpace.
        This also happens when adding in kv files
        :param instance: instance of the class containing the prop
        :param value: new value of the property
        """
        self.status_bar.counter = len(self.children)
