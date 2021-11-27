#!/bin/bash

# Install packages

sudo pacman -S --needed xorg-server xorg-xinit qtile alacritty libwebp wget feh
yay -S picom-jonaburg-git starship

pushd slock
sudo make clean install
popd

# Install font

wget https://github.com/ryanoasis/nerd-fonts/blob/e90d082ffc20567093b3d8448e0142f02e996b45/patched-fonts/FiraCode/Regular/complete/Fira%20Code%20Regular%20Nerd%20Font%20Complete.ttf

# Check if directories exists, otherwise create them
if [ ! -d "$HOME/.local/share/fonts" ]; then
    mkdir -p $HOME/.local/share/fonts
fi

if [ ! -d "$HOME/.config" ]; then
    mkdir -p $HOME/.config
fi

mv Fira\ Code\ Regular\ Nerd\ Font\ Complete.ttf $HOME/.local/share/fonts/FiraCodeNerdFont.ttf
fc-cache

# Install dotfiles

cp -r .config/* $HOME/.config/
cp -r Backgrounds $HOME/Backgrounds

# Confiure starship and xinit

echo 'eval "$(starship init bash)"' >> $HOME/.bashrc
echo "qtile start" >> $HOME/.xinitrc