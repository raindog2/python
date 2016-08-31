#!/usr/bin/env python

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Here's the list: ", ten_things

print "Wait there's not ten things in that list, let's fix that."

#splits ten_things into separate items at each space--we could have just defined an actual list to start with
stuff = ten_things.split(' ') 
#just creates a new list to use for additions
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

#while the numner of things in stuff is not 10...
while len(stuff) != 10:
	#take the last item in more_stuff, pop it off, and assign it to next_one
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	#append next_one to stuff
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

#prints the second item in the list
print stuff[1]

#prints the last item in the list
print stuff[-1] #whoa! fancy

#pops off (i.e. removes) the last item in the list and prints it 
print stuff.pop()

#joins all the items in stuff using a space and prints it, except corn, which was popped off
print ' '.join(stuff) #what? cool!

#joins the 4th (3) and 5th (up to but not including the 6th, which's index is 5) items in the list with an octothorpe and prints it
print '#'.join(stuff[3:5]) #super stellar!
