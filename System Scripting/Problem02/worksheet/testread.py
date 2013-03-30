# Open the file for reading. It's an error if the file doesn't exist.
f = open("testread.txt", "rb")
# Read the file as a single string
data = f.read()
print data