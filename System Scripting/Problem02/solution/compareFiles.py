import time

import os

#
os.chdir("../files/published")
# Check which directory you're currently in
print os.getcwd()

for entry in os.listdir("."):
    print "-", entry

path = "C:/SS/Problem02/src/files"

while True:
    for file in os.listdir(path + "/master"):
	masterpath = path + "/master/" + file
	if os.path.isfile(masterpath):
            f1 = open(masterpath, "rb")
            data = f1.read()
            f1.close()

            publishpath = path + "/published/" + file
            f2 = open(publishpath, "rb")
            data2 = f2.read()
            f2.close()

            if data == data2:
                print "Both files " + "(" + file + ")" + " from the two different directories are the same"

            else:
                j = open(publishpath, "wb")
                j.write(data)
                j.close()
                print file + "has been change to look like the one in the master directory"
    print ""
    time.sleep(60)