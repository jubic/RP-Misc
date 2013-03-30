import os
import time

MASTER = "master"
TARGET = "published"
MEDIA  = "images"

def copyfile(source, destination):
    source_file = open(source, "rb")
    destination_file = open(destination, "wb")
    destination_file.write(source_file.read())
    source_file.close()
    destination_file.close()

def check(content, master, target):
    master_file = master + "/" + content
    target_file = target + "/" + content
    fm = open(master_file, "rb")
    ft = open(target_file, "rb")

    strm = fm.read()
    strt = ft.read()

    if strm != strt:
        print target_file + " changed. Restoring it back..",
        copyfile(master_file, target_file)
        print "done"

while True:
    for content in os.listdir(MASTER):
        if os.path.isfile(MASTER + "/" + content):
            check(content, MASTER, TARGET)

    master_media = MASTER + "/" + MEDIA
    target_media = TARGET + "/" + MEDIA
    for content in os.listdir(master_media):
        if os.path.isfile(master_media + "/" + content):
            check(content, master_media, target_media)

    time.sleep(60)

 # vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
