#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Define paths
export PATH=$HOME/.local/bin:$PATH

PS1='[\u@\h \W]\$ '

eval "$(starship init bash)"

source ~/.aliases

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH=$BUN_INSTALL/bin:$PATH

# doom emacs
export PATH=$HOME/.config/emacs/bin:$PATH
. "$HOME/.cargo/env"

export PATH="$PATH:/home/ramage/.config/.foundry/bin"

export NVM_DIR="$HOME/.config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"                   # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/ramage/miniconda3/bin/conda' 'shell.bash' 'hook' 2>/dev/null)"
if [ $? -eq 0 ]; then
	eval "$__conda_setup"
else
	if [ -f "/home/ramage/miniconda3/etc/profile.d/conda.sh" ]; then
		. "/home/ramage/miniconda3/etc/profile.d/conda.sh"
	else
		export PATH="/home/ramage/miniconda3/bin:$PATH"
	fi
fi
unset __conda_setup
# <<< conda initialize <<<
