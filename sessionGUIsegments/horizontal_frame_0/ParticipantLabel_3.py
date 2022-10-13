from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk

class ParticipantLabel_3(AbstractGUISegment, ABC):

    def get_widget(self):
        label = tk.Label(master=self.get_frame(), text='Participant')
        return label,
