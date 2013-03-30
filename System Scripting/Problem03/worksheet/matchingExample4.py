import re
a = re.search("[^0-2]", "2010") # failed
b = re.search("[^0-2]", "1997") # matched

print a
print b