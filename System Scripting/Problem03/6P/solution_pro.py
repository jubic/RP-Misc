import re

File = "example.txt"
Template = "output.tmpl"
Matches = {}

TAG_PATTERNS = (
            r"^(title):\s+(.*)", 
            r"^(name):\s+(.*)", 
            r"^(problem):\s+(.*)", 
            r"^(date):\s+(20\d{2}/(0\d|1[0-2])/([0-2]\d|3[01])\s+([01]\d|2[0-3]):([0-5]\d)\s+-\s+([01]\d|2[0-3]):([0-5]\d))",
            r"^(solution):\s+(.*)", 
            r"^(p1):\s+(.*)",
            r"^(p2):\s+(.*)",
           )
BOLD_PATTERN = "@(.*?)@"
ITALIC_PATTERN = "_(.*?)_"

def process(line):
    global Matches

    for pattern in TAG_PATTERNS:
        m = re.search(pattern, line)
        if m:
            s = m.group(2)
            s = re.sub(ITALIC_PATTERN, r"<i>\1</i>", s)
            s = re.sub(BOLD_PATTERN, r"<b>\1</b>", s)
            Matches[m.group(1)] = s
            return

def template(lines):
    for (k,v) in Matches.iteritems():
        lines = re.sub("{{" + k + "}}", v, lines) 
    return lines

if __name__ == "__main__":
    f = open(File)
    lines = f.readlines()
    for line in lines:
        process(line)

    t = open(Template)
    lines = t.read()
    lines = template(lines)

    print lines

 # vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
