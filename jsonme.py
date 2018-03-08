#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :

import os
import re
from json import dumps, loads
import sys

import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox

# create a menu & define functions for each menu item
    
def open_command():
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
    if file is not None:
        contents = file.read()
        clear(text)
        text.insert('1.0',contents)
        file.close()
        clear(res)
        root.title("Editing %s" % file.name)        
        log("opened %s" % file.name)

def indent_json():
    if validate_json():
        str_json = text.get("1.0",END)
        clear(text)
        clear(res)
        text.insert('1.0', dumps(loads(str_json), indent=4))
        log("Indentation done")
    else: 
        log("please correct errors first")
        
def save_command():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file is not None:
        clear(res)
        try:
            data = text.get('1.0', END+'-1c')
            if data or tkMessageBox.askokcancel("Cancel", "Do you really want to save empty content?"):
                file.write(data)
                log("saved %s" % file.name)
                root.title("Editing %s" % file.name)        
            else:
                log("save canceled")
            file.close()
        except Exception as e:
            log(e)

    
def clear(text_stuff):
    text_stuff.delete("1.0", END)
    
def log(msg):
    res.insert("1.0", (type(msg) is str and msg or repr(msg))+ "\n")

def tab(arg):
    text.insert(INSERT, " " * 4)
    return 'break'

delim_re = re.compile(
'''
line\s(?P<line>\d+)\s
column\s(?P<col>\d+)\s
\(
    char\s(?P<before>\d+)
        (\s\-\s(?P<after>\d+))? # optionally followed by a range
\)''', re.VERBOSE) 

def validate_json():
    clear(res)
    str_json = text.get("1.0",END)
    text.tag_delete("error")

    try:
        loads(str_json)
    except ValueError as e:
        clear(res)
        log(e.message)
        mark = delim_re.search(e.message)
        if not mark:
            mark = dict(before = "0", after = "end", line = "0", col = "0")
        else:
            mark = mark.groupdict()
            mark["after"] =  "1.0 +%sc" % (mark["after"] or (int(mark["before"]) +1))
        
        before = "1.0 +%(before)sc" % mark
        has_delim = re.search("Expecting '(?P<delim>.)'", e.message)
        if has_delim:
            after = mark["after"] = "1.0 +%dc" % (int(mark["before"]) +1)
        
            text.insert(before,has_delim.groupdict()["delim"])
            #text.delete(after)
        after = "%s" % mark["after"]
        text.tag_add("error", before, after)
        text.tag_config("error", background="yellow", foreground="red")
        return False
    except Exception as e:
        log(e)
        return False
    log("JSON is valid")
    return True

            

pref = dict(padx=5, pady=5)
root = Tkinter.Tk(className=u"Minimal customized JSON editor")
upper = Frame(root, relief=GROOVE)
bottom = Frame(root, relief=GROOVE)

validate = Button(upper, text = "Validate", command=validate_json)
indent = Button(upper, text = "Indent", command=indent_json)
text= ScrolledText(upper, width=100, height=40)
text.bind("<Tab>", tab)
res= ScrolledText(bottom, width=100,height=10)
menu = Menu(root)


root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_command(label="Exit", command=root.destroy)

res.pack(side=LEFT,**pref)
upper.pack(side=TOP,**pref)
bottom.pack(side=BOTTOM, **pref)
text.pack(side=TOP,fill="y",**pref)
validate.pack(side=LEFT)
indent.pack(side=LEFT)
text.insert("1.0", """{ 
"a" : 1
    "b" ; 2
}""")
root.mainloop()
