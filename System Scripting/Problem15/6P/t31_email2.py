"""
h2. Mail with Two Image Attachments

Write a function @mailImages@ that takes a list of image files to be attached on an email. The function should return the @MIMEMultipart@ email object.

Additionally, your email must have:

# From: joe@nopoly.dom
# To: bob@nopoly.dom
# Subject: Two Images
# The images are, and the order is important, "tmp/pythonlogo.jpg" and "tmp/friendly.jpg" (don't use any other images)
# The HTML string is given in @Html@ variable. Please use this. Also note that you must use @<img src ... >@ link. Your image attachment must have correct "Content-ID"
# The Content-Disposition for the images must be "inline"
"""

from email import encoders
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.parser import Parser 

Html = "<html><body><img src='cid:file1'><br /><img src='cid:file2'></body></html>"

def mailImages(l):
	msg = MIMEMultipart()
	# your code here
	html = MIMEText(Html, "html")
	msg.attach(html)
	msg['From'] = "joe@nopoly.dom"
	msg['To'] = "bob@nopoly.dom"
	msg["Subject"] = "Two Images"

	for i in range(len(l)):
		imgfile = open(l[i], "rb")  
		img = MIMEImage(imgfile.read())
		imgfile.close()
		img.add_header("Content-Disposition", "inline",  filename=l[i])
		img.add_header("Content-ID", "<file" + str(i + 1) + ">")
		#
		msg.attach(img)

	return msg

if __name__ == '__main__':
	msg = mailImages(["tmp/pythonlogo.jpg", "tmp/friendly.jpg"])

