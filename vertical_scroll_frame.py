#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from functools import partial as fp

class VerticalScrollFrame(ttk.Frame):
    """ 
    A ttk frame allowing vertical scrolling.

    Use the '.interior' attribute to place widgets inside the scrollable frame.
    """
    def __init__(self, parent, height, *args, **options):
        # style variables
        self.canvas_bg = "white" 
        self.canvas_height = height

        ttk.Frame.__init__(self, parent)
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
        self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.vscrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=tk.FALSE)
        self.canvas = tk.Canvas(self,
                                yscrollcommand=self.vscrollbar.set,
                                background=self.canvas_bg)

        #  self.canvas.configure(height=screen_height - (screen_height * 0.3))
        self.canvas.configure(height=self.canvas_height)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        self.vscrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Enter>', self._bind_to_mousewheel)
        self.canvas.bind('<Leave>', self._unbind_from_mousewheel)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = ttk.Frame(self.canvas)
                                  
        self.interior_id = self.canvas.create_window(0, 0,
                                                     window=self.interior,
                                                     anchor=tk.NW,
                                                     tags="self.interior")

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

    def move_to_focus(line_number):
        self.canvas.xview_moveto(line_number)
        self.canvas.yview_moveto(line_number)

