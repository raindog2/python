#gets the argv module from sys
from sys import argv
#unpacks argv into two variables
script, filename = argv
#defines txt as a command, to open the filename that was defined by user when s/he started the script
txt = open(filename)
#bullshit
print "Here's your file %r:" % filename
#prints the contents of the txt variable (which is an opened file), then tells it to read ('calls the function' read) that opened file
print txt.read()
#the rest just does it all again, using user-prompted filename rather than filename given at outset 
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()


