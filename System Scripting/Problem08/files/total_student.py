import os
from lxml import etree

doc = open(os.getcwd() + "/data.xml")
Tree = etree.parse(doc)

# Count the total number of students
result = Tree.xpath("count(//student)")
print "Total number of students in the school:", int(result)

# Count the total number of female students
result = Tree.xpath("count(//student[gender='F'])")
print "Total number of female students in the school:", int(result)

# Count the total number of male students
result = Tree.xpath("count(//student[gender='M'])")
print "Total number of male students in the school:", int(result)