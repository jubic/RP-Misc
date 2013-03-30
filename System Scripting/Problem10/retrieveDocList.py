import gdata.docs.service
#
client = gdata.docs.service.DocsService()
client.ClientLogin('accidental.wong@gmail.com','91503149')
#
feed = client.GetDocumentListFeed()

for entry in feed.entry:
    print entry.title.text