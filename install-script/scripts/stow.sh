#!/bin/bash

set -e

echo -e ""
echo -e "========================"
echo -e "=    Stow migration    ="
echo -e "========================"
echo -e ""


#! ---- Install stow --------------------

read -p "Do you want to install stow? [y/N] " choice
case "$choice" in
    y|Y )
        echo "Installing stow..."
        
        # Install stow if not already installed
        if ! command -v stow &>/dev/null; then
            sudo pacman -S --noconfirm stow
        else
            echo -e "${GREEN}stow is already installed${NC}"
        fi
    ;;
    * )
        echo "Skipping stow installation..."
    ;;
esac

#! ---- Stow --------------------

read -p "Do you want to stow? [y/N] " choice
case "$choice" in
    y|Y )
        echo "Stowing..."
        
        # Remove conflicts
        if [ -f "$HOME/.bashrc" ]; then
            rm $HOME/.bashrc
        fi
        
        if [ -d "$HOME/.config/qtile" ]; then
            rm -r "$HOME/.config/qtile"
        fi
        
        # Run stow on the .dotfiles directory, ignoring pkgs and extras
        cd $HOME/.dotfiles
        stow --ignore='install-script' .
        cd $HOME
    ;;
    * )
        echo "Skipping stow..."
    ;;
esac
