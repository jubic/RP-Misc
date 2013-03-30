import gdata.docs.service
#
def list_all(user,password):
    client = gdata.docs.service.DocsService()
    client.ClientLogin(user,password)
#
    feed = client.GetDocumentListFeed()
    
    for entry in feed.entry:
        print entry.title.text