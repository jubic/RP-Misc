"""
h2. Dictionary Values to String

Write a function @getVals@ that takes a dictionary as an argument. Get all the values from the dictionary, sort them, and return them as a string with each value enclosed in a &lt;> bracket.

bc. {- python -}
"""
d = {"x":"y", "a":"b", "g":"h"}
"""
print getVals(d)   
# returns <x><h><y> (sorted alphabetically)
"""

# Write your function below
def getVals(list):
    dataList = []
    for item in list:
        dataList.append(list[item])
    dataList.sort()
    data = ''
    for item in dataList:
        data += '<'+item+'>'
    return data

if __name__ == '__main__':
	print getVals(d)
