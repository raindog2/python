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

numbers = [x for x in range(1, 27)]
letters = [chr(x) for x in range(97, 123)]
codex = list(zip(numbers, letters))

def word_value(word):
    value = 0
    for i in word:
        for (number, letter) in codex:
            if i == letter: value += number 
    return value

def main():
    storage = [0]
    filename = input("Which file should we use? ")
    with open(filename) as f:
        for i in f:
           if word_value(i) >= storage[0]:
               storage.insert(0, i)
               storage.insert(0, word_value(i))
    final_list = [storage[1]]
    for i in range(0, 400, 2):
        if storage[i] == storage[i+2]:
            final_list.append(storage[i+1])
        else: break
    print("The word(s) with the highest value are ", final_list, "with a score of", storage[0]) 

main()
