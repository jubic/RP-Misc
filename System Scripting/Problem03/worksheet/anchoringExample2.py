import re
date_good = "22 October 2010"
date_bad  = "9922 October 201020000"
#
# Note the ^ and $ - match the pattern from the beginning of the string
# until the end of the string. Or in short, match the pattern for
# the entire string.
a = re.search("^\d{1,2}\s+[A-Z][a-z]+\s+\d{4}$", date_good) # matched
b = re.search("^\d{1,2}\s+[A-Z][a-z]+\s+\d{4}$", date_bad)  # failed

print a
print b