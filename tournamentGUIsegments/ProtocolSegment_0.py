from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk
from controller import Controller


class ProtocolSegment_0(AbstractGUISegment, ABC):

    def get_widget(self):
        ctrl = Controller()
        protocol_list = ctrl.fetch_protocols()
        my_dict = self.get_var_dict()
        my_dict[self.get_name()][0].set('Select a protocol')
        optionMenu_protocol = tk.OptionMenu(self.get_frame(), my_dict[self.get_name()][0], *protocol_list)

        lable = tk.Label(master=self.get_frame(), text='Protocol')

        return lable, optionMenu_protocol

    def get_name(self):
        return 'ProtocolSegment_0'