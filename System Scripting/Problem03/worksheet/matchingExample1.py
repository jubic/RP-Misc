import re
a = re.search("Python", "This module is using Python programming language")
#
# But below will fail due to case sensitivity
b = re.search("Python", "There's a python in the garden")
#
# Matching regardless of the upper/lower cases, use "re.IGNORECASE" modifier
c = re.search("Python", "There's a python in the garden", re.IGNORECASE)

print a
print b
print c