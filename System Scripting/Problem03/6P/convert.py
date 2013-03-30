import re

def title(lines):
    lines = re.sub(r"^title:\s+(.*)", r"<h2>\1</h2>", lines, flags = re.M)
    return lines

def name(lines):
    lines = re.sub(r"^name:\s+(.*)", r"<h3 id='name'>\1</h3>", lines, flags = re.M)
    return lines

def problem(lines):
    lines = re.sub(r"^problem:\s+(.*)", r"<h2 class='problem'>\1</h2>", lines, flags = re.M)
    return lines

def date(lines):
    lines = re.sub(r"^date:\s+(20\d\d/[01]\d/[0123]\d\s+[012]\d:[0-5]\d\s+-\s+[012]\d:[0-5]\d)", r"<h3 id='date'>\1</h3>", lines, flags = re.M)
    return lines

def solution(lines):
    lines = re.sub(r"^solution:\s+(.*)", r"<h2 class='solution'>\1</h2>", lines, flags = re.M)
    return lines

def p(lines):
    lines = re.sub(r"^p:\s+(.*)", r"<p>\1</p>", lines, flags = re.M)
    return lines

def bold(lines):
    lines = re.sub(r"\*(.*?)\*", r"<b>\1</b>", lines)
    return lines

def italic(lines):
    lines = re.sub(r"_(.*?)_", r"<i>\1</i>", lines)
    return lines

def make_ol(m):
    output = "<ol>\n"
    bullets = m.group(1).split("\n")
    for item in bullets:
        if item.strip() == "":
            continue
        output += re.sub(r"^#\s*(.*)", r"\t<li>\1</li>\n", item)
    output.strip()
    output += "</ol>\n\n"
    return output


def ol(lines):
    lines = re.sub(r"^list:(.+?)\n\s*\n", make_ol, lines, flags = re.DOTALL | re.M)
    return lines

if __name__ == "__main__":
    f = open("example.txt")
    lines = f.read()

    lines = ol( name( date( title( problem( solution( p( bold( italic(lines) ) ) ) ) ) ) ) )
    
    t = open("template.html")
    template = t.read()
    #template = re.sub("{{data}}", lines, template)
    template = template.replace("{{data}}", lines)
    
    print template
    #print ol(lines)


 # vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
