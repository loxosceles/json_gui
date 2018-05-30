#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
import pudb
from decimal import Decimal

d = \
{
    "a": {
        "b": {
            "c": {
                "d": "v1",
                "key": "v2"  # line 6
                }
            },
        "x": {
            "c": {
                "d": "v11",
                "key": "v20" # line 12
                }
            },
        "c": {
            "g": [           # line 16
                3,
                10,
                100,
                3000
                ],           # line 21
            "key": "v4"      # line 22
            },
        "key": "v5"          # line 24
    }
}

def _create_dict(ds):
    l = ds.split('\n')
    return l, [x.lstrip() for x in l]

def _count_array_length(l):
    count = 0
    for el in l:
        count += 1
        if el.endswith('],'):
            return count

def find_linenumber(json_string, path):

    def findkey(l, t, lev=0, ind=0):
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
            return 1 + findkey(l[1:], t, lev, ind)

    #  pu.db
    l, ll = _create_dict(json_string) # l: list, ll: list (spaces stripped)

    start_row  = findkey(ll[1:], path)

    idx = start_row - 1
    start_col = l[idx].find(':') + 2

    if l[idx].endswith('['):
        pu.db
        end_row = _count_array_length(l[idx + 1:]) + start_row
        #end_col = l[end_row - 1].find('],') + 2
        end_col = start_col
    elif l[idx].endswith('"'):
        end_row = start_row
        end_col = len(l[idx]) - 1
    else:
        print("Something bad happend")

    start = Decimal(start_row) + Decimal('0.' + str(start_col))
    end  = Decimal(end_row) + Decimal('0.' + str(end_col))

    return start, end


if __name__ == "__main__":
    ds = json.dumps(d, indent=4)

    tup = ('a', 'key')
    start, end = find_linenumber(ds, tup)
    print("Found a -> key on line {}, {}".format(start, end))

    tup = ('a', 'x', 'c', 'key')
    start, end = find_linenumber(ds, tup)
    print("Found a -> x -> c -> key on line {}, {}".format(start, end))

    tup = ('a', 'c', 'key')
    start, end = find_linenumber(ds, tup)
    print("Found a -> c -> key on line {}, {}".format(start, end))

    tup = ('a', 'c', 'g')
    start, end = find_linenumber(ds, tup)
    print("Found a -> c -> g on line {}, {}".format(start, end))

