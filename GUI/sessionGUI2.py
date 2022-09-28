import tkinter as tk
from configurations import *
from GUI.gui import GUIsegments


class SessionGUI2:
    def __init__(self, window):
        gui_segments = GUIsegments(window=window, y=1)
        gui_segments.create_sessionGUI(segments_path=SESSION_GUI_SEGMENT_PATH, x=0)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('New Session')
    # root.geometry('400x400')
    SessionGUI2(root)
    root.mainloop()
