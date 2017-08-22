name = 'Bailey H. Hosea'
age = 20 # years
height = 70 # inches
weight = 155 # pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Blonde'

total = age + height + weight

inches_to_centimeters = 2.54 * height
pounds_to_kilograms = .453592 * weight

print "My name is %s" % (name)
print "My age is %d" % (age)
print "My height is %d" % (height)
print "My weight is %d" % (weight)
print "My eyes are %s" % (eyes)
print "My teeth are %s" % (teeth)
print "My hair is %s" % (hair)
print "                        "
print "And for my next trick, I will do two metric conversions."
print "                         "
print "I am going to convert my height from inches to centimeters."
print "This is the height conversion result %d" % (inches_to_centimeters)
print "                          "
print "Now I will convert my weight from pounds to kilograms."
print "This is the weight conversion result %d" % (pounds_to_kilograms)

print "If I add %d, %d, and %d I get %d" % (age, height, weight, total)
