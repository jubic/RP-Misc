from lxml import etree
from StringIO import StringIO

XMLString = """<?xml version='1.0' encoding='utf-8' ?>
<data>
	<state>
		<name>Arizona</name>
		<capital>Tucson</capital>
	</state>
	<state>
		<name>California</name>
		<capital>Sacramento</capital>
	</state>
	<state>
		<name>Oregon</name>
		<capital>Salem</capital>
	</state>
</data>"""

def xpath3(xmlstr, statename):
	t = etree.parse(StringIO(xmlstr))
	r = t.xpath("/data/state[name='" + statename + "']/capital") 
	if len(r) == 0:
		return None
	return r[0].text

if __name__ == "__main__":
	r = xpath3(XMLString, "Arizona")
	print r   # prints Tucson
	
