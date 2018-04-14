#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
import os, re, json, string
from functools import partial as fp
from decimal import * 

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

class DataObject(object):                
    """Object holding configuration variables."""                                         
    #config_file = 'tf_conf.json'                                 
    #json_validated = bool()                  

    def __init__(self):                      
        self.regex_nl = re.compile('\n')
        self.json_dict_flat = {}
        #  self.json_dict = self.import_file(json_file)
        #  self.gen_flat_key_dict(self.json_dict, '')
        self.dirty_tags = set() 
        self._name = ""
        
        self.textfield_length = 0
        self.previous_value = "" 

    @property
    def json_str(self):
        return json.dumps(self.json_dict, indent=4)
    
    def import_file(self, conf_file):   
        """Import configurations from tf_conf.json."""                                    
        try:                                 
            with open(str(conf_file), 'r') as infile:                                     
                conf = json.load(infile)     
                #self.json_validated = True   
                return conf                  
        except ValueError as e:              
            print("Decoding the JSON config file has failed. Please make sure the format is correct.")
            return None                      


    def gen_flat_key_dict(self, jobj, key_path):  
        """Parses json object recursively and returns path and value."""                  
        if not isinstance(jobj, dict):       
            path_tuple = tuple(key_path.strip().split(' '))

            label = key_path.split(' ')[-1]
            path = key_path.split(label)[0].strip(' ')

            if not self.json_dict_flat.get(path):
                self.json_dict_flat[path] = {} 

            self.json_dict_flat[path][label] = {}
            self.json_dict_flat[path][label]['value'] = jobj

            start, end = self.find_linenumber(self.json_str, path_tuple)
            self.json_dict_flat[path][label]['coordinates'] = [start, end]

        else:                                
            for key, value in jobj.items():  
                self.gen_flat_key_dict(value, key_path + ' ' + key)                            

    def find_linenumber(self, json_str, path):
        match_all = '([^}])*'              
        se = ''
        for i in range(len(path) - 1):
            se += '"' + path[i] + '"' + match_all

        se += '"' + path[-1] + '"' + ':\s*(\[[^}]*?\]|".*?"|\d+\.*\d*)' 

        s = re.compile(se, re.DOTALL)
        match = s.search(self.json_str)

        start = self.calc_match_position(self.json_str, match.start(len(path)))
        end = self.calc_match_position(self.json_str, match.end(len(path)))
        return start, end

    def calc_match_position(self, string, match_index):
        """Calculates the positions of the matched value in the editor window

        :match:   matched string
        :returns: position in the form of line.column 
        """
        line = 1
        for ln in self.regex_nl.finditer(string, 0, match_index):
            line += 1

        column = match_index - ln.start() - 1

        return Decimal(line) + Decimal('0.' + str(column))

    def dyn_dict_get(self, keys):          
        s = 'self.json_dict'  

        for i, el in enumerate(keys):   
            s += "[keys[" + str(i) + "]]"

        return eval(s)

    def dyn_dict_set(self, keys, val):     
        s = 'self.json_dict'  

        for i in range(len(keys)):   
            s += "[keys[" + str(i) + "]]" 

        if isinstance(val, str):
            s += " = " + str('"' + val + '"')
        else:
            s += " = " + str(val)

        exec(s)  

    def get_coords(self, keys, position):
        return self.json_dict_flat[keys[0]][keys[1]]['coordinates'][position]

    def get_init_value(self, keys):
        return self.json_dict_flat[keys[0]][keys[1]]['value']

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def is_field_dirty(self, keys, value):
        if self.json_dict_flat[keys[0]][keys[1]]['value'] != value:
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
    def __init__(self, parent, data_object=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.d_obj = data_object 

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
            self.d_obj.name = input_file_name
            self.parent.parent.title('{} - {}'.format(os.path.basename(self.d_obj.name),
            PROGRAM_NAME))
            self.parent.editor.textfield.delete(1.0, tk.END)

            with open(self.d_obj.name) as _file:
                self.d_obj.json_dict = json.loads(_file.read())
                self.parent.editor.textfield.insert(1.0, self.d_obj.json_str)
                self.parent.key_value_section.update()

        # reset previos value 
        self.d_obj.previous_value = "" 

    def save(self, event=None):
        print(self.d_obj.json_dict)
        print(self.d_obj.json_dict_flat)
        if len(self.d_obj.json_dict) == 0:
            return
        if not self.d_obj.name:
            self.save_as()
        else:
            self.write_to_file(self.d_obj.name)
            self.d_obj.dirty_tags.clear()
            self.parent.editor.refresh()
        return "break"

    def save_as(self, event=None):
        input_file_name = filedialog.asksaveasfilename(defaultextension=".json",
                filetypes=[("Configuration Files", "*.json")]) 
        if input_file_name:
            self.d_obj.name = input_file_name
            self.write_to_file(self.d_obj.name)
            self.parent.parent.title('{} - {}'
                    .format(os.path.basename(self.d_obj.name), PROGRAM_NAME)) 

            return "break"

    def write_to_file(self, file_name):
        try:
            content = self.d_obj.json_dict
            with open(file_name, 'w') as outfile: 
                json.dump(content, outfile)
        except IOError:
            pass
                

class KeyValueSection(tk.Frame):
    """ Section where configurations can be edited."""

    class ValidatingEntry(tk.Entry):
    # base class for validating entry widgets

        def __init__(self, parent, value="", **kwargs):
            tk.Entry.__init__(self, parent, **kwargs)
            self.__value = value
            self.__variable = tk.StringVar()
            self.__variable.set(value)
            self.__variable.trace("w", self.__callback)
            self.config(textvariable=self.__variable)

        def __callback(self, *dummy):
            value = self.__variable.get()
            newvalue = self.validate(value)
            if newvalue is None:
                self.__variable.set(self.__value)
            elif newvalue != value:
                self.__value = newvalue
                self.__variable.set(self.newvalue)
            else:
                self.__value = value

        def validate(self, value):
            # override: return value, new value, or None if invalid
            return value

    class IntegerEntry(ValidatingEntry):

        def validate(self, value):
            try:
                if value:
                    v = int(value)
                return value
            except ValueError:
                return None

    class FloatEntry(ValidatingEntry):

        def validate(self, value):
            try:
                if value:
                    v = float(value)
                return value
            except ValueError:
                return None

    class ArrayEntry(ValidatingEntry):

        def validate(self, value):
            try:
                if value:
                    v = list(map(lambda x: int(x), value.split()))
                return value
            except ValueError:
                return None

    class StringEntry(ValidatingEntry):

        def validate(self, value):
            try:
                if value:
                    if '"' in value:
                        raise ValueError
                return value
            except ValueError:
                return None

    def __init__(self, parent, data_object=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.d_obj = data_object
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.regex_nl = re.compile('\n')

    def _accomodate_rows(self, j, k):
        if j < 1:
            j += 1
            return j, k
        else:
            k +=2
            return 0, k

    def update(self):
        """Update the key-value section with entry fields."""

        self.parent.editor.splash.destroy()

        self.frame = VerticalScrollFrame(self, INTERIORBORDERWIDTH=2,)

        self.frame.grid(row=0, column=0, sticky=tk.NSEW)
        
        for i, (section, obj) in enumerate(self.d_obj.json_dict_flat.items(), 1):
            frame = tk.Frame(self.frame.interior)
            frame.grid(row=i, column=0, padx='20', sticky=tk.NSEW)
            ttk.Label(frame,
                      text=string.capwords(section.replace('_', ' ')),
                      justify=tk.LEFT,
                      padding=[0, 10, 0, 5],
                      font=('Arial', 10, 'bold')
                  ).grid(row=0, column=0, sticky=tk.NW)

            j = 0
            k = i

            for key, val in obj.items():
                ttk.Label(frame, text=key, justify=tk.LEFT).grid(row=k,
                        column=j, sticky=tk.NW)

                if isinstance(val['value'], int):
                    entry = self.IntegerEntry(frame, value=val['value'])
                elif isinstance(val['value'], float):
                    entry = self.FloatEntry(frame, value=val['value'])
                elif isinstance(val['value'], list):
                    val = str(val['value']).strip('[]').replace(',', '')
                    entry = self.ArrayEntry(frame, val)
                else:
                    entry = self.StringEntry(frame, value=val['value'])


                entry.config(justify=tk.LEFT)

                entry.grid(row=k+1, column=j, sticky=tk.NW)
                entry.bind("<FocusOut>", lambda event, flat_keys=(section, key):
                    self.save_field(event, flat_keys))

                j, k = self._accomodate_rows(j, k)

    def save_field(self, event, flat_keys):
        value = event.widget.get() 

        # set editor field length before changing it
        self.d_obj.textfield_length = len(self.regex_nl.findall(self.d_obj.json_str,
            re.DOTALL)) + 1 

        if isinstance(self.d_obj.get_init_value(flat_keys), int):
            try:
                value = int(value)
            except ValueError:
                value = ""
        if isinstance(self.d_obj.get_init_value(flat_keys), float):
            try:
                value = float(value)
            except ValueError:
                value = ""
        if isinstance(self.d_obj.get_init_value(flat_keys), list):
            try:
                value = [ int(x) for x in ' '.join(value.split()).split(' ') ]
            except ValueError:
                value = []

        keys = tuple((flat_keys[0] + " " + flat_keys[1]).split(' '))
        # save previous value for column comparison
        self.d_obj.previous_value = self.d_obj.dyn_dict_get(keys)
        # save value to master dict
        self.d_obj.dyn_dict_set(keys, value)
        # call the update method of the editor
        self.parent.editor.update(flat_keys, value)


class Editor(tk.Frame):
    def __init__(self, parent, data_object=None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.d_obj = data_object
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

    def vh_update(self, value, v_shift, h_shift=0):
        if h_shift != 0:
            aux = list(map(lambda x: int(x), str(value).split('.'))) 
            aux[0] = str(aux[0] + v_shift)                               
            aux[1] = str(aux[1] + h_shift)                               
            value = Decimal('.'.join(aux))                           
        else:
            value += v_shift
        return value

    def shift_positions(self, d, start_idx, v_shift, h_shift):
        for obj in d.values():
            for label in obj.values():
                start_cds = label['coordinates'][0]
                end_cds = label['coordinates'][1]
                if end_cds == start_idx:
                    label['coordinates'][1] = self.vh_update(end_cds, v_shift, h_shift)
                elif start_cds > start_idx:
                    label['coordinates'][0] = self.vh_update(start_cds, v_shift)
                    label['coordinates'][1] = self.vh_update(end_cds, v_shift)

    def update(self, flat_keys, value):
        textfield_length = len(self.regex_nl.findall(self.d_obj.json_str, re.DOTALL)) + 1
        line_diff = textfield_length - self.d_obj.textfield_length
        row_diff = len(str(value)) - len(str(self.d_obj.previous_value)) + 10 

        start = self.d_obj.get_coords(flat_keys, 0)
        end = self.d_obj.get_coords(flat_keys, 1)
        
        self.shift_positions(self.d_obj.json_dict_flat, end, line_diff, row_diff )
        self.d_obj.dirty_tags.discard(flat_keys)

        if self.d_obj.is_field_dirty(flat_keys, value):
            self.d_obj.dirty_tags.add(flat_keys)

        self.refresh()

        self.textfield.see(end)

    def refresh(self):
        self.textfield.delete(1.0, tk.END)
        self.textfield.insert(1.0, self.d_obj.json_str)
        for el in self.d_obj.dirty_tags:
            self.textfield.tag_add('match', self.d_obj.get_coords(el, 0),
                                            self.d_obj.get_coords(el, 1))


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
        # self.data_object = FileObj()
        self.data_object = DataObject()

        # Add menu bar
        self.menubar = MenuBar(self, self.data_object)

        # Create GUI elements
        self.key_value_section = KeyValueSection(self, self.data_object)
        self.editor = Editor(self, self.data_object)

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
