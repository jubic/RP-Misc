import xml.dom.minidom as dom
from StringIO import StringIO
from lxml import etree

def xml_from_list(alist):
	xml = "<?xml version='1.0' encoding='utf-8' ?>" + "\r\n"
        xml += "<data>" + "\r\n"
	for i in alist:
            xml += "<item>" + i + "</item>" + "\r\n"
	xml += "</data>"
	return xml

if __name__ == "__main__":
	print xml_from_list(["aa"])
	# prints: "<?xml version='1.0' encoding='utf-8' ?><data><item>aa</item></data>"

	# check the well-formedness
	etree.parse( StringIO(xml_from_list(["aa", "bb", "cc"]) ))