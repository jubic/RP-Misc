"""
h2. Get the Keys from Values

A dictionary has name as key and age as value that looks like the following: @{"joe":30, "don":25, "mary":29, "roger":42}@. Write a function @getNames@ that takes such dictionary, and return a list of "names" that have their corresponding "age" less than or equal to 30. 

bc. {- python -}
getNames({"joe":30, "don":25, "mary":29, "roger":42})
# returns ["joe", "don", "mary"]
"""

def getNames(d):
	l = []
	for (k,v) in d.items():
		if v <= 30:
			l.append(k)	
	return l

if __name__ == "__main__":
	print getNames({"joe":30, "don":25, "mary":29, "roger":42})
