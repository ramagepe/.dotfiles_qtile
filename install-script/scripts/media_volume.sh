#!/bin/bash

set -e

# Define colors for printing messages
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

VOLUME_UUID="38c3d749-e70b-433f-a8ff-663e729dbd50"
MOUNT_POINT="/home/ramage/media"
FILESYSTEM_TYPE="btrfs"
OPTIONS="defaults"
DUMP=0
FSCK=0

FSTAB_ENTRY="UUID=${VOLUME_UUID}  ${MOUNT_POINT}  ${FILESYSTEM_TYPE}  ${OPTIONS}  ${DUMP}  ${FSCK}"

# Function to check if the volume is already in /etc/fstab
check_fstab_entry() {
    grep -q "${VOLUME_UUID}" /etc/fstab
}

# Function to add the volume to /etc/fstab
add_fstab_entry() {
    echo -e "${GREEN}Adding volume to /etc/fstab...${NC}"
    echo -e "\n# /dev/nvme1n0 (media)\n${FSTAB_ENTRY}" | sudo tee -a /etc/fstab
    echo -e "${GREEN}Volume added to /etc/fstab successfully!${NC}"
}

# Function to create the mount point if it doesn't exist
create_mount_point() {
    if [ ! -d "${MOUNT_POINT}" ]; then
        echo -e "${GREEN}Creating mount point...${NC}"
        sudo mkdir -p "${MOUNT_POINT}"
        echo -e "${GREEN}Mount point created successfully!${NC}"
    fi
}

# Main script execution
echo -e "============================="
echo -e "=  Add Volume to /etc/fstab  ="
echo -e "============================="
echo -e ""

# Prompt user for adding the volume
read -p "Do you want to add media volume to /etc/fstab? [y/N] " choice
case "$choice" in
    y|Y )
        if check_fstab_entry; then
            echo -e "${RED}Volume is already in /etc/fstab...${NC}"
        else
            create_mount_point
            add_fstab_entry
        fi
    ;;
    * )
        echo -e "${RED}Skipping adding volume to /etc/fstab...${NC}"
    ;;
esac
