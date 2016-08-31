#!/usr/bin/env python

# Copyright (C) 2013 Mark Purcell <mpurcell@uw.edu>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License,version 3
# as published by the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# If you did not receive a copy of the GNU General Public License
# along with this program, see <http://www.gnu.org/licenses/>.

from sys import exit
import os

os.system('clear')

def oldest_level():
    print "\nYou arrive at the oldest level floor.  It is dark except for a small light shining on Neill."
    print "He says he will paint you with smelly glue unless you do a super-hard math problem."
    print "Do you: "
    print "--do the math problem"
    print "--take the stairs up to tell Briel"
    print "--run into Guy's office"
    print "--duck into the music room"
        
    while True:
        next = raw_input("> ")
        
        if "math" in next or "problem" in next:
            dead("\nYou get the math problem right, and Neill gives you a cookie.")
        
        elif "Briel" in next or "tell" in next or "stairs" in next:
            briel()
          
        elif "run" in next or "Guy" in next or "office" in next :
            guys_office()
        elif "duck" in next or "music" in next:
	    music_room()
        else:
            print "\nThat is not one of the options."

def briel():
    print "\nIn Briel's office, she holds two envelopes, X and Y, and tells you to choose."
    
    while True:
        next = raw_input("> ")
        
        if "X" in next or "x" in next:
            print "\nShe opens the X envelope and reads the note inside: 'Back to the Oldest Level!!'"
            oldest_level()
        
        if "Y" in next or "y" in next:
            dead("\nShe opens the Y envelope and reads the note inside: 'Spruce Street School is closed forever!!'")
        else:
            print "\nThat is not one of the options."
    
    
    
def guys_office():
    print "\nHere you see Guy, but it is not Guy.  He seems to have transformed into an evil God!"
    print "He, it, whatever stares at you and tries to make you go insane."
    print "Do you: "
    print "--flee to the rooftop"
    print "--duck into the music room"
    print "--go to the lobby in the elevator"
    
    while True:
        next = raw_input("> ")
    
        if "flee" in next or "rooftop" in next:
            rooftop()
            
        elif "music" in next or "duck" in next:
            music_room()
            
        elif "elevator" in next or "lobby" in next:
            dead("\nYou enter the elevator, but the floor of the elevator immediately drops out, and you are smooshed at the bottom!")
        
        else:
            print "\nThat is not one of the options."

def rooftop():
    print "\nYou arrive on the rooftop, and Ali and Clint are standing there."
    print "Do you: "
    print "--run to Ali"
    print "--run to Clint"
    
    while True:
        next = raw_input("> ")
    
        if "Ali" in next or "ali" in next:
            dead("\nShe picks you up and throws you into Puget Sound, and you are never seen again.")
                
        if "Clint" in next or "clint" in next:
            dead("\nThat is the right choice. Clint is the head of safety patrol. He takes you to the police station where you will finally be safe.")
    
        else:
            print "\nThat is not one of the options."

def music_room():
    print "\nHere you see Sheree. She says you can play a bass, tenor, or soprano marimba."
    print "What do you do?"
    
    while True:
        next = raw_input("> ")
    
        if "bass" in next:
            print "\nOn playing the first note you are transported to the roof."
            rooftop()
    
        if "tenor" in next:
            print "\nOn playing the first note you are transported to Briel's office."
            briel()
            
        if "soprano" in next:
            dead("\nOn playing the first note your head explodes.")
        
        else:
            print "\nThat is not one of the options."
             
def dead(why):
    print why, "\nThe End.\n"
    exit(0)

def start():
    print "\nYou walk into Spruce Street School, but all the lights are out."
    print"You don't see anyone.  Do you: "
    print "\n--go up to the oldest level"
    print "--go to the music room"
    print "--go to Guy's office"
    print "--go to the rooftop playground"
     
    while True:
    
        next = raw_input("> ")
    
        if "oldest" in next or "level" in next:
            oldest_level()
        
        elif "Guy" in next or "office" in next:
            guys_office()
        
        elif "roof" in next or "playground" in next:
            rooftop()
        
        elif "music" in next or "room" in next:
            music_room()
        
        else:
            print "\nThat is not one of the options."

start()
        
      
