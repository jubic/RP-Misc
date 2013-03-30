import re
# remember "\d" is equal to [0-9]
a = re.search("\d", "It's 6PM")     # matched
b = re.search("\d", "Apple orange") # failed (no digits)
#
# remember "\s" is for "whitespace"
c = re.search("\s", "Apple orange") # matched (a space between Apple and orange)
d = re.search("\s", "Pineapple")    # failed (no white space is found)
#
# "\w" is all alphanumeric and underscore
# As long as one alphanumeric character can be found, it matches
e = re.search("\w", "Apple orange") # matched
f = re.search("\w", "_")            # matched
g = re.search("\w", "   Apple")     # matched
h = re.search("\w", "    ")         # failed (space is not alphanumeric)
#
# "." matched anything including space (except newline)
i = re.search(".", "Apple orange")  # matched
j = re.search(".", "    ")          # matched
k = re.search(".", "\n")            # failed (end of line char)

print a
print b
print c
print d
print e
print f
print g
print h
print i
print j
print k