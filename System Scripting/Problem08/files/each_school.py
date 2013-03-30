import os
from lxml import etree

doc = open(os.getcwd() + "/data.xml")
Tree = etree.parse(doc)

Schools =  ["SIT", "STA", "SEG", "SHL", "SOH"]

# for each school
for school in Schools:
    # Get the school director
    r = Tree.xpath("//school[name='"+school+"']/director")
    print "* School:", school 
    print "* Director:", r[0].text
       
    print "=== Male students with GPA >= 3.5"
    r = Tree.xpath("//school[name='"+school+"']/student[gender='M' and gpa >= 3.5]")
    for item in r:
        print "\t*",
        for node in item.iterchildren():
           print node.text, ":",
        print
     
    print "=== Female students with GPA >= 3.5"
    r = Tree.xpath("//school[name='"+school+"']/student[gender='F' and gpa >= 3.5]")
    for item in r:
        print "\t*",
        for node in item.iterchildren():
           print node.text, ":",
        print

    print "=== Male students with GPA < 2.0"
    r = Tree.xpath("//school[name='"+school+"']/student[gender='M' and gpa < 2.0]")
    for item in r:
        print "\t*",
        for node in item.iterchildren():
           print node.text, ":",
        print
 
    print "=== Female students with GPA < 2.0"
    r = Tree.xpath("//school[name='"+school+"']/student[gender='F' and gpa < 2.0]")
    for item in r:
        print "\t*",
        for node in item.iterchildren():
           print node.text, ":",
        print

    print "---"
# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4