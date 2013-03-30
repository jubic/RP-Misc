import gdata.docs.service

def get_doc_type(entry):
    return entry.resourceId.text.split(":")[0]

client = gdata.docs.service.DocsService()
client.ClientLogin('myaccount@gmail.com', 'MyPassword')

feed = client.GetDocumentListFeed()
for entry in feed.entry:
    print "[%15s] %s" % (get_doc_type(entry), entry.title.text)


#   vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
