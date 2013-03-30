import win32com.client
import os
#
Application = win32com.client.Dispatch("Excel.Application")
Application.Visible = True
Workbook = Application.Workbooks.Add()