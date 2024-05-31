#!/bin/bash

set -e

# Define colors for printing messages
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "========================"
echo -e "=     GRUB Setup       ="
echo -e "========================"
echo -e ""

# Function to install the GRUB theme
install_grub_theme() {
    REPO_URL="https://github.com/vinceliuice/grub2-themes.git"
    TEMP_DIR=$(mktemp -d)
    
    echo -e "${GREEN}Cloning the GRUB themes repository...${NC}"
    git clone ${REPO_URL} ${TEMP_DIR}
    
    echo -e "${GREEN}Installing the GRUB theme...${NC}"
    cd ${TEMP_DIR}
    echo -e "${GREEN}Running sudo ./install.sh -t vimix -s 1080p...${NC}"
    sudo ./install.sh -t vimix -s 1080p
    
    echo -e "${GREEN}Cleaning up...${NC}"
    rm -rf ${TEMP_DIR}
    
    echo -e "${GREEN}GRUB theme changed successfully!${NC}"
}

# Function to edit grub-btrfsd service
edit_grub_btrfsd_service() {
    SERVICE_FILE="/usr/lib/systemd/system/grub-btrfsd.service"
    
    echo -e "${GREEN}Editing grub-btrfsd service...${NC}"
    sudo sed -i 's|grub-btrfsd --syslog /.snapshots|grub-btrfsd --syslog -t|' "$SERVICE_FILE"
    
    echo -e "${GREEN}grub-btrfsd service edited successfully!${NC}"
}

# Function to generate GRUB configuration
generate_grub_config() {
    echo -e "${GREEN}Generating GRUB configuration...${NC}"
    sudo grub-mkconfig -o /boot/grub/grub.cfg
    echo -e "${GREEN}GRUB configuration generated successfully!${NC}"
}

# Prompt user for GRUB theme installation
read -p "Do you want to install the GRUB theme? [y/N] " choice
case "$choice" in
    y|Y )
        install_grub_theme
    ;;
    * )
        echo -e "${RED}Skipping GRUB theme installation...${NC}"
    ;;
esac

# Prompt user for editing grub-btrfsd service
read -p "Do you want to edit the grub-btrfsd service for Timeshift? [y/N] " choice
case "$choice" in
    y|Y )
        edit_grub_btrfsd_service
    ;;
    * )
        echo -e "${RED}Skipping grub-btrfsd service edit...${NC}"
    ;;
esac

# Prompt user for editing grub-btrfsd service
read -p "Do you want to re-generate the grub config? [y/N] " choice
case "$choice" in
    y|Y )
        generate_grub_config
    ;;
    * )
        echo -e "${RED}Skipping grub config regeneration...${NC}"
    ;;
esac