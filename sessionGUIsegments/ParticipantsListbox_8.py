from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk


class ParticipantsListbox_8(AbstractGUISegment):

    def get_widget(self) -> tuple:
        listbox_participant = tk.Listbox(master=self.get_frame(), width=42)
        return listbox_participant,

    def get_name(self):
        return 'ParticipantsListbox_8.py'
