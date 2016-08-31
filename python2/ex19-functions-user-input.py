# defines the function (cheese_and_crackers) as having two arguments
# and printing some lines
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"

# gets integer input from user (hence %d in function) to define variables
amount_of_cheese = input("How many cheeses do you have? ")
amount_of_crackers = input("Aaaaand, how many boxes of crackers? ")

# calls the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


