#!/bin/bash
dpcmd --type N25Q128A13 -u HP/850g2/2.bin -v
echo "Press any key to continue" 
while [ true ] ; do
read -t 3 -n 1 
if [ $? = 0 ] ; then 
exit ; 
else 
echo 'waiting for the keypress' 
fi 
done
