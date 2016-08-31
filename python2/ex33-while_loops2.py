print "What value do you want to start at? ",
start = input()
print "What value do you want to be our ceiling? ",
ceiling = input()
print "And what increment do you want the loop to increase by? ",
increment = input()

numbers = []

def while_loop(start, ceiling, increment):
    while start < ceiling:
        print "\nAt the top 'start' is %d" % start
        numbers.append(start)
    
        start = start + increment
        print "Numbers now: ", numbers
        print "At the bottom 'start' is %d" % start

while_loop(start, ceiling, increment)

print "\nThe numbers: "

print numbers
