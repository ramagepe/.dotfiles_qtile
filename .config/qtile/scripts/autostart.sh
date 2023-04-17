#!/bin/bash

# Add your application commands in the "applications" array
applications=(
	"brave"
	"thunderbird"
	"discord"
	"steam"
)

# Check for internet connection by pinging Google DNS server
while true; do
	if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
		# echo "Internet connection detected. Starting the applications."

		# Start each application in the array
		for app in "${applications[@]}"; do
			# echo "Starting $app"
			$app &
		done

		# Wait for all applications to finish
		wait

		break
	else
		# echo "No internet connection detected. Waiting and retrying..."
		sleep 5
	fi
done
