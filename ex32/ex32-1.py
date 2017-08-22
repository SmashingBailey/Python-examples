the_names = ['Bailey','Ashley','Eric','Jacob','Shawna','Devon']
the_count = [1, 2, 3, 4, 5, 6]
alternate = ['Bailey', 1, 'Ashley', 2, 'Eric', 3]

for name in the_names:
    print "\tThis is %s" % name

for count in the_count:
    print "\tThis is %d" % count

for change in alternate:
    print "\tThis is %r" % change

stuff = []

for i in range(0, 6):
    print "Adding %d to the list." % i
    stuff.append(i)

for i in stuff:
    print "Element was: %d" % i

crap = []

for crunch in range(0, 6):
    print "Adding %d to the list." % crunch
    crap.append(crunch)

for crunch in crap:
    print "Element was: %d" % crunch

damn = []

for shiza in range(0, 6):
    print "I am adding %d" % shiza
    damn.append(shiza)

for shiza in damn:
    print "%d was added" % shiza
