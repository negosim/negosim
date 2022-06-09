from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk


class SeperatorLineSegment_4(AbstractGUISegment, ABC):

    def get_widget(self):
        txt = '************************************************************'
        my_seperator = tk.Label(master=self.get_frame(), text=txt)
        return my_seperator,

    def get_name(self):
        return 'SeperatorLineSegment_4.py'