import win32com.client
#
Application = win32com.client.Dispatch("Excel.Application")
Application.Visible = True
Application.Workbooks.Add()
#
Sheet = Application.ActiveSheet
Sheet.Range("B5").Value = "OK"
Sheet.Range("B5").Interior.ColorIndex = 3