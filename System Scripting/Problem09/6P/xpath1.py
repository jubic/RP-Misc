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

def xpath1(xmlstr):
	t = etree.parse(StringIO(xmlstr))
	r = t.xpath("/data/state")
	return r

if __name__ == "__main__":
	r = xpath1(XMLString)
	print r  # prints [<Element state at 7f791cf7a3c0>, <Element state at 7f791cf7a418>, <Element state at 7f791cf7a470>]
	
