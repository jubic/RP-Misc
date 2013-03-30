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
feed = client.GetSpreadsheetsFeed()
Worksheet = None
WorksheetKey = None
SpreadsheetKey = None
#
def get_key(entry):
    id = entry.id.text.split('/')
    return id[len(id) - 1]
#
for entry in feed.entry:
    if entry.title.text == 'students':
        SpreadsheetKey = get_key(entry)
        Worksheet = client.GetWorksheetsFeed(SpreadsheetKey)
        WorksheetKey = get_key(Worksheet.entry[0])
#
def make_list(entries, key):
    data = []
    for entry in entries:
        data.append(entry.custom[key].text)
    return data
#
schoolquery = gdata.spreadsheet.service.ListQuery()
schoolquery.sq = "school = SIT"
qfeed = client.GetListFeed(SpreadsheetKey, WorksheetKey, query=schoolquery)
#
gpa_list = make_list(qfeed.entry, 'gpa')
float_list = map(float, gpa_list)
total = sum(float_list)
mean = total/len(float_list)
sorted_list = sorted(float_list)
median = sorted(float_list)[len(float_list)/2]
#
print gpa_list
print float_list
print sorted_list
print total
print mean
print median