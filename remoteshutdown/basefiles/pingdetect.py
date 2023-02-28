
#Please note that this script is meant to be run on a Linux OS
hostname = "192.168.1.55"
response = os.system("ping -c 5 " + hostname)

print (response)
if response == 0:
    pingstatus = "Network Active"
else:
    pingstatus = "Network Error"
print (pingstatus)