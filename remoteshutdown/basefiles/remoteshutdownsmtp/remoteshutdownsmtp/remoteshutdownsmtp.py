import os, smtplib, ssl

#Ping Variables
hostname = "0.0.0.1"
response = os.system("ping -c 5 " + hostname)

#SMTP Variables
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "user@emailaddress.com"  # Enter your address
receiver_email = "user@emailaddress.com"  # Enter receiver address
password = "password"
message = """\
Subject: [Server] Power Failure 

This message is sent from Python."""

print ("The ping command exited with code " + str(response) + ".")
if response == 0:
    pingstatus = "Network Active"
else:
    pingstatus = "The remote host appears to be down, the local machine will\nbe shutting down to prevent corruption of data on this system.\nThis local machine will attempt to send an email to inform\na systems administrator that there has been a power failure\nor fault"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    os.system("shutdown -s +0 'Connection to Remote Host Lost'")
print (pingstatus)