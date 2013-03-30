import sys
from lxml import etree

# Note: this is more sophisticated solution by exploring more control over the output, and
# also the use of attribute with name like: "<name gender='F' sid='71234'>"

# Here's how your code only needs to deal with Output for both file and print to screen
# Print to screen
Output = sys.stdout
# Print to file
# Output = open("output.txt")

doc = open("data-attrib.xml")
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
    # XPath count() function can be used also to return count. This code relies on "lxml"
    result = Tree.xpath("count(//student/name[@gender='%s'])" % gender)  
    return int(result)

def query_students_by_school(school, where, gender):
    """Query students based on school. The "where" filter is used to refine the
       search"""
    result = Tree.xpath("/polytechnic/school[name='%s']/student[%s]/name[@gender='%s']/parent::node()" % (school, where, gender) )
    return result

def get_school_description(school):
    """Get school description for a given school name. 
       Given "SEG", it returns "School of Engineering" """
    result = Tree.xpath("/polytechnic/school[name='%s']/description" % school)
    if len(result) == 0:
        return None
    return result[0].text

def get_student_by_school_and_id(school, sid, startswith=False):
    """Get students by their id. Alternative, can search ids that start
       with a certain number."""
    if startswith:
        result = Tree.xpath("//student[school-name='%s']/name[starts-with(@sid, %s)]/parent::node()" % (school, sid) )
    else:
        result = Tree.xpath("//student[school-name='%s']/name[@sid=%s]/parent::node()/*" % (school, sid) )
    return result

def write_text(results, tags, formats, file_):
    """"results" from the query, 
       "tags" of which values to be printed,
       "formats" of the output,
       "file_" on which stream to output"""
    
    for node in results:
        data = {}
        _list = []
        for n in node.iterchildren():
            data[n.tag] = n.text
        for tag in tags:
            _list.append(data[tag])
        file_.write( formats % tuple(_list) ) 
    

Schools = get_schools()

Output.write("Total males: " + str(count_gender("M")) + "\r\n")
Output.write("Total females: " + str(count_gender("F")) + "\r\n")

# This may be refactored further as there's code duplication below
for school in Schools:
    Output.write("=== %s (%s) ===\r\n" % (get_school_description(school), school))
    Output.write("* Director: %s\r\n" % (get_school_director(school)))

    Output.write("\t===> GPA >= 3.5 <===\r\n")
    fresults = query_students_by_school(school, "gpa >= 3.5", 'F')
    total_females = len(fresults)
    write_text(fresults, ("gpa", "name"), "\t[F] %s : %s\r\n", sys.stdout)

    mresults = query_students_by_school(school, "gpa >= 3.5", 'M')
    total_males = len(mresults)
    write_text(mresults, ("gpa", "name"), "\t[M] %s : %s\r\n", sys.stdout)

    Output.write("Total: %d | Males: %d | Females: %d\n" % (total_males + total_females, total_males, total_females))

    Output.write("\t===> GPA < 2.0 <===\r\n")
    fresults = query_students_by_school(school, "gpa < 2.0", 'F')
    total_females = len(fresults)
    write_text(fresults, ("gpa", "name"), "\t[F] %s : %s\r\n", sys.stdout)

    mresults = query_students_by_school(school, "gpa < 2.0", 'M')
    total_males = len(mresults)
    write_text(mresults, ("gpa", "name"), "\t[M] %s : %s\r\n", sys.stdout)

    Output.write("Total: %d | Males: %d | Females: %d\r\n" % (total_males + total_females, total_males, total_females))

    Output.write("\r\n")

print "-----------------------------------------"
# Get student with sid 74182
print "SIT student with ID 74182"
result = get_student_by_school_and_id('SIT', 74182)
for item in result:
    print item.text, ":",
print

print "----"

# Get all SIT students from cohort with student id that starts with 7
print "SIT students' ID that start with 72"
result = get_student_by_school_and_id('SIT', '72', True)
for item in result:
    print "*",
    for n in item.iterchildren():
        print n.text, ":",
    print
#  vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4