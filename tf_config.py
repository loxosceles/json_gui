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
        return json.dumps(self.json_tree_dict, indent=4)

class VerticalScrollFrame(ttk.Frame):
    """A ttk frame allowing vertical scrolling only.
    Use the '.interior' attribute to place widgets inside the scrollable frame.
    Adapted from https://gist.github.com/EugeneBakin/76c8f9bcec5b390e45df.
    Amendments:
    1. Original logic for configuring the interior frame and canvas
       scrollregion left canvas regions exposed (not suppose to) and allowed
       vertical scrolling even when canvas height is greater than the canvas
       required height, respectively. I have provided a new logic to
       resolve these issues.
    2. Provided options to configure the styles of the ttk widgets.
    3. Tested in Python 3.5.2 (default, Nov 23 2017, 16:37:01),
                 Python 2.7.12 (default, Dec  4 2017, 14:50:18) and
                 [GCC 5.4.0 20160609] on linux.
    Author: Sunbear
    Website: https://github.com/sunbearc22
    Created on: 2018-02-26
    Amended on: 2018-03-01 - corrected __configure_canvas_interiorframe() logic.  
    """

    
    def __init__(self, parent, *args, **options):
        """
        WIDGET-SPECIFIC OPTIONS:
           style, pri_background, sec_background, arrowcolor,
           mainborderwidth, interiorborderwidth, mainrelief, interiorrelief 
        """
        # Extract key and value from **options using Python3 "pop" function:
        #   pop(key[, default])
        style          = options.pop('style',ttk.Style())
        pri_background = options.pop('pri_background','light grey')
        sec_background = options.pop('sec_background','grey70')
        arrowcolor     = options.pop('arrowcolor','black')
        mainborderwidth     = options.pop('mainborderwidth', 0)
        interiorborderwidth = options.pop('interiorborderwidth', 0)
        mainrelief          = options.pop('mainrelief', 'flat')
        interiorrelief      = options.pop('interiorrelief', 'flat')

        ttk.Frame.__init__(self, parent, style='main.TFrame',
                           borderwidth=mainborderwidth, relief=mainrelief)

        self.__setStyle(style, pri_background, sec_background, arrowcolor)

        self.__createWidgets(mainborderwidth, interiorborderwidth,
                             mainrelief, interiorrelief,
                             pri_background)
        self.__setBindings()


    def __setStyle(self, style, pri_background, sec_background, arrowcolor):
        '''Setup stylenames of outer frame, interior frame and verticle
           scrollbar'''        
        style.configure('main.TFrame', background=pri_background)
        style.configure('interior.TFrame', background=pri_background)
        style.configure('canvas.Vertical.TScrollbar', background=pri_background,
                        troughcolor=sec_background, arrowcolor=arrowcolor)

        style.map('canvas.Vertical.TScrollbar',
            background=[('active',pri_background),('!active',pri_background)],
            arrowcolor=[('active',arrowcolor),('!active',arrowcolor)])


    def __createWidgets(self, mainborderwidth, interiorborderwidth,
                        mainrelief, interiorrelief, pri_background):
        '''Create widgets of the scroll frame.'''
        self.vscrollbar = ttk.Scrollbar(self, orient='vertical',
                                        style='canvas.Vertical.TScrollbar')
        self.vscrollbar.pack(side='right', fill='y', expand='false')
        self.canvas = tk.Canvas(self,
                                bd=0, #no border
                                highlightthickness=0, #no focus highlight
                                yscrollcommand=self.vscrollbar.set,#use self.vscrollbar
                                background=pri_background #improves resizing appearance
                                )
        self.canvas.pack(side='left', fill='both', expand='true')
        self.vscrollbar.config(command=self.canvas.yview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = ttk.Frame(self.canvas,
                                  style='interior.TFrame',
                                  borderwidth=interiorborderwidth,
                                  relief=interiorrelief)
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
            #print('canvasHeight > interiorReqHeight')
            self.canvas.itemconfigure(self.interior_id,  height=canvasHeight)
            self.canvas.config(scrollregion="0 0 {0} {1}".
                               format(canvasWidth, canvasHeight))
        else:
            #print('canvasHeight <= interiorReqHeight')
            self.canvas.itemconfigure(self.interior_id, height=interiorReqHeight)
            self.canvas.config(scrollregion="0 0 {0} {1}".
                               format(canvasWidth, interiorReqHeight))


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
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        #  self.frame = VerticalScrollFrame(self)
        #  self.frame.grid()
        BG0 = '#aabfe0' #Blue scheme
        BG1 = '#4e88e5' #Blue scheme
        self.scroll_frame = VerticalScrollFrame(self,
                #  pri_background=BG1,
                #  sec_background=BG0,
                #  arrowcolor='white',
                #  mainborderwidth=10,
                interiorborderwidth=2,
                #  mainrelief='raised',
                #  interiorrelief='sunken'
            )
        self.scroll_frame.grid(row=0, column=0, sticky='nsew')

        
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
                value = [ int(x) for x in ' '.join(value.split()).split(' ') ]
                

            self.fobj.json_tree_dict[keys[0]][keys[1]] = value
        except TypeError as e:
            self.fobj.json_tree_dict[keys[0]] = value
#print(self.fobj.json_tree_dict)
        self.parent.editor.update()


    def createWidgets(self, BG0, BG1):
        self.frame = VerticalScrollFrame(self,
                                        #  pri_background=BG1,
                                        #  sec_background=BG0,
                                        #  arrowcolor='white',
                                        #  mainborderwidth=10,
                                        interiorborderwidth=2,
                                        #  mainrelief='raised',
                                        #  interiorrelief='sunken'
                                        )
        self.frame.grid(row=0, column=0, sticky='nsew')

        #  text="Shrink the window to activate the scrollbar."
        #  self.label = tk.Label(background='white', text=text)
        #  self.label.grid(row=1, column=0, sticky='nsew')

        #  buttons = []
        #  for i in range(100):
        #      buttons.append(ttk.Button(self.frame.interior,
        #                                text="Button " + str(i)))
        #      buttons[-1].grid(row=i, column=0, sticky='nsew')
        #
        def accomodate_rows(j, k):
            if j < 1:
                j += 1
                return j, k
            else:
                #  j = 0
                k +=2
                return 0, k
        i = 0
        for key, obj in self.fobj.json_tree_dict.items():
            i += 1
            frame = tk.Frame(self.frame.interior)
            #frame = tk.Frame(self)
            frame.grid(row=i, column=0, padx='20', sticky=tk.NSEW)

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

                    if isinstance(val, list):
                        val = str(val).strip('[]').replace(',', '')

                    value_field = tk.StringVar(frame, value=val)

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

        def accomodate_rows(j, k):
            if j < 2:
                j += 1
                return j, k
            else:
                #  j = 0
                k +=2
                return 0, k


    def update(self):
        BG0 = '#aabfe0' #Blue scheme
        BG1 = '#4e88e5' #Blue scheme
        self.createWidgets(BG0, BG1)

        #  i = 0
        #  for key, obj in self.fobj.json_tree_dict.items():
        #      i += 1
        #      frame = tk.Frame(self.scroll_frame.interior)
        #      #frame = tk.Frame(self)
        #      frame.grid(row=i, column=0, padx='20', sticky=tk.NSEW)
        #
        #      ttk.Label(frame,
        #                text=string.capwords(key.replace('_', ' ')),
        #                justify=tk.LEFT,
        #                padding=[0, 10, 0, 5],
        #                font=('Arial', 10, 'bold')
        #            ).grid(row=0, column=0, sticky='NW')
        #
        #      try:
        #          j = 0
        #          k = i
        #          for kkey, val in obj.items():
        #              ttk.Label(frame, text=kkey, justify=tk.LEFT).grid(row=k, column=j, sticky='NW')
        #
        #              if isinstance(val, list):
        #                  val = str(val).strip('[]').replace(',', '')
        #
        #              value_field = tk.StringVar(frame, value=val)
        #
        #              tmp = tk.Entry(frame, textvariable=value_field, justify=tk.LEFT)
        #              tmp.grid(row=k+1, column=j, sticky='NW')
        #              tmp.bind("<FocusOut>", lambda event, keys=(key, kkey): self.save_field(event, keys))
        #
        #              j, k = accomodate_rows(j, k)
        #
        #      except AttributeError as e:
        #          value_field = tk.StringVar(frame, value=obj)
        #          tmp = tk.Entry(frame, textvariable=value_field, justify=tk.LEFT)
        #          tmp.grid(row=k+1, column=j, sticky='NW')
        #          tmp.bind("<FocusOut>", lambda event, keys=(key, None): self.save_field(event, keys))
        #          j, k = accomodate_rows(j, k)


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
        self.textfield.delete(1.0, tk.END)
        self.textfield.insert(1.0, self.fobj.json_tree())

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
    #root.geometry('{}x{}'.format(int(screen_width // 2.5), int(screen_height)))
    root.configure(padx = 10, pady = 10)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
