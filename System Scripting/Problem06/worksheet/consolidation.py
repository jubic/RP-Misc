from win32com.client import Dispatch
import os
import mechanize

# Call the WMI COM object and activate it
server = Dispatch("WbemScripting.SWbemLocator")
# Connect to the server
connect = server.ConnectServer("localhost", "root\\cimv2")

data = {}

def query(wmiClass):
    results = connect.ExecQuery("Select * from " + wmiClass)
    for result in results:
        for each in result.Properties_:
            print each.Name, "=", each.Value
            data[each.Name] = each.Value

# Create list for all classes that are needed
wmiClassList = ['Win32_OperatingSystem','Win32_PhysicalMemory','Win32_Processor','Win32_LogicalDisk','Win32_NetworkAdapterConfiguration']

# .. write the result to the file
file = open(str(os.getenv('COMPUTERNAME'))+".txt", "w")

for wmiClass in wmiClassList:
    result = query(wmiClass)
    file.writelines(str(data))

file.close()

br = mechanize.Browser()
# The search web site - try it with browser
br.open("http://blast.sit.rp.sg:3000/upload/index")
# Select form number 0 - that's the first web form on the page
br.select_form(nr=0)
# This is the form's text field name. In the browser,
# it appears next to "Computer Name:" label.
br['name'] = os.getenv('COMPUTERNAME')
# To upload a file, supposed you have a Browser object called br, you can upload by:
br.form.add_file(open(os.getcwd() + "\Consolidation.py"), "text/plain", "Consolidation.py")
# Submit the form, as if you're pressing the "Search" button
result = br.submit()
# Print the output (in HTML)
print result.read()