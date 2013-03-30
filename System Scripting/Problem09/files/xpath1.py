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
	file = StringIO(xmlstr)
        Tree = etree.parse(file)
        list = []
        results = Tree.xpath("//state")

        for result in results:
            list = list + [result]

        return list
    
if __name__ == "__main__":
	r = xpath1(XMLString)
	print r  # prints [<Element state at 7f791cf7a3c0>, <Element state at 7f791cf7a418>, <Element state at 7f791cf7a470>]