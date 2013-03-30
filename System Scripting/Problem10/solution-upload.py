import gdata.docs.service
import glob
import re
#

def get_file_extension(file):
    m = re.search(r"\.([a-zA-Z0-9]+)$", file)
    if m:
        return m.groups(1)[0].upper()
#
def upload_all(user, password):
    for f in glob.glob("docs/*.*"):
        # print f  # prints all files
        client = gdata.docs.service.DocsService()
        client.ClientLogin(user, password)
        #
        file_to_upload = f
        ms = gdata.MediaSource(file_path=file_to_upload, content_type=gdata.docs.service.SUPPORTED_FILETYPES[get_file_extension(f)])
        client.Upload(ms, f)
