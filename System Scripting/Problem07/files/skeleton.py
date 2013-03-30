import csv
import sys

Schools = ("SIT", "STA", "SEG", "SOH", "SHL")

# Arguments:
# f: the file object. Use it later as f.write()
# school: is the school name "SIT", "STA", etc. Only prints data based on school
def xmlwriter(f, school):
    school_columns = ("director","name", "description", "email")
    f1 = open("schools.csv")
    school_data = csv.reader(f1)

    student_columns = ("name", "sid", "email", "school", "gpa", "address")
    f2 = open("students.csv")
    student_data = csv.reader(f2)
    f.write("<school>\r\n")
    
    for row in school_data:
        if row[1] == school:
            f.write("\t<director>" + row[0] + "</director>\r\n")
            f.write("\t<school-name>" + row[1] + "</school-name>\r\n")
            f.write("\t<description>" + row[2] + "</description>\r\n")
            f.write("\t<email>" + row[3] + "</email>\r\n")

        for row in student_data:
            if row[3] == school:
                f.write("\t<student>\r\n")
                f.write("\t\t<name>" + row[0] + "</name>\r\n")
                f.write("\t\t<sid>" + row[1] + "</sid>\r\n")
                f.write("\t\t<email>" + row[2] + "</email>\r\n")
                f.write("\t\t<school-name>" + row[3] + "</school-name>\r\n")
                f.write("\t\t<gpa>" + row[4] + "</gpa>\r\n")
                f.write("\t\t<address>" + row[5] + "</address>\r\n")
                f.write("\t</student>\r\n")

    f.write("</school>\r\n")

# Printes to standard output (console). You can replace this by opeing a file
f = open("nopoly.xml", "wb")
# f = sys.stdout
# f.flush()

f.write('<?xml version="1.0" encoding="utf-8" ?>\r\n')
f.write('<polytechnic>\r\n')
for school in Schools:
    xmlwriter(f, school)
f.write('</polytechnic>\r\n')

# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4