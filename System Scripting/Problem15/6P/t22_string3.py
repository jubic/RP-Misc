"""
h2. String that Starts with Digit

Write a function @startsWithDigit@ that take a list of strings. If a string item from the list starts with two or more digits, then put them in a list which shall be returned by the function later. 

Example, for a given list @["a1", "1a", "22a", "333aa"]@, the function should return @["22a", "333aa"]@.

*Hint:* use Regular Expression. See P03.
"""

import re

# your code starts here
def startsWithDigit(l):
	results = []
	for i in l:
	   if re.search("^\d{2,}", i):
	   	results.append(i)
	return results

if __name__ == "__main__":
	print startsWithDigit(["a1", "1a", "22a", "333aa"])
	

