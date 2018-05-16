import subprocess
import tkinter as tk
from pathlib import Path
from sys import platform
from tkinter import Tk, Button, Frame, Listbox, messagebox
from typing import Callable

import files
from version import version


class Instance:
    def __init__(self, directory: Path):
        self.directory = directory

    def delete_instance(self) -> None:
        files.delete_recursively(self.directory)

    def copy_instance(self, destination) -> None:
        raise NotImplementedError

    def use_dfhack(self) -> bool:
        return (self.directory / 'dfhack').exists()

    def launch_windows(self, quit_callback) -> None:
        raise NotImplementedError

    def launch_linux(self, quit_callback) -> None:
        exe = self.directory / 'dfhack' if self.use_dfhack() else self.directory / 'df'
        command = ['x-terminal-emulator', '-e', '"' + str(exe) + '"']
        proc = subprocess.Popen(args=command, cwd=str(self.directory))
        # call quit_callback if not None after proc finishes
        proc.wait()
        if quit_callback is not None:
            quit_callback()

    def launch_mac(self, quit_callback) -> None:
        raise NotImplementedError

    def launch(self, quit_callback = None) -> None:
        if platform == 'win32':
            self.launch_windows(quit_callback=quit_callback)
        elif platform == 'darwin':
            self.launch_mac(quit_callback=quit_callback)
        elif platform == 'linux':
            self.launch_linux(quit_callback=quit_callback)
        else:
            raise NotImplementedError

    def __str__(self):
        return str(self.directory.relative_to(files.instance_dir))


class MultiDorf:
    def __init__(self, master: Tk):
        self.controls = []
        self.instances = []

        self.master = master
        self.master.title('MultiDorf ' + version + ' ' + platform)

        self.header_frame = Frame(master)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        self.btn_frame = Frame(self.header_frame)
        self.btn_frame.pack(side=tk.LEFT, fill=tk.X)

        self.instance_btn = Button(self.btn_frame, text='New Instance', command=self.new_instance)
        self.instance_btn.pack(side=tk.LEFT)
        self.controls.append(self.instance_btn)

        self.reload_btn = Button(self.btn_frame, text='Reload instances', command=self.reload_instances)
        self.reload_btn.pack(side=tk.LEFT)
        self.controls.append(self.reload_btn)

        self.folders_btn = Button(self.btn_frame, text='Folders')
        self.folders_btn.pack(side=tk.LEFT)
        self.controls.append(self.folders_btn)

        self.settings_btn = Button(self.btn_frame, text='Settings', command=self.settings)
        self.settings_btn.pack(side=tk.LEFT)
        self.controls.append(self.settings_btn)

        self.help_btn = Button(self.btn_frame, text='Help', command=self.help)
        self.help_btn.pack(side=tk.LEFT)
        self.controls.append(self.help_btn)

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
        self.controls.append(self.instance_launch_btn)

        self.instance_edit_btn = Button(self.instance_opt_frame, text='Edit', command=self.edit_instance)
        self.instance_edit_btn.pack(side=tk.TOP)
        self.controls.append(self.instance_edit_btn)

        self.instance_saves_btn = Button(self.instance_opt_frame, text='View saves', command=self.view_saves)
        self.instance_saves_btn.pack(side=tk.TOP)
        self.controls.append(self.instance_saves_btn)

        self.instance_folder_btn = Button(self.instance_opt_frame, text='Instance folder', command=self.instance_folder)
        self.instance_folder_btn.pack(side=tk.TOP)
        self.controls.append(self.instance_folder_btn)

        self.instance_copy_btn = Button(self.instance_opt_frame, text='Copy instance', command=self.copy_instance)
        self.instance_copy_btn.pack(side=tk.TOP)
        self.controls.append(self.instance_copy_btn)

        self.instance_delete_btn = Button(self.instance_opt_frame, text='Delete instance', command=self.delete_instance)
        self.instance_delete_btn.pack(side=tk.TOP)
        self.controls.append(self.instance_delete_btn)

        self.instance_export_btn = Button(self.instance_opt_frame, text='Export instance', command=self.export_instance)
        self.instance_export_btn.pack(side=tk.TOP)
        self.controls.append(self.instance_export_btn)

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
        raise NotImplementedError

    def help(self) -> None:
        raise NotImplementedError

    def active_instance(self) -> Instance:
        cursel = self.instance_lb.curselection()
        if len(cursel) == 1:
            index = self.instance_lb.index(cursel[0])
            return self.instances[index]

    def view_saves(self) -> None:
        instance = self.active_instance()
        if instance is not None:
            files.browse(instance.directory / 'data' / 'save')

    def enable_controls(self):
        for c in self.controls:
            c.configure(state=tk.NORMAL)

    def disable_controls(self):
        for c in self.controls:
            c.configure(state=tk.DISABLED)

    def instance_folder(self) -> None:
        instance = self.active_instance()
        if instance is not None:
            files.browse(instance.directory)

    def reload_instances(self) -> None:
        self.instance_lb.delete(0, tk.END)
        self.instances = []
        for instance_dir in files.instance_dir.iterdir():
            if instance_dir.exists() and instance_dir.is_dir():
                instance = Instance(instance_dir)
                self.instances.append(instance)
        for instance in self.instances:
            self.instance_lb.insert(tk.END, instance)

    def edit_instance(self) -> None:
        raise NotImplementedError

    def new_instance(self) -> None:
        raise NotImplementedError

    def settings(self) -> None:
        raise NotImplementedError

    def launch_instance(self) -> None:
        instance = self.active_instance()
        if instance is not None:
            instance.launch(quit_callback=self.enable_controls())


def main():
    root = Tk()
    MultiDorf(root)
    root.mainloop()


if __name__ == '__main__':
    main()
