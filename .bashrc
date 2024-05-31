#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Define paths
export PATH=$HOME/.local/bin:$PATH

PS1='[\u@\h \W]\$ '

source ~/.aliases

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH=$BUN_INSTALL/bin:$PATH

# deno
export DENO_INSTALL="/home/ramage/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"

# doom emacs
export PATH=$HOME/.config/emacs/bin:$PATH

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
