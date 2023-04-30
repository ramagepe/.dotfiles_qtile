#!/bin/bash

set -e

echo -e ""
echo -e "========================"
echo -e "=  Theme installation  ="
echo -e "========================"
echo -e ""

read -p "Do you want to install theme icons? [y/N] " choice
case "$choice" in
    y|Y )
        echo "Installing icons..."
        
        # navigate to the extras folder
        cd extras/
        
        # iterate through each .zip file in the folder
        for file in *.zip
        do
            # extract the folder name (without .zip extension)
            folder_name="${file%.zip}"
            
            # extract the .zip file to the current directory
            unzip "$file"
            
            # move the extracted folder to /usr/share/icons with sudo
            sudo mv "$folder_name" /usr/share/icons
        done
    ;;
    * )
        echo "Skipping icons installation..."
    ;;
esac

