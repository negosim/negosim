from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk
from tkinter import ttk

INITIAL_DEADLINE_TIME = 60
MAX_DEADLINE_TIME = 3600000


class DeadLineSegment_10(AbstractGUISegment):

    def get_widget(self) -> tuple:
        my_dict = self.get_var_dict()
        lable = tk.Label(master=self.get_frame(), text='Deadline')
        spinbox_deadline = tk.Spinbox(self.get_frame(), from_=1, to=MAX_DEADLINE_TIME,
                                      textvariable=my_dict[self.get_name()][0])
        spinbox_deadline.delete(0, 'end')
        spinbox_deadline.insert(0, INITIAL_DEADLINE_TIME)

        time_type = ttk.OptionMenu(
            self.get_frame(), my_dict[self.get_name()][1], 's', *['s', 'ms'])
        time_type.config(width=3)

        return lable, spinbox_deadline, time_type

    def get_name(self):
        return 'DeadLineSegment_10'
