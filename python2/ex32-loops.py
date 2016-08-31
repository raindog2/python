the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop uses the list that defines a variable as the target of its 'for'
print "\nIn the number list we've got:"
for number in the_count:
    print number

print "\nIn list form that's:"
print the_count

print "\nIn the fruit list we've got:"
for fruit in fruits:
    print fruit

print "\nIn list form that's:"
print fruits

# mixed lists work too
# have to use %r since it can be either a string or an integer
print "\nIn the change list we've got:"
for i in change:
    print i

print "\nIn list form that's:"
print change

# we can also built lists, first start with an empty one:
elements = []
print "\nThe list 'elements' currently consists of:"
print elements

for i in range(0, 6):
    print "\nAdding %d to the list." %i
    # append is a function that lists understand
    elements.append(i)

print "\nNow 'elements' consists of:"
print elements
 



