import os
from lxml import etree

doc = open(os.getcwd() + "/data.xml")
Tree = etree.parse(doc)


r = Tree.xpath("count(//student[gender = 'F'])")
print "Total female students:", int(r)

r = Tree.xpath("count(//student[gender = 'M'])")
print "Total male students:", int (r)

print "---"

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

    total_male = Tree.xpath("count(/polytechnic/school[name='" + school + "']/student[gender = 'M'])")
    total_female = Tree.xpath("count(/polytechnic/school[name='" + school + "']/student[gender = 'F'])")

    print "Total", school, "students:", int(total_male + total_female), "with", int(total_male), "male students,", int(total_female), "female students"

    print "---"

# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4