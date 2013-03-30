import gdata.docs.service
#
client = gdata.docs.service.DocsService()
client.ClientLogin('accidental.wong@gmail.com', '91503149')
#
# Find the document first
q = gdata.docs.service.DocumentQuery()
q['title'] = 'UseThisNameLesson1.docx'
# Query and get the feed (the XML feed document)
feed = client.Query(q.ToUri())
# Get the first entry (beware no error checking here)
entry = feed.entry[0]
# Download as the desired format
client.Export(entry, entry.title.text)