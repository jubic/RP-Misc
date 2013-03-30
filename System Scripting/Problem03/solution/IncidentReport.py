import re

# Assuming example is in the "files" directory
exampleFile = open("../files/example.txt")
# lines is an array
lines = exampleFile.readlines()

outputFile = open("../files/output.tmpl")
# template is a string
output = outputFile.read()

for line in lines:
    # \d	Matches any digits. Same as [0-9]
    # \w	Matches any alphabets, digits and underscore. Same as [a-z, A-Z, 0-9_]
    # \s        Matches whitespaces, non printable characters such as new line, blank space, tab
    # .         Matches anything (except end of line)
    # +         Match 1 or more times
    a = re.search("(title:)\s(.*)" , line)
    b = re.search("(name:)\s(.*)", line)
    c = re.search("(date:)\s(.*)", line)
    d = re.search("(problem:)\s(.*)" , line)
    e = re.search("(p1:)\s(.*)", line)
    f = re.search("(solution:)\s(.*)", line)
    g = re.search("(p2:)\s(.*)", line)

    if a:
        output = re.sub("{{title}}", a.group(2), output)
    if b:
        output = re.sub("{{name}}", b.group(2), output)
    if c:
        output = re.sub("{{date}}", c.group(2), output)
    if d:
        output = re.sub("{{problem}}", d.group(2), output)
    if e:
        output = re.sub("{{p1}}", e.group(2), output)
    if f:
        output = re.sub("{{solution}}", f.group(2), output)
    if g:
        output = re.sub("{{p2}}", g.group(2), output)
        
print output