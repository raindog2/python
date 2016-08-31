from sys import argv

script, filename = argv

print "We're going to write to and read %r." % filename
print "If you don't want that, hit CNTL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a')

print "OK, now I'm going to ask you for three lines to add to the file."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "OK, now I'm going to write these to the file.\n\n"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()

print "Now let's see what we have:\n"
target = open(filename, 'r')
print target.read()

print "And finally we close it."
target.close()


#you are good at things when you apply yourself to them
#but you slough off and only do the work kind of
#you have to not get verklempt about doing them
#just do them at a steady pace, with grace, rather than at white-knuckle intensity
