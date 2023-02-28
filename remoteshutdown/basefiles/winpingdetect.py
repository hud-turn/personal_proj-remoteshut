import os

response = None
hostname = "78.255.255.255" #example
response = (os.system("ping " + hostname))

#and then check the response...
print (response)
if response == 1:
      print ("unreachable")
if response == 0:
  print (hostname, 'is not having connectivity issues')
exit