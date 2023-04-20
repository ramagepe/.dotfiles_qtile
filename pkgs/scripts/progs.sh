#!/bin/bash

set -e

# Define colors for printing messages
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "========================"
echo -e "=   Install  Programs  ="
echo -e "========================"
# Install programs that are not already installed

#! ---- Install programs from list ------
# Check if programs.yml file exists
if [ ! -f "$HOME/.dotfiles/pkgs/programs.yml" ]; then
    echo "${RED}programs.yml not found!${NC}"
else
    # Install programs that are not already installed
    while read program; do
        if ! pacman -Qi "$program" &>/dev/null; then
            paru -S --noconfirm "$program"
            if [ $? -eq 0 ]; then
                echo -e "${GREEN}$program installed successfully!${NC}"
            else
                echo -e "${RED}$program installation failed${NC}"
            fi
        else
            echo -e "${GREEN}$program is already installed...${NC}"
        fi
    done < <(yq -r '.programs[]' $HOME/.dotfiles/pkgs/programs.yml)
fi


#! ---- Install neovim + extensions -----
# Check if LazyVim is not already installed
if [ ! -f "$HOME/.config/nvim/init.lua" ]; then
    # Remove existing Neovim directories if they exist
    if [ -d "$HOME/.config/nvim" ]; then
        rm -rf $HOME/.config/nvim
    fi
    if [ -d "$HOME/.local/share/nvim" ]; then
        rm -rf $HOME/.local/share/nvim
    fi
    if [ -d "$HOME/.local/state/nvim" ]; then
        rm -rf $HOME/.local/state/nvim
    fi
    
    # Clone LazyVim starter repository and remove .git directory
    git clone https://github.com/LazyVim/starter $HOME/.config/nvim
    rm -rf $HOME/.config/nvim/.git
else
    echo -e "${GREEN}LazyVim is already installed...${NC}"
fi

# Install Python extension
if ! pip show pynvim &>/dev/null; then
    pip install pynvim
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}pynvim installed successfully!${NC}"
    else
        echo -e "${RED}pynvim installation failed${NC}"
    fi
else
    echo -e "${GREEN}pynvim is already installed...${NC}"
fi

# Check if node package neovim is installed
if ! command -v npm &>/dev/null; then
    echo "${RED}node is not installed${NC}"
else
    if ! npm list -g neovim &>/dev/null; then
        # Install neovim extension
        npm install -g neovim
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}neovim-node installed successfully!${NC}"
        else
            echo -e "${RED}neovim-node installation failed${NC}"
        fi
    else
        echo -e "${GREEN}neovim-node is already installed...${NC}"
    fi
fi
