from sys import argv

script, name = argv
prompt = '> '

script = "Hi, the script is %s, and your name is %s" % (script, name)

print "This is going to be the script"

print "Do you like your name? %s" % name
like_name = raw_input(prompt)

print "Where do you live? %s" % name
live = raw_input(prompt)

print "Where do you want to live? %s" % (name)
desire = raw_input(prompt)

print """
So, %s determines if you like your name.
You live in %s.
And you want to live in %s.
""" % (like_name, live, desire)
