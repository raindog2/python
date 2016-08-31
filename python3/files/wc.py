#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Copyright 2015 Mark Purcell <mpurcell@Callicles>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

from random import randint

def main():
    filename = input("Which file? ")
    with open(filename) as f:

        #count the lines
        lines = f.readlines()
        print("Total lines:", len(lines))

        #count the words
        total_words = 0
        for i in lines:
            words = i.split()
            total_words += len(words)
        print("Total words:", total_words)
        
        #count the characters
        total_chars = 0
        all_words = []
        for i in lines:
            all_words += i.split() 
        for i in all_words:
            total_chars += len(i)
        print("Total characters:", total_chars)

main()
