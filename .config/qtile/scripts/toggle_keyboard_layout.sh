#!/bin/bash

# Get the current keyboard layout using xkb-switch
CURRENT_LAYOUT=$(xkb-switch)

# Check if the current layout is 'us'
if [ "$CURRENT_LAYOUT" = "us" ]; then
    # If current layout is 'us', switch to 'es'
    setxkbmap es
    notify-send "ES Keyboard"
else
    # If current layout is not 'us', switch to 'us'
    setxkbmap us
    notify-send "US Keyboard"
fi
