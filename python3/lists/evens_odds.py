#!/usr/bin/env python3.2

# Copyright (C) 2014 Mark Purcell <mpurcell@uw.edu>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License,version 3
# as published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# If you did not receive a copy of the GNU General Public License
# along with this program, see <http://www.gnu.org/licenses/>.

import os
os.system('clear')
from random import randint

def evens(items):
    result = []
    for i in items:
        if i % 2 == 0:
            result.append(i)
    return result

def odds(items):
    result = []
    for i in items:
        if i % 2 != 0:
            result.append(i)
    return result

def block(names, blocked):
    for name in names:
        if name in blocked:
            names.remove(name)
    return names

random_list = []
for i in range (8):
    random_list.append(randint(0,35))

names = ["mark", "hell", "stacy", "ingrid", "henry", "steve"]
blocked = ["hell", "stacy", "henry"]

def main():
    print(random_list)
    print("evens:", evens(random_list))
    print("odds:", odds(random_list))
    print(block(names, blocked))    

main()
