try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree
import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet
import atom
from math import sqrt

#
client = gdata.spreadsheet.service.SpreadsheetsService()
client.email = "accidental.wong@gmail.com" # Insert your gmail
client.password = '91503149' # Insert your password
client.source = 'C307-P11'
client.ProgrammaticLogin()
#
feed = client.GetSpreadsheetsFeed()
Worksheet = None
WorksheetKey = None
SpreadsheetKey = None
#
Schools = ["STA", "SEG", "SIT", "SOH", "SHL"]

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
print ">> Total Student Populations per School"

for school in Schools:
    schoolquery = gdata.spreadsheet.service.ListQuery()
    schoolquery.sq = "school = " + school
    qfeed = client.GetListFeed(SpreadsheetKey, WorksheetKey, query=schoolquery)
    totalStudent = len(qfeed.entry)
    num = totalStudent/10

    print "[" + school + "]", "*" * num, str(totalStudent)

print "\n>> GPA Statistics per School"

for school in Schools:
    schoolquery = gdata.spreadsheet.service.ListQuery()
    schoolquery.sq = "school = " + school
    qfeed = client.GetListFeed(SpreadsheetKey, WorksheetKey, query=schoolquery)
    gpa_list = make_list(qfeed.entry, 'gpa')
    float_list = map(float, gpa_list)
    sorted_list = sorted(float_list)
    list_length = len(sorted_list)
    total = sum(sorted_list)
    average = total/list_length
    if list_length%2==0:
        #print "list is even"
        index = list_length/2
        median = (float_list[index - 1] + float_list[index]) / 2
    else:
        #print "list is odd"
        index = int(list_length/2)
        median = float_list[index]

    print "School: " + school
    print "\t* Average:", average
    print "\t* Median :", median