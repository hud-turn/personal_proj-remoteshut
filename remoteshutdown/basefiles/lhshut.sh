#!/bin/bash
#!/usr/bin/expect -f 
while [true]; do
	ping -c 5 ipaddr>>/dev/null
	if [$? -eq 0]
	then shutdown
	else
		sleep 30
	fi
done
