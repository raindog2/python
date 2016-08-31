import os
os.system("clear")

print "You enter a dark room with three doors. Do you go through door 1, door 2, or door 3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1 Take the cake."
    print "2 Scream at the bear."
    print "3 Leave."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "3":
        print "The bear follows you out and offers you half his cheese cake." 
    else:
        print "Well, doing %s is probably better. But it wasn't one of the choices." % bear
    
elif door == "2":
    print "You see a giant bug lying on its back, flailing its legs. Do you:"
    print "1 Kill the bug."
    print "2 Help the bug onto its legs."
    print "3 Begin speaking low German."
    
    bug = raw_input("> ")
    
    if bug == "1":
        print "Fail. His armor is too thick."
    elif bug == "2":
        print "Unwise. He eats you up."
    elif bug == "3":
        print "He eagerly engages you in a conversation that lasts hours."
    else:
        print "Sigh. Why do I even give users options??"
     
elif door == "3":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1 Blueberries."
    print "2 Yellow jacket."
    print "3 Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    elif insanity == "3":
        print "Gun with occasional music, indeed."
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
        
else:
    print "You stumble around and fall on a knife and die. Good job!"
    
