#!/bin/bash

set -e

echo -e ""
echo -e "========================"
echo -e "=   Enabling services  ="
echo -e "========================"
echo -e ""

read -p "Do you want to enable/start services? [y/N] " choice
case "$choice" in
y | Y)
	echo "Enabling and starting services..."

	services=("bluetooth.service" "NetworkManager.service" "grub-btrfsd")

	for service in "${services[@]}"; do
		if ! systemctl is-active --quiet "$service"; then
			sudo systemctl enable "$service"
			sudo systemctl start "$service"
			echo "$service has been enabled and started."
		else
			echo "$service is already running."
		fi
	done
	;;
*)
	echo "Skipping services..."
	;;
esac
