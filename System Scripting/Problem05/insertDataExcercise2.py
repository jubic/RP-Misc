import win32com.client
import os

Application = win32com.client.Dispatch("Excel.Application")
Application.Visible = True

# Office 2010 - Microsoft Office Object 14.0 Object Library
from win32com.client import gencache
gencache.EnsureModule('{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}', 0, 2, 5)
                                                                        #
# Office 2010 - Excel COM
from win32com.client import gencache
gencache.EnsureModule('{00020813-0000-0000-C000-000000000046}', 0, 1, 7)

from win32com.client import constants

Workbook = Application.Workbooks.Open(os.getcwd() + "/" + "test.xls")

for i in range(1,11):
    Sheet = Application.ActiveSheet
    Sheet.Range("A"+str(i)).Value = "OK"
    Sheet.Range("A"+str(i)).Interior.ColorIndex = 4