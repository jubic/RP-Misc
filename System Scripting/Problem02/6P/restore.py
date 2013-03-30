import os.path
import os
import filecmp
import time

MASTER = "master"
TARGET = "published"
MEDIA  = "images"

# Simple file copy function written from scratch.
# You can use "shutil" module with "copy" function: http://www.python.org/doc//current/library/shutil.html?highlight=shutil#shutil.copy
def copyfile(source, destination):
    source_file = open(source, "rb")
    # open the target file for writing, if the file doesn't exist, create it
    destination_file = open(destination, "wb")
    # read the source as string, then write it to the target!
    destination_file.write(source_file.read())

    # close both files to ensure they get written to the storage
    source_file.close()
    destination_file.close()

# SOLUTION: Simple file compare function written from scratch. This can't detect missing file in the target directory.
def check_naive(content, master, target):
    master_file = master + "/" + content
    target_file = target + "/" + content
    fm = open(master_file, "rb")
    ft = open(target_file, "rb")

    # Read the whole files as strings
    strm = fm.read()
    strt = ft.read()

    # Compare the content of two files
    if strm != strt:
        print target_file + " changed. Restoring it back..",
        copyfile(master_file, target_file)
        print "done"

# CHALLENGE: Simple file compare function written from scratch. This can't detect missing file in the target directory.
def check_naive_with_missing_file(content, master, target):
    master_file = master + "/" + content
    target_file = target + "/" + content
    fm = open(master_file, "rb")

    # Check if the target file is missing (due to deletion by hacker)
    if os.path.exists(target_file):
        # File exists, open and carry on
        ft = open(target_file, "rb")
    else:
        # File is missing. Copy from master and return. Ignore the rest of the operation below as the copied file will be the same as the master's anyway.
        print target_file + " is missing. Restoring it back..",
        copyfile(master_file, target_file)
        print "done"
        return


    # Read the whole files as strings
    strm = fm.read()
    strt = ft.read()

    # Compare the content of two files
    if strm != strt:
        print target_file + " changed. Restoring it back..",
        copyfile(master_file, target_file)
        print "done"

# CHALLENGE: Using "filecmp" module with "cmpfiles" function
# Check the manual for detail: http://www.python.org/doc//current/library/filecmp.html?highlight=cmpfiles#filecmp.cmpfiles
def check_cmpfiles(content, master, target):
    master_file = master + "/" + content
    target_file = target + "/" + content

    # Note what must be passed to cmpfiles function. Two directories, and list of file names
    result = filecmp.cmpfiles(master, target, [content])

    # result is a list with index 1 for filename that differs, and index 2 for file that exists in master but not target
    if result[1] or result[2]:
        print target_file + " changed. Restoring it back..",
        copyfile(master_file, target_file)
        print "done"

while True:
    # Check the directory of the webpages
    for content in os.listdir(MASTER):
        if os.path.isfile(MASTER + "/" + content):
            # check_cmpfiles(content, MASTER, TARGET)
            check_naive_with_missing_file(content, MASTER, TARGET)
            # check_naive(content, MASTER, TARGET)

    # Check the media (images) directory 
    master_media = MASTER + "/" + MEDIA
    target_media = TARGET + "/" + MEDIA
    for content in os.listdir(master_media):
        if os.path.isfile(master_media + "/" + content):
            # check_cmpfiles(content, master_media, target_media)
            check_naive_with_missing_file(content, master_media, target_media)
            # check_naive(content, master_media, target_media)

    # Change it to 60 seconds for 1 minute. It's set to 5 seconds for testing only.
    time.sleep(5)

 # vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
