x = "I have %d cars." % 2
car_1 = 'Blue'
car_2 = 'Red'
y = "One of them is %s and the other is %s." % (car_1, car_2)

print x
print y

print "I said: %r" % x
print "That's right, I said '%s'" % y

car = True
car_evaluation = "Doesn't the red car seem like it would be faster? %r"
print car_evaluation % car
print "-------------------------------------------------------------------"
G = "I am going to "
print G
old = "make these lines into one."
print old
print "               "
print G + old
