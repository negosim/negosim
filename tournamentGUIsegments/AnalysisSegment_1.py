from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
from tkinter import Label, OptionMenu
from controller import Controller


class AnalysisSegment_1(AbstractGUISegment, ABC):

    def get_widget(self):
        ctrl = Controller()
        frame = self.get_frame()
        analysis_list = ctrl.fetch_analysis_men()
        string_var = self.get_special_segment_special_StringVar(1, 0)
        string_var.set('Select an analysis')
        optionMenu_Analysis = OptionMenu(frame, string_var, *analysis_list)

        lable = Label(master=frame, text='Analysis ')

        return lable, optionMenu_Analysis

    def get_name(self):
        return 'AnalysisSegment_1.py'