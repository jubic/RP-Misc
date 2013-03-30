import smtplib
import zipfile
import glob
import os.path
import os
import time

from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase

WatchDir = "sendbox/"
SMTPServer = "blast.sit.rp.sg"
Sender = "andrew_hadinyoto@rp.sg"
Recipient = Sender
Subject = "Shortlisted Candidates @ " + time.ctime()
ZipFileName = "cv.zip"

def zipper(zipname, files):
    z = zipfile.ZipFile(zipname, 'w')
    for f in files:
        z.write(f)
    z.close()

def sendmail(sender, recipient, email):
    email['Subject'] = Subject
    email['From'] = sender
    email['To'] = recipient
    m = smtplib.SMTP(SMTPServer)
    m.sendmail(Sender, Recipient, email.as_string())
    
def list_files_by_extension(filelist, ext):
    files = []
    for f in filelist:
        (filename, fileext) = os.path.basename(f).split('.')
        if fileext.lower() == ext:
            files.append(f)
    return files

def delete_files(files):
    for f in files:
        os.remove(f) 

def handle_images(email, files):
    imgsrc = ""
    imagefiles = list_files_by_extension(files, 'png')
    print "List of images", imagefiles
    count = 0
    for filename in imagefiles:
        filename = os.path.basename(filename)
        (filename, ext) = filename.split('.')
        imgsrc += "<h2>%s</h2><img src='cid:image%d'><p/>" % (filename, count)
        count += 1

    html = "<html><body><h1>Candidates</h1>%s</body></html>" % imgsrc
    htmlpart = MIMEText(html, 'html')
    email.attach(htmlpart)

    count = 0
    for filename in imagefiles:
        f = open(filename, "rb")
        img = MIMEImage(f.read(), name=os.path.basename(filename))
        f.close()
        img.add_header('Content-ID', '<image%d>' % count)
        img.add_header('Content-Disposition', 'inline', filename=os.path.basename(filename))
        email.attach(img)
        count += 1

    delete_files(imagefiles)

def handle_docs(email, files):
    # Assume zipper always succeed
    docfiles = list_files_by_extension(files, 'docx')
    print "List of document files", docfiles
    zipper(ZipFileName, docfiles)

    zipfile = open(ZipFileName, "rb")  
    zip = MIMEBase('application', 'zip', name=ZipFileName)
    zip.set_payload(zipfile.read())
    zipfile.close()

    encoders.encode_base64(zip)
    email.attach(zip)

    delete_files(docfiles)

email = MIMEMultipart()

files = glob.glob(WatchDir + "*")
if len(files) > 0:
    print "* Processing..."
    handle_images(email, files)
    handle_docs(email, files)
    sendmail(Sender, Recipient, email)
    print "* Done processing"


#   vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
