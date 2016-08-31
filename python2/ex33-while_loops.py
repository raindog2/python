i = 0
numbers = []

while i < 6:
    print "\nAt the top i is %d" %i
    numbers.append(i)
    
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "\nThe numbers: "

for num in numbers:
    print num 
