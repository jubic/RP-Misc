from lxml import etree
from StringIO import StringIO

def xml_from_args(arg1, arg2, arg3):
	xml = "<?xml version='1.0' encoding='utf-8' ?>"
	xml += "<data>"
	xml += "<item>" + arg1 + "</item>"
	xml += "<item>" + arg2 + "</item>"
	xml += "<item>" + arg3 + "</item>"
	xml += "</data>"
	return xml

if __name__ == "__main__":
	print xml_from_args("Test One", "Test Two", "Test Three")
	xml = xml_from_args("Test One", "Test Two", "Test Three")
	t = etree.parse(StringIO(xml))


