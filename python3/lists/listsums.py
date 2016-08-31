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

def mysum(items):
    total = 0
    for i in range (len(items)):
        total += items[i]
    return total

random_list = []
for i in range (9):
    random_list.append(randint(0,9))

def main():
    print (random_list)
    print ("For mysum:",mysum(random_list))
    print ("For sum:", sum(random_list))
    
main()

