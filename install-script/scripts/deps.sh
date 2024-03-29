#!/bin/bash

set -e

# Define colors for printing messages
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e ""
echo -e "========================"
echo -e "= Install dependencies ="
echo -e "========================"
echo -e ""

#! ---- Install core dependencies --------

read -p "Do you want to install needed dependencies? [y/N] " choice
case "$choice" in
    y|Y )
        echo "Installing dependencies..."
        
        # Install stow if not already installed
        if ! command -v stow &>/dev/null; then
            sudo pacman -S --noconfirm stow
        else
            echo -e "${GREEN}stow is already installed${NC}"
        fi
        
        # Install curl if not already installed
        if ! command -v curl &>/dev/null; then
            sudo pacman -S --noconfirm curl
        else
            echo -e "${GREEN}curl is already installed${NC}"
        fi
        
        # Install yq if not already installed
        if ! type yq &>/dev/null; then
            sudo pacman -S --noconfirm yq
        else
            echo -e "${GREEN}yq is already installed${NC}"
        fi
        
        # Install base-devel if not already installed
        if ! pacman -Qqg base-devel &>/dev/null; then
            sudo pacman -S --noconfirm base-devel
        else
            echo -e "${GREEN}base-devel is already installed${NC}"
        fi
    ;;
    * )
        echo "Skipping dependencies installation..."
    ;;
esac

#! ---- Install rustup --------------------

read -p "Do you want to install rustup? [y/N] " choice
case "$choice" in
    y|Y )
        echo "Installing rustup..."
        
        # Install Rust using rustup if not already installed
        if ! command -v rustup &>/dev/null; then
            curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
            source $HOME/.cargo/env
        else
            echo -e "${GREEN}rustup is already installed${NC}"
        fi
    ;;
    * )
        echo "Skipping rustup installation..."
    ;;
esac

#! ---- Install paru --------------------

read -p "Do you want to install paru? [y/N] " choice
case "$choice" in
    y|Y )
        echo "Installing paru..."
        
        # Clone and install paru if not already installed
        if ! command -v paru &>/dev/null; then
            git clone https://aur.archlinux.org/paru.git $HOME/.local/share/paru
            cd $HOME/.local/share/paru
            makepkg -si --noconfirm
            cd -
        else
            echo -e "${GREEN}paru is already installed${NC}"
        fi
    ;;
    * )
        echo "Skipping paru installation..."
    ;;
esac

#! ---- Install nvm + node --------------

read -p "Do you want to install nvm + node? [y/N] " choice
case "$choice" in
    y|Y )
        echo "Installing nvm + node..."
        
        # Install nvm if not already installed
        if [ ! -d "$HOME/.nvm" ]; then
            curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
            source $HOME/.bashrc
        else
            echo -e "nvm is already installed"
        fi
        
        # Install node if not already installed
        if [ ! -d "$HOME/.npm" ]; then
            nvm install node
        else
            echo -e "node is already installed"
        fi
    ;;
    * )
        echo "Skipping nvm + node installation..."
    ;;
esac
