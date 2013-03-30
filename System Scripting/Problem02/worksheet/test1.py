# Open and write, but no close
write_file = open("test1.txt", "wb")
write_file.write("one\r\n")
write_file.write("two\r\n")
# Close the file first
write_file.close()  # data is written to storage
#
# Open the same file for reading
read_file = open("test1.txt", "rb")
data = read_file.read()
print data