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
from random import choice
from random import shuffle

def mychoice(items):
    workingitems = items[:]
    index = randint(0, (len(workingitems)-1))
    return workingitems[index]

def delrandom(items):
    workingitems = items[:]
    shuffle(workingitems)
    return workingitems.pop()

def main():
    print("Mychoice sez:",mychoice([1,2,3,4,5,6]))
    print("Choice sez:",choice([1,2,3,4,5,6]))
    print("delrandom sez:",delrandom([1,2,3,4,5,6]))

main()

