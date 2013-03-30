import csv
import sys

Schools = ("SIT", "STA", "SEG", "SOH", "SHL")

# same as solution simple, except it has "tabnum" which tells how many tabs (indentations)
# a particular group should have. 
def xmlwriter(f, school, tabnum=0):
    school_columns = ("director","name", "description", "email")
    school_data = csv.reader(open("schools.csv"))
    student_columns = ("name", "sid", "email", "school-name", "gpa", "address")
    student_data = csv.reader(open("students.csv"))
    
    has_school = False

    for row in school_data:
        if row[1] != school:
            has_school = True
            continue
        # level one indent, as <school> is the beginning of the group
        f.write("\t" * tabnum + "<school>\r\n")
        for idx in range(len(row)):
            # level two indent - indented by one from <school>
            f.write( "\t" * (tabnum + 1) + "<%s>%s</%s>\n" % (school_columns[idx], row[idx], school_columns[idx]))

    for row in student_data:
        if row[3] != school:
            continue
        # level two indent - <student> is in the same indentation as the school's information
        f.write("\t" * (tabnum + 1) + "<student>\r\n")
        for idx in range(len(row)):
            if student_columns[idx] == "school":
                continue
            # level 3 indent for student's data
            f.write( "\t" * (tabnum + 2) + "<%s>%s</%s>\n" % (student_columns[idx], row[idx], student_columns[idx]))
        f.write("\t" * (tabnum + 1) + "</student>\r\n")

    if has_school:
        f.write("\t" * tabnum + "</school>\r\n")

f = sys.stdout
f.flush()

f.write('<?xml version="1.0" encoding="utf-8" ?>\r\n')
f.write('<polytechnic>\r\n')
for school in Schools:
    xmlwriter(sys.stdout, school, 1)
f.write('</polytechnic>\r\n')

# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4