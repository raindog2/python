#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  files.py
#  
#  Copyright 2014 Mark Purcell <mpurcell@Callicles>
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

def main():
    filename = input("What file should we use? ")
    print("Here are the contents of that file: ")
    with open(filename) as f:
        #print(f.read())
        #print(f.readlines())
        #while True:
            #if len(f.readline()) == 0: return False
        #for line in f:
            #print(f.readline())
        for line in f:
            #print(line, end="")
            line = line[:-1]
            print(line)

main()
