#!/bin/bash
dpcmd --type W25Q128BV -u HP/6570b/2.bin -v
echo "Press any key to continue" 
while [ true ] ; do
read -t 3 -n 1 
if [ $? = 0 ] ; then 
exit ; 
else 
echo 'waiting for the keypress' 
fi 
done
