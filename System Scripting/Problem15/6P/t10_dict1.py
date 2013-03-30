"""
h2. Dictionary Values to String

Write a function @getVals@ that takes a dictionary as an argument. Get all the values from the dictionary, sort them, and return them as a string with each value enclosed in a &lt;> bracket.

bc. {- python -}
d = {"x":"y", "a":"b", "g":"h"}
print getVals(d)   
# returns <b><h><y> (sorted alphabetically)
"""

def getVals(d):
	# you code below
	v = d.values()
	v.sort()
	s = ""
	for i in v:
		s += "<%s>" % i	
	return s

if __name__ == '__main__':
	print getVals({"a":"b", "c":"d"})
