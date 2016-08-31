from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CNTL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally we close it."
target.close()


#you are good at things when you apply yourself to them
#but you slough off and only do the work kind of
#you have to not get verklempt about doing them
#just do them at a steady pace, with grace, rather than at white-knuckle intensity
