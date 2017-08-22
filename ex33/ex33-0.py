yellow = 0
numbers = []

while yellow < 4:
    print "I'm printing the original number %d" % yellow
    numbers.append(yellow)

    yellow = yellow + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % yellow


print "The numbers: "

for num in numbers:
    print num
