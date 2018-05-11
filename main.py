import sys
import os
from pathlib import Path
from tkinter import Tk, Label, Button, Frame, Listbox, LEFT, RIGHT, TOP, SINGLE, END
from multidorf import bay12, fs


class MultiDorf():
    def __init__(self, master):
        self.master = master
        master.title('MultiDorf VERSION/PLATFORM')

        # self.label = Label(master, text='this is multidorf')
        # self.label.pack()

        self.btn_frame = Frame(master)
        self.btn_frame.pack(side=TOP)

        self.instance_btn = Button(self.btn_frame, text='New Instance', command=self.new_instance)
        self.instance_btn.pack(side=LEFT)

        self.folders_btn = Button(self.btn_frame, text='Folders')
        self.folders_btn.pack(side=LEFT)

        self.settings_btn = Button(self.btn_frame, text='Settings', command=self.settings)
        self.settings_btn.pack(side=LEFT)

        self.help_btn = Button(self.btn_frame, text='Help', command=self.help)
        self.help_btn.pack(side=LEFT)

        self.instance_frame = Frame(master)
        self.instance_frame.pack(side=LEFT)

        self.instance_lb = Listbox(self.instance_frame, selectmode=SINGLE)
        self.instance_lb.pack()

    def help(self):
        print('Help!!!')

    def new_instance(self):
        print('creating new thing')

    def settings(self):
        print('settings pressed')


def main():
    if not fs.instance().exists():
        fs.instance().mkdir(parents=True)

    root = Tk()
    gui = MultiDorf(root)
    for instance in fs.instance().iterdir():
        gui.instance_lb.insert(END, instance)
    root.mainloop()


if __name__ == '__main__':
    main()