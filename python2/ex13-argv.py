#the way this script is called is by giving the values of the three variables in the command that calls the script: python ex13.py john peter paul

from sys import argv

script, first, second, third = argv #just the variable names

print "The script is called:", script
print "Your first variable is set to", first
print "Your second variable is set to", second
print "Your third variable is set to", third
