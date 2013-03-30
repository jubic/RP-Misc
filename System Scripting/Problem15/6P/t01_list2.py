"""
h2. Add Two Lists

Write a function called @add2list@s that takes 2 arguments. 

Both arguments are lists of integers. The function should add each item of the first list to each item in the second list (the first item in list 1, with the first item in list 2) and store the result in list 3. Return list 3 from the function.

bc. {- python -}
list1 = [1,2,3] 
list2 = [4,5,6]
# result should be [5,7,9]
"""

def add2lists(l1, l2):
	# your code here
	result = []
	for i in range(len(l1)):
		result.append(l1[i] + l2[i])
	return result

if __name__ == "__main__":
	print add2lists([1,2], [3,4])
