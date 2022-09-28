from GUI.AbstractGUISegment import AbstractGUISegment
from controller import Controller
from tkinter import Label, OptionMenu


class AnalysisTournamentSegment_2(AbstractGUISegment):

    def get_widget(self):
        ctrl = Controller()
        frame = self.get_frame()
        analysis_list = ctrl.fetch_tournament_analysis_men()
        string_var = self.get_special_segment_special_StringVar(2, 0)
        string_var.set('Select a Tournament Analysis')
        optionMenu_Analysis = OptionMenu(frame, string_var, *analysis_list)

        label = Label(master=frame, text='Tournament Analysis ')

        return label, optionMenu_Analysis

    def get_name(self):
        return 'AnalysisTournamentSegment_2'