#!/bin/bash

set -e

echo -e ""
echo -e "========================"
echo -e "=    Stow migration    ="
echo -e "========================"
echo -e ""

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
stow --ignore='pkgs|hypr' .
cd $HOME