import urllib
from lxml import etree

URL = "http://feeds.bbci.co.uk/news/rss.xml?edition=int"

rss = urllib.urlopen(URL)
rssobj = etree.parse(rss)

titles = rssobj.xpath("//item/title/text()")
descriptions = rssobj.xpath("//item/description/text()")

for i in range(len(titles)):
	print "*", titles[i]
	print descriptions[i] 
	print 
