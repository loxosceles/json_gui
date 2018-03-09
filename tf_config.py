#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import os
import json 
import string
import pprint

PROGRAM_NAME = 'Tensorflow Configuration Tool'
TEXTFIELD_WIDTH = 60
TEXTFIELD_PARAMS = ('arial', 10)
TEXTFIELD_HEIGHT = 10

class FileObj(object):

    """Container for the file object which is been worked on. """

    def __init__(self):
        """TODO: to be defined1. """
        self.name = ''
        #self.json_tree = tk.StringVar()
        self.json_tree_dict = {} 
    
    def json_tree(self):
        return json.dumps(self.json_tree_dict, indent=4, sort_keys=True)

class MenuBar(tk.Frame):
    def __init__(self, parent, file_obj=None, *args, **kwargs):
        #tk.Frame.__init__(self, parent, *args, **kwargs)
        tk.Frame.__init__(self)
        self.parent = parent
        self.fobj = file_obj 

        #self.menu_items = ['File', 'Edit', 'View', 'About']
        self.menu_items = ['File', 'About']

        # create menu bar
        self.menubar = tk.Menu(self)
        self.parent.parent.config(menu=self.menubar)

        # create file menu
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.file_menu)
        # Open
        self.file_menu.add_command(label='Open', accelerator='Ctrl + O',
                compound='left', command=self.open)
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
    
    def open(self, event=None):
        input_file_name = filedialog.askopenfilename(defaultextension=".json",
        filetypes=[("Configuration files", "*.json")])
        if input_file_name:
            self.fobj.name = input_file_name
            self.parent.parent.title('{} - {}'.format(os.path.basename(self.fobj.name),
            PROGRAM_NAME))
            self.parent.editor.textfield.delete(1.0, tk.END)

            with open(self.fobj.name) as _file:
                #self.fobj.json_tree = _file.read()
                self.fobj.json_tree_dict = json.loads(_file.read())
                self.parent.editor.textfield.insert(1.0, self.fobj.json_tree())
                self.parent.key_value_section.update()

    def save(self, event=None):
        print('save') 

    def save_as(self, event=None):
        print('save as') 
        

class KeyValueSection(tk.Frame):
    def __init__(self, parent, file_obj=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.fobj = file_obj
        self.content = tk.StringVar()
        self.content.set("Please load a config file")
        #  self.keys_values = ttk.Label(self, textvariable=self.content, padding=[50, 0, 10, 0])
        #  self.keys_values.pack()
        
        self.variables = {'str':tk.StringVar, 'int':tk.IntVar, 'list':tk.StringVar} 

    def save_field(self, event, keys):
        value = event.widget.get() 
        print(keys[0])
        print(keys[1])
        print(value)
        # print(self.fobj.json_tree)
        try:
            if isinstance(self.fobj.json_tree_dict[keys[0]][keys[1]], int):
                value = int(value)
            if isinstance(self.fobj.json_tree_dict[keys[0]][keys[1]], float):
                value = float(value)
            if isinstance(self.fobj.json_tree_dict[keys[0]][keys[1]], list):
                value = [ int(x) for x in value.split(' ') ]

            self.fobj.json_tree_dict[keys[0]][keys[1]] = value
        except TypeError as e:
            print(e)
            self.fobj.json_tree_dict[keys[0]] = value

        #print(self.fobj.json_tree_dict)
        self.parent.editor.update()


    def update(self):

        def accomodate_rows(j, k):
            if j < 2:
                j += 1
                return j, k
            else:
                #  j = 0
                k +=2
                return 0, k
        i = 0
        for key, obj in self.fobj.json_tree_dict.items():
            i += 1
            frame = tk.Frame(self)
            frame.grid(row=i, column=0, padx='20', sticky='NW')
            #key = string.capwords(key.replace('_', ' '))

            ttk.Label(frame, 
                      text=string.capwords(key.replace('_', ' ')), 
                      justify=tk.LEFT, 
                      padding=[0, 10, 0, 5], 
                      font=('Arial', 10, 'bold')
                  ).grid(row=0, column=0, sticky='NW')

            try:
                j = 0
                k = i
                for kkey, val in obj.items():
                    ttk.Label(frame, text=kkey, justify=tk.LEFT).grid(row=k, column=j, sticky='NW')

                    if isinstance(val, int):
                        value_field = tk.IntVar(frame, value=val) 
                    if isinstance(val, list):
                        vv = str(val).strip('[]').replace(',', '')
                        value_field = tk.StringVar(frame, value=val)
                    if isinstance(val ,float):
                        value_field = tk.DoubleVar(frame, value=val)

                    tmp = tk.Entry(frame, textvariable=value_field, justify=tk.LEFT)
                    tmp.grid(row=k+1, column=j, sticky='NW')
                    tmp.bind("<FocusOut>", lambda event, keys=(key, kkey): self.save_field(event, keys))

                    j, k = accomodate_rows(j, k)

            except AttributeError as e:
                value_field = tk.StringVar(frame, value=obj)
                tmp = tk.Entry(frame, textvariable=value_field, justify=tk.LEFT)
                tmp.grid(row=k+1, column=j, sticky='NW')
                tmp.bind("<FocusOut>", lambda event, keys=(key, None): self.save_field(event, keys))
                j, k = accomodate_rows(j, k)


class Editor(tk.Frame):
    def __init__(self, parent, file_obj=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.fobj = file_obj
        self.config(pady = 20)

        self.create_textfield()

    def create_textfield(self):
            self.scrollbar = ttk.Scrollbar(self)
            self.scrollbar.pack(side='right', fill='y')
            self.textfield = tk.Text(self, font=TEXTFIELD_PARAMS, yscrollcommand=self.scrollbar.set)
            self.textfield.pack(fill='both', expand=1)
            self.scrollbar.config(command=self.textfield.yview)

    def update(self):
        print("updating the editor")
        #print(self.fobj.json_tree)
        #self.entry.set(fobj.json_tree)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.file_obj = FileObj()

        # Add menu bar
        self.menubar = MenuBar(self, self.file_obj)

        # Create GUI elements
        self.key_value_section = KeyValueSection(self, self.file_obj)
        self.editor = Editor(self, self.file_obj)

        # Place GUI elements
        self.editor.grid(row=0, column=0, sticky='NS')
        self.key_value_section.grid(row = 0, column = 1)

        # bind open shortcut
        self.parent.bind('<Control-O>', self.menubar.open)
        self.parent.bind('<Control-o>', self.menubar.open)
        # bind save shortcut
        self.parent.bind('<Control-s>', self.menubar.save)
        self.parent.bind('<Control-S>', self.menubar.save)
        # bind save as shortcut
        self.parent.bind('<Control-Shift-s>', self.menubar.save_as)
        self.parent.bind('<Control-Shift-S>', self.menubar.save_as)
        # bind quit shortcut
        self.parent.bind('<Control-Q>', self.quit_editor)
        self.parent.bind('<Control-q>', self.quit_editor)

    def quit_editor(self, event=None):
        self.parent.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title(PROGRAM_NAME)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry('{}x{}'.format(int(screen_width // 2.5), int(screen_height)))
    root.configure(padx = 10, pady = 10)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
