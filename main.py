import tkinter as tk
from tkinter import Tk, Button, Frame, Listbox
from multidorf import bay12, fs


class MultiDorf:
    def __init__(self, master):
        self.master = master
        self.master.title('MultiDorf VERSION/PLATFORM')

        self.header_frame = Frame(master)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        self.btn_frame = Frame(self.header_frame)
        self.btn_frame.pack(side=tk.LEFT, fill=tk.X)

        self.instance_btn = Button(self.btn_frame, text='New Instance', command=self.new_instance)
        self.instance_btn.pack(side=tk.LEFT)

        self.folders_btn = Button(self.btn_frame, text='Folders')
        self.folders_btn.pack(side=tk.LEFT)

        self.settings_btn = Button(self.btn_frame, text='Settings', command=self.settings)
        self.settings_btn.pack(side=tk.LEFT)

        self.help_btn = Button(self.btn_frame, text='Help', command=self.help)
        self.help_btn.pack(side=tk.LEFT)

        self.content_frame = Frame(master)
        self.content_frame.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

        self.instance_frame = Frame(self.content_frame)
        self.instance_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.instance_lb = Listbox(self.instance_frame, selectmode=tk.SINGLE)
        self.instance_lb.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.instance_opt_frame = Frame(self.content_frame)
        self.instance_opt_frame.pack(side=tk.RIGHT)

        self.instance_launch_btn = Button(self.instance_opt_frame, text='Launch', command=self.launch_instance)
        self.instance_launch_btn.pack(side=tk.TOP)

        self.instance_edit_btn = Button(self.instance_opt_frame, text='Edit', command=self.edit_instance)
        self.instance_edit_btn.pack(side=tk.TOP)

        self.instance_saves_btn = Button(self.instance_opt_frame, text='View saves', command=self.view_saves)
        self.instance_saves_btn.pack(side=tk.TOP)

        self.instance_folder_btn = Button(self.instance_opt_frame, text='Instance folder', command=self.instance_folder)
        self.instance_folder_btn.pack(side=tk.TOP)

        self.instance_copy_btn = Button(self.instance_opt_frame, text='Copy instance', command=self.copy_instance)
        self.instance_copy_btn.pack(side=tk.TOP)

        self.instance_delete_btn = Button(self.instance_opt_frame, text='Delete instance', command=self.delete_instance)
        self.instance_delete_btn.pack(side=tk.TOP)

        self.instance_export_btn = Button(self.instance_opt_frame, text='Export instance', command=self.export_instance)
        self.instance_export_btn.pack(side=tk.TOP)

    def export_instance(self):
        pass

    def delete_instance(self):
        pass

    def copy_instance(self):
        pass

    def help(self):
        pass

    def view_saves(self):
        pass

    def instance_folder(self):
        pass

    def edit_instance(self):
        pass

    def new_instance(self):
        pass

    def settings(self):
        pass

    def launch_instance(self):
        pass


def main():
    if not fs.instance().exists():
        fs.instance().mkdir(parents=True)

    root = Tk()
    gui = MultiDorf(root)
    for instance in fs.instance().iterdir():
        gui.instance_lb.insert(tk.END, instance)
    root.mainloop()


if __name__ == '__main__':
    main()