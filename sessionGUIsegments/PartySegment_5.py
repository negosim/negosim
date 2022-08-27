from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk
from controller import Controller


class PartySegment_5(AbstractGUISegment, ABC):

    def get_widget(self):
        ctrl = Controller()
        party_list = ctrl.fetch_agents()
        my_dict = self.get_var_dict()
        my_dict[self.get_name()][0].set('Select a Party')
        optionMenu_party = tk.OptionMenu(self.get_frame(), my_dict[self.get_name()][0], *party_list)
        optionMenu_party.configure(width=25)
        lable = tk.Label(master=self.get_frame(), text='Party                      ')

        return lable, optionMenu_party

    def get_name(self):
        return 'PartySegment_5.py'
