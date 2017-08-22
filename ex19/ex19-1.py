def pizza_and_breadsticks(number_of_slices, number_of_breadsticks):
    print "There are %d pizza slices" % number_of_slices
    print "There are %d breadsticks" % number_of_breadsticks
    print "Now that's a party...\n"

print "Applying it directly"
pizza_and_breadsticks(27, 23)

arg1, arg2 = (27, 23)

print "Applying variables indirectly"
pizza_and_breadsticks(arg1, arg2)

print "Lets do some math"
pizza_and_breadsticks (20 + 7, 20 + 3)

print "Some more why not"
pizza_and_breadsticks(arg1 + 0, arg2 + 0)
