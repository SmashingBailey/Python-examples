def add(a,b):
    print "I'm adding %d and %d" % (a,b)
    return a + b

def subtract(a,b):
    print "I'm subtracting %d and %d" % (a,b)
    return a - b

def multiply(a,b):
    print "I'm MULTIPLYING %d and %d" % (a,b)
    return a * b

def divide(a,b):
    print "I'm DIVIDING %d and %d" % (a,b)
    return a / b

age = 21
maturity = 15
add_age = add (10,5)

subtract_age = subtract (10,5)

multiply_age = multiply (10,5)

divide_age = divide (10,5)

print """
Addition output is: %d
Subtraction output is: %d
Multiplication output is: %d
Division output is: %d
""" % (add_age, subtract_age, multiply_age, divide_age)


print "This is addition and subtraction"
