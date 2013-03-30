import csv
import sqlite3

conn = sqlite3.connect("students.db")
try: 
    conn.execute("drop table schools")
    conn.execute("drop table students")
except sqlite3.OperationalError, e:
    print e.message


sql = "PRAGMA foreign_keys = 1"
conn.execute(sql)

sql = """CREATE TABLE schools 
    (id INTEGER PRIMARY KEY, 
     dirname TEXT NOT NULL, 
     school TEXT NOT NULL, 
     school_desc TEXT NOT NULL, 
     diremail TEXT NOT NULL)"""
conn.execute(sql)

sql = """CREATE TABLE students 
    (id INTEGER PRIMARY KEY, 
     name TEXT NOT NULL, 
     student_id TEXT NOT NULL, 
     email TEXT NOT NULL, 
     school_id INTEGER NOT NULL REFERENCES schools, 
     gender CHAR NOT NULL, 
     gpa FLOAT NOT NULL, 
     address TEXT NOT NULL)"""
conn.execute(sql)

studentreader = csv.reader(open("studentsp13.csv"))
schoolreader = csv.reader(open("schools.csv"))
# remove the title
studentreader.next()
schoolreader.next()

school_pk = {}

for data in schoolreader:
    sql = """INSERT INTO schools (dirname, school, school_desc, diremail) 
           VALUES ('%s', '%s', '%s', '%s')""" % (data[0], data[1], data[2], data[3])
    cursor = conn.execute(sql)
    # map (and cache) the school's ID with the school name
    school_pk[ data[1] ] = cursor.lastrowid

conn.commit()

for data in studentreader:
    sql = """INSERT INTO students 
             (name, student_id, email, school_id, gender, gpa, address) 
             VALUES ('%s', '%s', '%s', %d, '%s', %f, '%s')""" % (data[0], data[1], 
             data[2], school_pk[data[3]], data[4], float(data[5]), data[6])
    cursor = conn.execute(sql)

conn.commit()

sql = """SELECT students.*, schools.school
         FROM students, schools 
         WHERE gpa >= 3.50 AND students.school_id = schools.id 
            AND schools.school = 'SIT'
         ORDER BY schools.school, students.gpa DESC
      """

cursor = conn.execute(sql)
data = cursor.fetchall()
print "TASK1: Total students with GPA >= 3.5:", len(data)

sql = """SELECT count(*) 
         FROM students, schools
         WHERE gender = 'F' AND students.school_id = schools.id
            AND schools.school = 'SIT'
      """
cursor = conn.execute(sql)
data = cursor.fetchall()
print "TASK2: Total female students in SIT:", data[0][0]

sql = """SELECT count(*) 
         FROM students, schools
         WHERE gender = 'M' AND students.school_id = schools.id
            AND schools.school = 'SIT'
      """
cursor = conn.execute(sql)
data = cursor.fetchall()
print "TASK2: Total male students in SIT:", data[0][0]

# Long and complicated SQL to find min
sql = """SELECT students.name
         FROM students, schools
         WHERE schools.school = 'SIT' AND students.school_id = schools.id
          AND students.gpa = (
            SELECT max(gpa) FROM students, schools WHERE
            schools.school = 'SIT' AND students.school_id = schools.id )
      """

# Other method is to query all SIT students, and order them based on GPA
# Get either the first or the last for min or max GPA
sql = """SELECT students.name, students.gpa
         FROM students, schools
         WHERE schools.school = 'SIT' AND students.school_id = schools.id
            ORDER BY students.gpa
      """

cursor = conn.execute(sql)
data = cursor.fetchall()
print "TASK3: Lowest GPA in SIT:", data[0][0], data[0][1]
print "TASK3: Highest GPA in SIT:", data[len(data) - 1][0], data[len(data) - 1][1]

sql = """SELECT avg(gpa)
         FROM students, schools
         WHERE schools.school = 'SIT' AND students.school_id = schools.id
      """
cursor = conn.execute(sql)
data = cursor.fetchall()
print "TASK4: Average GPA in SIT", data[0][0]



#  vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
