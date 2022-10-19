from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk
from controller import Controller


class UtilitySpaceSegment_7(AbstractGUISegment):
    def get_widget(self):
        ctrl = Controller()
        utility_spaces_list = ctrl.fetch_utility_spaces()
        var_tuple = self.get_special_segment_var_tuple(0, 7)
        var_tuple[0].set('Select a utility space')
        optionMenu_utility_spaces = tk.OptionMenu(self.get_frame(), var_tuple[0], *utility_spaces_list)
        optionMenu_utility_spaces.configure(width=25)
        label = tk.Label(master=self.get_frame(), text='Utility Space        ')
        return label, optionMenu_utility_spaces