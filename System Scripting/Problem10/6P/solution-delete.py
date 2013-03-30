import gdata.docs.service
import glob

client = gdata.docs.service.DocsService()
client.ClientLogin('myaccount@gmail.com', 'MyPassword')

# Delete folders
# Query folder
# q = gdata.docs.service.DocumentQuery(categories=['folder'])
# Query all folder
# q['title'] = ''

# Delete documents
q = gdata.docs.service.DocumentQuery()
# Query all folder
q['title'] = ''

feed = client.Query(q.ToUri())

for entry in feed.entry:
    # Ues edit link to delete
    print "Deleting", entry.title.text, "...",
    client.Delete(entry.GetEditLink().href)
    print "done"

#   vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
