import tkinter as tk
import matplotlib.colors as pltc
import pandas as pd

from tkinter import ttk
from matplotlib.figure import Figure
from random import sample
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:

    def __init__(self):
        self.__window = tk.Tk()
        self.__window.geometry('640x450')
        self.__window.title('Ujian Tengah Semester 2021')
        self.__init_widgets()

    def __init_widgets(self):
        self.__frame_one = tk.Frame(master=self.__window, borderwidth=1)  # , relief=tk.RAISED)
        self.__lbl_input = tk.Label(master=self.__frame_one, text='Masukan path file csv : ')
        self.__lbl_input.pack(pady=4)
        self.__frame_one.grid(row=0, column=0, sticky='nw')

        self.__frame_two = tk.Frame(master=self.__window, borderwidth=1)  # , relief=tk.RAISED)
        self.__ent_input = tk.Entry(master=self.__frame_two, width=50)
        self.__ent_input.pack(pady=3)
        self.__frame_two.grid(row=0, column=1, sticky='ne')

        self.__frame_three = tk.Frame(master=self.__window, borderwidth=1)  # , relief=tk.RAISED)
        self.__cbx_jenis_plot = ttk.Combobox(master=self.__frame_three, width=12)
        self.__cbx_jenis_plot['values'] = ('Line',
                                           'Scatter'
                                           , 'Bar')
        self.__cbx_jenis_plot.current(0)
        self.__cbx_jenis_plot.pack(pady=3)
        self.__frame_three.grid(row=0, column=2, sticky='ne')

        self.__frame_four = tk.Frame(master=self.__window, borderwidth=1)  # , relief=tk.RAISED)
        self.__submit_btn = tk.Button(master=self.__frame_four, width=13, text='Visualisasi Data')
        self.__submit_btn.pack(pady=3)
        self.__frame_four.grid(row=0, column=3, sticky='ne')

        self.__plot_figure = Figure(figsize=(5, 4), dpi=100)
        self.__plot = self.__plot_figure.add_subplot(1, 1, 1)
        self.__plot.set_title('Data Visualisasi')
        self.__canvas = FigureCanvasTkAgg(self.__plot_figure, self.__window)
        self.__canvas_widget = self.__canvas.get_tk_widget()
        self.__canvas_widget.grid(row=1, columnspan=4, sticky='news')
        self.__canvas_widget.columnconfigure(0, weight=1)

        self.__submit_btn.bind('<Button-1>', self.__on_submit_btn_left_click)
        self.__cbx_jenis_plot.bind("<<ComboboxSelected>>")

    def __on_submit_btn_left_click(self, event: tk.Event):

        self.__data = self.get_data()
        self.__plot.clear()
        print(self.__data)

        all_colors = [k for k, v in pltc.cnames.items()]
        colors = sample(all_colors, len(self.get_data()))
        cbx_val = self.__cbx_jenis_plot.get()


        if cbx_val == 'Bar':
            self.__plot.bar(self.__data['nama'], self.__data['nilai'], color=colors)
        elif cbx_val == 'Line':
            self.__plot.plot(self.__data['nama'], self.__data['nilai'])
        else:
            self.__plot.scatter(self.__data['nama'], self.__data['nilai'], color=colors)

        self.__canvas.draw()

    def get_data(self):
        value = self.__ent_input.get()

        try:
            data = pd.read_csv("{0}".format(value))
            df = pd.DataFrame(data)
        except IOError as e:
            print(e)
            df = []

        return df

    def show(self):
        self.__window.mainloop()
