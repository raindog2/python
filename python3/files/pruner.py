# !/usr/bin/env python
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
#  
#Deletes all words in a file that are 5 words or more

def main():
    existing_file_name = input("Which file do you want to prune? ")
    new_file_name = input("What is the new file name? ")
    with open(existing_file_name, "r") as input_file:
        with open (new_file_name, "w") as output_file:
            for line in input_file:
                if len(line) <= 9:
                    output_file.write(line)
    #with open(file_name, "r") as f:
        #lines = f.readlines()
        #f.close()
    #with open(file_name, "w") as f:
        #for i in lines:
            #if len(i) <= 4:
                #f.write(i)
        #f.close()
main()
