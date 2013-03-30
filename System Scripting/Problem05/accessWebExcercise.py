import urllib
#

urlList = ["http://google.com","http://rp.sg/test.html","http://blast.sit.rp.sg:8080"]

for url in urlList:
        result = urllib.urlopen(url)
        print result.code