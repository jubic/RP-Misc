"""
h2. First Character of a String

Write a function @getFirstChars@ that takes a list of strings. The function must return a string that consists of all of the first characters. 

Example: given the list @["one", "two", "six" "ten"]@, the function must return the string: @otst@ (all of the first characters of each string in the list).
"""
list = ["one", "two", "six", "ten"]

def getFirstChars(list):
    result = ''
    for item in list:
        result += item[0]
    return result

if __name__ == "__main__":
    print getFirstChars(list)
