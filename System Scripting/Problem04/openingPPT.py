import win32com.client
import os

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
p.Shapes(1).TextFrame.TextRange.Text = "C307 Test PPT"
p.Shapes(2).TextFrame.TextRange.Text = "Team 6"

p = Presentation.Slides.Add(2, constants.ppLayoutText)
p.Shapes(1).TextFrame.TextRange.Text = "My Custom Title"
p.Shapes(2).TextFrame.TextRange.Text = "The first bullet\r\nThe sub bullet of the first\r\nThe second bullet"
p.Shapes(2).TextFrame.TextRange.Paragraphs(2).IndentLevel = 2
p.Shapes(2).TextFrame.TextRange.Paragraphs(1).Font.Color.RGB = RGB(0,255,0)

# Save the PowerPoint file in the same directory as this Python code
# and name it "mypresentation.pptx"
Presentation.SaveAs(os.getcwd() + "/mypresentation.pptx")