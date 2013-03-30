import urllib
from lxml import etree
from StringIO import StringIO

def xml_from_rss(url):
    URL = urllib.urlopen(url)
    file = StringIO(URL.read())
    Tree = etree.parse(file)
    results = Tree.xpath("//item")

    for result in results:
        print "Title: " + result[0].text
        print "Description: " + result[1].text


if __name__ == "__main__":
    print xml_from_rss("http://feeds.bbci.co.uk/news/rss.xml?edition=int")   