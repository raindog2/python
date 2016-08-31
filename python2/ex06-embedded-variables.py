#just assigns the value 10 to the formatter %d
x = "There are %d types of people." % 10
#defines variable 
binary = "binary"
#defines variable
do_not = "don't"
#defines variable y with string, which includes two other variables
y = "Those who know %s and those who %s." % (binary, do_not)

#prints value of variable x
print x
#prints value of variable y
print y

#prints string with value of variable x embedded
print "I said: %r." % x
#prints string with value of variable y embedded
print "I also said: '%s'." % y

#defines variable
hilarious = False
#defines variable with string containing %r (?which says print the value of the next variable you see after a % ?)
joke_evaluation = "Isn't that joke funny?! %r"

#print content of variable joke_eval (a string) and insert variable hilarious in it
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

