try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree
import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet
import atom
#
client = gdata.spreadsheet.service.SpreadsheetsService()
client.email = "accidental.wong@gmail.com"
client.password = '91503149'
client.source = 'C307-P11'
client.ProgrammaticLogin()
#

def get_key(entry):
    # get the "id". To see how the id looks like, uncomment below
    # print entry.id.text
    id = entry.id.text.split('/')
    return id[len(id) - 1]
#
# Get the document list
feed = client.GetSpreadsheetsFeed()
Worksheet = None
WorksheetKey = None
SpreadsheetKey = None
for entry in feed.entry:
    # only choose "students" spreadsheet
    if entry.title.text == 'students':
        # get the spreadsheet key
        SpreadsheetKey = get_key(entry)
        # then retrieve the worksheet(s) from the Spreadsheet
        Worksheet = client.GetWorksheetsFeed(SpreadsheetKey)
        # get the worksheet key of the first worksheet (assume you only
        # have 1 worksheet
        WorksheetKey = get_key(Worksheet.entry[0])
#
# Get the spreadsheet content (data) using both SpreadsheeKey, and
# the WorksheetKey
qfeed = client.GetListFeed(SpreadsheetKey, WorksheetKey)
# Iterate (loop) through the returned data feed
for entry in qfeed.entry:
    print "--"
    # print the key (the label on first row) and the value of each row
    for (k,v) in entry.custom.items():
        print k, ":", v.text