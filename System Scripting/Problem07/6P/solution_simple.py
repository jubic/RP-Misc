import csv
import sys

Schools = ("SIT", "STA", "SEG", "SOH", "SHL")

# Arguments:
# f: the file object. Use it later as f.write()
# school: is the school name "SIT", "STA", etc. Only prints data based on school
def xmlwriter(f, school):
    # name all of the columns for schools.csv (the CSV file doesn't name the columns)
    school_columns = ("director","name", "description", "email")
    # read the csv file
    school_data = csv.reader(open("schools.csv"))

    # name all of the columns for students.csv
    student_columns = ("name", "sid", "email", "school-name", "gpa", "address")
    # read the csv file
    student_data = csv.reader(open("students.csv"))
    
    for row in school_data:
        # if the school_data is not equal the requested school in the argument (see above), ignore it
        if row[1] != school:
            continue
        # print the <school> opening tag
        f.write("<school>\r\n")
        # print the school information
        for idx in range(len(row)):
            # write the tag in the form of <tagname>Value</tagname>
            # where "tagname" is the column's name, and its associated value from the CSV file
            f.write("<%s>%s</%s>\n" % (school_columns[idx], row[idx], school_columns[idx]))

    for row in student_data:
        # Ignore student data that doesn't match the requested school
        if row[3] != school:
            continue
        f.write("<student>\r\n")
        # Prints the student information within the "student" tag
        for idx in range(len(row)):
            f.write("<%s>%s</%s>\n" % (student_columns[idx], row[idx], student_columns[idx]))
        f.write("</student>\r\n")

    # Close the "school" tag
    f.write("</school>\r\n")

# Printes to standard output (console). You can replace this by opeing a file
# f = open("output.xml", "wb")
f = sys.stdout
f.flush()

# print the prolog
f.write('<?xml version="1.0" encoding="utf-8" ?>\r\n')
# print the root tag <polytechnic> to enclose the entire "schools" and "students"
f.write('<polytechnic>\r\n')
# for each school, write the XML for school and its students
for school in Schools:
    xmlwriter(sys.stdout, school)
# close the root tag
f.write('</polytechnic>\r\n')

# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4