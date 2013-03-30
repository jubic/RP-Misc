from lxml import etree
from StringIO import StringIO

def example_xml():
	xml = "<?xml version='1.0' encoding='utf-8' ?>" + "\r\n"
	xml += "<example>" + "\r\n"
	xml += "<datum>One</datum>" + "\r\n"
	xml += "</example>" 
	return xml

# Testing XML
if __name__ == "__main__":
	# Print it for visual check
	print example_xml()

	# Or, use library "lxml.etree" to check well-formedness
	xml = example_xml()
	etree.parse(StringIO(xml))
