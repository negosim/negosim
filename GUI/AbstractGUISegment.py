from abc import ABC, abstractmethod
from tkinter import Frame


class AbstractGUISegment(ABC):

    def __init__(self, root: Frame, frame: Frame, frames: list, all_horizontal_frames: list, var_dict: dict):
        self.__root = root
        self.__frame = frame
        self.__all_frames = frames
        self.__var_dict = var_dict
        self.__gui_widgets_dict = {}
        self.__all_horizontal_frames = all_horizontal_frames

    def get_all_horizontal_frames(self):
        return self.__all_horizontal_frames

    def get_special_horizontal_frame(self, index: int):
        return self.__all_horizontal_frames[index]

    def replace_special_horizontal_frame(self, index: int, frame: Frame):
        frame1 = self.__all_horizontal_frames[index]
        frame1.destroy()
        self.__all_horizontal_frames.pop(index)
        frame.pack(side='left')
        self.add_horizontal_frame(index, frame)

    def add_horizontal_frame(self, index: int, frame: Frame):
        frame.pack(side='left')
        self.__all_horizontal_frames.insert(index, frame)

    def get_root(self):
        return self.__root

    def replace_frame(self, index, frame):
        frames = self.get_all_frames()
        frames[index].destroy()
        frames.pop(index)
        self.add_new_frame(index, frame)

    def add_new_frame(self, index: int, frame: Frame):
        '''
        this method adds a frame in special index of list (fram list)
        :param index: int
        '''
        self.__all_frames.insert(index, frame)
        frame.pack(side='left')

    def get_all_frames(self):
        return self.__all_frames

    def get_special_frame(self, index: int):
        return self.__all_frames[index]

    def get_special_segment_StringVars(self, segment_index: int):
        special_segment_name = list(self.__var_dict.keys())[segment_index]
        special_segment_vars = self.__var_dict[special_segment_name]
        return special_segment_vars

    def get_special_segment_special_StringVar(self, segment_index, col_index: int):
        special_segment_vars = self.get_special_segment_StringVars(segment_index)
        special_segment_segment_special_var = special_segment_vars[col_index]
        return special_segment_segment_special_var

    def set_gui_widgets(self, gui_widgets_dict: dict):
        '''
        this method maintains all existing widgets in the Gui
        :param gui_widgets_dict:
        '''
        self.__gui_widgets_dict = gui_widgets_dict

    def add_new_gui_widget(self, index: int, widget):
        self.__gui_widgets_dict[index].append(widget)

    def get_special_segment_name(self, index):
        all_segment_names = list(self.__var_dict.keys())
        return all_segment_names[index]

    def get_gui_widgets(self):
        '''
        this method returns all existing widgets in the Gui
        :return: all existing widgets in the Gui
        '''
        return self.__gui_widgets_dict

    def get_special_widget(self, segment_index, col_index):
        return self.__gui_widgets_dict[segment_index][col_index]

    def get_frame(self):
        return self.__frame

    def get_var_dict(self):
        return self.__var_dict

    @abstractmethod
    def get_widget(self) -> tuple:
        '''
        :param var_dict:
        :param frame:
        :return: tuple ([widget1, widget2, ...], row)
        '''
        raise NotImplementedError

    # @abstractmethod
    # def get_name(self):
    #     raise NotImplementedError
