#!/bin/bash
#!/usr/bin/expect -f
echo "Checking internet connectivity..."
ping -c 5 192.168.1.250>>/dev/null
if [ $? -eq  0 ]
then
echo "Able to reach internet, yay!"
else
echo " Not able to check internet connectivity!"
fi
