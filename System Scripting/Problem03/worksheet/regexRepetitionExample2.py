import re
date1 = "22 October 2010" # (month is capitalized)
date2 = "2 October 2010"  # (single date is correct also)
date3 = "2 10 2010"
date4 = "22    October    2010"
#
a = re.search("\d{1,2}\s+[A-Z][a-z]+\s+\d{4}", date1) # matched
b = re.search("\d{1,2}\s+[A-Z][a-z]+\s+\d{4}", date2) # matched
c = re.search("\d{1,2}\s+[A-Z][a-z]+\s+\d{4}", date3) # failed
d = re.search("\d{1,2}\s+[A-Z][a-z]+\s+\d{4}", date4) # matched

print a
print b
print c
print d