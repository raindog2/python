from sys import exit
import os

os.system('clear')

def gold_room():
    print "\nYou enter a room containing 100 gold pieces. How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next or "2" in next or "3" in next or "4" in next or "5" in next or "6" in next or "7" in next or "8" in next or "9" in next:
        how_much = int(next)
    else:
        dead("Man,learn to type a number.")    

    if how_much < 50:
        dead("Nice, you're not greedy, you win!")
    elif how_much >=50:
        print "You greedy jerk! You lose!!"
        exit(0)

def bear_room():
    print "\nYou enter a room in which there is a large grizzly bear. The bear has a bunch of honey. He is in front of the exit door."
    print "How are you going to move the bear?"
    print "--take honey"
    print "--taunt him"
    
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if "honey" in next or "take" in next:
            dead("The bear looks at you and then slaps your face off.")
        elif "taunt" in next and not bear_moved:
            print "\nThe bear has moved from the door. You can go through it now."
            bear_moved = True
            print "What do you do next?"
            print "--taunt him again"
            print "--open door and leave"
            next = raw_input("> ")
        if "taunt" in next and bear_moved:
            dead("\nThe bear gets hyper-angry and chews your leg off.")
        elif "open" in next or "leave" in next and bear_moved:
            gold_room()
        else:
            print "\nThat is not one of the options."

def cthulhu_room():
    print "\nHere you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next or "head" in next:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "\nYou are in a dark room. Pretty spooky."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("Since you chose neither door, you stumble around the room until you starve.")

start()
        
        
