import os
from lxml import etree

f = open("home.xml")
tree = etree.parse(f)

# Count the number of "<space>" node element
result = tree.xpath("count(//space)")
print "Total number of <space> node element:", int(result)

print "------"

# Get all the <name> node element that's the children of <space>, which is one of the children of <home>
result = tree.xpath("/home/space/name")
print "List of element objects that match the XPath expression:"
print result

print "------"

# To see the value of the returned element objects above
for item in result:
    print item.tag, "=>", item.text

print "------"

# You'd like to list down all the <space> contents.
result = tree.xpath("//space")
for item in result:
    print "Space:", item.attrib["id"]
    for node in item.iterchildren():
        print " *", node.tag, "=>", node.text

print "------"

# Count bed equal to 0
result = tree.xpath("count(//space[bed='0'])")
print "Total number of <space> node elements that has <bed> value equal to 0:", int(result)

print "------"

# Node with bed = 0, and chair = 4
result = tree.xpath("//space[bed='0' and chair='4']")
for item in result:
    print "Space:", item.attrib["id"]
    for node in item.iterchildren():
        print " *", node.tag, "=>", node.text