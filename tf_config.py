#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import os

PROGRAM_NAME = 'Tensorflow Configuration Tool'
TEXTFIELD_WIDTH = 60
TEXTFIELD_PARAMS = ('arial', 10)
TEXTFIELD_HEIGHT = 10

class FileObj(object):

    """Container for the file object which is been worked on. """

    def __init__(self):
        """TODO: to be defined1. """
        self.name = ''
        

class MenuBar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.file = FileObj()
        #self.menu_items = ['File', 'Edit', 'View', 'About']
        self.menu_items = ['File', 'About']
        self.json_tree = tk.StringVar() # is a dictionary

        # create menu bar
        self.menubar = tk.Menu(self)
        self.parent.parent.config(menu=self.menubar)

        # create file menu
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file_menu)
        # Open
        self.file_menu.add_command(label='Open', accelerator='Ctrl + O',
                compound='left', command=self.open_file)
        # Save
        self.file_menu.add_command(label='Save', accelerator='Ctrl + S',
                compound='left', command=self.save)
        # Save as
        self.file_menu.add_command(label='Save as..', accelerator='Shift + Ctrl + S',
                compound='left', command=self.save_as)
        # Quit
        self.file_menu.bind('<Control-Q>', self.parent.quit)
        self.file_menu.bind('<Control-q>', self.parent.quit)

        # create about menu
        self.about_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='About', menu=self.about_menu)
    
    def open_file(self, event=None):
        input_file_name = filedialog.askopenfilename(defaultextension=".json",
        filetypes=[("Configuration files", "*.json")])
        if input_file_name:
            self.file.name = input_file_name
            self.parent.parent.title('{} - {}'.format(os.path.basename(self.file.name),
            PROGRAM_NAME))
            self.parent.editor.entry.delete(1.0, tk.END)

            with open(self.file.name) as _file:
                self.json_tree = _file.read()
                self.parent.editor.entry.insert(1.0, self.json_tree)

    def save(self):
        print('save') 

    def save_as(self):
        print('save as') 
        

class KeyValueSection(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        #self.config(height = 10)

class Editor(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(pady = 20)

        self.create_textfield()


    def create_textfield(self):
            self.scrollbar = ttk.Scrollbar(self)
            self.scrollbar.pack(side='right', fill='y')
            self.entry = tk.Text(self, font=TEXTFIELD_PARAMS, yscrollcommand=self.scrollbar.set)
            self.entry.pack()
            self.scrollbar.config(command=self.entry.yview)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Add menu bar
        self.menubar = MenuBar(self)

        # Create GUI elements
        self.key_value_section = KeyValueSection(self)
        self.editor = Editor(self)

        # Place GUI elements
        self.editor.grid(row=0, column=0)
        self.key_value_section.grid(row = 0, column = 1)
        #  self.monitor.grid(row = 1, column = 0, columnspan = 3)
        #  self.number_row.grid(row = 3, column = 0)
        #  self.char_block.grid(row = 4, column = 0)
        #  self.spacebar.grid(row = 5, column = 0)
        #  self.arrow_block.grid(row = 4, column = 1, sticky = 'S')
        #  self.number_block.grid(row = 3, column = 2, rowspan = 2)

        # bind open shortcut
        self.parent.bind('<Control-O>', self.menubar.open_file)
        self.parent.bind('<Control-o>', self.menubar.open_file)
        # bind quit shortcut
        self.parent.bind('<Control-Q>', self.quit_editor)
        self.parent.bind('<Control-q>', self.quit_editor)

    def quit_editor(self, event=None):
        self.parent.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title(PROGRAM_NAME)
    root.configure(padx = 10, pady = 10)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
