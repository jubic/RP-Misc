try:
	import unittest2 as unittest
except ImportError:
	import unittest
import sys
import os
import glob
import random
import xml.dom.minidom as dom
import string
from StringIO import StringIO
from lxml import etree

XMLString = """<?xml version='1.0' encoding='utf-8' ?>
<data>
        <state>
                <name>Arizona</name>
                <capital>Tucson</capital>
        </state>
        <state>
                <name>Colorado</name>
                <capital>Denver</capital>
        </state>
        <state>
                <name>Illinois</name>
                <capital>Springfield</capital>
        </state>
        <state>
                <name>Alaska</name>
                <capital>Juneau</capital>
        </state>
</data>"""

def has_module(m):
    try:
        globals()[m] = __import__(m)
        return True
    except Exception, e:
        print e
        return False

class TestP09(unittest.TestCase):

    def tearDown(self):
        for file in glob.glob("*.pyc"):
            if file == "testall.pyc":
                continue
            os.unlink(file)

    @unittest.skipUnless(has_module("tuple0"), "Cannot run *tuple0* yet")
    def test_00_tuple0(self):
        """=========> EXAMPLE: Create simple tuple"""
        self.assertEqual(tuple0.browsers, ("Chrome", "Firefox", "Internet Explorer", "Opera", "Safari"))

    @unittest.skipUnless(has_module("list1"), "Cannot run *list1* yet")
    def test_01_list1(self):
        """===> Create simple list"""
        b = ["Chrome", "Firefox", "Internet Explorer", "Opera", "Safari"]
        b.sort()
        list1.browsers.sort()
        self.assertEqual(list1.browsers, b)
    
    @unittest.skipUnless(has_module("dict1"), "Cannot run *dict1* yet")
    def test_02_dict1(self):
        """===> Create simple dictionary"""
        b = {"Google" : "Chrome", "Mozilla": "Firefox", "Microsoft": "Internet Explorer", "Opera": "Opera", "Apple": "Safari" }
        t = dict1.browsers
        self.assertEqual(len(b.keys()), len(t.keys()))
        self.assertEqual(b, t)

    @unittest.skipUnless(has_module("dict2"), "Cannot run *dict2* yet")
    def test_03_dict2(self):
        """===> Dictionary with list as values"""
        b = { "Google" : ["Chrome", "Search", "Map"], "Apple" : ["iPod", "iPhone", "MacBook"], "Microsoft" : ["Internet Explorer", "Office", "MSN"] }
        keys = b.keys()
        self.assertEqual(len(keys), len(dict2.products.keys()))
        for key in keys:
            l = b[key]
            l.sort()
            dict2.products[key].sort()
            self.assertEqual(l, dict2.products[key])

    @unittest.skipUnless(has_module("func0"), "Cannot run *func0* yet")
    def test_04_func0(self):
        """=========> EXAMPLE: Create simple function"""
        self.assertEqual("python", func0.simple_function("python"))
    
    @unittest.skipUnless(has_module("func1"), "Cannot run *func1* yet")
    def test_05_func1(self):
        """===> Function with 2 string arguments and returns a string in <arg1 arg2> format"""
        self.assertEqual("<a b>", func1.combine("a", "b"))
        self.assertEqual("<one two>", func1.combine("one", "two"))
        self.assertEqual("<apple orange>", func1.combine("apple", "orange"))

    @unittest.skipUnless(has_module("func2"), "Cannot run *func2* yet")
    def test_06_func2(self):
        """===> Function with 3 arguments and returns a list"""
        self.assertEqual([1,2,3], func2.list_it(1,2,3))
        self.assertEqual(["x","y","z"], func2.list_it("x","y","z"))
        
    @unittest.skipUnless(has_module("func3"), "Cannot run *func3* yet")
    def test_07_func3(self):
        """===> Function with a list, and returns a string in <item1><item2>"""
        self.assertEqual("<a><b><c>", func3.combine(["a","b","c"]))
        self.assertEqual("<x><y><z><aa><bb>", func3.combine(["x","y","z","aa","bb"]))
        self.assertEqual("<tomato><garlic>", func3.combine(["tomato","garlic"]))

    # This is dangerous as dictionary may produce different string because no guarantee the keys are ordered. But simple
    # letters seem to be ordered correctly."""
    @unittest.skipUnless(has_module("func4"), "Cannot run *func4* yet")
    def test_08_func4(self):
        """===> Function with a dictionary, and returns a string in "k1,v1;k2,v2;" format"""
        self.assertEqual("a,b;c,d;", func4.combine({"a":"b","c":"d"}))
        self.assertEqual("x,y;", func4.combine({"x":"y"}))
        self.assertEqual("a,b;c,d;e,f;g,h;", func4.combine({"a":"b","c":"d","e":"f","g":"h"}))

    @unittest.skipUnless(has_module("excel1"), "Cannot run *excel1* yet")
    def test_09_excel1(self):
        """===> Excel cell range generation - row_only(c, r) generates "r" number of rows in column "c" """
        r = [ "A" + str(i+1) for i in range(1) ]
        self.assertEqual(excel1.row_only("A", 1), r)
         
        r = [ "Z" + str(i+1) for i in range(100) ]
        self.assertEqual(excel1.row_only("Z", 100), r)

    @unittest.skipUnless(has_module("excel2"), "Cannot run *excel2* yet")
    def test_10_excel2(self):
        """===> Excel cell range generation - column_only(c, r) generates "c" columns starting from "A" with row number "r" """
        l = string.uppercase
        r = [ l[i] + "1" for i in range(1) ]
        self.assertEqual(excel2.column_only(1, 1), r)
         
        r = [ l[i] + "100" for i in range(26) ]
        self.assertEqual(excel2.column_only(26, 100), r)

    @unittest.skipUnless(has_module("xml0"), "Cannot run *xml0* yet")
    def test_11_xml0(self):
        """=========> EXAMPLE: generate any well-formed XML"""
        try:
            xml = xml0.example_xml()
            dom.parseString(xml)
        except Exception, ex:
            self.fail(ex)

    @unittest.skipUnless(has_module("xml1"), "Cannot run *xml1* yet")
    def test_12_xml1(self):
        """===> Generate XML from 3 string arguments with root document <data>, and each child as <item>"""
        try:
            xml = xml1.xml_from_args("aa", "bb", "cc")
            p = etree.parse(StringIO(xml))
            r = p.xpath("/data/item/text()")
            self.assertEqual(r, ["aa", "bb", "cc"])

            xml = xml1.xml_from_args("Python", "PHP", "Ruby")
            p = etree.parse(StringIO(xml))
            r = p.xpath("/data/item/text()")
            self.assertEqual(r, ["Python", "PHP", "Ruby"])
        except Exception, ex:
            self.fail(ex)

    @unittest.skipUnless(has_module("xml2"), "Cannot run *xml2* yet")
    def test_13_xml2(self):
        """===> Generate XML from a list of strings with root document <data>, and each child as <item>"""
        try:
            xml = xml2.xml_from_list([])
            p = etree.parse(StringIO(xml))
            r = p.xpath("/data/item/text()")
            self.assertEqual(r, [])

            xml = xml2.xml_from_list(["aa"])
            p = etree.parse(StringIO(xml))
            r = p.xpath("/data/item/text()")
            self.assertEqual(r, ["aa"])
    
            xml = xml2.xml_from_list( list(string.letters) )
            p = etree.parse(StringIO(xml))
            r = p.xpath("/data/item/text()")
            self.assertEqual(r, list(string.letters))
        except Exception, ex:
            self.fail(ex)

    @unittest.skipUnless(has_module("xml3"), "Cannot run *xml3* yet")
    def test_14_xml3(self):
        """===> Generate XML from a dictionary (all strings) """
        try:
            xml = xml3.xml_from_dict( {"k1":"v1", "k2":"v2"} )
            p = etree.parse(StringIO(xml))
            r = p.xpath("/data/k2/text()")
            self.assertEqual(r, ["v2"])
            r = p.xpath("/data/k1/text()")
            self.assertEqual(r, ["v1"])
        except Exception, ex:
            self.fail(ex)

    @unittest.skipUnless(has_module("xpath1"), "Cannot run *xpath1* yet")
    def test_15_xpath1(self):
        """===> Use XPath to get all the "state" nodes from the given XML string"""
        try:
            r = xpath1.xpath1(XMLString)
            l = []
            for i in r:
                d = {}
                for child in i.iterchildren():
                    d[child.tag] = child.text    
                l += [d]
            
            correct = [{'name': 'Arizona', 'capital': 'Tucson'}, {'name': 'Colorado', 'capital': 'Denver'}, {'name': 'Illinois', 'capital': 'Springfield'}, {'name': 'Alaska', 'capital': 'Juneau'}]

            self.assertEqual(correct, l)
            
        except Exception, ex:
            self.fail(ex)

    @unittest.skipUnless(has_module("xpath2"), "Cannot run *xpath2* yet")
    def test_16_xpath2(self):
        """===> Use XPath to get all the "state" names and put them into the list"""
        try:
            r = xpath2.xpath2(XMLString)
            correct = ['Arizona','Colorado','Illinois','Alaska']
            self.assertEqual(correct, r)
        except Exception, ex:
            self.fail(ex)

    @unittest.skipUnless(has_module("xpath3"), "Cannot run *xpath3* yet")
    def test_17_xpath3(self):
        """===> Use XPath, given a "state" name, get the "capital" """
        try:
            r = xpath3.xpath3(XMLString, "Colorado")
            self.assertEqual(r, "Denver")
            r = xpath3.xpath3(XMLString, "Alaska")
            self.assertEqual(r, "Juneau")
            r = xpath3.xpath3(XMLString, "Illinois")
            self.assertEqual(r, "Springfield")
        except Exception, ex:
            self.fail(ex)
  

if __name__ == '__main__':
    unittest.main(verbosity=2)

#   vim:expandtab:tabstop=4
