import sys
from lxml import etree

# Note: this looks a bit more complex and sophisticated because it tries to assert
# better control on the output (output on selected tags)

# Here's how your code only needs to deal with Output for both file and print to screen
# Print to screen
Output = sys.stdout
# Print to file
# Output = open("output.txt")

doc = open("data.xml")
Tree = etree.parse(doc)

def get_schools():
    """Get all the schools from the XML file. Returns the school name (e.g. SEG)"""
    schools = []
    result = Tree.xpath("//school/name")
    # or to use Python list comprehension:
    # Schools = [ s.text for s in get_schools() ]
    for school in result:
        schools.append(school.text)
    return schools

def get_school_director(school):
    """Get the school's director's name"""
    result = Tree.xpath("//school[name='%s']/director" % school)  
    return result[0].text

def count_gender(gender):
    """Count the number of male or female students"""
    result = Tree.xpath("count(//student[gender='%s'])" % gender)  
    return int(result)

def query_students_by_school(school, where):
    """Query students based on school. The "where" filter is used to refine the
       search"""
    result = Tree.xpath("/polytechnic/school[name='%s']/student[%s]" % (school, where) )
    return result

def get_school_description(school):
    """Get school description for a given school name. 
       Given "SEG", it returns "School of Engineering" """
    result = Tree.xpath("/polytechnic/school[name='%s']/description" % school)
    if len(result) == 0:
        return None
    return result[0].text

def write_text(results, tags, formats, file_):
    """"results" from the query, 
       "tags" of which values to be printed,
       "formats" of the output,
       "file_" on which stream to output"""
    for nodes in results:
        data = {}
        _list = []
        for node in nodes.iter():
            data[node.tag] = node.text
        for tag in tags:
            _list.append(data[tag])
        file_.write( formats % tuple(_list) ) 

# Get list of schools from XML document itself
Schools = get_schools()

Output.write("Total males: " + str(count_gender("M")) + "\r\n")
Output.write("Total females: " + str(count_gender("F")) + "\r\n")

for school in Schools:
    Output.write("=== %s (%s) ===\r\n" % (get_school_description(school), school))
    Output.write("* Director: %s\r\n" % (get_school_director(school)))

    Output.write("\t===> GPA >= 3.5 <===\r\n")    
    # Query female students with GPA 3.5 and above for a school
    fresults = query_students_by_school(school, "gpa >= 3.5 and gender = 'F'")
    total_females = len(fresults)
    write_text(fresults, ("gender", "gpa", "name"), "\t[%s] %s : %s\r\n", sys.stdout)

    # Query male students with GPA 3.5 and above for a school
    mresults = query_students_by_school(school, "gpa >= 3.5 and gender = 'M'")
    total_males = len(mresults)
    write_text(mresults, ("gender", "gpa", "name"), "\t[%s] %s : %s\r\n", sys.stdout)

    Output.write("Total: %d | Males: %d | Females: %d\n" % (total_males + total_females, total_males, total_females))

    Output.write("\t===> GPA < 2.0 <===\r\n")    
    # Query female students with GPA less than 2.0 for a school
    fresults = query_students_by_school(school, "gpa < 2.0 and gender = 'F'")
    total_females = len(fresults)
    write_text(fresults, ("gender", "gpa", "name"), "\t[%s] %s : %s\r\n", sys.stdout)

    # Query male students with GPA less than 2.0 for a school
    mresults = query_students_by_school(school, "gpa < 2.0 and gender = 'M'")
    total_males = len(mresults)
    write_text(mresults, ("gender", "gpa", "name"), "\t[%s] %s : %s\r\n", sys.stdout)

    Output.write("Total: %d | Males: %d | Females: %d\r\n" % (total_males + total_females, total_males, total_females))
    
    Output.write("\r\n")

#  vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4