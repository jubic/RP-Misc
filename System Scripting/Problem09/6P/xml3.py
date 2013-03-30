from lxml import etree
from StringIO import StringIO

def xml_from_dict(adict):
	xml = "<?xml version='1.0' encoding='utf-8' ?>" + "\r\n"
	xml += "<data>" + "\r\n"
	for (k,v) in adict.items():
		xml += "<" + k + ">" + v + "</" + k + ">"  + "\r\n"
	xml += "</data>"
	return xml

if __name__ == "__main__":
	print xml_from_dict({"k1":"v1", "k2":"v2"})
	xml = xml_from_dict({"k1":"v1", "k2":"v2"})
	etree.parse(StringIO(xml))

