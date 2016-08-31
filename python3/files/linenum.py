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
    print("This program will number the lines in a given file and print it to standard output.")
    filename = input("Which file should we use? ")
    with open(filename) as f:
        lines = f.readlines()
        line_numbers = [x for x in range(1, len(lines) + 1)] 
        resource = zip(line_numbers, lines)
        for a,b in resource:
            print(a, b, end="")

main()
