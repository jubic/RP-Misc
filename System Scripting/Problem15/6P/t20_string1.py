"""
h2. First and Last Strings

Create a function name @getFirstLast@ that takes a string consisting of fields separated by a colon ":". Example: @"one:two:three:four:five"@. The function must return the first and the last field as a list. 

Given the string in the example, the function should return the list @['one', 'five']@.
"""

# your code here
def getFirstLast(s):
	l = s.split(":")
	return [ l[0], l[ len(l) - 1 ] ]

if __name__ == "__main__":
	print getFirstLast("aa:bb:cc:dd:ee")
