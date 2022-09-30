from abc import ABC
from GUI.AbstractGUISegment import AbstractGUISegment
import tkinter as tk
from controller import Controller


class AnalysisSegment_2(AbstractGUISegment, ABC):

    def get_widget(self):
        ctrl = Controller()
        analysis_list = ctrl.fetch_analysis_men()
        my_dict = self.get_current_horizontal_frame_var_dict()
        my_dict[self.get_name()][0].set('Select a AnalysisMan')
        optionMenu_Analysis = tk.OptionMenu(self.get_frame(), my_dict[self.get_name()][0], *analysis_list)
        optionMenu_Analysis.configure(width=25)
        lable = tk.Label(master=self.get_frame(), text='Analysis                 ')

        return lable, optionMenu_Analysis

    def get_name(self):
        return 2
