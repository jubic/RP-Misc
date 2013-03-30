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
    file = StringIO(xmlstr)
    Tree = etree.parse(file)
    results = Tree.xpath("//state[name='"+statename+"']/capital")

    for result in results:
        return result.text

if __name__ == "__main__":
    r = xpath3(XMLString, "Arizona")
    print r   # prints Tucson

    r = xpath3(XMLString, "California")
    print r   # prints Sacramento
	
    r = xpath3(XMLString, "Oregon")
    print r   # prints Salem