#Loading dependencies based off of this link https://www.twilio.com/docs/libraries/python
os.system("sudo apt install python3-pip && pip install twilio")


#We import the Twilio client from the dependency we just installed
from twilio.rest import Client

#The following line needs your Twilio Account SID and Auth Token
client = Client("Twilio Account SID", "Twilio Auth Token")

#Change the "from_" number to your Twilio number and the "to" number
#to the phone number you signed up for Twilio with, or upgrade your
#account to send SMS to any phone number
client.messages.create(to="+12345678901", 
                       from_="+12345678901",
                       body="Hello from Python!")

