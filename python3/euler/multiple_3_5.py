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

#def find_multiples(n):
    #result = []
    #for i in range(n):
        #if i % 3 == 0 or i % 5 == 0: result.append(i)
    #return sum(result)

# With list comprehension:

#def find_multiples(n):
    #return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])

def find_multiples(n):
    a = [x for x in range(3,n,3)]
    b = [x for x in range(5,n,5)]
    return sum(a + b)

def main():
    n = int(input("Let's find the sum of all the multiples of 3 and 5 below a max number.  What is your max number? "))
    print(find_multiples(n))

main()

