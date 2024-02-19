#!/bin/bash

# Specify the display number
DISPLAY_NUMBER=1

# Get the current brightness level using ddcutil
current_brightness=$(ddcutil --display "$DISPLAY_NUMBER" getvcp 10 | awk -F'current value = |, max value =' '{gsub(/^[ \t]+|[ \t]+$/, "", $2); print $2}')

# Validate that we have a brightness value
if [ -z "$current_brightness" ] || ! [[ "$current_brightness" =~ ^[0-9]+$ ]]; then
    echo "Failed to get current brightness or invalid brightness value."
    exit 1
fi

# Calculate the new brightness level, ensuring it doesn't go below 0
new_brightness=$((current_brightness + 10))
if [ "$new_brightness" -gt 100 ]; then
    new_brightness=100
fi

# Set the new brightness level using ddcutil
ddcutil --display "$DISPLAY_NUMBER" setvcp 10 "$new_brightness" 2>/dev/null

if [ $? -ne 0 ]; then
    echo "Failed to set new brightness."
    exit 1
else
    notify-send -t 2000 "Brightness Adjusted" "New brightness level: $new_brightness"
    echo "Brightness set to $new_brightness."
fi
