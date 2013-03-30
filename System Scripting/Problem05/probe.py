import win32com.client
import sys
import os
import time
import urllib2
import string

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
Workbook = Application.Workbooks.Open(os.getcwd() + "/" + "template.xls")

def save_file(workbook):
    save_time = time.strftime("%Y_%m_%d_%H_%M", time.localtime())
    workbook.SaveAs(os.getcwd() + "/Result-" + save_time + ".xls", )
        
def find_next_empty_column(sheet):
    for column in string.uppercase[1:]:
        if not sheet.Range(column + "1").Value:
            return column

def check(): 
    # Application is global. Remember the naming convention?
    sheet = Application.ActiveSheet
    #
    # ... the rest of your code here
    # 
        
for i in range(24):
    check()
    # Sleep for 10 seconds 
    time.sleep(10)

save_file(Workbook)

#s.Cells(10,1).Interior.ColorIndex = 6


#   vim:expandtab:tabstop=4
