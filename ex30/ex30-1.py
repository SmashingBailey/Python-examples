print """
This program will be good for finding out how much gas you'll use
and making a decision on which vehicle you should use.
"""

prompt = "> "

print "What's the vehicle model?"
vehicle_model = raw_input(prompt)

print "What's your city MPG in the %s" % vehicle_model
city_mpg = (int(raw_input(prompt)))

print "What's your highway MPG in the %s" % vehicle_model
hwy_mpg = (int(raw_input(prompt)))

print "How many gallons does your car hold?"
vehicle_gallons = (int(raw_input(prompt)))

print "How many highway miles will the trip take?"
hwy_miles = (int(raw_input(prompt)))

print "How many city miles will the trip take?"
city_miles = (int(raw_input(prompt)))

total_miles = city_miles + hwy_miles

vehicle_distance = ( / hwy_mpg) + (city_mpg / city_miles)

fuel_leftover = vehicle_distance - total_miles

fuel_needed = total_miles - vehicle_distance

if vehicle_distance > total_miles:
    print """
    You will make the trip without having to fill up.
    You will make the trip with %d miles left in the tank.""" % fuel_leftover
elif vehicle_distance < total_miles:
    print """
    You will have to stop for gas to make the trip.
    You will need to fill up with %d miles left.""" % fuel_needed
else:
    print "You will make it to your destination with no fuel left."
