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
from graphy.backends import google_chart_api

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

chart = google_chart_api.BarChart()
labels = [ ("SIT","A2C180"), ("STA","3D7930"), ("SEG","FF9900"), ("SOH","AA0033"), ("SHL","3366CC") ]
for label in labels:
    stats = get_gpa_stats(label[0], SpreadsheetKey, WorksheetKey)
    chart.AddBars(stats, label=label[0], color=label[1])

chart.left.min = 0
chart.left.max = 100
chart.bottom.labels = ["A", "B", "C", "D", "F"]
chart.left.labels = range(0, 110, 10)
chart.left.label_gridlines = True

print chart.display.Img(800,300)

#   vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
