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

def dec_to_bin(n):
    #integ = int(input("Give me a non-negative integer: "))
    #binar = str(bin(integ))
    #return binar[2:]
    binar = "" 
    if n == 0:
        binar += "0b0"
        return binar
    else:
        """ 
        This is the classic math formula for taking an integer and building
        a string that contains the information of a binary by incrementally
        doing math operations on the original integer. 
        """
        while n > 0: 
            binar = str(n % 2) + binar
            n = n // 2
        binar = "0b" + binar
        return binar

def bin_to_dec(s):
    #s = "0b" + s
    s = int(s, 2)
    return s

def main():
    print("Convert Integers to Binaries:\n")
    for i in range(101):
        print(str(i) + " => " + dec_to_bin(i))
    print("\nConvert Binaries to Integers:\n")
    for i in range(101):
        print(dec_to_bin(i) + " => " + str(bin_to_dec(dec_to_bin(i))))

main()
