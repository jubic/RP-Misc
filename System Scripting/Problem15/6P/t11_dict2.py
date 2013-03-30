"""
h2. Dictionary with List Values

Given the dictionary @{'age': [19,20,17,23], 'gpa':[3.5,4.0,3.1,2.3]}@. Write a function @getAve@ that takes that dictinary. Make the function calculate both the average age and average gpa, and return them as a list (average age as first item in the list, then followed by average gpa).

*Note* that your function should work not just with the above values. It should work with different values as well.

bc. {- python -}
getAve({'age': [19,20,17,23], 'gpa':[3.5,4.0,3.1,2.3]}) 
# result [19.75, 3.225]
"""

def getAve(d):
	# Your code below
	age = d['age'] #.values()
	gpa = d['gpa'] # .values()
	aveage = sum(age) / float(len(age))
	avegpa = sum(gpa) / float(len(gpa))

	return [aveage, avegpa]

if __name__ == '__main__':
	print getAve({'age': [19,20,17,23], 'gpa':[3.5,4.0,3.1,2.3]})
