import gdata.docs.service
#
client = gdata.docs.service.DocsService()
client.ClientLogin('accidental.wong@gmail.com', '91503149')
#
q = gdata.docs.service.DocumentQuery(categories=['document'])
q['title'] = 'UseThisNameLesson1.docx'
feed = client.Query(q.ToUri())
entry = feed.entry[0]
# Delete through the entry Edit URL
client.Delete(entry.GetEditLink().href)