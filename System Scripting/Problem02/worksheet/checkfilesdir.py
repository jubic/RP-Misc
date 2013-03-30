import os
#
for entry in os.listdir("."):
    if os.path.isdir(entry):     # is it a directory?
        print "d", entry
    elif os.path.isfile(entry):  # is it a file?
        print "-", entry