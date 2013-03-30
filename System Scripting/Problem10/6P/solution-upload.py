import gdata.docs.service
import glob
import os
import os.path
import re

BaseDir = "docs/"

def get_file_extension(fname):
    m = re.search(r"\.([a-zA-Z0-9]+)$", fname)
    if m:
        return m.groups(1)[0].upper()

client = gdata.docs.service.DocsService()
client.ClientLogin('myaccount@gmail.com', 'MyPassword')

types = ["DOC", "DOCX", "PPT"]

folder_id = {}
for f in glob.glob(BaseDir + "*.*"):
    ext = get_file_extension(f)
    if (not ext) or (not ext in types):
        continue
    gdoc_filename = os.path.basename(f) 
    print f, "=", gdoc_filename, ext
    ms = gdata.MediaSource(file_path=f, content_type=gdata.docs.service.SUPPORTED_FILETYPES[ext]) 
    entry = client.Upload(ms, gdoc_filename)

#   vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
