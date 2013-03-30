"""
h2. String that Starts with Digit

Write a function @startsWithDigit@ that take a list of strings. If a string item from the list starts with two or more digits, then put them in a list which shall be returned by the function later. 

Example, for a given list @["a1", "1a", "22a", "333aa"]@, the function should return @["22a", "333aa"]@.

*Hint:* use Regular Expression. See P03.
"""

import re
lst = ["a12233", "113a", "22a", "333aa"]
def startsWithDigit(lst):
        newlist = []
        for x in range(len(lst)):
                m = re.search("^\d\d",lst[x])
                if m:
                        newlist.append(str(lst[x]))
        return newlist
        

# your your function below

if __name__ == "__main__":
	print startsWithDigit(lst)
	

