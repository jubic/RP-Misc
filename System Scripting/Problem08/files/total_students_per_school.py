import os
from lxml import etree

doc = open(os.getcwd() + "/data.xml")
Tree = etree.parse(doc)

Schools = ["SIT", "STA", "SEG", "SHL", "SOH"]

for school in Schools:
    total_male = Tree.xpath("count(//school[name='"+school+"']/student[gender='M'])")
    total_female = Tree.xpath("count(//school[name='"+school+"']/student[gender='F'])")

    print "Total", school, "students:", int(total_male + total_female), "with", int(total_male), "male students,", int(total_female), "female students"

# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
