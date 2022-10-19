from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk


class BtnDeleteParticipant_10(AbstractGUISegment):

    def get_widget(self) -> tuple:
        btn_delete_participant = tk.Button(master=self.get_frame(), text='Delete Participant',
                                                width=42, command=self.delete_participant)
        return btn_delete_participant,

    def delete_participant(self):
        listbox_party_and_preference = self.get_special_widget(0, 9, 0)
        listbox_party_and_preference.delete(tk.ANCHOR)

