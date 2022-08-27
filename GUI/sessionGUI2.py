import tkinter as tk
from configurations import *
from GUI.gui import GUIsegments


class SessionGUI2(GUIsegments):
    def __init__(self, window):
        GUIsegments(window=window, segments_path=SESSION_GUI_SEGMENT_PATH)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('New Session')
    # root.geometry('400x400')
    SessionGUI2(root)
    root.mainloop()
