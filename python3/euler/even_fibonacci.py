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

# this is working, except that it can't handle 4000000, so I need to find a more efficient way to do it

import os
os.system('clear')

def fib(n):
    result = []
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
        result.append(a)
    return result

def even_fibonacci(m):
    return [x for x in fib(m) if x % 2 == 0]

def main():
    print(sum(even_fibonacci(4000000)))

main()
