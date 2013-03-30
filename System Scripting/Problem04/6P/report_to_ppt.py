import win32com.client
import os
import report_parser
import glob

# Office 2007 - Generate Python code for "Microsoft Office Object 12.0 Object Library" 
#from win32com.client import gencache
#gencache.EnsureModule('{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}', 0, 2, 4)

# Office 2007 - Generate Python code for "Microsoft PowerPoint 12.0 Object Library"
#from win32com.client import gencache
#gencache.EnsureModule('{91493440-5A91-11CF-8700-00AA0060263B}', 0, 2, 9)

# Office 2010 - Generate Python code for "Microsoft PowerPoint 14.0 Object Library"
from win32com.client import gencache
gencache.EnsureModule('{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}', 0, 2, 5)

# Office 2010 - Generate Python code for "Microsoft PowerPoint 14.0 Object Library"
from win32com.client import gencache
gencache.EnsureModule('{91493440-5A91-11CF-8700-00AA0060263B}', 0, 2, 10)

# Allow constants from the above objects to be accessible
from win32com.client import constants

Files = glob.glob("ex*.txt")
Data = []
for file in Files:
    Data.append(report_parser.process(file))

Application = win32com.client.Dispatch("PowerPoint.Application")
Application.Visible = True

Presentation = Application.Presentations.Open(os.getcwd() + "/template.pptx")

# s variable stands for "Slide"
s = Presentation.Slides(1)
s.Shapes(1).TextFrame.TextRange.Text = "Incident Reports"
s.Shapes(2).TextFrame.TextRange.Text = "Support Team"

def RGB(r,g,b):
    return (b << 16) | (g << 8) | (r)

count = 2
for d in Data:
    
    s = Presentation.Slides.Add(count, constants.ppLayoutText)
    s.Shapes(1).TextFrame.TextRange.Text = d['title']
    s.Shapes(2).TextFrame.TextRange.Text = ( d['date'] + "\r\n"  + 
                                           d['problem'] + "\r\n" +   
                                           d['p1'] + "\r\n" +
                                           d['solution'] + "\r\n"  + 
                                           d['p2'] )
    s.Shapes(2).TextFrame.TextRange.Paragraphs(3).IndentLevel = 2
    s.Shapes(2).TextFrame.TextRange.Paragraphs(5).IndentLevel = 2
    s.Shapes(2).TextFrame.TextRange.Paragraphs(1).Font.Color.RGB = RGB(255,255,0)
    count += 1
    

s = Presentation.Slides.Add(5, constants.ppLayoutObject)
s.Shapes(1).TextFrame.TextRange.Text = "2009 Incident Chart"
pict = s.Shapes.AddPicture(os.getcwd() + "/2009_graph.png", 
                            constants.msoFalse, constants.msoTrue, 1, 1, 1, 1)

Presentation.SaveAs(os.getcwd() + "/test_output.pptx")