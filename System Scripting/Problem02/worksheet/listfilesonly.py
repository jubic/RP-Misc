import os
#
# Change to "C:\Python27" directory.
os.chdir("C:/Python27")
# Check which directory you're currently in
print os.getcwd()   # prints C:\\Python27

for entry in os.listdir("."):
    if os.path.isfile(entry):  # is it a file?
        print "-", entry