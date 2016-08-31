#!/usr/bin/env python

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

#this 'input' synatax works in 3.2 but in 2.7 'input' expects an integer,
#and so you would need "raw_input" if you want it to expect a string
adjective = input("Give me an adjective: ")
noun = input("Give me a noun: ")
verb = input("Give me a verb: ")
adverb = input("Give me an adverb: ")

print("As you may know, a", adjective, noun, "should never", verb, adverb,"!")

#the following works in 2.7; the parentheses above are how it's done in 3.2, like a function, i.e. print()
#print "As you may know, a", adjective, noun, "should never", verb, adverb,"!"

