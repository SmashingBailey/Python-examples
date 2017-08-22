from sys import argv

script, filename = argv

print "The script name is %r" % script
print "NOW. SOME OF THE BEST MOVIE QUOTES"

text = open(filename)

print text.read()
