# Open the file for writing. The previous content is deleted.
f = open("testwrite.txt", "wb")
data = ["one\r\n", "two\r\n"]
# Write the list to file
f.writelines(data)
# Close it to ensure the file is written to the storage (disk)
f.close()