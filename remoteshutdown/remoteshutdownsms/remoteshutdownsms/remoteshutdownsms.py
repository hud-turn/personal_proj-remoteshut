import os
#Loading dependencies based off of this link https://www.twilio.com/docs/libraries/python
os.system("sudo apt install python3-pip && pip install twilio")

#Ping Variables you will change the host name to the client you want to reach
hostname = "0.0.0.1"
response = os.system("ping -c 5 " + hostname)

#We import the Twilio client from the dependency we just installed
from twilio.rest import Client

#The following line needs your Twilio Account SID and Auth Token
twilio_account_sid = "Twilio Account SID"
twilio_auth_token = "Twilio Authentication Token"

client = Client(twilio_account_sid, twilio_auth_token)

#Change the "from_" number to your Twilio number and the "to" number
#to the phone number you signed up for Twilio with, or upgrade your

print ("The ping command exited with code " + str(response) + ".")
if response == 0:
    pingstatus = "Network Active"
else:
    pingstatus = "The remote host appears to be down, the local machine will\nbe shutting down to prevent corruption of data on this system.\nThis local machine will attempt to send an email to inform\na systems administrator that there has been a power failure\nor fault"
    # account to send SMS to any phone number
    client.messages.create(to="+12345678901",
                        from_="+12345678901",
                        body=pingstatus)
    #os.system("shutdown -s +0 'Connection to Remote Host Lost'")
    #This line is commented out and mus be uncommented in order to allow for the OS to shut down.
print (pingstatus)



