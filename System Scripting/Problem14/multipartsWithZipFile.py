import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
#
me = "92807@myrp.edu.sg"
you = "accidental.wong@gmail.com"
#
msg = MIMEMultipart()
msg['Subject'] = "HTML with zipped folder"
msg['From'] = me
msg['To'] = you
#
# HTML message for the email body
html = """
<html>
  <head></head>
  <body>
       <h1>Hello</h1>
    </p>
  </body>
</html>
"""
# Add the HTML text using MIMEText
html = MIMEText(html, 'html')
#
msg.attach(html)
#
zipfile = open("files/mydoc.zip", "rb")
zip = MIMEBase('application', 'zip', name="mydoc.zip")
zip.set_payload(zipfile.read())
zipfile.close()
#
encoders.encode_base64(zip)
msg.attach(zip)
# Send the message
s = smtplib.SMTP("blast.sit.rp.sg")
s.sendmail(me, you, msg.as_string())