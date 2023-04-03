# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
setopt autocd extendedglob nomatch
unsetopt beep
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle ':completion:*' menu select

fpath+=~/.zfunc
autoload -Uz compinit && compinit
compinit
# End of lines added by compinstall

# Starship
eval "$(starship init zsh)"

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Define paths
export PATH=$HOME/.local/bin:$PATH
export PATH=$HOME/.emacs.d/bin:$PATH

source ~/.custom_aliases

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"                   # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion

. "$HOME/.cargo/env"
