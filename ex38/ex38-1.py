first_list = "One Two Three"

print "Wait there are not 6 things in that list. Let's fix it"

first_crap = first_list.split(' ')

second_list = ["Four", "Five", "Six"]

print "The first list of items are", first_crap

print "The second list of items are", second_list

print "......"
print "Now I'm going to combine the lists"
print "......"
print first_crap + second_list

while len(first_crap) != 6:
    new_line = second_list.pop()
    print "This is the first word %s" % first_crap
    first_crap.append(new_line)
    print "The new length is %d" % len(first_crap)

print first_crap[1]
print first_crap[-1]
print first_crap.pop()
print ' '.join(first_crap)
print '#'.join(first_crap[3:5])
