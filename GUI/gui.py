import tkinter as tk
import CreateObjectByPath
from configurations import *
from controller import Controller


class GUIsegments:

    def __init__(self, window, segments_path):
        self.window = window
        self.__segments_path = segments_path


    def create_sessionGUI(self):

        controller = Controller()

        frame_dirs_names = controller.fetch_gui_segments(path=self.__segments_path)
        number_of_frame_directory = len(frame_dirs_names)

        all_horizontal_frames = []
        for i in range(number_of_frame_directory):
            frame = tk.Frame(master=self.window)
            frame.pack(side='left')
            all_horizontal_frames.append(frame)

        all_var_dict = {}
        all_vertical_frames = {}
        all_segments = {}
        for horizontal_frame_name in frame_dirs_names:
            horizontal_frame_index = int(horizontal_frame_name.split('_')[-1])
            segments_names = controller.fetch_gui_segments(path=f'{self.__segments_path}/{horizontal_frame_name}')

            widgets = []
            vertical_frames = []
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
                segment_index = int(segments_name[:-3].split('_')[-1])
                var_dict[segment_index] = tuple(tk.StringVar() for x in range(NUMBER_OF_STRINGVAR))
                index = int(horizontal_frame_index)
                frame = tk.Frame(master=all_horizontal_frames[index])
                vertical_frames.append(frame)

            all_vertical_frames[horizontal_frame_index] = vertical_frames

            all_var_dict[horizontal_frame_index] = var_dict

            i = 0
            for segments_name in segments_names:
                obj = CreateObjectByPath.get_object(f'{self.__segments_path}/{horizontal_frame_name}', segments_name, self.window, vertical_frames[i], all_horizontal_frames, all_var_dict, horizontal_frame_index, all_vertical_frames, all_segments)
                segments.append(obj)
                all_segments[horizontal_frame_index] = segments
                widgets_row = obj.get_widget()
                widgets.append(widgets_row)
                i += 1

            all_widgets_in_horizontal_frame = {}
            i = 0
            for widgets_row in widgets:
                vertical_frames[i].pack(side='top')
                all_row_widgets = []
                for widget_col in widgets_row:
                    widget_col.pack(side='left', padx=5, pady=5, fill='both')
                    all_row_widgets.append(widget_col)
                all_widgets_in_horizontal_frame[i] = all_row_widgets
                i += 1

            for obj in segments:
                obj.set_gui_widgets(all_widgets_in_horizontal_frame, horizontal_frame_index)
