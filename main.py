import tkinter as tk
from tkinter import Tk, Button, Frame, Listbox, messagebox
import files
from appconfig import AppConfig
from pathlib import Path
import subprocess
from sys import platform


children = []

class Instance:
    def __init__(self, directory:Path, appconfig:AppConfig):
        self.directory = directory
        self.appconfig = appconfig

    def delete_instance(self) -> None:
        files.delete_recursively(self.directory)

    def copy_instance(self, destination) -> None:
        raise NotImplementedError

    def use_dfhack(self) -> bool:
        return (self.directory / 'dfhack').exists()

    def launch_windows(self) -> None:
        raise NotImplementedError

    def launch_linux(self) -> None:
        exe = self.directory / 'dfhack' if self.use_dfhack() else self.directory / 'df'
        p = subprocess.Popen(args=[self.appconfig.terminal, '-e', '"' + str(exe) + '"'], cwd=str(self.directory))
        children.append(p)

    def launch_mac(self) -> None:
        raise NotImplementedError

    def launch(self) -> None:
        if platform == 'win32':
            self.launch_windows()
        elif platform == 'darwin':
            self.launch_mac()
        else:
            self.launch_linux()

    def __str__(self):
        return str(self.directory.relative_to(files.instance_dir))


class MultiDorf:
    def __init__(self, master:Tk, config:AppConfig):
        self.config = config

        self.master = master
        self.master.title('MultiDorf VERSION/PLATFORM')

        self.header_frame = Frame(master)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        self.btn_frame = Frame(self.header_frame)
        self.btn_frame.pack(side=tk.LEFT, fill=tk.X)

        self.instance_btn = Button(self.btn_frame, text='New Instance', command=self.new_instance)
        self.instance_btn.pack(side=tk.LEFT)

        self.reload_btn = Button(self.btn_frame, text='Reload instances', command=self.reload_instances)
        self.reload_btn.pack(side=tk.LEFT)

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

        self.instances = []
        self.reload_instances()

    def export_instance(self) -> None:
        pass

    def delete_instance(self) -> None:
        instance = self.active_instance()
        if instance is not None:
            result = messagebox.askquestion('Delete', 'Are you sure?', icon='warning')
            if result == 'yes':
                instance.delete_instance()
                self.reload_instances()

    def copy_instance(self) -> None:
        instance = self.active_instance()
        if instance is not None:
            # show a copy dialogue, get the name of the destination, new name of instance, and make the new instance
            pass

    def help(self) -> None:
        messagebox.showinfo('Info', 'Not implemented')

    def active_instance(self) -> Instance:
        cursel = self.instance_lb.curselection()
        if len(cursel) == 1:
            index = self.instance_lb.index(cursel[0])
            return self.instances[index]

    def view_saves(self) -> None:
        instance = self.active_instance()
        if instance is not None:
            files.browse(instance.directory / 'data' / 'save')

    def instance_folder(self) -> None:
        instance = self.active_instance()
        if instance is not None:
            files.browse(instance.directory)

    def reload_instances(self) -> None:
        self.instance_lb.delete(0, tk.END)
        self.instances = []
        for instance_dir in files.instance_dir.iterdir():
            if instance_dir.exists() and instance_dir.is_dir():
                instance = Instance(instance_dir, self.config)
                self.instances.append(instance)
        for instance in self.instances:
            self.instance_lb.insert(tk.END, instance)

    def edit_instance(self) -> None:
        pass

    def new_instance(self) -> None:
        pass

    def settings(self) -> None:
        pass

    def launch_instance(self) -> None:
        if self.active_instance() is not None:
            self.active_instance().launch()


def main():
    root = Tk()
    config = AppConfig()
    gui = MultiDorf(root, config)
    root.mainloop()


if __name__ == '__main__':
    main()