"""
h2. Query with Criteria

Given the database "weather.db":tmp/weather.db (use *sqlite3.exe* to see the schema), write a Python function @getInfoByRegion@ that takes the database name and a region, and return the result of the query.

The return value is the output from the @fetchall()@ function call.
"""

import sqlite3

# Complete the function below
def getInfoByRegion(dbname, region):
	conn = sqlite3.connect(dbname)
	query = conn.execute("SELECT * FROM weather WHERE region='"+region+"'")
	fetchquery = query.fetchall()
	return fetchquery

if __name__ == '__main__':
	data = getInfoByRegion('tmp/weather.db', "East Asia")
	print data
