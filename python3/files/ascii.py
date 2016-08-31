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

def encode(msg):
    global result_lst
    result_lst = []
    result = "" 
    for i in msg:
        result += str(ord(i))
        result_lst.append(ord(i))
    return result

def decode(msg):
    result = ""
    for i in msg:
        result += chr(i)
    return result

def main():
    word = input("What word shall we use? ")
    print("In code, your word is", encode(word))
    print("And decoded, it is", decode(result_lst))
    #for i in range(32, 127):
        #print(i, chr(i))
main()

