"""
h2. Zip Two Lists into One

Write a function @zipper@ that takes 2 arguments.

Both arguments are lists of integers. The function must then create a new list to put the first item of the first list, followed by the first item of the second list. Then second item of the first list, followed by the second item in the second list.

Check the example below:

bc. {- python -}
"""
a = [1,2,3]
b = [4,5,6]
# After running zipper(a, b), you'll get [1,4,2,5,3,6]

def zipper(l1, l2):
    result = []
    i=0
    for item in l1:
        result.append(item)
        result.append(l2[i])
        i = i+1
    return result

if __name__ == "__main__":
	print zipper(a, b)
