import time
print "\nWelcome to the python generator of number-lists!\nLet's generate a list of ascending numbers..."
time.sleep(3)
print "What value do you want to start at? ",
start = input()
print "What value do you want to be our upper limit? ",
ceiling = input()
print "And what increment do you want each addition to increase by? ",
increment = input()

numbers = []

time.sleep(3)

print "\nThe list 'numbers' is currently empty..."

time.sleep(3) 

def for_loop(start, ceiling, increment):
    for i in range(start, ceiling, increment):
        print "\nAdding %d to list 'numbers'" % i
        numbers.append(i)
    
        print "List 'numbers' is now: ", numbers
        time.sleep(3)
        

for_loop(start, ceiling, increment)

print "\nThe final contents of the list 'numbers': "

print numbers
