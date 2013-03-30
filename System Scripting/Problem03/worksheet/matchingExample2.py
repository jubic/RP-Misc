import re
# below, match a string againts character "4" and "x"
a = re.search("[4x]", "It's 4PM")     # matched
b = re.search("[4x]", "5x5 is 25")    # matched
c = re.search("[4x]", "It's 6PM")     # failed

print a
print b
print c