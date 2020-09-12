#!/bin/sh

#Check to see if user is root
if [[ $(/usr/bin/id -u) -ne 0 ]]; then 
    echo "Not running as root" 
    exit 
fi 

# Get current directory
CURR_DIR=`pwd`

# Create a temporary mount point
mkdir ${CURR_DIR}/hp_linuxbios_temp 2> /dev/null

# Mount HP_TOOLS partition
mount -L HP_TOOLS ${CURR_DIR}/hp_linuxbios_temp
if [ $? != 0 ]; then
{
   echo " "
   echo "Failed mounting HP_TOOLS partition."
   echo " "
   echo "Please create a FAT32 partition with the label HP_TOOLS in order to update the BIOS."
   echo " "
   rmdir ${CURR_DIR}/hp_linuxbios_temp
   exit 1
} fi

# Extract BIOS files to HP_TOOLS partition
for i in `ls *.gz`; do
	tar zxf $i -C  ${CURR_DIR}/hp_linuxbios_temp
done

# Unmount HP_TOOLS partition
umount ${CURR_DIR}/hp_linuxbios_temp

# Remove tempoeary directory
rmdir ${CURR_DIR}/hp_linuxbios_temp

echo "Bios files have been transferred to local drive successfully."
echo "To complete the final phase of the Bios Installation, please follow steps below."
echo "1. Upon reboot press the F10 key to boot into your BIOS menu"
echo "2. Check the UPDATE SYSTEM BIOS checkbox"
echo "3. Save the changes and exit. The system will then perform the flashing of the bios"


#####Edit for Linux Bios flashing 
#####
