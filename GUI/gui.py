import tkinter as tk
import CreateObjectByPath
from configurations import *
from controller import Controller


class GUIsegments:

    def __init__(self, window, y: int):
        """
        :param y: refer to number of segment that we need
        :return:
        """
        if y < 1:
            raise ValueError("x and y should be grater than 0 and y should be grater than x")

        self.__y = y
        self.window = window
        self.controller = Controller()

        self.__all_horizontal_frames = []
        for i in range(self.__y):
            frame = tk.Frame(master=self.window)
            frame.pack(side='left')
            self.__all_horizontal_frames.append(frame)


    def create_sessionGUI(self, segments_path, x: int):

        if x > self.__y:
            raise ValueError(f"y (y={self.__y}) should be grater than x")

        # package_name = segments_path.split("./")[1]

        # all_horizontal_frames = []
        # for i in range(self.__y):
        #     frame = tk.Frame(master=self.window)
        #     frame.pack(side='left')
        #     all_horizontal_frames.append(frame)


        # # 5 horizontal frame reserved
        # horizontal_frame1 = tk.Frame(master=self.window)
        # horizontal_frame1.pack(side='left')
        # horizontal_frame2 = tk.Frame(master=self.window)
        # horizontal_frame2.pack(side='left')
        # horizontal_frame3 = tk.Frame(master=self.window)
        # horizontal_frame3.pack(side='left')
        # horizontal_frame4 = tk.Frame(master=self.window)
        # horizontal_frame4.pack(side='left')
        # horizontal_frame5 = tk.Frame(master=self.window)
        # horizontal_frame5.pack(side='left')
        #
        # self.__all_horizontal_frames.append(horizontal_frame1)
        # self.__all_horizontal_frames.append(horizontal_frame2)
        # self.__all_horizontal_frames.append(horizontal_frame3)
        # self.__all_horizontal_frames.append(horizontal_frame4)
        # self.__all_horizontal_frames.append(horizontal_frame5)

        # if package_name == SESSION_GUI_PACKAGE_NAME:
        segments_names = self.controller.fetch_gui_segments(path=segments_path)
        # elif package_name == TOURNAMENT_GUI_PACKAGE_NAME:
        #     segments_names = self.controller.fetch_gui_segments(path=segments_path)
        # else:
        #     raise ValueError('There is no package_name')
        widgets = []
        frames = []
        var_dict = {}
        segments = []

        segments_nums = [s.split('_')[1].split('.')[0] for s in segments_names]

        def my_map_func(f_segments_name, f_segments_num):
            return f_segments_name, f_segments_num

        segments_names_num_map = map(my_map_func, segments_names, segments_nums)
        segments_names_num_list = list(segments_names_num_map)
        segments_names_num_list.sort(key=lambda tup: int(tup[1]))
        segments_names = [s[0] for s in segments_names_num_list]

        for segments_name in segments_names:
            var_dict[segments_name[:-3]] = tuple(tk.StringVar() for x in range(NUMBER_OF_STRINGVAR))
            frame = tk.Frame(master=self.__all_horizontal_frames[x])
            frames.append(frame)

            i = 0
        for segments_name in segments_names:
            obj = CreateObjectByPath.get_object(segments_path, segments_name, self.window, frames[i], frames, self.__all_horizontal_frames, var_dict)
            segments.append(obj)
            widgets_row = obj.get_widget()
            widgets.append(widgets_row)
            i += 1

        all_widgets_in_Gui = {}
        i = 0
        for widgets_row in widgets:
            frames[i].pack(side='top')
            all_row_widgets = []
            for widget_col in widgets_row:
                widget_col.pack(side='left', padx=5, pady=5, fill='both')
                all_row_widgets.append(widget_col)
            all_widgets_in_Gui[i] = all_row_widgets
            i += 1

        for obj in segments:
            obj.set_gui_widgets(all_widgets_in_Gui)
