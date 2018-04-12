#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import filedialog
import tkinter as tk
from tkinter import font
from tkinter import ttk
import os, re, json, string, pprint
from functools import partial as fp
from sortedcontainers import SortedList
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

class Configurations(object):                
    """Object holding configuration variables."""                                         
    config_file = 'tf_conf.json'                                 
    json_validated = bool()                  

    def __init__(self):                      
        self.regex_nl = re.compile('\n')
        self.json_dict_flat = {}
        self.json_dict = self.__import_configs(self.config_file)                            
        self.json_dict_cmp = self.json_dict
        self.parse_json(self.json_dict, '')                                           
        self.dirty_tags = set() 
        
        self.textfield_length = 0
        #  print(self.json_dict)
        #  print(self.json_dict_flat)
        #  print(self.json_str)

    @property
    def json_str(self):
        return json.dumps(self.json_dict, indent=4)
    
    def __import_configs(self, conf_file):   
        """Import configurations from tf_conf.json."""                                    
        try:                                 
            with open(str(conf_file), 'r') as infile:                                     
                conf = json.load(infile)     
                self.json_validated = True   
                return conf                  
        except ValueError as e:              
            print("Decoding the JSON config file has failed. Please make sure the format is correct.")
            return None                      


    def parse_json(self, jobj, key_path):  
        """Parses json object recursively and returns path and value."""                  
        if not isinstance(jobj, dict):       
            #print(key_path)
            path_tuple = tuple(key_path.strip().split(' '))

            label = key_path.split(' ')[-1]
            #print("Label: ", label)
            path = key_path.split(label)[0].strip(' ')
            #print("Path: ", path)
            if not self.json_dict_flat.get(path):
                self.json_dict_flat[path] = {} 
            self.json_dict_flat[path][label] = {}
            self.json_dict_flat[path][label]['value'] = jobj

            start, end = self.find_linenumber(self.json_str, path_tuple)
            self.json_dict_flat[path][label]['coordinates'] = [start, end]

        else:                                
            for key, value in jobj.items():  
                self.parse_json(value, key_path + ' ' + key)                            

    def find_linenumber(self, json_str, path):
        match_all = '([^}])*'              
        se = ''
        for i in range(len(path) - 1):
            se += '"' + path[i] + '"' + match_all

        se += '"' + path[-1] + '"' + ':\s*(\[[^}]*?\]|".*?"|\d+\.*\d*)' 

        s = re.compile(se, re.DOTALL)
        match = s.search(self.json_str)

        start = self.calc_match_position(self.json_str, match.start(2))
        end = self.calc_match_position(self.json_str, match.end(2))
        #  print("Start: {}, End: {}".format(start), end))
        return start, end

    def calc_match_position(self, string, match_index):
        """Calculates the positions of the matched value in the editor window

        :match:   matched string
        :returns: position in the form of line.column 
        """
        line = 1
        for ln in self.regex_nl.finditer(string, 0, match_index):
            line += 1
            #  print(ln)

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

        print("Exec string: ", s)
        exec(s)  

    def print_configs(self):                 
        """Print out variables parsed from json file."""                                  
        attrs = dict((key, getattr(self, key)) for key in dir(self) if key.startswith('self'))        
        for key, value in attrs.items():     
            print("{}: {}".format(key, value))                                            

    def validated(self):                     
        return self.json_validated           

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def is_field_dirty(self, keys, value):
        if self.json_dict_cmp[keys[0]][keys[1]] != value:
            print("Dirty")
            return True
        else:
            print("Clean")
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

        self.frame = VerticalScrollFrame(self, INTERIORBORDERWIDTH=2,)

        self.frame.grid(row=0, column=0, sticky=tk.NSEW)
        
        for i, (section, obj) in enumerate(self.fobj.json_dict_flat.items(), 1):
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

                if isinstance(val['value'], list):
                    val = str(val['value']).strip('[]').replace(',', '')
                else:
                    val = val['value']

                value_field = tk.StringVar(frame, value=val)

                entry = tk.Entry(frame, textvariable=value_field, justify=tk.LEFT)
                entry.grid(row=k+1, column=j, sticky=tk.NW)
                entry.bind("<FocusOut>", lambda event, keys=tuple((section + " " +
                    key).split(' ')), flat_keys=(section, key): self.save_field(event, keys, flat_keys))

                j, k = _accomodate_rows(j, k)


    def save_field(self, event, keys, flat_keys):
        value = event.widget.get() 
        print("keys: ", keys)
        print("flat_keys: ", flat_keys)
        #print("value: ", value)

        self.fobj.textfield_length = len(self.regex_nl.findall(self.fobj.json_str,
            re.DOTALL)) + 1 
        #print("UPDATING LINES: ", self.fobj.textfield_length) 

        #  try:
        if isinstance(self.fobj.json_dict_flat[flat_keys[0]][flat_keys[1]]['value'], int):
            value = int(value)
        if isinstance(self.fobj.json_dict_flat[flat_keys[0]][flat_keys[1]]['value'], float):
            value = float(value)
        if isinstance(self.fobj.json_dict_flat[flat_keys[0]][flat_keys[1]]['value'], list):
            print("its a list")
            value = [ int(x) for x in ' '.join(value.split()).split(' ') ]
            
        #self.fobj.json_dict[keys[0]][keys[1]] = value
        self.fobj.dyn_dict_set(keys, value)

        self.parent.editor.update(keys, flat_keys, value)

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

    def vh_update(self, value, v_shift, h_shift=0):
        if h_shift != 0:
            aux = list(map(lambda x: int(x), str(value).split('.'))) 
            aux[0] = str(aux[0] + v_shift)                               
            aux[1] = str(aux[1] + h_shift)                               
            value = Decimal('.'.join(aux))                           
        else:
            value += v_shift
        #  print(value)
        return value

    def shift_positions(self, d, start_idx, v_shift, h_shift):           
        #  print("start_idx:", start_idx)
        for obj in d.values():                           
            for label in obj.values():                   
                #  print("label: ", label['coordinates'])
                if label['coordinates'][1] == start_idx:
                    label['coordinates'][1] = self.vh_update(label['coordinates'][1], v_shift, h_shift)
                    #  print("label after: ", label['coordinates'])
                elif label['coordinates'][0] > start_idx:
                    #  print("label 2: ", label['coordinates'])
                    label['coordinates'][0] = self.vh_update(label['coordinates'][0], v_shift)
                    label['coordinates'][1] = self.vh_update(label['coordinates'][1], v_shift)
                    #  print("label 2 after: ", label['coordinates'])

    def update(self, keys, flat_keys, value):
        print(keys)
        textfield_length = len(self.regex_nl.findall(self.fobj.json_str, re.DOTALL)) + 1
        line_diff = textfield_length - self.fobj.textfield_length
        #FIXME
        row_diff = 3 

        start = self.fobj.json_dict_flat[flat_keys[0]][flat_keys[1]]['coordinates'][0]
        end = self.fobj.json_dict_flat[flat_keys[0]][flat_keys[1]]['coordinates'][1]
        
        self.shift_positions(self.fobj.json_dict_flat, end, line_diff, row_diff )
        self.fobj.dirty_tags.discard(keys)

        #if self.fobj.is_field_dirty:
        if self.fobj.json_dict_flat[flat_keys[0]][flat_keys[1]]['value'] != value:
            self.fobj.dirty_tags.add(flat_keys)

        self.refresh()

        self.textfield.see(end)

    def refresh(self):
        self.textfield.delete(1.0, tk.END)
        self.textfield.insert(1.0, self.fobj.json_str)
        for el in self.fobj.dirty_tags:
            self.textfield.tag_add('match', self.fobj.json_dict_flat[el[0]][el[1]]['coordinates'][0], 
                                            self.fobj.json_dict_flat[el[0]][el[1]]['coordinates'][1])


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
        # self.file_obj = FileObj()
        self.file_obj = Configurations()

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
