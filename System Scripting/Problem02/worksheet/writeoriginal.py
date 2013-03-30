# Open the file for reading. It's an error if the file doesn't exist.
x = open("original.html", "rb")
# Read the file as a single string
data = x.read()
print data

# Open the file for writing. The previous content is deleted.
y = open("copy.html", "wb")
# Write the list to file
y.write(data)
# Close it to ensure the file is written to the storage (disk)
y.close()