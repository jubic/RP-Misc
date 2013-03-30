"""
h2. Count the Occurence in a List

Write a function @countInList@ that takes two list of integers. The first list is longer. And the second list is shorter. The function is to *count* how many integers from the first list that are in the second list.

Here's an example:

bc. {- python -}
print countInList([1,2,3,4,5], [3,2,10])
# print 2 - number 2 and 3 in the first list are in the second list
# 
print countInList([1,2,3,4,5], [6,10])
# print 0 - none of the number in the first list is in the second list

Hint: you can use Python's @in@ to check if an item is in a list.

bc. {- python -}
if 5 in [4,5,6]:
	print "Found"
# prints "Found"
"""
list1 = [1, 2, 3, 4, 5]
list2 = [3, 2, 10]
list3 = [6,10]

# Write your function below here:
def countInList(l1, l2):
    i=0
    for item in l1:
        if item in l2:
            i= i+1
    return i

if __name__ == "__main__":
    print countInList(list1, list2)
