from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk
from controller import Controller


class DomainSegment_1(AbstractGUISegment, ABC):

    def get_widget(self):
        self.__first_click = True
        ctrl = Controller()
        domain_list = ctrl.fetch_domains()
        self.my_dict = self.get_current_horizontal_frame_var_dict()
        self.my_dict[self.get_name()][0].set('Select a Domain')
        self.optionMenu_domain = tk.OptionMenu(self.get_frame(), self.my_dict[self.get_name()][0], *domain_list, command=self.create_select_preference)
        self.optionMenu_domain.configure(width=25)
        label = tk.Label(master=self.get_frame(), text='Domain                 ')

        return label, self.optionMenu_domain

    def create_select_preference(self, selected_domain):

        self.optionMenu_domain.config(state='disable') # disable domain option menu selection after first selection in order to prevent bug

        ctrl = Controller()
        preference_list = ctrl.fetch_preferences_of_domain(selected_domain)
        if self.__first_click:
            new_frame = tk.Frame(self.get_special_vertical_frame(0, 6))
            self.add_new_frame(horizontal_index=0, vertical_index=6, new_frame=new_frame)
            self.__first_click = False
        else:
            new_frame = tk.Frame(self.get_special_horizontal_frame(0))
            self.replace_special_vertical_frame(horizontal_frame_index=0, vertical_frame_index=6, new_frame=new_frame)

        preference_var_dict = self.get_special_StringVar(6, 0, 0)
        preference_var_dict.set('Select a Preference')
        self.optionMenu_preference = tk.OptionMenu(self.get_special_vertical_frame(0, 6), preference_var_dict, *preference_list)
        self.optionMenu_preference.configure(width=25)
        self.label = tk.Label(master=self.get_special_vertical_frame(0, 6), text='Preference profile')
        self.add_new_gui_widget(0, 6, self.label)
        self.add_new_gui_widget(0, 6, self.optionMenu_preference)
        self.label.pack(side='left')
        self.optionMenu_preference.pack(side='left')


    def get_name(self):
        return 1
