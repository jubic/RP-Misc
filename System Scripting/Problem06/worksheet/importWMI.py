# Import the Python Win32 COM module
from win32com.client import Dispatch
# Call the WMI COM object and activate it
server = Dispatch("WbemScripting.SWbemLocator")
# Connect to the server
connect = server.ConnectServer("localhost", "root\cimv2")

#
results = connect.ExecQuery("Select * from Win32_OperatingSystem")
#
for result in results:
    for each in result.Properties_:
        print each.Name, "=", each.Value