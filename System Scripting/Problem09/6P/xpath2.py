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

def xpath2(xmlstr):
	t = etree.parse(StringIO(xmlstr))
	r = t.xpath("/data/state/name")
	l = []
	for i in r:
		l.append(i.text)
	return l

if __name__ == "__main__":
	r = xpath2(XMLString)
	print r
	
