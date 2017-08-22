# I'm going to create a dictionary of states

state_to_abbrev = {
'TX' : 'Texas',
'CA' : 'California',
'FL' : 'Florida',
'OR' : 'Oregon',
'AL' : 'Alabama',
}

abbrev_to_state = {
'Texas' : 'TX',
'California' : 'CA',
'Florida' : 'FL',
'Oregon' : 'OR',
'Alabama' : 'AL',
}

cities = {
'TX' : 'Dallas',
'CA' : 'Hollywood',
'FL' : 'Orlando',
}

cities['OR'] = 'Oregon'
cities['AL'] = 'Alabama'

abbrev_to_state ['New Mexico'] = 'NM'
state_to_abbrev ['NM'] = 'New Mexico'

breaker = '-' * 10
print "I am printing the cities for Texas:", cities['TX']
print "I am printing the cities for California:", cities['CA']
print breaker
print "I am printing the state name for TX:", state_to_abbrev['TX']
print "I am printing the state name for CA:", state_to_abbrev['CA']
print breaker
print "I am printing the abbreviation for Texas:", abbrev_to_state['Texas']
print "I am printing the abbreviation for California:", abbrev_to_state['California']
print breaker
print "Now I'm going to integrate states and cities to display an abbreviation"
print "This is the abbreviation of Texas:", abbrev_to_state[state_to_abbrev['TX']]
print breaker

for state, abbrev in abbrev_to_state.items():
    print "The abbreviation for %s is %s." % (state, abbrev)
print breaker
for thing, doohickey in state_to_abbrev.items():
    print "The abbreviation %s belongs to the state %s." % (thing, doohickey)

print breaker
for x, y in cities.items():
    print "The city for %s is %s" % (x, y)
print breaker

abbreviation = abbrev_to_state.get('California', 'CA')
