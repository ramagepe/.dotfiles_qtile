#!/bin/bash

chosen=$(echo -e " Power Off\n Reboot\n Suspend\n Lock" | rofi -dmenu -p "Power Menu")

case "$chosen" in
    " Power Off") systemctl poweroff ;;
    " Reboot") systemctl reboot ;;
    " Suspend") systemctl suspend ;;
    " Lock") i3lock-fancy ;;  # Change to your lockscreen (e.g., betterlockscreen, i3lock)
esac
