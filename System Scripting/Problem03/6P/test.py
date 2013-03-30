import unittest
import convert

class TestConvertTextileToHtml(unittest.TestCase):

    def test_title(self):
        p = convert.title("title: olah")
        self.assertEqual("<h1>olah</h1>", p)

    def test_problem(self):
        p = convert.problem("problem: olah")
        self.assertEqual("<h2 id='problem'>olah</h2>", p)

    def test_solution(self):
        p = convert.solution("solution: olah")
        self.assertEqual("<h2 id='solution'>olah</h2>", p)

    def test_name(self):
        p = convert.name("name: joe blow")
        self.assertEqual("<h3 id='name'>joe blow</h3>", p)

    def test_date(self):
        p = convert.date("date: 2001/12/30 11:55 - 13:55")
        self.assertEqual("<h3 id='date'>2001/12/30 11:55 - 13:55</h3>", p)

    def test_p(self):
        p = convert.p("p: paragraph test one two three")
        self.assertEqual("<p>paragraph test one two three</p>", p)

    def test_b(self):
        p = convert.bold("* blah quiver *")
        self.assertEqual("<b> blah quiver </b>", p)

    def test_b_multiple_in_a_line(self):
        p = convert.bold("*blah* space nothing *quiver* strange")
        self.assertEqual("<b>blah</b> space nothing <b>quiver</b> strange", p)

    def test_b_with_p(self):
        p = convert.bold("p: nope *blah* and *quiver*")
        p = convert.p(p)
        self.assertEqual("<p>nope <b>blah</b> and <b>quiver</b></p>", p)

    def test_i(self):
        p = convert.italic("_ blah quiver _")
        self.assertEqual("<i> blah quiver </i>", p)
    
    def test_i_multiple_in_a_line(self):
        p = convert.italic("_blah_ space nothing _quiver_ strange")
        self.assertEqual("<i>blah</i> space nothing <i>quiver</i> strange", p)

    def test_i_with_p(self):
        p = convert.italic("p: nope _blah_ and _quiver_")
        p = convert.p(p)
        self.assertEqual("<p>nope <i>blah</i> and <i>quiver</i></p>", p)

    def test_ol(self):
        s = """list: 
# p1
# p2
# p3

"""
        p = convert.ol(s)
        self.assertEqual("<ol>\n\t<li>p1</li>\n\t<li>p2</li>\n\t<li>p3</li>\n</ol>\n\n", p)
        #self.assertTrue(True)
            
if __name__ == "__main__":
    unittest.main()

#    vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
