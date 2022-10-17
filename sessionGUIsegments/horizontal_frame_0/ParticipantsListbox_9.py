from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk


class ParticipantsListbox_9(AbstractGUISegment):

    def get_widget(self) -> tuple:
        listbox_participant = tk.Listbox(master=self.get_frame(), width=50)
        return listbox_participant,

