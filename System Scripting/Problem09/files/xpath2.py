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
	file = StringIO(xmlstr)
        Tree = etree.parse(file)
        list = []
        results = Tree.xpath("//name")

        for result in results:
            list = list + [result.text]

        return list
    
if __name__ == "__main__":
	r = xpath2(XMLString)
	print r  # prints ['Arizona', 'California', 'Oregon'] 