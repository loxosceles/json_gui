#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, os, re
from sortedcontainers import SortedList
from decimal import *

class Configurations(object):                
    """Object holding configuration variables."""                                         
    config_file = 'tf_conf.json'                                 
    json_validated = bool()                  

    def __init__(self):                      
        self.regex_nl = re.compile('\n')
        self.json_dict_flat = {}
        self.json_dict = self.__import_configs(self.config_file)                            
        self.parse_json(self.json_dict, '')                                           
        #  print(self.json_dict)
        print(self.json_dict_flat)
        #  print(self.json_str)
        #self.find_linenumber(self.json_dict, self.json_str)
        
        self.test()

    def test(self):
        for section in self.json_dict_flat.values():
            for label, val in section.items():   
                print(val['value'])              
                print(val['coordinates'])        


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
            self.json_dict_flat[path][label]['coordinates'] = (start, end) 

        else:                                
            for key, value in jobj.items():  
                self.parse_json(value, key_path + ' ' + key)                            

    def find_linenumber(self, json_str, path):
        print("Path: ", path)
        match_all = '([^}])*'              
        se = ''
        for i in range(len(path) - 1):
            se += '"' + path[i] + '"' + match_all

        se += '"' + path[-1] + '"' + ':\s*(\[[^}]*?\]|".*?"|\d+\.*\d*)' 
        #print(se)

        s = re.compile(se, re.DOTALL)
        #print(s)
        match = s.search(self.json_str)

        start = self.calc_match_position(self.json_str, match.start(2))
        end = self.calc_match_position(self.json_str, match.end(2))
        #print("Start: {}, End: {}".format(start, end))
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

        return line + float('0.' + str(column))


    def print_configs(self):                 
        """Print out variables parsed from json file."""                                  
        attrs = dict((key, getattr(self, key)) for key in dir(self) if key.startswith('self'))        
        for key, value in attrs.items():     
            print("{}: {}".format(key, value))                                            

    def validated(self):                     
        return self.json_validated           


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


c = Configurations()

#print(c.configs)
