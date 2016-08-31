#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex25.py
#  
#  Copyright 2013 Mark Purcell <mpurcell@Callicles>
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

sentence = "We do not confront, fight, and smash the state.  We do not seize the state and then use it to create the conditions by which it withers.  Rather, we engage, starting now, in the positive project of building a viable alternative way of life, another polity without the state [Virno: 'non-State republic'].  We lose ourselves in this project.  Over time, we so develop our common ability to rule ourselves that we look up one day from our work and notice the state, oINver in the corner, living “out its days in isolation,” having fallen into disuse, having become obsolete, having been put out to pasture.  And we wonder what we ever used it for, why we ever thought we needed it in the first place."
	
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"Sorts the words then prints the first and last one."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sortetd(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
	

