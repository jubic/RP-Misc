import win32com.client
import os
import time
import urllib

Application = win32com.client.Dispatch("Excel.Application")
Application.Visible = True

# Office 2010 - Microsoft Office Object 14.0 Object Library
from win32com.client import gencache
gencache.EnsureModule('{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}', 0, 2, 5)
                                                                        #
# Office 2010 - Excel COM
from win32com.client import gencache
gencache.EnsureModule('{00020813-0000-0000-C000-000000000046}', 0, 1, 7)

Workbook = Application.Workbooks.Open(os.getcwd() + "/template.xls")

columns = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]
rows = ["1","2","3"]

for i in range(24):
    sheet = Application.ActiveSheet
    urlList = [sheet.Range("A2").Value, sheet.Range("A3").Value, sheet.Range("A4").Value]

    for url in urlList:
        result = urllib.urlopen(url)