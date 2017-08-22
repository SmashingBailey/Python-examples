print "This is a raw input and if/then demonstration"

prompt = "> "

print "How many cats would you own?"

cats = raw_input(prompt)

print "How many dogs would you own?"

dogs = raw_input(prompt)

if dogs > cats:
    print "\nYOU ARE A DOG PERSON"

if cats > dogs:
    print "\nYOU ARE A CAT PERSON"

if cats == dogs:
    print "\nYOU DIRTY NEUTRAL"

print """
There's a second part to this
To continue press "ENTER"
To exit press "CTRL-C"
"""

raw_input("> ")

print """
Now I have heard animal ownership has a
direct correlation to height
"""

print "How tall are you in inches?"
height = int(raw_input(prompt))

height_total = height - 68

if height <= 68:
    print "You are short. Sorry. It's not correlated. You suck"

if height > 68:
    print """
    You are not short. The cutoff was 68 inches.
    You beat the cutoff by %r inches.
    """ % height_total
