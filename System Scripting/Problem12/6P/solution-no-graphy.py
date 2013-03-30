try:
    from xml.etree import ElementTree
except ImportError:  
    from elementtree import ElementTree
import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet
import atom
import sys

def get_key(entry):
    id = entry.id.text.split('/')
    return id[len(id) - 1]

client = gdata.spreadsheet.service.SpreadsheetsService()
client.email = "myaccount@gmail.com"
client.password = 'MyPassword'
client.source = 'C307-P12'
client.ProgrammaticLogin()

feed = client.GetSpreadsheetsFeed()
Worksheet = None
WorksheetKey = None
SpreadsheetKey = None
for entry in feed.entry:
    if entry.title.text == 'studentsp12':
        SpreadsheetKey = get_key(entry)
        Worksheet = client.GetWorksheetsFeed(SpreadsheetKey)
        WorksheetKey = get_key(Worksheet.entry[0])

def get_gpa_stats(school, ss_id, ws_id):
    gpa_cluster = [ (3.5, 4.0), (3.0, 3.5), (2.0, 3.0), (1.0, 2.0), (0.0, 1.0) ]
    query = gdata.spreadsheet.service.ListQuery()
    chart_data = []
    for gpa in gpa_cluster:
        if gpa[1] >= 4.0:
            query.sq = "school = %s and gpa >= %s and gpa <= %s" % (school,gpa[0],gpa[1])
        else:
            query.sq = "school = %s and gpa >= %s and gpa < %s" % (school,gpa[0],gpa[1])
        qfeed = client.GetListFeed(SpreadsheetKey, WorksheetKey, query=query)
        # Create a list that looks like [#A, #B, #C, #D, #F] (number of As, Bs, Cs, etc.)
        chart_data.append(len(qfeed.entry))
    return chart_data

chart_data = {}
chart_vals = ""
schools = ["SIT", "STA", "SEG", "SOH", "SHL"]
for school in schools:
    stats = get_gpa_stats(school, SpreadsheetKey, WorksheetKey)
    chart_data = map(str, stats)
    chart_vals += ",".join(chart_data) + "|"

# remove the last "|" from the "chart_vals" string
chart_vals = chart_vals.strip("|")

chart_url = chart_url = "http://chart.apis.google.com/chart?http://chart.apis.google.com/chart?&chxs=1,000000,11.5,-1,l,676767&chxt=y,x&chxl=1:|A|B|C|D|F&chbh=a&chs=800x300&cht=bvg&chco=A2C180,3D7930,FF9900,AA0033,3366CC&&chdl=" + "|".join(schools) + "&chg=0,10&chtt=GPA+Stats+Overall&chm=N*f0*,000000,0,-1,11|N*f0*,000000,1,-1,11|N*f0*,000000,2,-1,11|N*f0*,000000,3,-1,11|N*f0*,000000,4,-1,11&chd=t:" + chart_vals

print "<html><body>"
print "<h1>End of Semester Report 1, 2010/2011</h1>"
print "<img src='" + chart_url + "'>"
print "</body></html>"
#   vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
