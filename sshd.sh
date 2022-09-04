echo "Enter the port number you want"
read PORTNUM
if  [ ${PORTNUM} -gt 0 ] && [ ${PORTNUM} -lt 65536 ] 
then
	echo " The entered port number is accepted"
else
	echo " The entered port number is out of range"
fi
