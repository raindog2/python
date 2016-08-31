print '''
Hi, welcome to the Python BMI calculator.  
BMI is BS, but it provides aspiring 
programmers with an equation to work with.
'''

print "Ready? (y/n)",
raw_input()

height = input("\nHow tall are you, in inches? ")
weight = input("\nHow much do you weigh, in pounds? ")

print "\nOK, so you are %i inches tall, and you weigh %i pounds. \nDo I have that right? (y/n)" % (height, weight),
raw_input()

bmi = (weight * 703) / height**2

print "\nThen according to my calculations, your BMI is roughly %i (n.b. Python uses fuzzy math)." % bmi

