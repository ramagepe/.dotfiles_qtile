#!/bin/bash

set -e

SCRIPTS_DIR="/home/ramage/.dotfiles/install-script/scripts"

source "${SCRIPTS_DIR}/preps.sh"
source "${SCRIPTS_DIR}/deps.sh"
source "${SCRIPTS_DIR}/stow.sh"
source "${SCRIPTS_DIR}/progs.sh"
source "${SCRIPTS_DIR}/theme.sh"
source "${SCRIPTS_DIR}/daemons.sh"
