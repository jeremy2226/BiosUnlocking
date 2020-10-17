#!/bin/bash
dpcmd -d
echo "Press any key to continue" 
while [ true ] ; do
read -t 3 -n 1 
if [ $? = 0 ] ; then 
exit ; 
else 
echo 'waiting for the keypress' 
fi 
done
