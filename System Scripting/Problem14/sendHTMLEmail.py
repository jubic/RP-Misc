import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#
msg = MIMEMultipart()
msg['Subject'] = "Test Email"
msg['From'] = "92807@myrp.edu.sg"
msg['To'] = "accidental.wong@gmail.com"
#
textmsg = "<html><body><h1>Test HTML email</h1></body></html>"
textpart = MIMEText(textmsg, 'html')
msg.attach(textpart)
#
s = smtplib.SMTP("blast.sit.rp.sg")
s.sendmail("92807@myrp.edu.sg", "jubic@live.com.sg", msg.as_string())