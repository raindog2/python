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

""" Creates a checksum to make sure the received data of a 13-digit isbn) is the same as the sent data. The formula is 10 - ((1*1stDigit + 3*2ndDigit + 1*3rdDigit + 3*4th digit...etc.) % 10). The checksum result is then appended to the 12-digit isbn (51). """

def data_checker(isbn):
    for c in isbn:
        if c not in "1234567890":
            return 0 
    if len(isbn) != 12:
        return 1
    else:
        return 2

def create_chksum(isbn):
    multiplier = 1
    total = 0
    for i in range(12):
        # uses string parsing to extract each digit
        multiplier = 3 if i % 2 != 0 else 1
        total += (multiplier * int(isbn[i]))
    chksum = 10 - (total % 10)
    return chksum

def main():
    # gets the isbn as a string (see line 26)
    isbn = input("What is the 12-digit ISBN? ")
    if data_checker(isbn) == 0:
        print ("That isbn has letters or symbols!")
    elif data_checker(isbn) == 1:
        print ("That isbn is not 12 digits long!!")
    else:
        #print(total)
        print("The checksum is " + str(create_chksum(isbn)))
        print("The ISBN is " + isbn + str(create_chksum(isbn)))

main()
