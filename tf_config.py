#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

from tkinter import filedialog
from tkinter import font
import os, re, json, string
from decimal import * 
from collections import OrderedDict
import pprint

import insert_dialog
from validating_entry import ValidatingEntry,\
        ArrayEntry, IntegerEntry, FloatEntry, StringEntry 
from vertical_scroll_frame import VerticalScrollFrame

#  Global constants
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
REGEX_NL = re.compile('\n')


class DataObject(object):                
    """Object holding configuration variables."""                                         
    def __init__(self):                      
        self.json_dict_flat = {} 
        self.json_dict = OrderedDict()
        self.dirty_tags = set() 
        self._name = ""
        
        self.textfield_length = 0
        self.previous_value = "" 

    @property
    def json_str(self):
        return json.dumps(self.json_dict, indent=4)
    
    def import_file(self, json_file):   
        """Import configurations from tf_conf.json."""                                    
        try:                                 
            with open(json_file, 'r') as infile:
                self.json_dict = json.load(infile)
                self.gen_flat_key_dict(self.json_dict, '')
        except ValueError as e:
            print("Decoding the JSON config file has failed. Please make sure the format is correct.")

    def gen_flat_key_dict(self, jobj, key_path):  
        """Parses json object recursively and returns path and value."""                  
        if not isinstance(jobj, dict):       
            path_tuple = tuple(key_path.strip().split(' '))

            label = key_path.split(' ')[-1]
            path = key_path[:-(len(label))].strip(' ')

            if not self.json_dict_flat.get(path):
                self.json_dict_flat[path] = {} 

            self.json_dict_flat[path][label] = {}
            self.json_dict_flat[path][label]['value'] = jobj

            start, end = self.gen_value_coords(self.json_str, path_tuple)
            self.json_dict_flat[path][label]['coords'] = [start, end]
        else:                                
            for key, value in jobj.items():  
                self.gen_flat_key_dict(value, key_path + ' ' + key)

    def gen_value_coords(self, json_str, path):
        #  print("JSON String: ", json_str)
        match_all = '([^}])*'              
        se = ''
        for i in range(len(path) - 1):
            se += '"' + path[i] + '"' + match_all

        se += '"' + path[-1] + '"' + ':\s*(\[[^}]*?\]|".*?"|\d+\.*\d*)' 
        #  print("Search expression: ", se)

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
        for ln in REGEX_NL.finditer(string, 0, match_index):
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
            try:
                eval(s)
            except KeyError:
                exec(s + " = {}")

        if isinstance(val, str):
            s += " = " + str('"' + val + '"')
        else:
            s += " = " + str(val)

        exec(s)  

    def get_coords(self, keys, position):
        return self.json_dict_flat[keys[0]][keys[1]]['coords'][position]

    def get_init_value(self, keys):
        return self.json_dict_flat[keys[0]][keys[1]]['value']

    def flat_keys_list(self):
        return list(self.json_dict_flat)

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


class MenuBar(ttk.Frame):
    def __init__(self, parent, data_object=None, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
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
                compound=tk.LEFT, command=self.open)
        # Save
        self.file_menu.add_command(label='Save', accelerator='Ctrl + S',
                compound=tk.LEFT, command=self.save)
        # Save as
        self.file_menu.add_command(label='Save as..', accelerator='Shift + Ctrl + S',
                compound=tk.LEFT, command=self.save_as)
        # Quit
        self.file_menu.add_command(label='Quit', accelerator='Ctrl + Q',
                compound=tk.LEFT, command=self.parent.quit)

        # Create edit menu
        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Edit', menu=self.edit_menu)
        # Add object
        self.edit_menu.add_command(label='Add Object', accelerator='Shift + Ctrl + O',
                compound=tk.LEFT, command=self.add_object)

        # Create about menu
        self.about_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='About', menu=self.about_menu)
    
    # File menu methods
    def open(self, event=None):
        input_file_name = filedialog.askopenfilename(defaultextension=".json",
        filetypes=[("Configuration files", "*.json")])
        if input_file_name:
            self.d_obj.name = input_file_name
            self.parent.parent.title('{} - {}'.format(os.path.basename(self.d_obj.name),
            PROGRAM_NAME))
            self.parent.editor.textfield.configure(state=tk.NORMAL)
            self.parent.editor.textfield.delete(1.0, tk.END)

            ##FIXME: Need to instantiate a new data object
            ##FIXME
            self.d_obj.json_dict_flat.clear()
            self.d_obj.dirty_tags.clear()
            self.d_obj.textfield_length = 0
            self.d_obj.previous_value = ""

            self.d_obj.import_file(input_file_name)
            self.parent.editor.textfield.insert(1.0, self.d_obj.json_str)
            self.parent.editor.textfield.configure(state=tk.DISABLED)
            self.parent.key_value_section.create_entry_boxes()

        # reset previos value 
        self.d_obj.previous_value = "" 

    def save(self, event=None):
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
        if len(self.d_obj.json_dict) == 0:
            return

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

    # Edit menu methods
    def add_object(self, event=None, object_key="Default"):
        self.parent.create_dialog()
                

class KeyValueSection(ttk.Frame):
    """ Section where configurations can be edited."""

    def __init__(self, parent, data_object=None, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.d_obj = data_object

        # style variables
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def _accomodate_rows(self, j, k):
        if j < 1:
            j += 1
            return j, k
        else:
            k +=2
            return 0, k

    def create_entry_boxes(self):
        """Update the key-value section with entry fields."""

        self.label_style = ttk.Style()
        self.label_style.configure("label_style.TLabel", 
                          justify=tk.LEFT,
                          padding=[0, 10, 0, 5],
                          font=('Arial', 10, 'bold')
                          )

        self.parent.editor.splash.destroy()
        self.parent.editor.textfield.configure(width=self.parent.editor.textfield_width)
        self.frame = VerticalScrollFrame(self, (screen_height - (screen_height * 0.3)))

        self.frame.grid(row=0, column=0, sticky=tk.NSEW)
        
        for i, (section, obj) in enumerate(self.d_obj.json_dict_flat.items(), 1):
            frame = ttk.Frame(self.frame.interior)
            frame.grid(row=i, column=0, padx='20', sticky=tk.NSEW)
            ttk.Label(frame, style="label_style.TLabel",
                      text=string.capwords(section.replace('_', ' '))
                  ).grid(row=0, column=0, sticky=tk.NW)

            j = 0
            k = i

            for key, val in obj.items():
                ttk.Label(frame, text=key, justify=tk.LEFT).grid(row=k,
                        column=j, sticky=tk.NW)

                if isinstance(val['value'], int):
                    entry = IntegerEntry(frame, value=val['value'])
                elif isinstance(val['value'], float):
                    entry = FloatEntry(frame, value=val['value'])
                elif isinstance(val['value'], list):
                    val = str(val['value']).strip('[]').replace(',', '')
                    entry = ArrayEntry(frame, val)
                else:
                    entry = StringEntry(frame, value=val['value'])

                entry.config(justify=tk.LEFT)

                entry.grid(row=k+1, column=j, sticky=tk.NW)
                entry.bind("<FocusOut>", lambda event, flat_keys=(section, key):
                    self.save_field(event, flat_keys))

                j, k = self._accomodate_rows(j, k)

    def save_field(self, event, flat_keys):
        # FIXME: get position of event inside canvas
        #  print(event.widget.winfo_y())
        #  print(self.frame.canvas.coords(entry))
        
        value = event.widget.get() 

        # set editor field length before changing it
        self.d_obj.textfield_length = len(REGEX_NL.findall(self.d_obj.json_str,
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
        self.parent.editor.update_tags(flat_keys, value)


class Editor(ttk.Frame):
    def __init__(self, parent, data_object=None, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.d_obj = data_object

        # style variables
        self.splashscreen_width = 80 
        self.textfield_width = 50
        self.textfield_font = ('Consolas', 10)

        self.startup_screen = tk.StringVar()

        self.frame_style = ttk.Style()
        self.frame_style.configure("TFrame", pady = 20)
        self.configure(style="TFrame")

        self.startup_screen.set(SPLASHSCREEN_TEXT)
        self.create_textfield()
        self.textfield.tag_config('match', foreground='red')


    def create_textfield(self):
            self.scrollbar = ttk.Scrollbar(self)
            self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.textfield = tk.Text(self, font=self.textfield_font, 
                    yscrollcommand=self.scrollbar.set,
                    width=self.splashscreen_width)
            # make textfield copy-pastable
            self.textfield.bind("<1>", lambda event: self.textfield.focus_set())
            self.textfield.pack(fill=tk.BOTH, expand=1)
            self.scrollbar.config(command=self.textfield.yview)

            self.splash_style = ttk.Style()                                                           
            self.splash = ttk.Label(self.textfield, textvariable=self.startup_screen, 
                    style="SPLASH.TLabel")
            self.splash_style.configure("SPLASH.TLabel", font=('Courier', 8, 'bold'), 
                    background="white", anchor=tk.CENTER, padding=50)
            self.splash.pack()

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
                start_cds = label['coords'][0]
                end_cds = label['coords'][1]
                if end_cds == start_idx:
                    label['coords'][1] = self.vh_update(end_cds, v_shift, h_shift)
                elif start_cds > start_idx:
                    label['coords'][0] = self.vh_update(start_cds, v_shift)
                    label['coords'][1] = self.vh_update(end_cds, v_shift)

    def update_tags(self, flat_keys, value):
        print("Flat keys inside update_tags (Editor): ", flat_keys)
        textfield_length = len(REGEX_NL.findall(self.d_obj.json_str, re.DOTALL)) + 1
        line_diff = textfield_length - self.d_obj.textfield_length
        row_diff = len(str(value)) - len(str(self.d_obj.previous_value)) + 10 

        start = self.d_obj.get_coords(flat_keys, 0)
        end = self.d_obj.get_coords(flat_keys, 1)
        
        self.shift_positions(self.d_obj.json_dict_flat, end, line_diff, row_diff )
        self.d_obj.dirty_tags.discard(flat_keys)

        #  if self.d_obj.is_field_dirty(flat_keys, value):
        self.d_obj.dirty_tags.add(flat_keys)

        start = self.d_obj.get_coords(flat_keys, 0)
        end = self.d_obj.get_coords(flat_keys, 1)
        print("start inside update_tags: ", start)
        print("end same same: ", end)

        self.refresh()
        self.textfield.see(end)

    def refresh(self):
        self.textfield.configure(state=tk.NORMAL)
        self.textfield.delete(1.0, tk.END)
        self.textfield.insert(1.0, self.d_obj.json_str)
        for el in self.d_obj.dirty_tags:
            self.textfield.tag_add('match', self.d_obj.get_coords(el, 0),
                                            self.d_obj.get_coords(el, 1))
        self.textfield.configure(state=tk.DISABLED)


class CreateDialog(insert_dialog.Dialog):
    def __init__(self, parent, data_object, title):
        print("CREATED NEW DIALOG")
        self.tab_widgets = []
        self.tab_ids = ["Array", "Float", "Integer", "String"]
        self.checked = tk.IntVar()
        self.flat_keys = tk.StringVar()
        self.data_object = data_object
        insert_dialog.Dialog.__init__(self, parent, title)

    def body(self, root):
        self.options_frame = ttk.Frame(root)
        self.options_frame.pack()

        self.n = ttk.Notebook(root)

        # create tabs
        for element in self.tab_ids:
            tf = ttk.Frame(self.n, padding=20)
            self.tab_widgets.append(self.create_tabs(tf, element))
            self.n.add(tf, text=element)

        # checkbutton 
        self.checked.set(0)
        self.obj_cb = ttk.Checkbutton(self.options_frame,
                                      variable=self.checked,
                                      text="Inside new object", 
                                      onvalue=1,
                                      offvalue=0,)
        self.obj_cb.grid(row=0, column=0)
        self.obj_cb.configure(command=lambda e=[ x[1] for x in self.tab_widgets ],
                v=self.checked: self.toggle_objectname_field(e,v))

        self.n.pack()


    def create_tabs(self, tab, value_type):

        # create elements
        nodes = ttk.Combobox(tab, textvariable=self.flat_keys)
        obj_key_entry = StringEntry(tab, state=tk.DISABLED)
        key_entry = StringEntry(tab)

        if value_type == "Array":
            value_entry = ArrayEntry(tab)
        elif value_type == "Float":
            value_entry = FloatEntry(tab)
        elif value_type == "Integer":
            value_entry = IntegerEntry(tab)
        elif value_type == "String":
            value_entry = StringEntry(tab)

        # key list config and placement
        nodes['values'] = (self.parent.data_object.flat_keys_list()) 
        nodes.grid(row=0, column=0, sticky=tk.NW)

        # Object key label
        ttk.Label(tab, style="id_label_style.TLabel", text="Object Key"
                 ).grid(row=1, column=0, sticky=tk.NW)

        # Object key entry
        obj_key_entry.grid(row=2, column=0, sticky=tk.NW)

        # Key label
        key_label = ttk.Label(tab, style="id_label_style.TLabel", text="Key"
                 ).grid(row=3, column=0, sticky=tk.NW)

        # Key entry
        key_entry.grid(row=4, column=0, sticky=tk.NW)
        
        # Value label
        ttk.Label(tab, style="id_label_style.TLabel", text="Value"
                 ).grid(row=5, column=0, sticky=tk.NW)

        # Value entry
        value_entry.grid(row=6, column=0, sticky=tk.NW)

        return [nodes, obj_key_entry, key_entry, value_entry]


    def apply(self):
        active_tab = self.n.index(self.n.select())       

        node = self.tab_widgets[active_tab][0].get().strip().replace(' ', '_').lower()
        key = self.tab_widgets[active_tab][2].get().strip().replace(' ', '_').lower()
        value = self.tab_widgets[active_tab][3].get()

        if active_tab == 0:
            try:
                value = [ int(x) for x in ' '.join(value.split()).split(' ') ]
            except ValueError:
                value = []
        elif active_tab == 1:
            value = float(value)
        elif active_tab == 2:
            value = int(value)
        elif active_tab == 3:
            value = value.strip() # strip spaces from string, left and right

        if self.checked.get() == 1:
            object_key = self.tab_widgets[active_tab][1].get().strip().replace(' ', '_').lower()
            aux = (node + " " + object_key + " " + key).strip()
        else:
            aux = (node + " " + key).strip()

        keys = tuple(aux.split(' '))

        self.parent.data_object.dyn_dict_set(keys, value)

        self.parent.data_object.gen_flat_key_dict(self.parent.data_object.json_dict, "")
        self.parent.key_value_section.create_entry_boxes()
        print("Keys: ", keys)
        self.parent.editor.update_tags(keys, value)
        #  self.parent.editor.refresh()

    def toggle_objectname_field(self, entry_widgets, var):
        for ew in entry_widgets:
            if var.get() == 0:
                ew.configure(state=tk.DISABLED)
            else:
                ew.configure(state=tk.NORMAL)


class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
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
        # bind add object
        self.parent.bind('<Control-Shift-O>', self.menubar.add_object)
        self.parent.bind('<Control-Shift-o>', self.menubar.add_object)

    def quit_editor(self, event=None):
        self.parent.destroy()

    def create_dialog(self):
        self.obj_dialog = CreateDialog(self, self.data_object, "Create Object")
        self.parent.wait_window(self.obj_dialog.parent.parent)

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
