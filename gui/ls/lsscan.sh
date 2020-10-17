#!/bin/bash
flashrom -p linux_spi:dev=/dev/spidev0.0,spispeed=12000 -VVV
echo "Press any key to continue" 
while [ true ] ; do
read -t 3 -n 1 
if [ $? = 0 ] ; then 
exit ; 
else 
echo 'waiting for the keypress' 
fi 
done
