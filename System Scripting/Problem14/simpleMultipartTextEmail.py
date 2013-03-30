import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#
msg = MIMEMultipart()
msg['Subject'] = "Test Email"
msg['From'] = "92807@myrp.edu.sg"
msg['To'] = "accidental.wong@gmail.com"
#
textmsg = "Test mail"
textpart = MIMEText(textmsg, 'text')
#
msg.attach(textpart)
#
s = smtplib.SMTP("blast.sit.rp.sg")
s.sendmail("92807@myrp.edu.sg", "jubic@live.com.sg", msg.as_string())