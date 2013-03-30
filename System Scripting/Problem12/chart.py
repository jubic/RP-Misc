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
#
def get_key(entry):
    id = entry.id.text.split('/')
    return id[len(id) - 1]
#
def make_list(entries, key):
    data = []
    for entry in entries:
        data.append(entry.custom[key].text)
    return data
#
client = gdata.spreadsheet.service.SpreadsheetsService()
client.email = ""
client.password = ''
client.source = 'C307-P12'
client.ProgrammaticLogin()
#
schoolquery = gdata.spreadsheet.service.ListQuery()
#
feed = client.GetSpreadsheetsFeed()
Worksheet = None
WorksheetKey = None
SpreadsheetKey = None
for entry in feed.entry:
    if entry.title.text == 'studentsp12':
        SpreadsheetKey = get_key(entry)
        Worksheet = client.GetWorksheetsFeed(SpreadsheetKey)
        WorksheetKey = get_key(Worksheet.entry[0])
#
# By now you'll have your spreadsheet and worksheet keys. Ready for query below (see P11)
#
def get_gpa_stats(school, spreadsheet_id, worksheet_id):
    gradeF = 0
    gradeD = 0
    gradeC = 0
    gradeB = 0
    gradeA = 0
    
    schoolquery.sq = "school =" + school
    qfeed = client.GetListFeed(spreadsheet_id, worksheet_id, query=schoolquery)
    gpa_list = make_list(qfeed.entry, 'gpa')
    float_gpa_list = map(float, gpa_list)

    for gpa in float_gpa_list:
        if gpa >= 0.0 and gpa < 1.0:
            gradeF+=1
        elif gpa >= 1.0 and gpa < 2.0:
            gradeD+=1
        elif gpa >= 2.0 and gpa < 3.0:
            gradeC+=1
        elif gpa >= 3.0 and gpa < 3.5:
            gradeB+=1
        elif gpa >= 3.5 and gpa <= 4.0:
            gradeA+=1
            
    grade_list = [gradeA, gradeB, gradeC, gradeD, gradeF]
    print grade_list
    
    return grade_list
#
chart = google_chart_api.BarChart()
# a list of "labels", each item is a tuple of school name and its chart color (in RGB)
labels = [ ("SIT","A2C180"), ("STA","3D7930"), ("SEG","FF9900"), ("SOH","AA0033"), ("SHL","3366CC") ]
for label in labels:
    stats = get_gpa_stats(label[0], SpreadsheetKey, WorksheetKey)
    chart.AddBars(stats, label=label[0], color=label[1])
#
chart.left.min = 0
chart.left.max = 100
chart.bottom.labels = ["A", "B", "C", "D", "F"]
chart.bottom.labels_positions = [10,30,50,70,90]
chart.left.labels = range(0, 110, 10)
chart.left.label_gridlines = True
#
print chart.display.Img(1000,300)