#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk


class ValidatingEntry(ttk.Entry):

    """Entry Widget serving as base class for datatype specific Entry Widgets. """

# base class for validating entry widgets
    def __init__(self, parent, value="", **kwargs):
        ttk.Entry.__init__(self, parent, **kwargs)
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
    #  def __init__(self, parent, value="", **kwargs):
    #      super().__init__(parent, value="", **kwargs)
    #      print("ArrayEntry Value: ", value)

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
