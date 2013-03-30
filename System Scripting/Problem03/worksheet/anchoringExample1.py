import re
date1 = "9922 October 201020000"
#
a = re.search("\d{1,2}\s+[A-Z][a-z]+\s+\d{4}", date1) # matched

print a