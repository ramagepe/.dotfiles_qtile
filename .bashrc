#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Define paths
export PATH=$HOME/.local/bin:$PATH
export PATH=$HOME/go/bin:$PATH

PS1='[\u@\h \W]\$ '

source ~/.aliases
source ~/.env

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH=$BUN_INSTALL/bin:$PATH

# deno
export DENO_INSTALL="/home/ramage/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"

# doom emacs
export PATH=$HOME/.config/emacs/bin:$PATH
export PATH="$HOME/.emacs.d/bin:$PATH"

# rustup
. "$HOME/.cargo/env"

# foundry
export PATH="$PATH:/home/ramage/.config/.foundry/bin"

# nvm
export NVM_DIR="$HOME/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"                   # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion

# starship
eval "$(starship init bash)"
eval "$(~/.local/bin/mise activate bash)"
export HOMELAB_DIR="/home/ramage/code/homelab-remote/homelab"

# Added by LM Studio CLI (lms)
export PATH="$PATH:/home/ramage/.lmstudio/bin"
# End of LM Studio CLI section

