# Open the file for appending. If the file doesn't exist, it'll get created.
# If the file exists, the write position will start from the end of the file.
f = open("testappend.txt", "ab")
f.write("one\r\n")
f.write("two\r\n")
f.close()
#
f = open("testappend.txt", "ab")
f.write("three\r\n")
f.write("four\r\n")
f.close()
#
# Open for reading.
f = open("testappend.txt", "rb")
data = f.read()
print data