import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Frame, LEFT, BOTH


class Charts:

    def scatter_chart(self, data, col_name1: str, col_name2: str, frame: Frame, position: str):
        df = pd.DataFrame(data, columns=[col_name1, col_name2])
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        ax = figure.add_subplot(111)
        ax.scatter(df[col_name1], df[col_name2], color='r')
        scatter_plt = FigureCanvasTkAgg(figure, frame)
        scatter_plt.get_tk_widget().pack(side=position, fill='both')
        ax.legend(['Bids'])
        ax.set_xlabel(col_name1)
        ax.set_ylabel(col_name2)
        ax.set_title(f'{col_name1} Vs. {col_name2}')

    def bar_chart(self, data, frame: Frame, col1_name: str, col2_name: str):
        df1 = pd.DataFrame(data, columns=[col1_name, col2_name])
        figure1 = plt.Figure(figsize=(3, 10), dpi=60)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, frame)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
        df1 = df1[[col1_name, col2_name]].groupby(col1_name).sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title(f'{col1_name} Vs. {col2_name} Per agent')
