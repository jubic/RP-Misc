import os
from lxml import etree

doc = open(os.getcwd() + "/data.xml")
Tree = etree.parse(doc)

r = Tree.xpath("count(//student)")
print "Total:", int(r)

r = Tree.xpath("count(//student[gender = 'F'])")
print "Total female students:", int(r)

r = Tree.xpath("count(//student[gender = 'M'])")
print "Total male students:", int (r)

for school in ["SIT", "STA", "SEG", "SHL", "SOH"]:
    total_male = Tree.xpath("count(/polytechnic/school[name='" + school + "']/student[gender = 'M'])")
    total_female = Tree.xpath("count(/polytechnic/school[name='" + school + "']/student[gender = 'F'])")

    print "Total", school, "students:", int(total_male + total_female), "with", int(total_male), "male students,", int(total_female), "female students"

# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
