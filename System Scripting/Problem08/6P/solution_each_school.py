import os
from lxml import etree

doc = open(os.getcwd() + "/data.xml")
Tree = etree.parse(doc)

for school in ["SIT", "STA", "SEG", "SHL", "SOH"]:
    r = Tree.xpath("/polytechnic/school[name='" + school + "']/director")
    print "* School:", school 
    print "* Director:", r[0].text
       
    print "=== Male students with GPA >= 3.5"
    r = Tree.xpath("/polytechnic/school[name='" + school + "']/student[gpa >= 3.5 and gender='M']")
    for item in r:
        print "\t*",
        for node in item.iterchildren():
           print node.text, ":",
        print
     
    print "=== Female students with GPA >= 3.5"
    r = Tree.xpath("/polytechnic/school[name='" + school + "']/student[gpa >= 3.5 and gender='F']")
    for item in r:
        print "\t*",
        for node in item.iterchildren():
           print node.text, ":",
        print

    print "=== Male students with GPA < 2.0"
    r = Tree.xpath("/polytechnic/school[name='" + school + "']/student[gpa < 2.0 and gender='M']")
    for item in r:
        print "\t*",
        for node in item.iterchildren():
           print node.text, ":",
        print
 
    print "=== Female students with GPA < 2.0"
    r = Tree.xpath("/polytechnic/school[name='" + school + "']/student[gpa < 2.0 and gender='F']")
    for item in r:
        print "\t*",
        for node in item.iterchildren():
           print node.text, ":",
        print

    print "---"
# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
