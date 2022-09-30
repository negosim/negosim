from abc import ABC, abstractmethod
from tkinter import Frame


class AbstractGUISegment(ABC):

    def __init__(self, root: Frame, frame: Frame, all_horizontal_frames: list, all_var_dict: dict,
                 current_horizontal_frame_index: int, all_vertical_frames):
        self.__root = root
        self.__frame = frame
        # self.__all_frames = frames
        self.__all_var_dict = all_var_dict
        # self.__gui_widgets_dict = {}
        self.__all_horizontal_frames = all_horizontal_frames
        self.__current_horizontal_frame_index = current_horizontal_frame_index
        self.__all_vertical_frames = all_vertical_frames

        self.__all_widgets_in_GUI = {}

    def get_all_vertical_frames(self):
        return self.__all_vertical_frames

    def get_all_vertical_frames_of_special_horizontal_frame(self, horizontal_frame_index):
        return self.__all_vertical_frames[str(horizontal_frame_index)]

    def get_special_vertical_frame(self, horizontal_frame_index, vertical_frame_index):
        return self.__all_vertical_frames[horizontal_frame_index][vertical_frame_index]

    # def replace_special_vertical_frame(self, horizontal_frame_index, vertical_frame_index, new_frame):
    #     frames = self.get_all_frames()
    #     frames[index].destroy()
    #     frames.pop(index)
    #     self.add_new_frame(index, frame)

    def get_all_horizontal_frames(self):
        return self.__all_horizontal_frames

    def get_special_horizontal_frame(self, index: int):
        return self.__all_horizontal_frames[index]

    def replace_special_horizontal_frame(self, horizontal_index: int, frame: Frame):
        frame1 = self.__all_horizontal_frames[horizontal_index]
        frame1.destroy()
        self.__all_horizontal_frames.pop(horizontal_index)
        frame.pack(side='left')
        self.add_horizontal_frame(horizontal_index, frame)

    def add_horizontal_frame(self, horizontal_index: int, frame: Frame):
        frame.pack(side='left')
        self.__all_horizontal_frames.insert(horizontal_index, frame)

    def get_root(self):
        return self.__root

    def replace_special_vertical_frame(self, horizontal_frame_index, vertical_frame_index, new_frame):
        old_frame = self.get_special_vertical_frame(horizontal_frame_index=horizontal_frame_index, vertical_frame_index=vertical_frame_index)
        old_frame.destroy()
        self.__all_vertical_frames[str(horizontal_frame_index)].pop(vertical_frame_index)
        self.add_new_frame(horizontal_frame_index, vertical_frame_index, new_frame)

    def add_new_frame(self, horizontal_index, vertical_index: int, new_frame: Frame):
        '''
        this method adds a frame in special index of list (frame list)
        :param index: int
        '''
        new_frame.pack(side='left')
        self.__all_vertical_frames[horizontal_index].insert(vertical_index, new_frame)


    # def get_all_vertical_frames(self):
    #     return self.__all_frames

    # def get_special_frame(self, index: int):
    #     return self.__all_frames[index]

    # def get_special_segment_StringVars(self, segment_index: int, horizontal_frame_index: int):
    #     special_segment_name = list(self.__all_var_dict[horizontal_frame_index].keys())[segment_index]
    #     special_segment_vars = self.__all_var_dict[horizontal_frame_index][special_segment_name]
    #     return special_segment_vars

    def get_special_StringVar(self, segment_index, index: int, horizontal_frame_index: int = None):
        """
        :param segment_index: چندمین سگمنت یا به عبارتی جندمین ایندکس عمودی
        :param index: چندمین ویحتی که به استرینگ-وار نیاز دارد
        :param horizontal_frame_index: چندمین فریم افقی
        :return:
        """
        if horizontal_frame_index is None:
            horizontal_frame_index = self.__current_horizontal_frame_index
        # special_segment_vars = self.get_special_segment_StringVars(segment_index, horizontal_frame_index)
        # special_segment_segment_special_var = special_segment_vars[col_index]
        special_segment_segment_special_var = self.__all_var_dict[horizontal_frame_index][segment_index][index]
        return special_segment_segment_special_var

    def set_gui_widgets(self, hf_widgets_dict: dict, horizontal_index: int):
        '''
        this method maintains all existing widgets in the Gui
        :param hf_widgets_dict:
        '''
        # self.__gui_widgets_dict = hf_widgets_dict
        self.__all_widgets_in_GUI[horizontal_index] = hf_widgets_dict

    def add_new_gui_widget(self, horizontal_index, index: int, widget):
        # print(self.__all_widgets_in_GUI['0'][index])
        # print(horizontal_index)
        self.__all_widgets_in_GUI[horizontal_index][index].append(widget)

    # def get_special_segment_name(self, index):
    #     all_segment_names = list(self.__all_var_dict.keys())
    #     return all_segment_names[index]

    def get_all_gui_widgets(self):
        '''
        this method returns all existing widgets in the Gui
        :return: all existing widgets in the Gui
        '''
        return self.__all_widgets_in_GUI

    def get_all_gui_widget_in_hf(self, horizontal_index: int):
        return self.__all_widgets_in_GUI[horizontal_index]

    def get_special_widget(self, horizontal_index: int, segment_index: int, index: int):
        return self.__all_widgets_in_GUI[horizontal_index][segment_index][index]

    def get_frame(self):
        return self.__frame

    def get_current_horizontal_frame_var_dict(self, horizontal_frame_index: int = None):
        if horizontal_frame_index == None:
            horizontal_frame_index = self.__current_horizontal_frame_index
        return self.__all_var_dict[horizontal_frame_index]

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
