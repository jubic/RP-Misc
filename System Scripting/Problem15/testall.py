import unittest
import sys
import os
import os.path
import glob
import random
import xml.dom.minidom as dom
import string
import re
import sqlite3
import filecmp
import base64
from StringIO import StringIO
from lxml import etree

FirstNames = ["Anna", "Bob", "Charles", "Derek", "Eva", "Evi", "Fatimah", "Greg", "George", "Hannah", "Helen", "Ike", "Ivy", "John", "Jonah", "Jacob", "Louis", "Madison", "Mary", "Nathan", "Otis", "Peter", "Paul", "Quentin", "Robert", "Ronald", "Roy", "Ray", "Stephen", "Steven", "Salim", "Taufiq", "Trent", "Theodore", "Valentine", "Valentino", "William", "Zul"]
LastNames = ["Tan", "Lim", "Neo", "Perez", "John", "Obama", "Smith", "Jones", "Suleiman", "Akbar", "May", "Taylor", "Miller", "Carpenter", "Tay", "Lin", "Lam","Yang","Gonzales","Rios","Iskandar","Zulkarnaen","Abdul"]

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

TestDb = 'tmp/t.db'

def has_module(m):
    try:
        globals()[m] = __import__(m)
        return True
    except Exception, e:
        print e
        return False

class TestP15(unittest.TestCase):

    def tearDown(self):
        for file in glob.glob("*.pyc"):
            if file == "testall.pyc":
                continue
            os.unlink(file)
        if os.path.isfile(TestDb):
            os.unlink(TestDb)

    @unittest.skipUnless(has_module("t00_list1"), "Cannot run *t00_list1* yet")
    def test_t00_list1(self):
        loi = t00_list1.list_of_int
        los = t00_list1.list_of_string
        lol = t00_list1.list_of_lists

        self.assertEqual(len(loi), 3)
        self.assertEqual(len(los), 3)
        self.assertEqual(len(lol), 3)

        for i in range(3):
            self.assertTrue(isinstance(loi[i], int))
            self.assertTrue(isinstance(los[i], str))
            self.assertTrue(isinstance(lol[i], list))

    @unittest.skipUnless(has_module("t01_list2"), "Cannot run *t01_list2* yet")
    def test_t01_listt2(self):
        # self.maxDiff = None
        l1 = range(100)
        random.shuffle(l1)
        l2 = range(100)
        random.shuffle(l2)
        l3 = []
        for i in range(len(l1)):
            l3.append(l1[i] + l2[i])
        r = t01_list2.add2lists(l1,l2)
        self.assertEqual(r, l3)

    @unittest.skipUnless(has_module("t02_list3"), "Cannot run *t02_list3* yet")
    def test_t02_list3(self):
        l1 = range(100)
        random.shuffle(l1)
        l2 = range(100)
        random.shuffle(l2)
        l3 = []
        for i in range(len(l1)):
            l3.append(l1[i])
            l3.append(l2[i])
        r = t02_list3.zipper(l1, l2)
        self.assertEqual(r, l3)

    @unittest.skipUnless(has_module("t03_list4"), "Cannot run *t03_list4* yet")
    def test_t03_list4(self):
        l1 = [random.randint(0,100) for i in range(100)]
        set = [random.randint(21, 93) for i in range(10)]
        count = 0
        for i in l1:
            if i in set:
                count += 1
        self.assertEqual(count, t03_list4.countInList(l1, set))

    @unittest.skipUnless(has_module("t10_dict1"), "Cannot run *t10_dict1* yet")
    def test_t10_dict1(self):
        d = { "n1":"joe", "n2":"john", "n3":"bob", "n4":"alex" }
        r = t10_dict1.getVals(d)
        c = d.values()
        c.sort()
        s = ""
        for i in c:
            s += "<%s>" % i
 
        self.assertEqual(s, r)

    @unittest.skipUnless(has_module("t11_dict2"), "Cannot run *t11_dict2* yet")
    def test_t10_dict2(self):
        d = {"age": [10,20,30,50], "gpa": [10.0, 20.0, 30.0, 40.0] }
        age = d['age']
        gpa = d['gpa']
        aveage = sum(age) / float(len(age)) 
        avegpa = sum(gpa) / float(len(gpa))
    
        self.assertEqual([aveage, avegpa], t11_dict2.getAve(d))

    @unittest.skipUnless(has_module("t12_dict3"), "Cannot run *t12_dict3* yet")
    def test_t10_dict3(self):
        d = {"joe_age33":33, "bob_age25":25, "charlie_age19":19, "don_agen45":45, "eva_age30":30}
        l = []
        for (k,v) in d.items():
            if v <= 30:
                l.append(k)    

        self.assertEqual(l, t12_dict3.getNames(d))

    @unittest.skipUnless(has_module("t20_string1"), "Cannot run *t20_string1* yet")
    def test_t20_string1(self):
        d = "aa:bb:cc:dd:ee"
        dl = d.split(":")
        nl = [ dl[0], dl[-1] ]
        self.assertEqual(nl, t20_string1.getFirstLast(d))

    @unittest.skipUnless(has_module("t21_string2"), "Cannot run *t21_string2* yet")
    def test_t21_string2(self):
        d = ["xth", "eth", "rot", "dec", "kon"]
        s = ""
        for i in d:
            s += i[0]
        self.assertEqual(s, t21_string2.getFirstChars(d))

    @unittest.skipUnless(has_module("t22_string3"), "Cannot run *t22_string3* yet")
    def test_t22_string3(self):
        d = ["1db", "22ef", "ff33", "222ghi", "2222.."]
        l = []
        for i in d:
            if re.search("^\d{2,}", i):
                l.append(i)
        self.assertEqual(l, t22_string3.startsWithDigit(d))
    
    @unittest.skipUnless(has_module("t30_email1"), "Cannot run *t30_email1* yet")
    def test_t30_email1(self):
        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.parser import Parser 

        def mailZip(l):
            msg = MIMEMultipart()
            for f in l:
                zipfile = open(f, "rb")  
                zip = MIMEBase('application', 'zip', name=f)
                zip.set_payload(zipfile.read())
                zipfile.close()
                #
                encoders.encode_base64(zip)
                msg.attach(zip)
            return msg

        d = glob.glob("tmp/*.zip")
        mymsg = mailZip(d)    
        yrmsg = t30_email1.mailZip(d)
        for i in range(len(d)):
            self.assertEqual(str(mymsg.get_payload(i)), str(yrmsg.get_payload(i)))

    @unittest.skipUnless(has_module("t31_email2"), "Cannot run *t31_email2* yet")
    def test_t31_email2(self):
        def _get_b64_payload(text):
            f = StringIO(text)
            l = f.readlines()
            while True:
                if l[0] != "\r" and l[0] != "\n":
                    l.pop(0)
                else:   
                    break

            s = "".join(l)
            return s
 
        from email.mime.image import MIMEImage
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        files = ["tmp/guido.jpeg", "tmp/cookbook.jpeg"]

        msg = t31_email2.mailImages(["tmp/guido.jpeg", "tmp/cookbook.jpeg"])
        html = msg.get_payload(0)
        img1 = msg.get_payload(1)
        img2 = msg.get_payload(2)

        self.assertEqual('joe@nopoly.dom', msg['From'])
        self.assertEqual('bob@nopoly.dom', msg['To'])
        self.assertEqual('text/html', html.get_content_type())
        self.assertEqual('image/jpeg', img1.get_content_type())
        self.assertEqual('image/jpeg', img2.get_content_type())
        self.assertEqual('inline', img1['Content-Disposition'].split(';')[0])
        self.assertEqual('inline', img2['Content-Disposition'].split(';')[0])
        self.assertEqual('filename="tmp/guido.jpeg"', img1['Content-Disposition'].split(';')[1].strip())
        self.assertEqual('filename="tmp/cookbook.jpeg"', img2['Content-Disposition'].split(';')[1].strip())
        self.assertEqual('<file1>', img1['Content-ID'])
        self.assertEqual('<file2>', img2['Content-ID'])

        # compare the files
        for f in files:
            f1 = open("tmp/__img1", "wb")
            s1 = _get_b64_payload(img1)
            sf1 = StringIO(s1)
            base64.decode(sf1, f1)
            sf1.close()
            f1.close()
            filecmp.cmp("tmp/__img1", files[0])

    @unittest.skipUnless(has_module("t40_db1"), "Cannot run *t40_db1* yet")
    def test_t40_db1(self):
        dbname = "tmp/t.db"
        fnames = FirstNames[0:10]
        lnames = LastNames[0:10]
        ages = [ random.randint(30,50) for i in range(10) ]
        fl = []
        ll = []
        la = []
        t40_db1.putData(dbname, fnames, lnames, ages)
        conn = sqlite3.connect(dbname)
        cursor = conn.execute("SELECT * FROM people")
        data = cursor.fetchall()
        for item in data:
            fl.append(item[1])
            ll.append(item[2])
            la.append(item[3])

        self.assertEqual(fl, fnames)
        self.assertEqual(ll, lnames)
        self.assertEqual(la, ages)

    @unittest.skipUnless(has_module("t41_db2"), "Cannot run *t41_db2* yet")
    def test_t41_db2(self):
        import sqlite3

        def getInfoByRegion(dbname, region):
            conn = sqlite3.connect(dbname)
            cursor = conn.execute("SELECT * FROM weather WHERE region = '%s'" % region)
            data = cursor.fetchall()
            return data

        regionlist = ['East Asia', 'South East Asia', 'South Asia']
        region = random.sample(regionlist, 1)[0]
        dbname = "tmp/weather.db"
        data = t41_db2.getInfoByRegion(dbname, region)
        expected = getInfoByRegion(dbname, region)

        self.assertEqual(expected, data)

    @unittest.skipUnless(has_module("t42_db3"), "Cannot run *t42_db3* yet")
    def test_t42_db3(self):
        import sqlite3
        def getAveTempByRegion(dbname, region):
            conn = sqlite3.connect(dbname)
            cursor = conn.execute("SELECT avg(temperature) FROM weather WHERE region = '%s'" % region)

            data = cursor.fetchall()
            return data[0][0]
        
        regionlist = ['East Asia', 'South East Asia', 'South Asia']
        region = random.sample(regionlist, 1)[0]
        dbname = "tmp/weather.db"
        data = t42_db3.getAveTempByRegion(dbname, region)
        expected = getAveTempByRegion(dbname, region)
        
        self.assertEqual(expected, data)        

    @unittest.skipUnless(has_module("t50_xml1"), "Cannot run *t50_xml1* yet")
    def test_t50_xml1(self):
        l = [ {'tle':'title one', 'ath':'author one'}, {'tle':'title two', 'ath':'author two'}, {'tle':'title three', 'ath':'author three'}]
        r = t50_xml1.xmlFromList(l)
        p = etree.parse(StringIO(r))
        authors = p.xpath('//ath/text()')
        authors.sort()
        titles = p.xpath('//tle/text()')
        titles.sort()
        self.assertEqual(titles, ['title one','title three','title two'])
        self.assertEqual(authors, ['author one', 'author three', 'author two'])
    
    @unittest.skipUnless(has_module("t51_xml2"), "Cannot run *t51_xml2* yet")
    def test_t51_xml2(self):
        xml = """<?xml version='1.0' encoding='UTF-8' ?>
        <weather>
            <area>
                <city>Boston</city>
                <temperature>30</temperature>
            </area>
            <area>
                <city>Seattle</city>
                <temperature>55</temperature>
            </area>
            <area>
                <city>Portland</city>
                <temperature>17</temperature>
            </area>
            <area>
                <city>Tucson</city>
                <temperature>42</temperature>
            </area>
        </weather>
        """
        p = etree.parse(StringIO(xml))
        temp = p.xpath("//temperature/text()")
        convertFtoC = lambda x: (x - 32) * 5.0 / 9.0
        result = t51_xml2.xmlDegreeConverter(xml)
        mine = map(convertFtoC, [30, 55, 17, 42])
        self.assertEqual(result, mine)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)

#   vim:expandtab:tabstop=4
