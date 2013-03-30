from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import glob
import os.path
import zipfile
import os
import smtplib
#
sender = "92807@myrp.edu.sg"
recipient = "92807@myrp.edu.sg"
#
msg = MIMEMultipart()
msg['Subject'] = "Sendbox"
msg['From'] = sender
msg['To'] = recipient
# Getting the names of the files
cvs = glob.glob("*.docx")
images = glob.glob("*.png")
#
names=[]
for image in images:
    imagename = os.path.basename(image)
    (name, ext) = imagename.split('.')
    names = names + [name]
# HTML message for the email body
html = """
<html>
    <body>
        <h1>Candidates</h1>
        <h3>"""+names[0]+"""</h3>
        <img src=cid:image1>
        <h3>"""+names[1]+"""</h3>
        <img src=cid:image2>
    </body>
</html>
"""
# Add the HTML text using MIMEText
html = MIMEText(html, 'html')
#
msg.attach(html)
# Open the "*.png" images
f1 = open('Odin Jobseeker.png', "rb")
f2 = open('Thor Job Hunter.png', "rb")
# Create the MIMEImage object
img1 = MIMEImage(f1.read())
img2 = MIMEImage(f2.read())
# Note how "<image1>" below for Content-ID match the HTML "src" above
img1.add_header('Content-ID', '<image1>')
img2.add_header('Content-ID', '<image2>')
# Always close after done reading
f1.close()
f2.close()
# Set it to be viewed "inline"
img1.add_header('Content-Disposition', 'inline', filename='Odin Jobseeker.png')
img2.add_header('Content-Disposition', 'inline', filename='Thor Job Hunter.png')
msg.attach(img1)
msg.attach(img2)
#
def zipper(zipname, files):
    z = zipfile.ZipFile(zipname, 'w')
    for f in files:
        z.write(f)
    z.close()

zipper("cv.zip", cvs)
zipfile = open("cv.zip","rb")
zip = MIMEBase('application', 'zip', name="cv.zip")
zip.set_payload(zipfile.read())
zipfile.close()
#
encoders.encode_base64(zip)
msg.attach(zip)
# File deletion
def delete_files(files):
    for f in files:
        os.remove(f)

files = [cvs, images]
delete_files(files)
# Send the message
s = smtplib.SMTP("blast.sit.rp.sg")
s.sendmail(sender, recipient, msg.as_string())