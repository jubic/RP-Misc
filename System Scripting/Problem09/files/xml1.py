from lxml import etree
from StringIO import StringIO

def xml_from_args(arg1, arg2, arg3):
	xml = "<?xml version='1.0' encoding='utf-8' ?>" + "\r\n"
        xml += "<data>" + "\r\n"
	xml += "<item>" + str(arg1) + "</item>" + "\r\n"
        xml += "<item>" + str(arg2) + "</item>" + "\r\n"
        xml += "<item>" + str(arg3) + "</item>" + "\r\n"
	xml += "</data>"
	return xml

if __name__ == "__main__":
	print xml_from_args("Test One", "Test Two", "Test Three")
	# prints:
	# "<?xml version='1.0' encoding='utf-8' ?>"
	# "<data><item>Test One</item><item>Test Two</item><item>Test Three</item></data>"

	# Test the XML well-formedness by parsing it with etree 
	xml = xml_from_args("Test One", "Test Two", "Test Three")
	t = etree.parse(StringIO(xml))