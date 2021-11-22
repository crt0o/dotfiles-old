#  Dotfiles
![A screenshot of the config](https://i.redd.it/qen8itx7az081.png)
Here's the dotfiles for my Qtile config, they're a bit quick-and-dirty but I hope they'll do. Please tell me if i forgot anything, I'll try to keep the repo up to date if I change stuff.
## Some info
- **WM** -> `qtile`.
- **Bar** -> `qtile`'s built in bar.
- **Wallpaper setter** -> `feh`. Note: wallpaper is automatically picked from `~/Backgrounds`.
- **Terminal** -> `alacritty`
- **Shell** -> `bash`. Note: didn't change `.bashrc` apart from adding `eval "$(starship init bash)"` for Starship.
- **Prompt** -> [Starship](https://starship.rs/).
- **Compositor** -> [jonaburg/picom](https://github.com/jonaburg/picom), [ibhagwan's fork](https://github.com/ibhagwan) would also work.
- **Lockscreen** -> `slock`. Note: I changed something so I included the source for that too. Install with `sudo make clean install`.
- **Font** -> [Fira Code Nerd Font](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode).
- **Color scheme** -> custom, generated with [Pywal](https://github.com/dylanaraps/pywal).
- **VS Code theme** -> custom, basically monokai dark but changed the background colors.
- **GTK theme** -> Arc-Dark
## Install script
It's also possible to install automatically using the `install.sh` script. Simply run it with `./install.sh`. It will install all of the needed packages and copy over the config files. Please read the script (and modify it if necessary) before using.
Note: If you encounter graphical glitches try commenting out the corners and blurring sections and the backend setting in `~/.config/picom/picom.conf`.
### Packages included
- xorg-server and xorg-xinit
- qtile
- alacritty
- feh
- wget and libwebp
- picom-jonaburg-git
- starship