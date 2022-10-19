from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
from tkinter import Listbox, END, Label, Scrollbar
from controller import Controller


class UtilitySpaceSegment_4(AbstractGUISegment, ABC):

    def get_widget(self):
        ctrl = Controller()
        frame = self.get_frame()
        scroll_bar = Scrollbar(master=frame)
        listbox_utility_spaces = Listbox(master=frame, width=50, selectmode="multiple", exportselection=0, yscrollcommand=scroll_bar.set, height=6)
        list_utility_spaces = ctrl.fetch_utility_spaces()
        listbox_utility_spaces.insert(END, *list_utility_spaces)

        scroll_bar.config(command=listbox_utility_spaces.yview)

        label_Vs = Label(master=frame, text='Utility Space ')

        return label_Vs, listbox_utility_spaces, scroll_bar

    def get_name(self):
        return 4
