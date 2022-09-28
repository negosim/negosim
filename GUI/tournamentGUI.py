import tkinter as tk
from configurations import *
from GUI.gui import GUIsegments


class Tournament:
    def __init__(self, window):
        gui_segments = GUIsegments(window=window, y=5)
        gui_segments.create_sessionGUI(segments_path=TOURNAMENT_GUI_SEGMENT_PATH, x=0)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('New Tournament')
    # root.geometry('400x400')
    Tournament(root)
    root.mainloop()
