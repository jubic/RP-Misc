import re
s = "title: Fixing Windows printer"
p = re.sub("^(title:) ", "", s)
print p   # output: Fixing Windows printer