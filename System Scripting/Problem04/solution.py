import win32com.client
import os
import report_parser

print os.getcwd()

Application = win32com.client.Dispatch("PowerPoint.Application")
Application.Visible = True

# Office 2010 - Generate Python code for "Microsoft PowerPoint 14.0 Object Library"
from win32com.client import gencache
gencache.EnsureModule('{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}', 0, 2, 5)
                                                                            #
# Office 2010 - Generate Python code for "Microsoft PowerPoint 14.0 Object Library"
from win32com.client import gencache
gencache.EnsureModule('{91493440-5A91-11CF-8700-00AA0060263B}', 0, 2, 10)
                                                                            #
# Allow constants from the above objects to be accessible
from win32com.client import constants

def RGB(r,g,b):
    return (b << 16) | (g << 8) | (r)

Presentation = Application.Presentations.Open(os.getcwd() + "/template.pptx")
#
p = Presentation.Slides(1)
p.Shapes(1).TextFrame.TextRange.Text = "Incident Reports"
p.Shapes(2).TextFrame.TextRange.Text = "Support Team"

# "data" is a dictionary indexed by the tags
data = report_parser.process("ex1.txt")
print data["title"]     # prints the title content
print data["date"]      # prints the date
print data["problem"]   # prints the problem
print data["p1"]        # prints description 1
print data["solution"]  # prints the solution
print data["p2"]        # prints description 2

p = Presentation.Slides.Add(2, constants.ppLayoutText)
p.Shapes(1).TextFrame.TextRange.Text = data["title"]
p.Shapes(2).TextFrame.TextRange.Text = data["date"] + "\r\n" + data["problem"] + "\r\n" + data["p1"] + "\r\n" + data["solution"] + "\r\n" + data["p2"]
p.Shapes(2).TextFrame.TextRange.Paragraphs(1).Font.Color.RGB = RGB(255,255,0)
p.Shapes(2).TextFrame.TextRange.Paragraphs(3).IndentLevel = 2
p.Shapes(2).TextFrame.TextRange.Paragraphs(5).IndentLevel = 2

data = report_parser.process("ex2.txt")
print data["title"]     # prints the title content
print data["date"]      # prints the date
print data["problem"]   # prints the problem
print data["p1"]        # prints description 1
print data["solution"]  # prints the solution
print data["p2"]        # prints description 2

p = Presentation.Slides.Add(3, constants.ppLayoutText)
p.Shapes(1).TextFrame.TextRange.Text = data["title"]
p.Shapes(2).TextFrame.TextRange.Text = data["date"] + "\r\n" + data["problem"] + "\r\n" + data["p1"] + "\r\n" + data["solution"] + "\r\n" + data["p2"]
p.Shapes(2).TextFrame.TextRange.Paragraphs(1).Font.Color.RGB = RGB(255,255,0)
p.Shapes(2).TextFrame.TextRange.Paragraphs(3).IndentLevel = 2
p.Shapes(2).TextFrame.TextRange.Paragraphs(5).IndentLevel = 2

data = report_parser.process("ex3.txt")
print data["title"]     # prints the title content
print data["date"]      # prints the date
print data["problem"]   # prints the problem
print data["p1"]        # prints description 1
print data["solution"]  # prints the solution
print data["p2"]        # prints description 2

p = Presentation.Slides.Add(4, constants.ppLayoutText)
p.Shapes(1).TextFrame.TextRange.Text = data["title"]
p.Shapes(2).TextFrame.TextRange.Text = data["date"] + "\r\n" + data["problem"] + "\r\n" + data["p1"] + "\r\n" + data["solution"] + "\r\n" + data["p2"]
p.Shapes(2).TextFrame.TextRange.Paragraphs(1).Font.Color.RGB = RGB(255,255,0)
p.Shapes(2).TextFrame.TextRange.Paragraphs(3).IndentLevel = 2
p.Shapes(2).TextFrame.TextRange.Paragraphs(5).IndentLevel = 2

p = Presentation.Slides.Add(5, constants.ppLayoutObject)
p.Shapes(1).TextFrame.TextRange.Text = "2009 Incident Chart"
pict = p.Shapes.AddPicture(os.getcwd() + "/2009_graph.png",
                              constants.msoFalse, constants.msoTrue, 1, 1, 1)
                                  
Presentation.SaveAs(os.getcwd() + "/incidentReport.pptx")