from win32com.client import Dispatch, GetObject
import win32con
import os
import mechanize
import webbrowser

server = Dispatch("WbemScripting.SWbemLocator")
conn = server.ConnectServer("localhost", "root\\cimv2")

def query(what, filter=""):
	where = ""
	if filter:
		where = "where " + filter
	results = conn.ExecQuery("Select * from %s %s" % (what, where) )

	collections = []
	for item in results:
		data = {}
		for each in item.Properties_:
			data[each.Name] = each.Value
		collections.append(data)
	
	return collections

def write_to_file(fd, results):
	for result in results:
		for key, value in result.items():
			f.write("%40s = %s\n" % (key, value) )
		f.write("%50s" % "---------------------")
		f.write("\n")

results = query("Win32_OperatingSystem")
filename = results[0]["CSName"]
f = open(filename, "wb")

f.write("%50s" % "====== OperatingSystem ======\n")
write_to_file(f, results)
	
f.write("%50s" % "====== Win32_Processor ======\n")
results = query("Win32_Processor")
write_to_file(f, results)

f.write("%50s" % "====== Win32_PhysicalMemory ======\n")
results = query("Win32_PhysicalMemory")
write_to_file(f, results)

f.write("%50s" % "====== Win32_LogicalDisk ======\n")
results = query("Win32_LogicalDisk")
write_to_file(f, results)

f.write("%50s" % "====== Win32_NetworkAdapterConfiguration ======\n")
results = query("Win32_NetworkAdapterConfiguration", filter="IpEnabled = TRUE")
write_to_file(f, results)

f.write("%50s" % "====== Win32_Product ======\n")
results = query("Win32_Product")
write_to_file(f, results)

f.close()

br = mechanize.Browser()
br.open("http://blast.sit.rp.sg:3000/upload/index")
br.select_form(nr=0)
br["name"] = filename
br.form.add_file(open(filename), "text/plain", filename)
webbrowser.open_new_tab("http://blast.sit.rp.sg:3000/upload/show/" + filename)
resp = br.submit()
#print resp.get_data()
