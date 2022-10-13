from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk
from controller import Controller


class ProtocolSegment_0(AbstractGUISegment):

    def get_widget(self):
        ctrl = Controller()
        protocol_list = ctrl.fetch_protocols()
        var_tuple = self.get_special_segment_var_tuple(0, 0)
        var_tuple[0].set('Select a protocol')
        optionMenu_protocol = tk.OptionMenu(self.get_frame(), var_tuple[0], *protocol_list)
        optionMenu_protocol.configure(width=25)
        label = tk.Label(master=self.get_frame(), text='Protocol                ')

        return label, optionMenu_protocol
