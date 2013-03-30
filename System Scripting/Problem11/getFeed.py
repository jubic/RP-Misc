try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree
import gdata.spreadsheet.service
import gdata.service
import atom.service
import gdata.spreadsheet
import atom
#
client = gdata.spreadsheet.service.SpreadsheetsService()
client.email = "accidental.wong@gmail.com"
client.password = '91503149'
client.source = 'C307-P11'
client.ProgrammaticLogin()
#
feed = client.GetSpreadsheetsFeed()
print feed