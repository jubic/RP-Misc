"""
h2. Putting Data into SQLite Database

Write a function @putData@ that takes 4 arguments as specified below:

# @dbname@ - a string that specifies the location of the database name 
# @fnames@ - the list of first names 
# @lnames@ - the list of last names corresponding to the first names list
# @ages@ - the list of the age corresponding to each name in the first name and last name lists 

Insert those lists into a table named @people@ in a database with name that is in the first argument. The table must have the following columns "firstname", "lastname", and "age". It also must have a primary key of auto incrementing integer.

The function needs not return anything. See the example below:

bc. {- python -}
putData("tmp/test.db", ["Bob", "John"], ["Lim", "Tan"], [45, 32])

@testall.pyc@ will check the database that's created by @putData@ directly.
"""

import sqlite3

def putData(dbname, fnames, lnames, ages):
	conn = sqlite3.connect(dbname)
	sql = "CREATE TABLE people (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, age INTEGER)"
	# print sql
	conn.execute(sql)

	for i in range(len(fnames)):
		# sql = "INSERT INTO people (firstname, lastname, age) VALUES ('%s', '%s', %d)" % (fnames[i], lnames[i], ages[i])
		sql = "INSERT INTO people (firstname, lastname, age) VALUES ('%s', '%s', %d)" % (fnames[i], lnames[i], ages[i])
		# print sql
		conn.execute(sql)

	conn.commit()

if __name__ == '__main__':
	print putData("tmp/names.db", ["John", "Paul", "George", "Ringo"], ["Lennon", "McCartney", "Harrison", "Star"], [25, 26, 27, 28])
