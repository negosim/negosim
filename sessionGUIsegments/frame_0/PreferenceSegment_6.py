from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk
from controller import Controller


class PreferenceSegment_6(AbstractGUISegment, ABC):

    def get_widget(self):
        # my_dict = self.get_current_horizontal_frame_var_dict()
        # domain_var_tuple = my_dict['DomainSegment_1.py']
        # domain_name = domain_var_tuple[0].get()
        # ctrl = Controller()
        # optionMenu_preference = None
        # if domain_name != 'Select a Domain':
        #     preference_list = ctrl.fetch_preferences_of_domain(domain=domain_name)
        # else:
        #     preference_list = ['Select a Preference']
        # my_dict = self.get_current_horizontal_frame_var_dict()
        # my_dict[self.get_name()][0].set('Select a Preference')
        # optionMenu_preference = tk.OptionMenu(self.get_frame(), my_dict[self.get_name()][0], *preference_list)
        # optionMenu_preference.configure(width=25, state='disable')
        # lable = tk.Label(master=self.get_frame(), text='Preference Profile')
        # if optionMenu_preference == None:
        #     return lable,
        # else:
        #     return lable, optionMenu_preference

        label = tk.Label(master=self.get_frame(), text='')
        return label,


