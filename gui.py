import tkinter as tk
from draw import draw
from rasterization import *


class Rasterization:
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.title('Rasterization')
        self.__root.resizable(False, False)
        self.__root.geometry('300x200')

        self.__option_value = tk.StringVar(self.__root)
        self.__option_value.set("Select an Option")
        self.__option_value.trace('w', self.option_on_change)

        self.__options_list = ['step by step', 'dda', 'bresenham', 'bresenham circle']
        self.__algorithms = [step_by_step, dda, bresenham, bresenham_circle]
        question_menu = tk.OptionMenu(self.__root, self.__option_value, *self.__options_list)
        question_menu.pack()

        self.__spin_boxes = [tk.Spinbox(self.__root) for _ in range(4)]
        for spinbox in self.__spin_boxes:
            spinbox.pack()

        button = tk.Button(self.__root, text='Rasterize', command=self.process)
        button.pack()

    def option_on_change(self, *args):
        if self.__option_value.get() == 'bresenham circle':
            self.__spin_boxes[-1]['state'] = 'disabled'
        else:
            self.__spin_boxes[-1]['state'] = 'normal'

    def process(self):
        args = [int(value.get()) for value in self.__spin_boxes if value['state'] != 'disabled']
        algorithm = self.__algorithms[self.__options_list.index(self.__option_value.get())]
        draw(*args, algorithm)

    def mainloop(self):
        self.__root.mainloop()
