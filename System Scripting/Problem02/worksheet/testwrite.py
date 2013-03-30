# Open file for writing. It'll be created if it doesn't exist.
f = open("testwrite.txt", "wb")
# Write to the file "one" and "two" on separate lines
f.write("one\r\n")
f.write("two\r\n")
# Close the file to ensure content is written to the storage
f.close()