#!/bin/bash

# Install packages

sudo pacman -S xorg-server xorg-xinit qtile alacritty 
yay -S picom-jonaburg-git starship pywal

pushd slock
sudo make clean install
popd

# Install font

wget https://github.com/ryanoasis/nerd-fonts/blob/e90d082ffc20567093b3d8448e0142f02e996b45/patched-fonts/FiraCode/Regular/complete/Fira%20Code%20Regular%20Nerd%20Font%20Complete.ttf
mv Fira\ Code\ Regular\ Nerd\ Font\ Complete.ttf $HOME/.local/share/fonts/FiraCodeNerdFont.ttf
fc-cache

# Install dotfiles

cp -r .config/* $HOME/.config/
cp -r Backgrounds $HOME/Backgrounds

# Run pywal

wal $HOME/Backgrounds/background.webp