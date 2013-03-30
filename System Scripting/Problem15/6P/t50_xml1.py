"""
h2. XML from List of Dictionary

Create a function @xmlFromList@ that takes a list of dictionaries. The XML must have the root tag @<storage>@. 

Each item in the dictionary should be put inside the @<container>@ tag. The dictionary can contain any keys (just make sure the keys are the same for all of the dictionaries in the list). and different values. See the example below.

bc. {- python -}
print xmlFromList([ 
	{'title':'Introduction to Algoritms', 'author':'Ronald Rivest'}, 
	{'title':'Learning Python', 'author':'Mark Lutz'}, 
	{'title':'The Ruby Programming Language', 'author':'David Flanagan'}
	])

bc. {- xml -}
<?xml version='1.0' encoding='UTF-8'?>
<storage>
        <container>
                <author>Ronald Rivest</author>
                <title>Introduction to Algoritms</title>
        </container>
        <container>
                <author>Mark Lutz</author>
                <title>Learning Python</title>
        </container>
        <container>
                <author>David Flanagan</author>
                <title>The Ruby Programming Language</title>
        </container>
</library>

*{color:red;}Notes:* Don't hardcode @<author>@ and @<title>@ as they can change according to keys and values in the dictionary. Only @<storage>@ and @<container>@ are fix.
"""

def xmlFromList(l):
	# your code here
	s = "<?xml version='1.0' encoding='UTF-8'?>\r\n"
	s += "<storage>\r\n"
	for dict in l:
		s += "\t<container>\r\n"
		for (k,v) in dict.items():
			s += "\t\t<%s>%s</%s>\r\n" % (k, v, k)
		s += "\t</container>\r\n"
	s += "</storage>\r\n"
	return s

if __name__ == "__main__":
	print xmlFromList([ {'title':'Introduction to Algoritms', 'author':'Ronald Rivest'}, {'title':'Learning Python', 'author':'Mark Lutz'}, {'title':'The Ruby Programming Language', 'author':'David Flanagan'}])

