#!/bin/bash

set -e

echo "========================"
echo "=   Install Programs   ="
echo "========================"
# Install programs that are not already installed

#! ---- Install programs from list ------
# Check if programs.yml file exists
if [ ! -f "$HOME/.dotfiles/pkgs/programs.yml" ]; then
    echo "programs.yml not found!"
else
    # Install programs that are not already installed
    while read program; do
        if ! pacman -Qi "$program" &>/dev/null; then
            paru -S --noconfirm "$program"
        else
            echo "$program is already installed"
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
    echo "LazyVim is already installed"
fi

# Install Python extension
if ! pip show pynvim &>/dev/null; then
    pip install pynvim
else
    echo "pynvim is already installed"
fi

# Check if node package neovim is installed
if ! command -v npm &>/dev/null; then
    echo "node not installed"
else
    if ! npm list -g neovim &>/dev/null; then
        # Install neovim extension
        npm install -g neovim
    else
        echo "neovim package is already installed"
    fi
fi