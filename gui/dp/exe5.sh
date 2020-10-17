#!/bin/bash
dpcmd --type W25Q64BV -u Dell/e6440/8.bin -v
echo "Press any key to continue" 
while [ true ] ; do
read -t 3 -n 1 
if [ $? = 0 ] ; then 
exit ; 
else 
echo 'waiting for the keypress' 
fi 
done
