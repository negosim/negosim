from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
from tkinter import Label, Spinbox, IntVar
from tkinter import ttk


MIN_MAX_PARTICIPANTS = 2
INITIAL_DEADLINE_TIME = 1
MAX_DEADLINE_TIME = 3600000


class DeadlineSegment_6(AbstractGUISegment, ABC):

    def get_widget(self):
        frame = self.get_frame()
        string_var = self.get_special_StringVar(5, 0)
        lebel1 = Label(frame, text=' Deadline ')
        spinbox_deadline = Spinbox(frame, from_=1, to=MAX_DEADLINE_TIME, textvariable=string_var)
        spinbox_deadline.delete(0, 'end')
        spinbox_deadline.insert(0, INITIAL_DEADLINE_TIME)

        var_time_type = self.get_special_StringVar(5, 1)
        time_type = ttk.OptionMenu(frame, var_time_type, 's', *['s', 'ms'])
        time_type.config(width=3)

        return lebel1, spinbox_deadline, time_type

    def get_name(self):
        return 6