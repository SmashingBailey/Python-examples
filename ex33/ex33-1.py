print "How many pieces of bacon do we have?"
prompt = ("> ")

silly = int(raw_input(prompt))

bacon = silly
script = []

while bacon <= 10:
    print "The current bacon count is %d" % bacon
    script.append(bacon)

    bacon = bacon + 1
    print "The numbers are now", script
    print "The bacon count is now %d" % bacon

print "The bacon count is: "

for count in script:
    print count

print "This program will display the amount of cars"
desired_amount = int(raw_input("How many cars would you like? > "))

bmw = 0
infiniti = 0

def cars(desired_amount):
    bmw = desired_amount * 0
    infiniti = desired_amount * 0
    return bmw, infiniti

print """
That's a shame. You'll get nothing and you'll like it!
You'll get %d BMWs and %d Infinitis.
""" % (bmw, infiniti)
