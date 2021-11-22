#!/usr/bin/bash

# This script is automatically run by qtile on startup

# Set up second display
# Modify this for your setup
# xrandr --output HDMI-1-1 --auto --left-of eDP1

# Start picom
picom --experimental-backends --config "${HOME}/.config/picom/picom.conf" &

# Draw background
# Picks random backgrounds from ~/Backgrounds
feh --randomize --bg-scale "${HOME}/Backgrounds/"