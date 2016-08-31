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

def firstvowelindex(word):
    i = 0
    vowels = 0
    for t in range(0, len(word)):
        if word[t] in "aeiou":
            vowels += 1
    if vowels == 0:
        return vowels
    else:
        while word[i] not in "aeiou":
            i += 1
        return i

def piglatin(word):
    i = firstvowelindex(word)
    if i == 0:
        return word + "yay"
    return word[i:] + "-" + word[:i] + "ay"

def main():
    w = input("Welcome to the Python pig latin translator.  What word would you like to translate into pig latin? ")
    w = w.lower()
    print(w, "in pig latin is", piglatin(w))

main()
