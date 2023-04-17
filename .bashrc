#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Define paths
export PATH=$HOME/.local/bin:$PATH
export PATH=$HOME/.emacs.d/bin:$PATH

PS1='[\u@\h \W]\$ '

eval "$(starship init bash)"

source ~/.qtile_aliases

export NVM_DIR="$HOME/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
