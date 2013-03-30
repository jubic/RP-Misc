import re

good1 = "title: Fixing Windows printer"
good2 = "    title: Fixing Windows printer"

bad1 = "Note - title: Fixing Windows printer"
bad2 = "    * title: Fixing Windows printer"

a = re.search("^title",good1)
b = re.search("^\s+title",good2)
c = re.search("^title",bad1)
d = re.search("^\s+.title",bad2)

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

if d:
    print "FOUND"
else:
    print "NOT FOUND"