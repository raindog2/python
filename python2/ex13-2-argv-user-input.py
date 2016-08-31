from sys import argv

script, cephalus, polemarchus, thrasymachus, socrates = argv

#these lines have the user redefine the value of the 4 variables that were originally defined when the script was called
cephalus = raw_input ("What is the value of the first variable? "),
polemarchus = raw_input ("What is the value of the second variable? "),
thrasymachus = raw_input ("What is the value of the third variable? "),
socrates = raw_input ("What is the value of the fourth variable? "),

print "The name of the script is:", script
print "The value of the first variable:", cephalus
print "The value of the second variable:", polemarchus
print "The value of the third variable:", thrasymachus
print "The value of the fourth variable:", socrates

