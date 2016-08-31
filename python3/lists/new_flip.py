#!/usr/bin/env python

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
import time
from random import choice

#def flip():
#    x = randint(0, 1)
#    return x

def flip():
    options = ['heads', 'tails']
    return choice(options)

def main():
    tails = 0
    heads = 0
    flips = int(input("How many times do you want to flip?\n> "))
    for i in range(0, flips):
        time.sleep(0.5)
        if flip() == 'tails':
            print(flip())
            tails += 1
        else:
            print(flip())
            heads += 1
    print("All told, we saw", heads, "heads, and", tails, "tails!!")

main()
