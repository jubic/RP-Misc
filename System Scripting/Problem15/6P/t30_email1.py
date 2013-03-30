"""
h2. Email with Zip attachments

Create a function @mailZip@ that takes a list as an argument. The list contains the location of the zip files that must be attached to an email message object. Therefore, attach those files to an email object.

The function should return the @MIMEMultipart@ object. The sender, recipient and subject don't matter.

You can use the following list: @['tmp/doc1.zip', 'tmp/doc2.zip']@ (the files are in the "tmp":files/tmp directory).

*Note:* you don't need to send the email. Just create the email object only.
"""

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.parser import Parser 

def mailZip(l):
	msg = MIMEMultipart()
	# your code here
	for f in l:
		zipfile = open(f, "rb")  
		zip = MIMEBase('application', 'zip', name=f)
		zip.set_payload(zipfile.read())
		zipfile.close()
		#
		encoders.encode_base64(zip)
		msg.attach(zip)

	# return the msg object
	return msg

if __name__ == '__main__':
	a = mailZip(['tmp/doc1.zip', 'tmp/doc2.zip']) 
	print str(a)

