#!/usr/bin/env python

from sys import exit
import os

os.system('clear')

print "\nWelcome to the flashcards for working with strings in python!\n"

def lower():
    while True:
    
        lowercase = raw_input("What is the code to make a string s lowercase?\n" )
    
        if lowercase == "s.lower()":
            print "Right!\n"
            upper()
        else:
            print "\nNot quite. Try again!\n"    

def upper():
    while True:
    
        uppercase = raw_input("What is the code to make a string s UPPERCASE?\n" )
    
        if uppercase == "s.upper()":
            print "Right!\n"
            strip()
        else:
            print "\nNot quite. Try again!\n" 

def strip():
    while True:
        
        strip = raw_input("What is the code to remove the whitespace from the start and end of a string s?\n" )
    
        if strip == "s.strip()":
            print "Right!\n"
            isalpha()
        else:
            print "\nNot quite. Try again!\n" 

def isalpha():
    while True:
        
        isalpha = raw_input("What is the code to test if all characters in a string s are alphabetic?\n" )
    
        if isalpha == "s.isalpha()":
            print "Right!\n"
            isdigit()
        else:
            print "\nNot quite. Try again!\n" 

def isdigit():
    while True:
        
        isdigit = raw_input("What is the code to test if all characters in a string s are numbers?\n" )
    
        if isdigit == "s.isdigit()":
            print "Right!\n"
            isspace()
        else:
            print "\nNot quite. Try again!\n"

def isspace():
    while True:
        
        isspace = raw_input("What is the code to test if all characters in a string s are whitespace?\n" )
    
        if isspace == "s.isspace()":
            print "Right!\n"
            startswith()
        else:
            print "\nNot quite. Try again!\n"
            
def startswith():
    while True:
        
        startswith = raw_input("What is the code to test if a string s starts with 'xxx'?\n" )
    
        if startswith == "s.startswith('xxx')":
            print "Right!\n"
            endswith()
        else:
            print "\nNot quite. Try again!\n"

def endswith():
    while True:
        
        endswith = raw_input("What is the code to test if a string s ends with 'xxx'?\n" )
    
        if endswith == "s.endswith('xxx')":
            print "Right!\n"
            find()
        else:
            print "\nNot quite. Try again!\n"

def find():
    while True:
        
        find = raw_input("What is the code to search for a string 'xxx' within a string s?\n" )
    
        if find == "s.find('xxx')":
            print "Right!\n"
            replace()
        else:
            print "\nNot quite. Try again!\n"            

def replace():
    while True:
        
        replace = raw_input("What is the code to replace all occurences of 'xxx' with 'yyy' within a string s?\n" )
    
        if replace == "s.replace('xxx', 'yyy')":
            print "Right!\n"
            split()
        else:
            print "\nNot quite. Try again!\n"            

def split():
    while True:
        
        split = raw_input("What is the code to chop a string s and return a list of substrings separated by a given delimiter 'x'?\n" )
    
        if split == "s.split('x')":
            print "Right!\n"
            join()
        else:
            print "\nNot quite. Try again!\n"            
	
def join():
    while True:
        
        join = raw_input("What is the code to concatenate elements in a given list 'list' into a new string without spaces?\n" )
    
        if join == "''.join(list)":
            print "Right!\n"
            slice1()
        else:
            print "\nNot quite. Try again!\n"            

def slice1():
    while True:
        
        slice1 = raw_input("Slicing: given the string s = 'concatenate', what is the code to return the string 'catenate'?\n" )
    
        if slice1 == "s[3:]":
            print "Right!\n"
            slice2()
		
        else:
            print "\nNot quite. Try again!\n"            

def slice2():
    while True:
        
        slice2 = raw_input("More slicing: what about returning 'cat'?\n" )
    
        if slice2 == "s[3:6]":
            print "Right!\n"
            print "And that brings us to the end of the flashhcards for strings in python.  Thanks for playing!\n"
            exit(0) 
		
        else:
            print "\nNot quite. Try again!\n"              

lower()


