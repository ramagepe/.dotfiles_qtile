#!/bin/bash

set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e ""
echo -e "========================"
echo -e "=     Preparations     ="
echo -e "========================"
echo -e ""

#! ---- Update mirrors -------------------

read -p "Do you want to update mirrors? [y/N] " choice
case "$choice" in
    y|Y )
        # Install reflector if not already installed
        if ! command -v reflector &>/dev/null; then
            sudo pacman -S --noconfirm reflector
            if ! command -v reflector &>/dev/null; then
                echo -e "${RED}Failed to install reflector.${NC}"
            else
                echo -e "${GREEN}Reflector is now installed!${NC}"
            fi
        else
            echo -e "${GREEN}Reflector is already installed...${NC}"
        fi
        
        echo -e ""
        echo -e "   Updating Mirrors   "
        echo -e "======================"
        echo -e ""
        
        # Update mirrors
        if command -v reflector &>/dev/null; then
            sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist
        else
            echo "Updating mirrors failed! reflector not installed"
        fi
    ;;
    * )
        echo "Skipping mirrors update..."
    ;;
esac

#! ---- Update system --------------------

read -p "Do you want to update the system? [y/N] " choice
case "$choice" in
    y|Y )
        echo -e ""
        echo -e "   Updating System    "
        echo -e "======================"
        echo -e ""
        
        # Update package lists
        sudo pacman -Sy --noconfirm
    ;;
    * )
        echo "Skipping system update..."
    ;;
esac





