import smtplib
#
s = smtplib.SMTP("blast.sit.rp.sg")
msg = "Hello, C307 Test"
s.sendmail("92807@myrp.edu.sg", "accidental.wong@gmail.com", msg)