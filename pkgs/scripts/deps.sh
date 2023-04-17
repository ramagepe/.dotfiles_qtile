#!/bin/bash

set -e

echo "========================"
echo "= Install dependencies ="
echo "========================"

#! ---- Install more dependencies --------
# Install stow if not already installed
if ! command -v stow &>/dev/null; then
    sudo pacman -S --noconfirm stow
else
    echo "stow is already installed"
fi

# Install curl if not already installed
if ! command -v curl &>/dev/null; then
    sudo pacman -S --noconfirm curl
else
    echo "curl is already installed"
fi

# Install yq if not already installed
if ! type yq &>/dev/null; then
    sudo pacman -S --noconfirm yq
else
    echo "yq is already installed"
fi

# Install base-devel if not already installed
if ! pacman -Qqg base-devel &>/dev/null; then
    sudo pacman -S --noconfirm base-devel
else
    echo "base-devel is already installed"
fi

#! ---- Install rustup --------------------
# Install Rust using rustup if not already installed
if ! command -v rustup &>/dev/null; then
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    source $HOME/.cargo/env
else
    echo "rustup is already installed"
fi

#! ---- Install paru --------------------
# Clone and install paru if not already installed
if ! command -v paru &>/dev/null; then
    git clone https://aur.archlinux.org/paru.git $HOME/.local/share/paru
    cd $HOME/.local/share/paru
    makepkg -si --noconfirm
    cd -
else
    echo "paru is already installed"
fi

#! ---- Install nvm + node --------------
# Install nvm if not already installed
if [ ! -d "$HOME/.nvm" ]; then
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
    [ -f "$HOME/.bashrc" ] && source $HOME/.bashrc
    [ -f "$HOME/.zshrc" ] && source $HOME/.zshrc
else
    echo "nvm is already installed"
fi

#! ---- Install node --------------
if [ ! -d "$HOME/.npm" ]; then
    nvm install --lts
    nvm install node
else
    echo "node is already installed"
fi