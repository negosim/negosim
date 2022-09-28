from tkinter import Label, Spinbox
from GUI.AbstractGUISegment import AbstractGUISegment
INITIAL_DEADLINE_TIME = 1
MAX_DEADLINE_TIME = 100

class RepetitionSegment_6(AbstractGUISegment):

    def get_widget(self) -> tuple:
        frame = self.get_frame()
        string_var = self.get_special_segment_special_StringVar(6, 0)
        label1 = Label(frame, text=' Tournament Repetition')
        spinbox_deadline = Spinbox(frame, from_=1, to=MAX_DEADLINE_TIME, textvariable=string_var, width=5)
        spinbox_deadline.delete(0, 'end')
        spinbox_deadline.insert(0, INITIAL_DEADLINE_TIME)
        label2 = Label(frame, text='          ')
        return label1, spinbox_deadline, label2

    def get_name(self):
        return 'RepetitionSegment_6'
