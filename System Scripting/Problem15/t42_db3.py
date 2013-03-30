"""
h2. Query with Aggregate Function

Given the database "weather.db":tmp/weather.db (use *sqlite3.exe* to see the schema), write a Python function @getAveTempByRegion@ that takes the database name and a region as its arguments, and return the average temperature for a particular region.

The function must return a float (not a list).
"""

import sqlite3

# Complete the function below
def getAveTempByRegion(dbname, region):
	conn = sqlite3.connect(dbname)
        cursor = conn.execute("SELECT avg(temperature) FROM weather WHERE region ='"+region+"'")

        data = cursor.fetchall()
        return data[0][0]

if __name__ == '__main__':
	data = getAveTempByRegion('tmp/weather.db', "East Asia")
        print data