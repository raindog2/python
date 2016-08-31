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

""" Creates a checksum to make sure the received data of a 9-digit isbn) is the same as the sent data. The formula is (1*1stDigit + 2*2ndDigit + 3*3rdDigit...etc.) % 11. The checksum result is then appended to the 9-digit isbn (line 30), and if the checksum is 10, "X" is used. """

def data_checker(isbn):
    for c in isbn:
        if c not in "1234567890":
            return 0 
    if len(isbn) != 9:
        return 1
    else:
        return 2

def create_chksum(isbn):
    multiplier = 1
    sum = 0
    for i in range(9):
        # uses string parsing to extract each digit
        sum += (multiplier * int(isbn[i]))
        multiplier += 1
    chksum = sum % 11
    return chksum if chksum != 10 else "X"

def main():
    # gets the isbn as a string (see line 26)
    isbn = input("What is the 9-digit ISBN? ")
    if data_checker(isbn) == 0:
        print ("That isbn has letters or symbols!")
    elif data_checker(isbn) == 1:
        print ("That isbn is not 9 digits long!!")
    else:
        print("The checksum is " + str(create_chksum(isbn)))
        print("The ISBN is " + isbn + str(create_chksum(isbn)))

main()
