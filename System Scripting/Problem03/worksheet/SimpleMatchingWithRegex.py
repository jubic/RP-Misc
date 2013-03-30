import re
a = re.search("\d", "I need to buy 3 watermelons")
b = re.search("\d", "1 apple a day keeps the doctor away")
c = re.search("\d", "One apple a day keeps the doctor away")

if a:
    print "FOUND"
else:
    print "NOT FOUND"

if b:
    print "FOUND"
else:
    print "NOT FOUND"

if c:
    print "FOUND"
else:
    print "NOT FOUND"