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
import time
os.system('clear')

start_time = time.time()

def fib(n):
    fib_list = [1, 1]
    for i in range(n-2):
        fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list

def main():
    for i in range(2, 101, 7):
        print("The first", i, "fibonnaci numbers are:", fib(i))
main()

print(time.time() - start_time, "elapsed.")
