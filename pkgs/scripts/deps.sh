#!/bin/bash

set -e

# Define colors for printing messages
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "========================"
echo "= Install dependencies ="
echo "========================"

#! ---- Install more dependencies --------
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

# #! ---- Install rustup --------------------
# # Install Rust using rustup if not already installed
# if ! command -v rustup &>/dev/null; then
#     curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
#     source $HOME/.cargo/env
# else
#     echo -e "${GREEN}rustup is already installed${NC}"
# fi

#! ---- Install paru --------------------
# Clone and install paru if not already installed
if ! command -v paru &>/dev/null; then
    git clone https://aur.archlinux.org/paru.git $HOME/.local/share/paru
    cd $HOME/.local/share/paru
    makepkg -si --noconfirm
    cd -
else
    echo -e "${GREEN}paru is already installed${NC}"
fi

#! ---- Install nvm + node --------------
# Install nvm if not already installed
if [ ! -d "$HOME/.nvm" ]; then
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
    source $HOME/.bashrc
else
    echo -e "nvm is already installed"
fi

#! ---- Install node --------------
if [ ! -d "$HOME/.npm" ]; then
    nvm install node
else
    echo -e "node is already installed"
fi
