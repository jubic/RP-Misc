import gdata.docs.service
#
# Get the document type
def get_doc_type(entry):
    return entry.resourceId.text.split(":")[0]
#
client = gdata.docs.service.DocsService()
client.ClientLogin('accidental.wong@gmail.com', '91503149')
#
feed = client.GetDocumentListFeed()
for entry in feed.entry:
    print get_doc_type(entry) + " => " + entry.title.text