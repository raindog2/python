#This is no longer really ex11...I re-wrote 
#it to be a BMI calculator.

print '''
Hi, welcome to the Python BMI
calculator.  BMI is BS, but it provides
aspiring programmers with an equation
to work with.
'''
print "\nReady? (y/n)",
answer1 = raw_input()

print "." *10

#print "How old are you?",
#age = raw_input()


print "\nOK...How tall are you (in inches)?",
height = input()
print "\nHow much do you weigh? (in pounds please, this is America)",
weight = input()

print "." *10

print "\nOK, so what I have is this: \nyou are %s inches tall, \nand you weigh %s lbs. \n\nIs that correct?" % (height, weight),
answer2 = raw_input()
bmi = (weight * 703) / height**2

print "\nOK, so according to my calculations, your BMI is circa %i (sorry I can't be more precise, I use fuzzy math).\n\n" % bmi
