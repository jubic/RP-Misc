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

def get_data(spkey, wskey, querystr):
    query = gdata.spreadsheet.service.ListQuery()
    query.sq = querystr
    qfeed = client.GetListFeed(spkey, wskey, query=query)
    return qfeed.entry

def make_list(entries, key):
    """Make list from gdata entry based on a given key"""
    data = []
    for entry in entries:
        data.append(entry.custom[key].text)
    return data

def compute_average_gpa(datalist):
    float_datalist = map(float, datalist)
    return sum(float_datalist) / len(datalist)

def compute_median_gpa(datalist):
    float_datalist = map(float, datalist)
    float_datalist.sort()
    if len(datalist) % 2 == 0:
        # even number of data
        index = len(datalist) / 2 
        median = (float_datalist[index - 1] + float_datalist[index]) / 2.0
    else:
        index = int(len(datalist) / 2.0)
        median = float_datalist[index]
    return median

def print_stats_for_school(school):
    data = get_data(SpreadsheetKey, WorksheetKey, "school = " + school)
    gpalist = make_list(data, 'gpa')
    print "School:", school
    print "\t* Average:", compute_average_gpa(gpalist)
    print "\t* Median :", compute_median_gpa(gpalist)
    print

def print_students_graph(school):
    data = get_data(SpreadsheetKey, WorksheetKey, "school = " + school) 
    total = len(data) 
    total_normalized = int(total / 10)
    print "[%s]" % school, "*" * total_normalized, total
    
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

print ">> Total Student Populations per School"
for school in ["STA", "SEG", "SIT", "SOH", "SHL"]:
    print_students_graph(school)

print

print ">> GPA Statistics per School"
for school in ["STA", "SEG", "SIT", "SOH", "SHL"]:
    print_stats_for_school(school)

# new_data = {"school": "SIT", "studentid":"999999", "name":"Zorro", "gpa":"3.9", "address":"99 Woodlands Ave. 999", "email":"9999999@b.c"}
# client.InsertRow(new_data, SpreadsheetKey, WorksheetKey)

# PrintFeed(list_feed)
#   vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4