import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#
me = "92807@myrp.edu.sg"
you = "accidental.wong@gmail.com"
#
msg = MIMEMultipart()
msg['Subject'] = "HTML with an image"
msg['From'] = me
msg['To'] = you
#
# HTML message for the email body
html = """
<html>
  <head></head>
  <body>
       <h1>Hello</h1>
       <img src='cid:image1'>
    </p>
  </body>
</html>
"""
# Add the HTML text using MIMEText
html = MIMEText(html, 'html')
#
msg.attach(html)
#
# Open the "chart.png" image (the file is in "files" directory)
f = open('files/chart.png', "rb")
# Create the MIMEImage object
img = MIMEImage( f.read() )
# Note how "<image1>" below for Content-ID match the HTML "src" above
img.add_header('Content-ID', '<image1>')
# Always close after done reading
f.close()
# Set it to be viewed "inline"
img.add_header('Content-Disposition', 'inline', filename='chart.png')
msg.attach(img)
#
# Send the message
s = smtplib.SMTP("blast.sit.rp.sg")
s.sendmail(me, you, msg.as_string())