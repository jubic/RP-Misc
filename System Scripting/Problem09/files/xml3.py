from lxml import etree
from StringIO import StringIO

def xml_from_dict(adict):
	xml = "<?xml version='1.0' encoding='utf-8' ?>" + "\r\n"
        xml += "<data>" + "\r\n"
	for i in adict:
            xml += "<"+i+">"+adict[i]+"</"+i+">" + "\r\n"
	xml += "</data>"
	return xml

if __name__ == "__main__":
	print xml_from_dict({"k1":"v1", "k2":"v2"})
	# prints the order of k1 and k2 maybe reversed:
	# <?xml version='1.0' encoding='utf-8' ?><data><k1>v1</k1><k2>v2</k2></data>

	# check the well-formedness
	xml = xml_from_dict({"k1":"v1", "k2":"v2"})
	etree.parse(StringIO(xml))