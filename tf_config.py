#!/usr/bin/env python
# -*- coding: utf-8 -*-

## imports

# debugger
import pudb

import tkinter as tk
from tkinter import ttk

from tkinter import filedialog
from tkinter import font
import os, re, json, string
from decimal import *
from collections import OrderedDict
from orderedset import OrderedSet
from copy import deepcopy

from functools import reduce
import operator

import copy
import pprint

import dialog_window
from validating_entry import ValidatingEntry,\
        ArrayEntry, IntegerEntry, FloatEntry, StringEntry
from vertical_scroll_frame import VerticalScrollFrame

##  Global constants
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
ARROW_SYM = ' \u2799 '


class DataObject(object):
    """Object holding configuration variables. """

    def __init__(self):
        """TODO: to be defined1. """
        self.json_dict_flat = OrderedDict()
        self.json_file_repres = OrderedDict()
        self.json_dict = OrderedDict()
        self.dirty_tags = set()
        self._name = ""

        self._textfield_length = 0
        self.previous_value = ""

    @property
    def json_str(self):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        return json.dumps(self.json_dict, indent=4)

    @property
    def name(self):
        return self._name

    @property
    def prev_tf_length(self):
        return self._textfield_length

    @property
    def curr_tf_length(self):
        return len(self.json_str.split('\n'))

    @name.setter
    def name(self, name):
        self._name = name

    def is_live(self):
        return True if self.name else False

    def is_empty(self):
        return True if not self.json_dict else False

    def import_file(self, json_file):
        """Import configurations from tf_conf.json.

        :json_file: Name of the json file on disk
        :returns:   None

        """
        try:
            with open(json_file, 'r') as infile:
                self.json_dict = json.load(infile)
                self.gen_file_dict()
                self.gen_flat_key_dict()
        except ValueError as e:
            print("Decoding the JSON config file has failed. Please make sure the\
                    format is correct.")

    def update_json_dict(self, value, flat_keys):

        path = flat_keys[:-1]
        label = flat_keys[-1]
        fd_value = self.json_dict_flat[path][label]['buffered_value']

        if isinstance(fd_value, int):
            try:
                value = int(value)
            except ValueError:
                value = ""
        if isinstance(fd_value, float):
            try:
                value = float(value)
            except ValueError:
                value = ""
        if isinstance(fd_value, list):
            try:
                value = [ int(x) for x in ' '.join(value.split()).split(' ') ]
            except ValueError:
                value = []

        # set textfield field length before it changes (on save)
        self.set_prev_tf_length()

        # save previous value for column comparison
        # FIXME: move this into flat_dict
        self.previous_value = self.dyn_dict_get(flat_keys)

        # save value to master dict
        self.dyn_dict_set(value, flat_keys)

        # call the update method of the monitor
        self.update_tags(value, flat_keys)

    def gen_file_dict(self):
        """ Parse json object recursivly and build a dictionary holding (flat)
        path and value.

        This method serves as a representation of the read-in file. The resulting
        dictionary will not be modified during execution. Instead, it holds the
        original structure of the file.

        :jsd:    The json dictionary which was built from the file
        :jsfrep: The resulting dictionary as a representation of the file

        """
        def _gen_dict(d, path_tuple=tuple()):
            if not isinstance(d, dict):
                label = path_tuple[-1]
                path = path_tuple[:-1]

                if not self.json_file_repres.get(path):
                    self.json_file_repres[path] = {}

                self.json_file_repres[path][label] = {}
                self.json_file_repres[path][label]['original_value'] = d

            else:
                for key, value in d.items():
                    _gen_dict(value, path_tuple + (key,))

        self.json_file_repres.clear()
        _gen_dict(self.json_dict)

    def gen_flat_key_dict(self):
        """ Parses json object recursively and returns path and value.

        :returns: None

        """
        def gen_dict(d, path_tuple=tuple()):
            if not isinstance(d, dict):
                label = path_tuple[-1]
                path = path_tuple[:-1]

                if not self.json_dict_flat.get(path):
                    self.json_dict_flat[path] = {}

                self.json_dict_flat[path][label] = {}
                self.json_dict_flat[path][label]['buffered_value'] = d

                try:
                    self.json_dict_flat[path][label]['original_value'] =\
                            self.json_file_repres[path][label]['original_value']
                except KeyError as e:
                    self.json_dict_flat[path][label]['original_value'] = None

                start, end = self.gen_value_coords(path_tuple)
                self.json_dict_flat[path][label]['coords'] = [start, end]
            else:
                for key, value in d.items():
                    gen_dict(value, path_tuple + (key,))

        self.json_dict_flat.clear()
        gen_dict(self.json_dict)

    def gen_value_coords(self, path):

        def _create_dict(ds):
            l = ds.split('\n')
            return l, [x.lstrip() for x in l]

        def _count_array_length(l):
            count = 0
            for el in l:
                count += 1
                if el.endswith('],') or el.endswith(']'):
                    return count

        def _findkey(l, t, lev=0, ind=0):
            if ind == len(t):
                return 1
            else:
                el = l[0]
                try:
                    if el.startswith('"' + t[ind]) and t.index(t[ind]) == lev:
                        ind += 1
                except IndexError as e:
                    pass

                if "{" in el:
                    lev += 1
                if "}" in el:
                    lev -= 1
                return 1 + _findkey(l[1:], t, lev, ind)

        l, ll = _create_dict(self.json_str) # l: list, ll: list (spaces stripped)

        start_row  = _findkey(ll[1:], path)
        idx = start_row - 1
        start_col = l[idx].find(':') + 2

        if l[idx].endswith('['):
            end_row = _count_array_length(l[idx + 1:]) + start_row
            end_col = start_col
        else:
            end_row = start_row
            end_col = len(l[idx])

        start = Decimal(start_row) + Decimal('0.' + str(start_col))
        end  = Decimal(end_row) + Decimal('0.' + str(end_col))

        return start, end

    def dyn_dict_get(self, flat_keys):
        try:
            return reduce(operator.getitem, flat_keys, self.json_dict)
        except KeyError:
            pass

    def dyn_dict_set(self, value, flat_keys):
        dic = self.json_dict

        for key in flat_keys[:-1]:
            dic = dic.setdefault(key, {})
        dic[flat_keys[-1]] = value

    def dyn_dict_delete(self, flat_keys):
        del self.dyn_dict_get(flat_keys[:-1])[flat_keys[-1]]

    def get_coords(self, flat_keys, position):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        path = flat_keys[:-1]
        label = flat_keys[-1]
        return self.json_dict_flat[path][label]['coords'][position]

    def node_list(self):
        node_set = OrderedSet()
        node_key_dict = OrderedDict()

        def get_list(d, path_tuple=tuple()):
            if not isinstance(d, dict):
                label = path_tuple[-1]
                path = path_tuple[:-1]
                if node_key_dict.get(path):
                    node_key_dict[path].append(label)
                else:
                    node_key_dict[path] = [label]
                return
            else:
                for key, value in d.items():
                    if not isinstance(value, dict):
                        node_set.add(path_tuple)
                    else:
                        node_set.add(path_tuple + (key,))
                    get_list(value, path_tuple + (key,))

        get_list(self.json_dict)
        node_set.discard('')
        return list(node_set), node_key_dict

    def is_field_dirty(self, flat_keys, value):
        """Boolean method which checks if a field has been modified.

        :keys:    flat keys in order to find the value
        :value:   current value
        :returns: True if the value differs from the original one, else False
        """
        path = flat_keys[:-1]
        label = flat_keys[-1]
        if self.json_dict_flat[path][label]['original_value'] != value:
            return True
        else:
            return False

    def set_prev_tf_length(self):
        self._textfield_length = len(self.json_str.split('\n'))

    def clean_dirty_tags(self, flat_keys):
        for el in deepcopy(self.dirty_tags):
            if flat_keys == el[:len(flat_keys)]:
                self.dirty_tags.discard(el)

    def vh_update(self, value, v_shift, h_shift=0):
        if h_shift != 0:
            aux = list(map(lambda x: int(x), str(value).split('.')))
            aux[0] = str(aux[0] + v_shift)
            aux[1] = str(aux[1] + h_shift)
            value = Decimal('.'.join(aux))
        else:
            value += v_shift
        return value

    def shift_positions(self, start_idx, v_shift, h_shift):
        for obj in self.json_dict_flat.values():
            for label in obj.values():
                start_cds = label['coords'][0]
                end_cds = label['coords'][1]
                if end_cds == start_idx:
                    label['coords'][1] = self.vh_update(end_cds, v_shift, h_shift)
                elif start_cds > start_idx:
                    label['coords'][0] = self.vh_update(start_cds, v_shift)
                    label['coords'][1] = self.vh_update(end_cds, v_shift)

    def update_tags(self, value, flat_keys):
        line_diff = self.curr_tf_length - self.prev_tf_length
        column_diff = len(str(value)) - len(str(self.previous_value))
        end = self.get_coords(flat_keys, 1)

        self.shift_positions(end, line_diff, column_diff)
        self.dirty_tags.discard(flat_keys)

        if self.is_field_dirty(flat_keys, value):
            self.dirty_tags.add(flat_keys)


class MenuBar(ttk.Frame):

    """
    Define namespace, styling and method calls of the menubar.

    The menubar hosts the usual file, edit, about, and other menus with their
    corresponding sub-menus. All sub-menu entries trigger callbacks which can bundle
    information and call a method of the main applications (if necessary).
    Methods inside the menubar are not designed to execute much of the application
    logic, but rather passing events and received user interaction down to the main
    application. The main application takes care of recollecting information from
    other GUI elements and/or the data object.

    """

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create menu bar
        self.menubar = tk.Menu(self)
        self.parent.parent.config(menu=self.menubar)

        # Create file menu
        self.file_menu = tk.Menu(self.menubar, tearoff=0, postcommand=self.set_file_submenus)
        self.menubar.add_cascade(label='File', menu=self.file_menu)
        # Open
        self.file_menu.add_command(label='Open', accelerator='Ctrl + O',
                compound=tk.LEFT, command=self.open)
        # Save
        self.file_menu.add_command(label='Save', accelerator='Ctrl + S',
                compound=tk.LEFT, state=tk.DISABLED, command=self.save)
        # Save as
        self.file_menu.add_command(label='Save as..', accelerator='Shift + Ctrl + S',
                compound=tk.LEFT, state=tk.DISABLED, command=self.save_as)
        # Quit
        self.file_menu.add_command(label='Quit', accelerator='Ctrl + Q',
                compound=tk.LEFT, command=self.parent.quit)

        # Create edit menu
        self.edit_menu = tk.Menu(self.menubar, tearoff=0, postcommand=self.set_edit_submenus)
        self.menubar.add_cascade(label='Edit', menu=self.edit_menu)
        # Add object
        self.edit_menu.add_command(label='Add Object', accelerator='Shift + Ctrl + O',
                compound=tk.LEFT, command=self.add_object)

        # Delete object
        self.edit_menu.add_command(label='Delete Object', accelerator='Shift + Ctrl + D',
                compound=tk.LEFT, state=tk.DISABLED, command=self.delete_object)

        # Create about menu
        self.about_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='About', menu=self.about_menu)

    def set_file_submenus(self):
        """Enable/disable file menu entries depending on data object state."""
        if self.parent.data_object.is_live() and not self.parent.data_object.is_empty():
            self.file_menu.entryconfig('Save', state=tk.NORMAL)
            self.file_menu.entryconfig('Save as..', state=tk.NORMAL)
        elif not self.parent.data_object.is_empty():
            self.file_menu.entryconfig('Save', state=tk.DISABLED)
            self.file_menu.entryconfig('Save as..', state=tk.NORMAL)
        else:
            self.file_menu.entryconfig('Save', state=tk.DISABLED)
            self.file_menu.entryconfig('Save as..', state=tk.DISABLED)

    def set_edit_submenus(self, event=None):
        """Enable/disable edit menu entries depending on data object state."""
        if not self.parent.data_object.is_empty():
            self.edit_menu.entryconfig('Delete Object', state=tk.NORMAL)
        else:
            self.edit_menu.entryconfig('Delete Object', state=tk.DISABLED)

    def open(self, event=None):
        """Open callback in menubar

        :event:   Callback event
        :returns: None
        """
        file_name = filedialog.askopenfilename(defaultextension=".json",
        filetypes=[("Configuration files", "*.json")])
        if file_name:
            self.parent.init_data_object(file_name)

    def save(self, event=None):
        """Save callback in menubar

        :event:   Callback event
        :returns: None
        """
        if self.parent.data_object.is_empty():
            # This will appear inside the status bar later
            print("Nothing to save")
            return

        if not self.parent.data_object.is_live():
            self.save_as()
        else:
            self.parent.write_to_file()
            self.parent.clear_do_tags()
            self.parent.refresh_monitor()
        return "break"

    def save_as(self, event=None):
        """Save as callback in menubar

        :event:    Callback event
        :returns: None
        """
        if self.parent.data_object.is_empty():
            # This will appear inside the status bar later
            print("Nothing to save")
            return

        file_name = filedialog.asksaveasfilename(defaultextension=".json",
                filetypes=[("Configuration Files", "*.json")])

        if file_name:
            self.parent.set_do_name(file_name)
            self.parent.write_to_file()
            self.parent.set_title()
            self.parent.clear_do_tags()
            self.parent.refresh_monitor()
            return "break"

    def add_object(self, event=None):
        """Trigger action in MainApplication on selection "add object."""
        self.parent.create_dialog()

    def delete_object(self, event=None):
        """Trigger action in MainApplication on selection "delete object."""
        self.parent.delete_dialog()


class Editor(ttk.Frame):
    """ Section where configurations can be edited."""

    def __init__(self, parent, *args, **kwargs):
        """TODO: to be defined1. """
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.frame = VerticalScrollFrame(self, (screen_height - (screen_height * 0.3)))
        self.parent = parent
        #  self.entry_list = []

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

    def create_entry_widgets(self, jdf_nodes):
        """Update the key-value section with entry fields."""

        self.label_style = ttk.Style()
        self.label_style.configure("label_style.TLabel",
                          justify=tk.LEFT,
                          padding=[0, 10, 0, 5],
                          font=('Arial', 10, 'bold')
                          )

        self.parent.destroy_splash()

        self.frame.destroy()
        self.frame = VerticalScrollFrame(self, (screen_height - (screen_height * 0.3)))
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        for i, (path, label) in enumerate(jdf_nodes, 1):
            frame = ttk.Frame(self.frame.interior)
            frame.grid(row=i, column=0, padx='20', sticky=tk.NSEW)
            ttk.Label(frame, style="label_style.TLabel",
                      text=('\n' + ARROW_SYM + ' ').join(path)
                  ).grid(row=0, column=0, columnspan=2, sticky=tk.NW)

            j = 0
            k = i

            for key, val in label.items():
                ttk.Label(frame, text=key, justify=tk.LEFT).grid(row=k,
                        column=j, sticky=tk.NW)

                v  = val['buffered_value']

                if isinstance(v, int):
                    entry = IntegerEntry(frame, value=v)
                elif isinstance(v, float):
                    entry = FloatEntry(frame, value=v)
                elif isinstance(v, list):
                    val = str(v).strip('[]').replace(',', '')
                    entry = ArrayEntry(frame, val)
                else:
                    entry = StringEntry(frame, value=v)

                entry.config(justify=tk.LEFT)

                entry.grid(row=k+1, column=j, sticky=tk.NW)
                entry.bind("<FocusOut>", lambda event, flat_keys=(path + (key,)):
                    self.save_entry_value(event, flat_keys))

                j, k = self._accomodate_rows(j, k)

    def save_entry_value(self, event, flat_keys):
        value = event.widget.get()
        self.parent.update_json_dict(value, flat_keys)
        self.parent.refresh_monitor(flat_keys)


class Monitor(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

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
        self.create_splash()
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

    def create_splash(self):
        self.splash_style = ttk.Style()
        self.splash = ttk.Label(self.textfield, textvariable=self.startup_screen,
                style="SPLASH.TLabel")
        self.splash_style.configure("SPLASH.TLabel", font=('Courier', 8, 'bold'),
                background="white", anchor=tk.CENTER, padding=50)
        self.splash.pack()

    def destroy_splash(self):
        self.splash.destroy()

    def insert(self, string):
        self.textfield.configure(state=tk.NORMAL)
        self.textfield.delete(1.0, tk.END)
        self.textfield.insert(1.0, string)
        self.textfield.configure(state=tk.DISABLED)

    def refresh(self, string, dtags, end=None):
        self.textfield.configure(state=tk.NORMAL)
        self.textfield.delete(1.0, tk.END)
        self.textfield.insert(1.0, string)

        for coords in dtags:
            self.textfield.tag_add('match', coords[0], coords[1])

        self.textfield.configure(state=tk.DISABLED)

        if end:
            self.parent.monitor.textfield.see(end)

    def adjust_textfield(self):
        self.textfield.configure(width=self.textfield_width)


class CreateDialog(dialog_window.Dialog):
    def __init__(self, parent, title):
        self.parent = parent
        self.tab_widgets = []
        self.tab_ids = ["Array", "Float", "Integer", "String"]
        self.checked = tk.IntVar()
        self.node_list, self.node_labels = self.parent.data_object.node_list()
        dialog_window.Dialog.__init__(self, parent, title)

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
        nodes = ttk.Combobox(tab)
        nodes.config(width=self._calc_cb_length())
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

        # Node label
        ttk.Label(tab, style="id_label_style.TLabel", text="Node"
                 ).grid(row=0, column=0, sticky=tk.NW)

        # key list config and placement
        list_items = [ ARROW_SYM.join(i) for i in self.node_list ]
        nodes['values'] = list_items
        try:
            nodes.current(0)
        except tk.TclError as e:
            pass

        nodes.grid(row=1, column=0, sticky=tk.NW)

        # Object key label
        ttk.Label(tab, style="id_label_style.TLabel", text="Object Key"
                 ).grid(row=2, column=0, sticky=tk.NW)

        # Object key entry
        obj_key_entry.grid(row=3, column=0, sticky=tk.NW)

        # Key label
        key_label = ttk.Label(tab, style="id_label_style.TLabel", text="Key"
                 ).grid(row=4, column=0, sticky=tk.NW)

        # Key entry
        key_entry.grid(row=5, column=0, sticky=tk.NW)

        # Value label
        ttk.Label(tab, style="id_label_style.TLabel", text="Value"
                 ).grid(row=6, column=0, sticky=tk.NW)

        # Value entry
        value_entry.grid(row=7, column=0, sticky=tk.NW)

        return [nodes, obj_key_entry, key_entry, value_entry]

    def validate(self):
        active_tab = self.n.index(self.n.select())
        node =  self.tab_widgets[active_tab][0].get()
        key =   self.tab_widgets[active_tab][2].get()
        value = self.tab_widgets[active_tab][3].get()

        if self.checked.get() == 1:
            object_key = self.tab_widgets[active_tab][1].get()
            if node == '' or object_key == '' or key == '' or value == '':
                return 0
        else:
            if node == '' or key == '' or value == '':
                return 0
        return 1

    def apply(self):
        active_tab = self.n.index(self.n.select())

        node = tuple(self.tab_widgets[active_tab][0].get().strip().split(ARROW_SYM))

        key = self.tab_widgets[active_tab][2].get().strip()
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
            value = value.strip()

        if self.checked.get() == 1:
            object_key = self.tab_widgets[active_tab][1].get().strip()
            node = node + (object_key,)

        flat_keys =  (node + (key,))

        self.parent.data_object.dyn_dict_set(value, flat_keys)

        self.parent.data_object.gen_flat_key_dict()

        self.parent.create_entry_widgets()

        self.parent.data_object.set_prev_tf_length()
        self.parent.data_object.update_tags(value, flat_keys)
        self.parent.refresh_monitor(flat_keys)

    def toggle_objectname_field(self, entry_widgets, checkbox):
        for ew in entry_widgets:
            if checkbox.get() == 0:
                ew.configure(state=tk.DISABLED)
            else:
                ew.configure(state=tk.NORMAL)


class DeleteDialog(dialog_window.Dialog):
    def __init__(self, parent, title):
        self.parent = parent
        self.node_list, self.node_labels = self.parent.data_object.node_list()
        dialog_window.Dialog.__init__(self, parent, title)

    def body(self, root):
        self.frame = ttk.Frame(root)
        self.frame.pack()
        self.nodes = ttk.Combobox(self.frame, state='readonly')
        self.nodes.config(width=self._calc_cb_length())
        self.key = ttk.Combobox(self.frame, state='readonly')

        # Nodes label
        ttk.Label(self.frame, style="id_label_style.TLabel", text="Node"
                 ).grid(row=0, column=0, sticky=tk.NW)

        list_items = [ ARROW_SYM.join(i) for i in self.node_list ]
        print(list_items)
        self.nodes['values'] = list_items
        self.nodes.bind("<<ComboboxSelected>>", self._update_label_cb)
        self.nodes.bind("<FocusIn>", self._update_label_cb)
        self.nodes.focus_set()
        self.nodes.current(0)
        self.nodes.grid(row=1, column=0, sticky=tk.NW)

        # Labels label
        ttk.Label(self.frame, style="id_label_style.TLabel", text="Key"
                 ).grid(row=2, column=0, sticky=tk.NW)
        self.key.grid(row=3, column=0, sticky=tk.NW)

    def apply(self):
        node = tuple(self.nodes.get().strip().split(ARROW_SYM))
        key = self.key.get().strip()

        if key:
            node = node + (key,)

        flat_keys =  node
        self.parent.data_object.set_prev_tf_length()
        self.parent.data_object.dyn_dict_delete(node)
        self.parent.data_object.gen_flat_key_dict()
        self.parent.create_entry_widgets()
        self.parent.data_object.clean_dirty_tags(flat_keys)
        self.parent.refresh_monitor()

    def _update_label_cb(self, event=None):
        try:
            self.key.config(values=self.node_labels[tuple(event.widget.get().split(ARROW_SYM))], state=tk.NORMAL)
            self.key.current(0)
            self.key.config(state="readonly")
        except KeyError:
            self.key.set('')
            self.key.config(state=tk.DISABLED)


class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.init_data_object()

        # Create GUI elements
        self.monitor = Monitor(self)
        self.editor = Editor(self)

        # Place GUI elements
        self.editor.grid(row = 0, column = 1)
        self.monitor.grid(row=0, column=0, sticky=tk.NS)

        # Add menu bar
        self.menubar = MenuBar(self)

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
        self.parent.bind('<Control-Q>', self.quit_monitor)
        self.parent.bind('<Control-q>', self.quit_monitor)
        # bind add object
        self.parent.bind('<Control-Shift-O>', self.menubar.add_object)
        self.parent.bind('<Control-Shift-o>', self.menubar.add_object)
        # bind delete object
        self.parent.bind('<Control-Shift-D>', self.menubar.delete_object)
        self.parent.bind('<Control-Shift-d>', self.menubar.delete_object)

    def init_data_object(self, file_name=None):
        self.data_object = DataObject()

        if file_name:
            self.data_object.name = file_name
            self.set_title()
            self.data_object.import_file(file_name)
            self.monitor.insert(self.data_object.json_str)
            self.create_entry_widgets()

    def set_title(self):
        self.parent.title('{} - {}'.format(os.path.basename(
                self.data_object.name), PROGRAM_NAME))

    def set_do_name(self, file_name):
        self.data_object.name = file_name

    def update_json_dict(self, value, flat_keys):
        self.data_object.update_json_dict(value, flat_keys)

    def clear_do_tags(self):
        self.data_object.dirty_tags.clear()

    def refresh_monitor(self, flat_keys=None):
        dtags = []

        for fkey in self.data_object.dirty_tags:
            dtags.append([self.data_object.get_coords(fkey, 0),
                          self.data_object.get_coords(fkey, 1)])

        try:
            end = self.data_object.get_coords(flat_keys, 1)
            self.monitor.refresh(self.data_object.json_str, dtags, end)
        except TypeError:
            self.monitor.refresh(self.data_object.json_str, dtags)

    def quit_monitor(self, event=None):
        self.parent.destroy()

    def create_dialog(self):
        self.create_dlg = CreateDialog(self, "Create Object")
        self.parent.wait_window(self.create_dlg.parent.parent)

    def delete_dialog(self):
        self.delete_dlg = DeleteDialog(self, "Delete Object")
        self.parent.wait_window(self.delete_dlg.parent.parent)

    def write_to_file(self):
        """Write current json_dict to file

        :returns: None
        """
        try:
            content = self.data_object.json_dict
            file_name = self.data_object.name

            with open(file_name, 'w') as outfile:
                json.dump(content, outfile)
        except IOError:
            pass

    def create_entry_widgets(self):
        jdf_nodes = self.data_object.json_dict_flat.items()
        self.editor.create_entry_widgets(jdf_nodes)

    def destroy_splash(self):
        self.monitor.destroy_splash()
        self.monitor.adjust_textfield()


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
