import gdata.docs.service
import glob
import re

def PrintFeed(feed):
  """Prints out the contents of a feed to the console."""
  print '\n'
  if not feed.entry:
     print 'No entries in feed.\n'
  for entry in feed.entry:
     print '%s %s %s' % (entry.title.text.encode('UTF-8'), entry.GetDocumentType(), entry.resourceId.text)

def get_file_extension(fname):
    m = re.search(r"\.([a-zA-Z0-9]+)$", fname)
    if m:
        return m.groups(1)[0]

def get_doc_type(entry):
    return entry.resourceId.text.split(":")[0]

client = gdata.docs.service.DocsService()
client.ClientLogin('myaccount@gmail.com', 'MyPassword')

q = gdata.docs.service.DocumentQuery()
# Query all files
q['title'] = ''
feed = client.Query(q.ToUri())
save_directory = "download/"

format_list = {'presentation':'ppt', 'document':'doc'}

for entry in feed.entry:
    print "Downloading", entry.title.text, "...",
    format = get_doc_type(entry)
    if format == "spreadsheet":
        print "ignored"
        continue # ignore spreadsheet document
    # Using Download method
    # client.Download(entry, save_directory + entry.title.text + "." + format_list[format], export_format=format_list[format])
    # Using Export method (more convenient). It detects the file type from the extension (.doc, .pdf, .ppt, etc.)
    client.Export(entry, save_directory + entry.title.text + "." + format_list[format])
    # Download all as PDF
    client.Export(entry, save_directory + entry.title.text + "." + "pdf")
    print "done"

#   vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
