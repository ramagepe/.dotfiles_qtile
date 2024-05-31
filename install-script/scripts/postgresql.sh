#!/bin/bash

set -e

# Define colors for printing messages
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "========================"
echo -e "=  PostgreSQL Setup    ="
echo -e "========================"
echo -e ""

# Function to initialize PostgreSQL database
initialize_postgresql() {
    echo -e "${GREEN}Initializing PostgreSQL database...${NC}"
    sudo -u postgres initdb -D /var/lib/postgres/data
    echo -e "${GREEN}PostgreSQL database initialized successfully!${NC}"
}

# Function to disable Copy-on-Write on PostgreSQL data directory
disable_copy_on_write() {
    echo -e "${GREEN}Disabling Copy-on-Write on PostgreSQL data directory...${NC}"
    sudo -u postgres chattr +C /var/lib/postgres/data
    echo -e "${GREEN}Copy-on-Write disabled successfully!${NC}"
}

# Function to enable PostgreSQL service
enable_postgresql_service() {
    echo -e "${GREEN}Enabling PostgreSQL service...${NC}"
    sudo systemctl enable postgresql.service
    sudo systemctl start postgresql.service
    echo -e "${GREEN}PostgreSQL service enabled successfully!${NC}"
}

# Prompt user for the whole PostgreSQL setup
read -p "Do you want to configure PostgreSQL (initialize database, disable Copy-on-Write, and enable service)? [y/N] " choice
case "$choice" in
    y|Y )
        initialize_postgresql
        disable_copy_on_write
        enable_postgresql_service
    ;;
    * )
        echo -e "${RED}Skipping PostgreSQL setup...${NC}"
    ;;
esac
