try:
    from xml.etree import ElementTree
except ImportError:  
    from elementtree import ElementTree
import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet
import atom

def get_key(entry):
    id = entry.id.text.split('/')
    return id[len(id) - 1]

client = gdata.spreadsheet.service.SpreadsheetsService()
client.email = "myaccount@gmail.com"
client.password = 'MyPassword'
client.source = 'C307-P11'
client.ProgrammaticLogin()

feed = client.GetSpreadsheetsFeed()
Worksheet = None
WorksheetKey = None
SpreadsheetKey = None
for entry in feed.entry:
    if entry.title.text == 'students':
        SpreadsheetKey = get_key(entry)
        Worksheet = client.GetWorksheetsFeed(SpreadsheetKey)
        WorksheetKey = get_key(Worksheet.entry[0])

qfeed = client.GetListFeed(SpreadsheetKey, WorksheetKey) 
for entry in qfeed.entry:
    print "--"
    for (k,v) in entry.custom.items():
        print k, ":", v.text

#   vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
