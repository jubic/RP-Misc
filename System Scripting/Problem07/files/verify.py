import sys
from xml.parsers.expat import ParserCreate, ExpatError

parser = ParserCreate()
try:
	parser.ParseFile( open(sys.argv[1]) )
	print 
	print "\t*", sys.argv[1], "is well-formed!"
	print
except ExpatError as e:
	print 
	print "\t*", "ERROR: ", e.message
	print
