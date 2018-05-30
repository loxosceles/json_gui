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
REGEX_NL = re.compile('\n')
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
    def previous_textfield_length(self):
        return self._textfield_length

    @property
    def current_textfield_length(self):
        return len(REGEX_NL.findall(self.json_str, re.DOTALL)) + 2

    @name.setter
    def name(self, name):
        self._name = name

    def import_file(self, json_file):
        """Import configurations from tf_conf.json.

        :arg1: TODO
        :returns: TODO

        """
        try:
            with open(json_file, 'r') as infile:
                self.json_dict = json.load(infile)

                self.gen_file_dict()

                self.gen_flat_key_dict()
        except ValueError as e:
            print("Decoding the JSON config file has failed. Please make sure the\
                    format is correct.")

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

        :arg1: TODO
        :returns: TODO

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
                if el.endswith('],'):
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
            #end_col = l[end_row - 1].find('],') + 2
            end_col = start_col
        else:# l[idx].endswith('"'):
            end_row = start_row
            end_col = len(l[idx]) - 1
        #  else:
        #      print("Something bad happend")

        start = Decimal(start_row) + Decimal('0.' + str(start_col))
        end  = Decimal(end_row) + Decimal('0.' + str(end_col))
        #pu.db

        return start, end

    #  def gen_value_coords(self, path):
    #      """TODO: Docstring for function.
    #
    #      :arg1: TODO
    #      :returns: TODO
    #
    #      """
    #      match_all = '([^}]|[^}]{[^}]*})*[^{]*'
    #      se = ''
    #      for i in range(len(path) - 1):
    #          se += '"' + path[i] + '"' + match_all
    #
    #      se += '"' + path[-1] + '"' + ':\s*(\[[^}]*?\]|".*?"|\d+\.*\d*)'
    #      print(se)
    #      print(self.json_str)
    #
    #      s = re.compile(se, re.DOTALL)
    #      match = s.search(self.json_str)
    #
    #      start = self.calc_match_position(self.json_str, match.start(len(path)))
    #      end = self.calc_match_position(self.json_str, match.end(len(path)))
    #      return start, end
    #
    #  def calc_match_position(self, match_index):
    #      """
    #      Calculates the positions of the matched value in the editor window.
    #
    #      :match:   matched string
    #      :returns: position in the form of line.column
    #      """
    #      #  line = 1
    #      #  for ln in REGEX_NL.finditer(string, 0, match_index):
    #      #      line += 1
    #
    #      s = re.compile(t[-1] + ': (\s*(\[[^}]*?\]|".*?"|\d+\.*\d*))', re.DOTALL)
    #      match = s.search(l[line - 1])
    #
    #      column = match_index - ln.start() - 1
    #
    #      return Decimal(line) + Decimal('0.' + str(column))

    def dyn_dict_get(self, flat_keys):
        try:
            return reduce(operator.getitem, flat_keys, self.json_dict)
        except KeyError:
            pass

    def dyn_dict_set(self, flat_keys, value):
        dic = self.json_dict

        for key in flat_keys[:-1]:
            dic = dic.setdefault(key, {})
        dic[flat_keys[-1]] = value
        #  try:
        #      self.dyn_dict_get(flat_keys[:-1])[flat_keys[-1]] = value
        #  except TypeError as e:
        #      print(e)
        #      reduce(operator.getitem, flat_keys[:-1], self.json_dict)
        #  except KeyError:
        #      print("Error")
        #      self.dyn_dict_get(flat_keys[:-2])[flat_keys[-2]] = {}
        #      self.dyn_dict_get(flat_keys[:-1])[flat_keys[-1]] = value
        #  print(self.json_dict)

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

    def get_value_dict_flat(self, flat_keys):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        path = flat_keys[:-1]
        label = flat_keys[-1]
        return self.json_dict_flat[path][label]['buffered_value']

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

    def set_previous_textfield_length(self):
        self._textfield_length = len(REGEX_NL.findall(self.json_str, re.DOTALL)) + 2

    def clean_dirty_tags(self, flat_keys):
        for el in deepcopy(self.dirty_tags):
            if flat_keys == el[:len(flat_keys)]:
                self.dirty_tags.discard(el)


class MenuBar(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

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
                compound=tk.LEFT, state=tk.DISABLED, command=self.save)
        # Save as
        self.file_menu.add_command(label='Save as..', accelerator='Shift + Ctrl + S',
                compound=tk.LEFT, state=tk.DISABLED, command=self.save_as)
        # Quit
        self.file_menu.add_command(label='Quit', accelerator='Ctrl + Q',
                compound=tk.LEFT, command=self.parent.quit)

        # Create edit menu
        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
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

    def open(self, event=None):
        input_file_name = filedialog.askopenfilename(defaultextension=".json",
        filetypes=[("Configuration files", "*.json")])
        if input_file_name:
            self.parent.init_data_object()
            self.parent.data_object.name = input_file_name
            self.parent.set_title()
            self.parent.editor.textfield.configure(state=tk.NORMAL)
            self.parent.editor.textfield.delete(1.0, tk.END)
            self.parent.data_object.import_file(input_file_name)
            self.parent.editor.textfield.insert(1.0, self.parent.data_object.json_str)
            self.parent.editor.textfield.configure(state=tk.DISABLED)
            self.parent.key_value_section.create_entry_widgets()
            self.enable_menu_entries()

    def enable_menu_entries(self):
            self.edit_menu.entryconfig('Delete Object', state=tk.NORMAL)
            self.file_menu.entryconfig('Save', state=tk.NORMAL)
            self.file_menu.entryconfig('Save as..', state=tk.NORMAL)

    def save(self, event=None):
        """TODO: Docstring for .

        :arg1: TODO
        :returns: TODO

        """
        if len(self.parent.data_object.json_dict) == 0:
            return

        if not self.parent.data_object.name:
            self.save_as()
        else:
            self.write_to_file(self.parent.data_object.name)
            self.parent.data_object.dirty_tags.clear()
            self.parent.editor.refresh()
        return "break"

    def save_as(self, event=None):
        """TODO: Docstring for .

        :arg1: TODO
        :returns: TODO

        """
        if len(self.parent.data_object.json_dict) == 0:
            return

        input_file_name = filedialog.asksaveasfilename(defaultextension=".json",
                filetypes=[("Configuration Files", "*.json")])
        if input_file_name:
            self.parent.data_object.name = input_file_name
            self.write_to_file(self.parent.data_object.name)
            self.parent.parent.title('{} - {}'
                    .format(os.path.basename(self.parent.data_object.name), PROGRAM_NAME))
            return "break"

    def write_to_file(self, file_name):
        """TODO: Docstring for .

        :arg1: TODO
        :returns: TODO

        """

        try:
            content = self.parent.data_object.json_dict
            with open(file_name, 'w') as outfile:
                json.dump(content, outfile)
        except IOError:
            pass

    def add_object(self, event=None):
        """TODO: Docstring for .

        :arg1: TODO
        :returns: TODO

        """
        self.parent.create_dialog()

    def delete_object(self, event=None):
        """TODO: Docstring for delete_object

        :arg1: TODO
        :returns: TODO

        """
        self.parent.delete_dialog()


class KeyValueSection(ttk.Frame):
    """ Section where configurations can be edited."""

    def __init__(self, parent, *args, **kwargs):
        """TODO: to be defined1. """
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        #self.frame = VerticalScrollFrame(self, (screen_height - (screen_height * 0.3)))
        self.frame = VerticalScrollFrame(self, 630)
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

    def create_entry_widgets(self):
        """Update the key-value section with entry fields."""

        self.label_style = ttk.Style()
        self.label_style.configure("label_style.TLabel",
                          justify=tk.LEFT,
                          padding=[0, 10, 0, 5],
                          font=('Arial', 10, 'bold')
                          )

        self.parent.editor.splash.destroy()
        self.parent.editor.textfield.configure(width=self.parent.editor.textfield_width)

        self.frame.destroy()
        self.frame = VerticalScrollFrame(self, (screen_height - (screen_height * 0.3)))
        self.frame.grid(row=0, column=0, sticky=tk.NSEW)

        for i, (path, label) in enumerate(self.parent.data_object.json_dict_flat.items(), 1):
            frame = ttk.Frame(self.frame.interior)
            frame.grid(row=i, column=0, padx='20', sticky=tk.NSEW)
            ttk.Label(frame, style="label_style.TLabel",
                      text=(' ' + ARROW_SYM + ' ').join(path)
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
                    self.buffer_entry_value(event, flat_keys))

                j, k = self._accomodate_rows(j, k)

    def buffer_entry_value(self, event, flat_keys):
        # FIXME: get position of event inside canvas

        value = event.widget.get()

        fd_value = self.parent.data_object.get_value_dict_flat(flat_keys)

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
        self.parent.data_object.set_previous_textfield_length()

        # save previous value for column comparison
        # FIXME: Move this to data object
        self.parent.data_object.previous_value = self.parent.data_object.dyn_dict_get(flat_keys)

        # save value to master dict
        self.parent.data_object.dyn_dict_set(flat_keys, value)

        # call the update method of the editor
        self.parent.editor.update_tags(value, flat_keys)


class Editor(ttk.Frame):
    def __init__(self, parent, data_object=None, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.data_object = parent.data_object

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

    def update_tags(self, value, flat_keys=None):
        prev_tf_length = self.parent.data_object.previous_textfield_length
        curr_tf_length = self.parent.data_object.current_textfield_length
        line_diff = curr_tf_length - prev_tf_length
        #FIXME: + 10 should not be necessary (but without it some brackets aren't marked consistently in red)
        column_diff = len(str(value)) - len(str(self.parent.data_object.previous_value)) + 10


        start = self.parent.data_object.get_coords(flat_keys, 0)
        end = self.parent.data_object.get_coords(flat_keys, 1)

        self.shift_positions(self.parent.data_object.json_dict_flat, end, line_diff, column_diff )
        self.parent.data_object.dirty_tags.discard(flat_keys)

        if self.parent.data_object.is_field_dirty(flat_keys, value):
            self.parent.data_object.dirty_tags.add(flat_keys)

        self.refresh()
        self.textfield.see(end)

    def refresh(self):
        self.textfield.configure(state=tk.NORMAL)
        self.textfield.delete(1.0, tk.END)
        self.textfield.insert(1.0, self.parent.data_object.json_str)
        for el in self.parent.data_object.dirty_tags:
            self.textfield.tag_add('match', self.parent.data_object.get_coords(el, 0),
                                            self.parent.data_object.get_coords(el, 1))
        self.textfield.configure(state=tk.DISABLED)


class CreateDialog(dialog_window.Dialog):
    def __init__(self, parent, title):
        self.parent = parent
        self.tab_widgets = []
        self.tab_ids = ["Array", "Float", "Integer", "String"]
        self.checked = tk.IntVar()
        self.node_list, self.node_labels = self.parent.data_object.node_list()
        if not self.parent.data_object.name:
            self.parent.menubar.enable_menu_entries()

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
        nodes['values'] = (self.node_list)
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

        node = tuple(self.tab_widgets[active_tab][0].get().strip().split(' '))

        if not self.parent.data_object.dyn_dict_get(node):
            node = self.tab_widgets[active_tab][0].get().strip(),

        key = self.tab_widgets[active_tab][2].get().strip()#.replace(' ', '_').lower()
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
            object_key = self.tab_widgets[active_tab][1].get().strip()#.replace(' ', '_').lower()
            node = node + (object_key,)

        flat_keys =  (node + (key,))

        self.parent.data_object.dyn_dict_set(flat_keys, value)

        self.parent.data_object.gen_flat_key_dict()

        self.parent.key_value_section.create_entry_widgets()

        self.parent.data_object.set_previous_textfield_length()
        self.parent.editor.update_tags(value, flat_keys)

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

        self.nodes['values'] = (self.node_list)
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
        node = tuple(self.nodes.get().strip().split(' '))
        key = self.key.get().strip()

        if key:
            node = node + (key,)

        flat_keys =  node
        value = self.parent.data_object.dyn_dict_get(flat_keys)

        self.parent.data_object.set_previous_textfield_length()

        self.parent.data_object.dyn_dict_delete(node)

        self.parent.data_object.gen_flat_key_dict()

        self.parent.key_value_section.create_entry_widgets()
        print("Dirty tags before discard: \n", self.parent.data_object.dirty_tags)
        #  self.parent.data_object.dirty_tags.discard(flat_keys)
        self.parent.data_object.clean_dirty_tags(flat_keys)
        print("Flat keys: \n", flat_keys)
        #  print("Value: ", value)
        print("Dirty tags: \n", self.parent.data_object.dirty_tags)
        self.parent.editor.refresh()

    def _update_label_cb(self, event=None):
        try:
            self.key.config(values=self.node_labels[tuple(event.widget.get().split(' '))], state=tk.NORMAL)
            self.key.current(0)
        except KeyError:
            self.key.set('')
            self.key.config(state=tk.DISABLED)


class MainApplication(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.init_data_object()

        # Create GUI elements
        self.editor = Editor(self)
        self.key_value_section = KeyValueSection(self)

        # Place GUI elements
        self.key_value_section.grid(row = 0, column = 1)
        self.editor.grid(row=0, column=0, sticky=tk.NS)

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
        self.parent.bind('<Control-Q>', self.quit_editor)
        self.parent.bind('<Control-q>', self.quit_editor)
        # bind add object
        self.parent.bind('<Control-Shift-O>', self.menubar.add_object)
        self.parent.bind('<Control-Shift-o>', self.menubar.add_object)
        # bind delete object
        self.parent.bind('<Control-Shift-D>', self.menubar.delete_object)
        self.parent.bind('<Control-Shift-d>', self.menubar.delete_object)

    def init_data_object(self):
        self.data_object = DataObject()

    def set_title(self):
        self.parent.title('{} - {}'.format(os.path.basename(
                self.data_object.name), PROGRAM_NAME))

    def quit_editor(self, event=None):
        self.parent.destroy()

    def create_dialog(self):
        self.create_dlg = CreateDialog(self, "Create Object")
        self.parent.wait_window(self.create_dlg.parent.parent)

    def delete_dialog(self):
        self.delete_dlg = DeleteDialog(self, "Delete Object")
        self.parent.wait_window(self.delete_dlg.parent.parent)


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
