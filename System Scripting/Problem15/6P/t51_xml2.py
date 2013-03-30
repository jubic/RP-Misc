"""
h2. Map Each XML value

Given the XML below, write a function @xmlDegreeConverter@ that takes the given XML (as string) below, and return a list of all the temperatures converted (from Fahrenheit) to Celcius. The formula to convert Fahrenheit and Celsius is given - @convertFtoC@.

bc. {- xml -}
<?xml version='1.0' encoding='UTF-8' ?>
<weather>
    <area>
        <city>Boston</city>
        <temperature>80</temperature>
    </area>
    <area>
        <city>Seattle</city>
        <temperature>85</temperature>
    </area>
    <area>
        <city>Portland</city>
        <temperature>87</temperature>
    </area>
    <area>
        <city>Tucson</city>
        <temperature>102</temperature>
    </area>
</weather>
"""


from StringIO import StringIO
from lxml import etree

Xml = """<?xml version='1.0' encoding='UTF-8' ?>
<weather>
    <area>
        <city>Boston</city>
        <temperature>80</temperature>
    </area>
    <area>
        <city>Seattle</city>
        <temperature>85</temperature>
    </area>
    <area>
        <city>Portland</city>
        <temperature>87</temperature>
    </area>
    <area>
        <city>Tucson</city>
        <temperature>102</temperature>
    </area>
</weather>
"""

convertFtoC = lambda x: (x - 32) * 5.0 / 9.0
# use it just like a normal function convertFtoC(32) - it'll return 0 

def xmlDegreeConverter(xml):
    p = etree.parse(StringIO(xml))
    temp = p.xpath("//temperature/text()")
    ftemp = map(float, temp)
    # result = map(convertFtoC, ftemp)
    # or
    result = []
    for i in ftemp:
        result.append(convertFtoC(i))
    return result

if __name__ == '__main__':
    print xmlDegreeConverter(Xml)

#  vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
