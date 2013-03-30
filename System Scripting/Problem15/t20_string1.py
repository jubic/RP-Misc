"""
h2. First and Last Strings

Create a function name @getFirstLast@ that takes a string consisting of fields separated by a colon ":". Example: @"one:two:three:four:five"@. The function must return the first and the last field as a list. 

Given the string in the example, the function should return the list @['one', 'five']@.
"""

# Write your function below
string = "one:two:three:four:five"
def getFirstLast(string):
    string = string.split(':')
    result = []
    result.append(string[0])
    result.append(string[len(string)-1])
    return result
    

if __name__ == "__main__":
    print getFirstLast(string)
