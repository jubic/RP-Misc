import gdata.docs.service
#
def delete_all(user,password):
    client = gdata.docs.service.DocsService()
    client.ClientLogin(user,password)
#
    feed = client.GetDocumentListFeed()

    for entry in feed.entry:
        q = gdata.docs.service.DocumentQuery(categories=['document'])
        q['title'] = entry.title.text
        feed = client.Query(q.ToUri())
        entry = feed.entry[0]
        # Delete through the entry Edit URL
        client.Delete(entry.GetEditLink().href)
