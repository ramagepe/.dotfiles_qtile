#!/bin/bash

set -e

echo "========================"
echo "=    Stow migration    ="
echo "========================"

#! ---- Remove stow conflicts -----------
# Remove $HOME/.bashrc if it exists
if [ -f "$HOME/.bashrc" ]; then
    rm $HOME/.bashrc
fi

if [ -f "$HOME/.xprofile" ]; then
    rm $HOME/.xprofile
fi

if [ -d "$HOME/.config/qtile" ]; then
    rm -r "$HOME/.config/qtile"
fi

if [ -d "$HOME/.config/redshift" ]; then
    rm -r "$HOME/.config/redshift"
fi

#! ---- Run stow ------------------------
# Run stow on the .dotfiles directory, ignoring pkgs and extras
cd $HOME/.dotfiles
stow --ignore='pkgs' .
cd $HOME