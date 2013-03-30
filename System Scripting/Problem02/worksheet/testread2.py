f = open("testread.txt", "rb")
data = f.readlines()  # data is ['one\r\n','two\r\n']
print data
#
for line in data:
    print line