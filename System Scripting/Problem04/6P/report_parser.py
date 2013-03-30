import re
import os

Data = {}

def collect(matches, data):
    if matches:
        data[matches.group(1)] = matches.group(2)

def process(f):
    lines = open(f, "r").readlines()    
    data = {}
    for line in lines:
        m = re.search("^(title):\s+(.*)", line)
        collect(m, data)

        m = re.search(r"^(name):\s+(.*)", line) 
        collect(m, data)
        
        m = re.search(r"^(problem):\s+(.*)", line) 
        collect(m, data)

        m = re.search(r"^(date):\s+(20\d\d/[01]\d/[0123]\d\s+[012]\d:[0-5]\d\s+-\s+[012]\d:[0-5]\d)", line)
        collect(m, data)
        
        m = re.search("^(solution):\s+(.*)",  line)
        collect(m, data)

        m = re.search(r"^(p1):\s+(.*)", line)
        collect(m, data)

        m = re.search(r"^(p2):\s+(.*)", line)
        collect(m, data)
    
    return data
	
if __name__ == '__main__':
    import glob
    Files = glob.glob("ex*.txt")
    for file in Files:
        Data[file] = process(file)
    print Data

# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
