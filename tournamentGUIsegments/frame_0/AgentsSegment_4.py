from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
from tkinter import Frame, Listbox, END, Label, Scrollbar
from controller import Controller


class AgentsSegment_4(AbstractGUISegment, ABC):

    def get_widget(self):
        ctrl = Controller()

        frame = self.get_frame()

        frame_left = Frame(master=frame)
        frame_left.pack(side='left')

        frame_right = Frame(master=frame)
        frame_right.pack(side='left')

        lebel1 = Label(master=frame_left, text='Agent ')

        scroll_bar1 = Scrollbar(master=frame_left)
        listbox_agents1 = Listbox(master=frame_left, width=25, selectmode="multiple", exportselection=0,  yscrollcommand=scroll_bar1.set)
        list_agents1 = ctrl.fetch_agents()
        listbox_agents1.insert(END, *list_agents1)
        scroll_bar1.config(command=listbox_agents1.yview)

        lebel_Vs = Label(master=frame_left, text='Vs  Opponents ')

        scroll_bar2 = Scrollbar(master=frame_right)
        listbox_agents2 = Listbox(master=frame_right, width=25, selectmode="multiple", exportselection=0, yscrollcommand= scroll_bar2.set)
        list_agents2 = ctrl.fetch_agents()
        listbox_agents2.insert(END, *list_agents2)
        scroll_bar2.config(command=listbox_agents2.yview)

        return lebel1, listbox_agents1, scroll_bar1, lebel_Vs, listbox_agents2, scroll_bar2

    def get_name(self):
        return 4
