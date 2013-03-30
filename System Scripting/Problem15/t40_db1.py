"""
h2. Putting Data into SQLite Database

Write a function @putData@ that takes 4 arguments as specified below:

# @dbname@ - a string that specifies the location of the database name 
# @fnames@ - the list of first names 
# @lnames@ - the list of last names corresponding to the first names list
# @ages@ - the list of the age corresponding to each name in the first name and last name lists 

Insert those lists into a table named @people@ in a database with name that is in the first argument. The function needs not return anything. See the example below:

bc. {- python -}
putData("tmp/test.db", ["Bob", "John"], ["Lim", "Tan"], [45, 32])

@testall.pyc@ will check the database that's created by @putData@ directly.
"""

import sqlite3

# Complete the function below
def putData(dbname, fnames, lnames, ages):
        conn = sqlite3.connect(dbname)
        #conn.execute("drop table people")
        conn.execute("CREATE TABLE people (id INTEGER PRIMARY KEY, fnames TEXT, lnames TEXT, ages INTEGER)")
        for x in range(len(fnames)):
                #age = ", "+ str(ages[x])
                conn.execute("INSERT INTO people (fnames, lnames, ages) VALUES ('"+fnames[x]+"', '"+lnames[x]+"', "+str(ages[x])+")")
                #print "INSERT INTO people (firstname, lastname, age) VALUES ('"+fnames[x]+"', '"+lnames[x]+"', "+str(ages[x])+")"
        conn.commit()

if __name__ == '__main__':
        putData("tmp/names.db", ["John", "Paul", "George", "Ringo"], ["Lennon", "McCartney", "Harrison", "Star"], [25, 26, 27, 28])
