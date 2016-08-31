# !/usr/bin/env python
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
#  
def signature(word):
    chars = list(word)
    chars.sort()
    return chars

def wordlist(fname):
    with open(fname) as f:
        #return f.read().split()
        return f.readlines()

def matches(jumble):
    sign = signature(jumble)
    result = 0
    for word in wordlist(file_name):
        if signature(word) == sign:
            result += 1
    return result - 1 # to prevent it from counting itself as an anagram of itself
    
def main():
    global file_name
    file_name = input("Give me a file with a list of words to use, and I will return a list of words that have the highest number of anagrams: ")
    storage = [0]
    with open(file_name) as f:
        for i in f:
            print(matches(i),":", i, end="")
            if matches(i) >= storage[0]:
                storage.insert(0, i)
                storage.insert(0, matches(i))
    print(storage)
    final_list = []
    for i in range(0, 400, 2):
        if storage[i] == storage[i+2]:
            final_list.append(storage[i+1])
        else: break
    print("The words with most anagrams are", final_list, "with", storage[0], "anagrams!")
    #print("The words with most anagrams are", storage[1], "with", storage[0], "anagrams!")

main()

