#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import filedialog
import tkinter as tk
from tkinter import font
from tkinter import ttk
import os, re, json, string, pprint
from functools import partial as fp
from sortedcontainers import SortedList

SPLASHSCREEN_TEXT = \
"""
 _______                                     ___  __                  
|_     _|.-----..-----..-----..-----..----..'  _||  |.-----..--.--.--.
  |   |  |  -__||     ||__ --||  _  ||   _||   _||  ||  _  ||  |  |  |
  |___|  |_____||__|__||_____||_____||__|  |__|  |__||_____||________|
                                                                      
 ______                 ___  __             _______                __ 
|      |.-----..-----..'  _||__|.-----.    |_     _|.-----..-----.|  |
|   ---||  _  ||     ||   _||  ||  _  |      |   |  |  _  ||  _  ||  |
|______||_____||__|__||__|  |__||___  |      |___|  |_____||_____||__|
                                |_____|                               
                                                                      
        === Configuration Editor for Neuronal Networks ===            
"""
PROGRAM_NAME = 'Tensorflow Configuration Tool'
TEXTFIELD_WIDTH = 60
#TEXTFIELD_PARAMS = ('arial', 10)
TEXTFIELD_PARAMS = ('Consolas', 10)
TEXTFIELD_HEIGHT = 10

MAINBORDERWIDTH = 2
INTERIORBORDERWIDTH = 2 
#PRI_BACKGROUND = '#4e88e5'
PRI_BACKGROUND = "white" 

class TagList(SortedList):           
    """Docstring for TagList. """    
                                     
    def __init__(self):              
        """TODO: to be defined1. """ 
        SortedList.__init__(self)    

    def add(self, start, end, diff):
        SortedList.add(self, start)
        index = SortedList.index(self, start)
        self.shift_values(index, diff)
        SortedList.insert(self, index + 1, end)

    def discard(self, start):
        try:
            index = SortedList.index(self, start)
            SortedList.pop(self, index + 1) # end
            SortedList.discard(self, start)
        except ValueError:
            pass

    def get_pair(self, index):
        return SortedList.__getitem__(self, index),\
               SortedList.__getitem__(self, index + 1)

    def shift_values(self, index, change):
        print("change: ", change)
        if change >= 0:
            for i in reversed(range(index + 1, SortedList.__len__(self))):
                updated_value = SortedList.__getitem__(self, i)
                updated_value += change
                SortedList.__setitem__(self, i, updated_value)
        else:
            for i in range(index + 1, SortedList.__len__(self)):
                updated_value = SortedList.__getitem__(self, i)
                updated_value += change
                SortedList.__setitem__(self, i, updated_value)


class FileObj(object):

    def __init__(self):
        """TODO: Docstring for function."""
        self.dirty_tags = TagList()
        self.textfield_length = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def json_str(self):
        return json.dumps(self._json_dict, indent=4)
    
    @property
    def json_dict(self):
        return self._json_dict

    @json_dict.setter
    def json_dict(self, d):
        self._json_dict = d

    def is_field_dirty(self, keys, value):
        if self.json_dict[keys[0]][keys[1]] != value:
            return True 
        else:
            return False


class VerticalScrollFrame(ttk.Frame):
    """ 
    A ttk frame allowing vertical scrolling.

    Use the '.interior' attribute to place widgets inside the scrollable frame.
    """
    
    def __init__(self, parent, *args, **options):
        ttk.Frame.__init__(self, parent, borderwidth=MAINBORDERWIDTH )
        self.__createWidgets()
        self.__setBindings()

    def _on_mousewheel(self, event, scroll):
        self.canvas.yview_scroll(int(scroll), "units")

    def _bind_to_mousewheel(self, event):
        self.canvas.bind_all("<Button-4>", 
                fp(self._on_mousewheel, scroll=-1))
        self.canvas.bind_all("<Button-5>", 
                fp(self._on_mousewheel, scroll=1))

    def _unbind_from_mousewheel(self, event):
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")


    def __createWidgets(self):
        '''Create widgets of the scroll frame.'''
        self.vscrollbar = ttk.Scrollbar(self, orient='vertical',
                                        style='canvas.Vertical.TScrollbar')
        self.vscrollbar.pack(side='right', fill='y', expand='false')
        self.canvas = tk.Canvas(self,
                                bd=0,
                                highlightthickness=0,
                                yscrollcommand=self.vscrollbar.set,
                                background=PRI_BACKGROUND 
                                )
        self.canvas.configure(height=screen_height - (screen_height * 0.3))
        self.canvas.pack(side='left', fill='both', expand='true')
        self.vscrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Enter>', self._bind_to_mousewheel)
        self.canvas.bind('<Leave>', self._unbind_from_mousewheel)

        #  # reset the view
        #  self.canvas.xview_moveto(0)
        #  self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = ttk.Frame(self.canvas, borderwidth=INTERIORBORDERWIDTH)
                                  
        self.interior_id = self.canvas.create_window(0, 0,
                                                     window=self.interior,
                                                     anchor='nw')

    def __setBindings(self):
        '''Activate binding to configure scroll frame widgets.'''
        self.canvas.bind('<Configure>',self.__configure_canvas_interiorframe)
        

    def __configure_canvas_interiorframe(self, event):
        '''Configure the interior frame size and the canvas scrollregion'''
        #Force the update of .winfo_width() and winfo_height()
        self.canvas.update_idletasks() 

        #Internal parameters 
        interiorReqHeight= self.interior.winfo_reqheight()
        canvasWidth    = self.canvas.winfo_width()
        canvasHeight   = self.canvas.winfo_height()

        #Set interior frame width to canvas current width
        self.canvas.itemconfigure(self.interior_id, width=canvasWidth)
        
        # Set interior frame height and canvas scrollregion
        if canvasHeight > interiorReqHeight:
            self.canvas.itemconfigure(self.interior_id,  height=canvasHeight)
            self.canvas.config(scrollregion="0 0 {0} {1}".
                               format(canvasWidth, canvasHeight))
        else:
            self.canvas.itemconfigure(self.interior_id, height=interiorReqHeight)
            self.canvas.config(scrollregion="0 0 {0} {1}".
                               format(canvasWidth, interiorReqHeight))


class MenuBar(tk.Frame):
    def __init__(self, parent, file_obj=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.fobj = file_obj 

        # Create menu bar
        self.menubar = tk.Menu(self)
        self.parent.parent.config(menu=self.menubar)

        # Create file menu
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
        self.file_menu.add_command(label='Quit', accelerator='Ctrl + Q',
                compound='left', command=self.parent.quit)

        # Create about menu
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
                self.fobj.json_dict = json.loads(_file.read())
                self.parent.editor.textfield.insert(1.0, self.fobj.json_str)
                self.parent.key_value_section.update()

    def save(self, event=None):
        if not self.fobj.name:
            save_as()
        else:
            self.write_to_file(self.fobj.name)
            self.fobj.dirty_tags.clear()
            self.parent.editor.refresh()
        return "break"

    def save_as(self, event=None):
        input_file_name = filedialog.asksaveasfilename(defaultextension=".json",
                filetypes=[("Configuration Files", "*.json")]) 
        if input_file_name:
            self.fobj.name = input_file_name
            self.write_to_file(self.fobj.name)
            self.parent.parent.title('{} - {}'
                    .format(os.path.basename(self.fobj.name), PROGRAM_NAME)) 

            return "break"

    def write_to_file(self, file_name):
        try:
            content = self.fobj.json_dict
            with open(file_name, 'w') as outfile: 
                json.dump(content, outfile)
        except IOError:
            pass
                

class KeyValueSection(tk.Frame):
    """ Section where configurations can be edited."""

    def __init__(self, parent, file_obj=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.fobj = file_obj
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        #FIXME
        self.regex_nl = re.compile('\n')

    def update(self):
        """Update the key-value section with entry fields."""

        def _accomodate_rows(j, k):
            if j < 1:
                j += 1
                return j, k
            else:
                k +=2
                return 0, k

        self.parent.editor.splash.destroy()

        self.frame = VerticalScrollFrame(self,
                    INTERIORBORDERWIDTH=2,
                )

        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        for i, (key, obj) in enumerate(self.fobj.json_dict.items(), 1):
            frame = tk.Frame(self.frame.interior)
            frame.grid(row=i, column=0, padx='20', sticky=tk.NSEW)

            ttk.Label(frame,
                      text=string.capwords(key.replace('_', ' ')),
                      justify=tk.LEFT,
                      padding=[0, 10, 0, 5],
                      font=('Arial', 10, 'bold')
                  ).grid(row=0, column=0, sticky=tk.NW)

            try:
                j = 0
                k = i
                for kkey, val in obj.items():
                    ttk.Label(frame, text=kkey, justify=tk.LEFT).grid(row=k,
                            column=j, sticky=tk.NW)

                    if isinstance(val, list):
                        val = str(val).strip('[]').replace(',', '')

                    value_field = tk.StringVar(frame, value=val)

                    entry = tk.Entry(frame, textvariable=value_field, justify=tk.LEFT)
                    entry.grid(row=k+1, column=j, sticky=tk.NW)
                    entry.bind("<FocusOut>", lambda event, keys=(key, kkey):
                            self.save_field(event, keys))

                    j, k = _accomodate_rows(j, k)

            except AttributeError as e:
                value_field = tk.StringVar(frame, value=obj)
                entry = tk.Entry(frame, textvariable=value_field, justify=tk.LEFT)
                entry.grid(row=k+1, column=j, sticky=tk.NW)
                entry.bind("<FocusOut>", lambda event, keys=(key, None):
                        self.save_field(event, keys))
                j, k = _accomodate_rows(j, k)

    def save_field(self, event, keys):
        value = event.widget.get() 
        print("value: ", value)
        print("keys: ", keys)

        self.fobj.textfield_length = len(self.regex_nl.findall(self.fobj.json_str,
            re.DOTALL)) + 1 
        print("UPDATING LINES: ", self.fobj.textfield_length) 

        try:
            if isinstance(self.fobj.json_dict[keys[0]][keys[1]], int):
                value = int(value)
            if isinstance(self.fobj.json_dict[keys[0]][keys[1]], float):
                value = float(value)
            if isinstance(self.fobj.json_dict[keys[0]][keys[1]], list):
                value = [ int(x) for x in ' '.join(value.split()).split(' ') ]
                
            if self.fobj.is_field_dirty(keys, value):
                self.fobj.json_dict[keys[0]][keys[1]] = value
        except TypeError as e:
            if self.fobj.is_field_dirty(keys, value):
                self.fobj.json_dict[keys[0]] = value

        self.parent.editor.update(keys, value)

class Editor(tk.Frame):
    def __init__(self, parent, file_obj=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.fobj = file_obj
        self.startup_screen = tk.StringVar()
        self.config(pady = 20)
        self.regex_nl = re.compile('\n')
        self.startup_screen.set(SPLASHSCREEN_TEXT)
        self.create_textfield()
        self.textfield.tag_config('match', foreground='red')#, background='yellow')

    def create_textfield(self):
            self.scrollbar = ttk.Scrollbar(self)
            self.scrollbar.pack(side='right', fill='y')
            self.textfield = tk.Text(self, font=TEXTFIELD_PARAMS, yscrollcommand=self.scrollbar.set)
            self.textfield.pack(fill='both', expand=1)
            self.scrollbar.config(command=self.textfield.yview)
            self.splash = tk.Label(self.textfield, 
                                     textvariable=self.startup_screen,
                                     font=('Courier', 8, 'bold'),
                                     bg="white",
                                     )
            self.splash.place(x=100, y=100)

    def update(self, keys, value):


        #FIXME: Build this dynamically denpending on depth
        match_all = '([^}])*'              
        search_expression = re.compile('"{}"{}"{}":\s*(\[.*?\]|".*?"|\d+\.*\d*)'.format(keys[0], match_all,
            keys[1]), re.DOTALL)

        match = search_expression.search(self.fobj.json_str)

        start = self.calc_match_position(self.fobj.json_str, match.start(2))
        end = self.calc_match_position(self.fobj.json_str, match.end(2))

        textfield_length = len(self.regex_nl.findall(self.fobj.json_str, re.DOTALL)) + 1
        diff = textfield_length - self.fobj.textfield_length
        
        self.fobj.dirty_tags.discard(start)

        print("Before TagList: " , self.fobj.dirty_tags)
        if self.fobj.is_field_dirty:
            self.fobj.dirty_tags.add(start, end, diff)
            print(" Before TagList: " , self.fobj.dirty_tags)

        self.refresh()

        self.textfield.see(end)

    def refresh(self):
        self.textfield.delete(1.0, tk.END)
        self.textfield.insert(1.0, self.fobj.json_str)
        #  for position in self.fobj.dirty_tags:
        #      self.textfield.tag_add('match', position[0], position[1])
        #FIXME: This is ugly
        for i in range(0, len(self.fobj.dirty_tags), 2):       
            pair = self.fobj.dirty_tags.get_pair(i)
            self.textfield.tag_add('match', pair[0], pair[1])


    def calc_match_position(self, string, match_index):
        """Calculates the positions of the matched value in the editor window

        :match:   matched string
        :returns: position in the form of line.column 
        """
        line = 1
        for ln in self.regex_nl.finditer(string, 0, match_index):
            line += 1

        column = match_index - ln.start() - 1

        return line + float('0.' + str(column))
        

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
        self.editor.grid(row=0, column=0, sticky=tk.NS)
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
    root.configure(padx = 10, pady = 10)
    root.columnconfigure(0, minsize=150)
    root.resizable(False, False)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
