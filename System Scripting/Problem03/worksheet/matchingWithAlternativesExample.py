import re
a = re.search("Linux|FreeBSD|MacOSX", "My laptop runs Linux OS")     # matched
b = re.search("Linux|FreeBSD|MacOSX", "My laptop runs Windows only") # failed
c = re.search("Linux|FreeBSD|MacOSX", "Here's linux ") # failed (case not matched)
d = re.search("Linux|FreeBSD|MacOSX", "Here's linux ", re.IGNORECASE) # matched

print a
print b
print c
print d