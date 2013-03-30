import re
# The "?" quantifier
a = re.search("\d?", "Age 20")  # matched
b = re.search("\d?", "Age 2")   # matched
c = re.search("\d?", "Age two") # matched (0 or 1 match)
#
# The "*" quantifier
d = re.search("\d*", "Age 20")  # matched
e = re.search("\d*", "Age two") # matched (0 or more matches)
#
# The "+" quantifier
f = re.search("\d+", "Age 20")  # matched
g = re.search("\d+", "Age two") # failed (1 or more matches)
#
# The {M,N} quantifier
h = re.search("\d{2}",   "Age 20")   # matched
i = re.search("\d{2}",   "Age 5")    # failed
j = re.search("\d{2,}",  "91234567") # matched
k = re.search("\d{2,}",  "Age 5")    # failed
l = re.search("\d{2,4}", "Age 20")   # matched
m = re.search("\d{2,4}", "91234567") # matched
n = re.search("\d{2,4}", "Age 5")    # failed

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
print l
print m
print n