import win32com.client
import os
#
Application = win32com.client.Dispatch("Excel.Application")
Application.Visible = True
Workbook = Application.Workbooks.Open(os.getcwd() + "/" + "test.xls")
#
# .. do some work ..
#
Workbook.SaveAs(os.getcwd() + "/" + "output.xls")

Workbook.Save()