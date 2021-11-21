#  Dotfiles
![A screenshot of the config](https://i.redd.it/qen8itx7az081.png)
Here's the dotfiles for my Qtile config, they're a bit quick-and-dirty but I hope they'll do. Please tell me if i forgot anything, I'll try to keep the repo up to date if I change stuff.
## Some info
- **WM** -> `qtile`. Note: change `home_dir` in `~/.config/qtile/config.py` to fit your setup.
- **Bar** -> `qtile`'s built in bar
- **Wallpaper setter** -> `feh`. Note: wallpaper is automatically picked from `~/Backgrounds`.
- **Terminal** -> `alacritty`
- **Shell** -> `bash`. Note: didn't change `.bashrc` apart from adding `eval "$(starship init bash)"` for Starship.
- **Prompt** -> [Starship](https://starship.rs/).
- **Compositor** -> [jonaburg/picom](https://github.com/jonaburg/picom), [ibhagwan's fork](https://github.com/ibhagwan) would also work.
- **Lockscreen** -> `slock`. Note: I changed something so I included the source for that too. Install with `sudo make clean install`.
- **Font** -> [Fira Code Nerd Font](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode).
- **Color scheme** -> custom, generated with [Pywal](https://github.com/dylanaraps/pywal). Note: run `wal` on the background before using otherwise colors won't load properly.
- **VS Code theme** -> custom, basically monokai dark but changed the background colors.
- **GTK theme** -> Arc-Dark

