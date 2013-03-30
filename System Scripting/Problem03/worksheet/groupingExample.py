import re
s = "title: Fixing Windows printer"
m = re.search("^title: (\w+)", s)
print m.groups()  # output: ('Fixing',)
m = re.search("^title: (\w+) (\w+)", s)
print m.groups()  # output: ('Fixing', 'Windows')
print m.group(1)  # output: Fixing
print m.group(2)  # output: Windows