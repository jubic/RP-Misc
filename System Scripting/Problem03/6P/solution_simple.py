import re

f = open("example.txt")
lines = f.readlines()

t = open("output.tmpl")
template = t.read()

# substitute the place holder in template with the content string
def change_template(matches, template):
    if matches:
        template = re.sub("{{" + matches.group(1) + "}}", matches.group(2), template)
    return template

for line in lines:
    # "^(title):\s+(.*) means
    # match string "title" from the beginning of the line
    # followed by a ":" and one or more space
    # then capture the rest (the title content)
    m = re.search("^(title):\s+(.*)", line)
    template = change_template(m, template)

    m = re.search(r"^(name):\s+(.*)", line) 
    template = change_template(m, template)

    m = re.search(r"^(problem):\s+(.*)",  line)
    template = change_template(m, template)

    # means: 
    # match "date" from the beginning, then follwoed by colon ":" and
    # one or more spaces, then followed by
    # "20\d\d/" number 20 followed by 2 digits (for year) then "/"
    # "[01]\d/" number 0 or 1, followed by 1 digit (for month) then "/"
    # "[0123]\d\s+" number 0 to 3, followed by 1 digit (for date) then one
    # or more spaces
    # "[012]\d:" number 0, 1 or 2 followed by 1 digit then ":" (hour)
    # "[0-5]\d"  number 0 to 5 followed by 1 digit (minute)
    # one or more spaces (and then the finish hour below)
    # "[012]\d:" number 0, 1 or 2 followed by 1 digit then ":" (hour)
    # "[0-5]\d"  number 0 to 5 followed by 1 digit (minute)
    m = re.search(r"^(date):\s+(20\d\d/[01]\d/[0123]\d\s+[012]\d:[0-5]\d\s+-\s+[012]\d:[0-5]\d)", line)
    template = change_template(m, template)
    
    m = re.search("^(solution):\s+(.*)",  line)
    template = change_template(m, template)

    m = re.search(r"^(p1):\s+(.*)", line)
    template = change_template(m, template)

    m = re.search(r"^(p2):\s+(.*)", line)
    template = change_template(m, template)

    # substitute any thing that's sandwiched in between two "@" to
    # HTML bold
    template = re.sub("@(.*?)@", r"<b>\1</b>", template)
    # substitute any thing that's sandwiched in between two "_" to
    # HTML italic
    template = re.sub("_(.*?)_", r"<i>\1</i>", template)

print template
 # vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
