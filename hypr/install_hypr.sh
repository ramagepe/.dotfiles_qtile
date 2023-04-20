#!/bin/bash

# Read list of programs from YAML file
programs=$(yq -r '.programs[]' deps.yml)

# Install programs that are not already installed
for program in $programs; do
	if ! pacman -Qi "$program" &>/dev/null; then
		paru -S --noconfirm "$program"
	else
		echo "$program is already installed"
	fi
done
