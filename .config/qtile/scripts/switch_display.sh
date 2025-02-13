#!/bin/bash

DISPLAY_NUMBER=1
DP_SYSTEM="ramage@192.168.1.45"

# Prevent infinite SSH loop
if [[ -n "$SSH_TTY" && "$HOSTNAME" == "displayport-system" ]]; then
  echo "Already running remotely on DisplayPort. Not SSHing again."
else
  if ddcutil detect | grep -q "Display 1"; then
    echo "Running locally on DisplayPort system."

    current_input=$(ddcutil --display "$DISPLAY_NUMBER" getvcp 60 2>/dev/null | grep -oP 'sl=0x\K[0-9a-fA-F]+')

    if [ -z "$current_input" ]; then
      echo "Error: Could not read current input source. Exiting."
      exit 1
    fi

    echo "Current input source: $current_input"

    DP_INPUT="0f"   # DisplayPort-1
    HDMI_INPUT="11"  # HDMI-1

    if [ "$current_input" == "$DP_INPUT" ]; then
      new_input=$HDMI_INPUT
    else
      new_input=$DP_INPUT
    fi

    ddcutil --display "$DISPLAY_NUMBER" setvcp 60 0x"$new_input" 2>/dev/null

    if [ $? -eq 0 ]; then
      notify-send -t 2000 "Input Switched" "New input source: $new_input"
      echo "Switched to input $new_input."
    else
      echo "Failed to switch input."
      exit 1
    fi
  else
    echo "Running on HDMI system, sending command to DisplayPort system via SSH."
    /usr/bin/ssh -o IdentitiesOnly=yes -i ~/.ssh/id_ed25519 "$DP_SYSTEM" "bash ~/.config/qtile/scripts/switch_display.sh"
  fi
fi
