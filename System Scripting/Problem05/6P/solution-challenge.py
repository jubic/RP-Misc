import win32com.client
import sys
import os
import time
import urllib
import string
import smtplib

# Office 2007 - MS Office Object Library 12.0
#from win32com.client import gencache
#gencache.EnsureModule('{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}', 0, 2, 4)

# Office 2010 - Generate Python code for "Microsoft Office Object 14.0 Object Library"
from win32com.client import gencache
gencache.EnsureModule('{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}', 0, 2, 5)

# Office 2007 - Excel COM 
#from win32com.client import gencache
#gencache.EnsureModule('{00020813-0000-0000-C000-000000000046}', 0, 1, 6)

# Office 2010 - Excel COM
from win32com.client import gencache
gencache.EnsureModule('{00020813-0000-0000-C000-000000000046}', 0, 1, 7)

# generate by running: "Python27/Lib/site-packages/win32com/client/makepy.py" 
# Choose "Microsoft Office 12.0 Object Library" and "Microsoft PowerPoint 12.0 Object Library" (generate separately)
from win32com.client import constants

Application = win32com.client.Dispatch("Excel.Application")
Application.Visible = True
# Only one Workbook (one Excel file) is opened at one time
Workbook = Application.Workbooks.Open(os.getcwd() + "/" + "template-challenge.xls")
#Application.Workbooks.Add()

def save_file(workbook, newfile = False):
    if newfile:
        save_time = time.strftime("%Y_%m_%d_%H_%M", time.localtime())
        workbook.SaveAs(os.getcwd() + "/Result-" + save_time + ".xls", )
    else:
        workbook.Save()
        
def find_next_empty_column(sheet):
    for column in string.uppercase[1:]:
        if not sheet.Range(column + "1").Value:
            return column

def check(): 
    # Application is global. Remember the naming convention?
    sheet = Application.ActiveSheet
    date_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
    column = find_next_empty_column(sheet)
    sheet.Range(column + "1").Value = date_time
    sheet.Columns(column).EntireColumn.AutoFit()
    
    status_color = { "OK": 4, "NOT OK": 3 }
    count = 2
    while True:
        host = sheet.Range("A" + str(count)).Value
        status = None
        if not host:
            break
		
		# Check for SMTP connection
        if host.startswith("smtp:"):
            data = host.split("://")
            try:
                # if there's no exception, the connection is good
                smtplib.SMTP(data[1])
                status = "OK"
            except Exception:
                status = "NOT OK"
        # Check for HTTP connection
        elif host.startswith("http:"):
            result = urllib.urlopen(host)
            if result.code == 200:
                status = "OK"
            else:
                status = "NOT OK"
		
        if status:
            sheet.Range(column + str(count)).Value = status
            sheet.Range(column + str(count)).Interior.ColorIndex = status_color[status]
        count += 1

        
for i in range(24):
    check()
    if i == 0:
        # At the beginning of a check, save to a new file
        save_file(Workbook, True)
    # Save to an existing file
    save_file(Workbook)
    time.sleep(10)
    


#s.Cells(10,1).Interior.ColorIndex = 6

