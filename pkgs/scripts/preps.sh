#!/bin/bash

set -e

echo "========================"
echo "=     Preparations     ="
echo "========================"

#! ---- Install mirror dependency --------
# Install reflector if not already installed
if ! command -v reflector &>/dev/null; then
    sudo pacman -S --noconfirm reflector
else
    echo "reflector is already installed"
fi

#! ---- Update mirrors -------------------
# Update mirrors
if command -v reflector &>/dev/null; then
    sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist
else
    echo "Updating mirrors failed! reflector not installed"
fi

#! ---- Update system --------------------
# Update package lists
sudo pacman -Sy --noconfirm