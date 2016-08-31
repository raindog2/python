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
from random import choice

#this 'input' synatax works in 3.2 but in 2.7 'input' expects an integer,
#and so you would need "raw_input" if you want it to expect a string
adjectives = ['green', 'wild', 'new', 'clean', 'cheery']
nouns = ['platform', 'tile', 'tryst', 'field', 'laptop']
verbs = ['kill', 'reach', 'read', 'climb', 'force']
adverbs = ['clearly', 'fast', 'swimmingly', 'loudly']

print("There is no way one should ever", choice(verbs), "a", choice(nouns), choice(adverbs), "because you never know how", choice(adjectives), "a", choice(nouns), "will be.")

#the following works in 2.7; the parentheses above are how it's done in 3.2, like a function, i.e. print()
#print "As you may know, a", adjective, noun, "should never", verb, adverb,"!"

