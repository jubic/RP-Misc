import sqlite3
import csv
# Connect to database, if it does not exist, it will create it.
conn = sqlite3.connect("nopoly.db")
# Creating table.
conn.execute("PRAGMA foreign_keys = 1")
conn.execute("CREATE TABLE schools (id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT NOT NULL, director TEXT NOT NULL, email TEXT NOT NULL)")
conn.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT NOT NULL, student_id TEXT NOT NULL, email TEXT NOT NULL, school TEXT NOT NULL REFERENCES schools, gender TEXT NOT NULL, gpa TEXT NOT NULL, address TEXT NOT NULL)")
# Opening the csv files
schoolreader = csv.reader(open("files/schools.csv"))
studentreader = csv.reader(open("files/studentsp13.csv"))
# Skip the headers
schoolreader.next()
studentreader.next()
# Extract each row, print, insert into database
for data in schoolreader:
    print data
    sql = """INSERT INTO schools (name, description, director, email) VALUES ('%s','%s','%s','%s')"""%(data[0],data[1],data[2],data[3])
    print "DEBUG", sql
    conn.execute(sql)
for data in studentreader:
    print data
    sql = """INSERT INTO students(name, student_id, email, school, gender, gpa, address) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"""%(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    print "DEBUG", sql
    conn.execute(sql)
#
conn.commit()