import urllib
#
result = urllib.urlopen("http://rp.sg")
print result.code
print result.headers.values()
print result.read()