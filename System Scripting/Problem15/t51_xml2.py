"""
h2. Map Each XML value

Given the XML below, write a function @xmlDegreeConverter@ that takes the given XML (as string) below, and return a list of all the temperatures converted (from Fahrenheit) to Celcius. The formula to convert Fahrenheit and Celsius is given - @convertFtoC@.
"""

convertFtoC = lambda x: (x - 32) * 5.0 / 9.0
# use it just like a normal function convertFtoC(32) - it'll return 0 

# Write the function below
def xmlDegreeConverter(xml):
    p = etree.parse(StringIO(xml))
    temp = p.xpath("//temperature/text()")


if __name__ == '__main__':
    print xmlDegreeConverter(Xml)
#  vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
