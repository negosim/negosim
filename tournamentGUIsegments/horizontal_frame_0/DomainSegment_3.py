from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
from tkinter import Listbox, END, Label, Scrollbar
from controller import Controller


class DomainSegment_3(AbstractGUISegment, ABC):

    def get_widget(self):
        ctrl = Controller()
        frame = self.get_frame()
        scroll_bar = Scrollbar(master=frame)
        listbox_domain = Listbox(master=frame, width=50, selectmode="multiple", exportselection=0, yscrollcommand=scroll_bar.set, height=6)
        list_domain = ctrl.fetch_domains()
        listbox_domain.insert(END, *list_domain)

        scroll_bar.config(command=listbox_domain.yview)

        lebel_Vs = Label(master=frame, text='Domains ')

        return lebel_Vs, listbox_domain, scroll_bar

    def get_name(self):
        return 3
