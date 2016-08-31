from sys import argv

script, filename = argv

print "Hi! Welcome to the Python file manipulator."
print "We're going to add some lines to the existing file %r." % filename
print "If you don't want that, hit CNTL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "OK, here's what is currently in the file:"
target = open(filename, 'r')
print target.read()

print "Now I'm going to ask you for three lines to add to the file."
target = open(filename, 'a')

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "OK, now I'm going to add these to the file.\n\n"

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
print "Done! Thank you for using the Python file manipulator."
target.close()


#you are good at things when you apply yourself to them
#but you slough off and only do the work kind of
#you have to not get verklempt about doing them
#just do them at a steady pace, with grace, rather than at white-knuckle intensity
