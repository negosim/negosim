import tkinter as tk
from configurations import *
from GUI.gui import GUIsegments


class Tournament:
    def __init__(self, window):
        GUIsegments(window=window, segments_path=TOURNAMENT_GUI_SEGMENT_PATH)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('New Tournament')
    # root.geometry('400x400')
    Tournament(root)
    root.mainloop()
