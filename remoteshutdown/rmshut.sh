#!/bin/bash
#!/usr/bin/expect -f 
while [true]; do
	ping -c 5 ipaddr>>/dev/null
	if [$? -eq 0]
	then ssh username@addr -p [portnumber]
		expect "password:"
		sleep 1
		send"password\r"
		'command1'
	else
		sleep 30
	fi
done
