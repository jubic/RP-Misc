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

print "----------------------------------------------------------"

Schools = ["SIT", "STA", "SEG", "SHL", "SOH"]

for school in Schools:
    total_male = Tree.xpath("count(//school[name='"+school+"']/student[gender='M'])")
    total_female = Tree.xpath("count(//school[name='"+school+"']/student[gender='F'])")

    print "Total", school, "students:", int(total_male + total_female), "with", int(total_male), "male students,", int(total_female), "female students"

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