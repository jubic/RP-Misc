import gdata.docs.service
import glob
import os
import re

BaseDir = "docs-challenge"

def get_file_extension(fname):
    m = re.search(r"\.([a-zA-Z0-9]+)$", fname)
    if m:
        return m.groups(1)[0].upper()

client = gdata.docs.service.DocsService()
client.ClientLogin('myaccount@gmail.com', 'MyPassword')

# types = {'doc':'DOC', 'docx':'DOCX', 'xls':'XLS', 'xlsx':'XLSX', 'ppt':'PPT'}
types = ["DOC", "DOCX", "PPT"]

folder_id = {}
for (path, dirname, filename) in os.walk(BaseDir):
        print path, dirname, filename
        for d in dirname:
            print "Create Folder", d
            p = client.CreateFolder(d)
            folder_id[d] = p.resourceId

        for each_file in filename:
            ext = get_file_extension(each_file)
            if (not ext) or (not ext in types):
                continue
            filepath = "/".join([path,each_file])
            current_file_path = re.sub("^"+BaseDir+"/?", "", path)
            ms = gdata.MediaSource(file_path=filepath, content_type=gdata.docs.service.SUPPORTED_FILETYPES[ext]) 

            if current_file_path == "":
                entry = client.Upload(ms, each_file)
            else:
                resource_id = folder_id[current_file_path]
                (k,id) = resource_id.text.split(":")
                dir_uri = "/feeds/folders/private/full/folder%3A" + id
                entry = client.Upload(ms, each_file , folder_or_uri=dir_uri)

#   vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
