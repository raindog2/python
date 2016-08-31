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
from random import randint

def main():
    choice = int(input("Number of instances? "))
    total0 = 0
    total1 = 0
    for i in range(1, choice + 1):
        x = randint(0, 1)
        if x == 0:
            total0 += 1
        if x == 1:
            total1 += 1
    print("Total 0:", total0, "or", total0 / choice * 100, "%")
    print("Total 1:", total1, "or", total1 / choice * 100, "%")

main()   
