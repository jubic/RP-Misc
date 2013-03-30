import gdata.docs.service
#
def download_all(user, password):
    client = gdata.docs.service.DocsService()
    client.ClientLogin(user,password)
#
    feed = client.GetDocumentListFeed()
    
    for entry in feed.entry:
        q = gdata.docs.service.DocumentQuery()
        q['title'] = entry.title.text
        feed = client.Query(q.ToUri())
        entry = feed.entry[0]
        client.Export(entry, entry.title.text)
