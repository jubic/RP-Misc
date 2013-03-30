"""
h2. First Character of a String

Write a function @getFirstChars@ that takes a list of strings. The function must return a string that consists of all of the first characters. 

Example: given the list @["one", "two", "six" "ten"]@, the function must return the string: @otst@ (all of the first characters of each string in the list).
"""

# your code here
def getFirstChars(l):
	s = ""
	for i in l:
		s += i[0]
	return s

if __name__ == "__main__":
	print getFirstChars(["pete", "tom", "joe", "ray"])
	
