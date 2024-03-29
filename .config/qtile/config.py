# crt0o's qtile config

# --- Imports ---

from typing import List

import subprocess
import os
import json

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# --- Mod, terminal and home dir ---

mod = "mod4"
terminal = guess_terminal()
home_dir = os.getenv('HOME')

# --- Colors ---

colors = [
    '#12101d',
    '#6B3448',
    '#3A426E',
    '#50466C',
    '#6E4A66',
    '#C45F3E',
    '#A15760',
    '#dfac9f',
    '#9c786f',
    '#6B3448',
    '#3A426E',
    '#50466C',
    '#6E4A66',
    '#C45F3E',
    '#A15760',
    '#A15760'
]

# --- Hooks ---

# Run the autostart.sh script on startup
@hook.subscribe.startup
def startup():
    subprocess.call(home_dir + '/.config/qtile/autostart.sh')

# --- Keybindings ---

keys = [
    # -- Switch windows --
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # -- Shuffle windows --
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # -- Resize windows --
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # -- Switch layouts --
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # -- Kill windows --
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    # -- Restart, shutdown and spawn --
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # -- Spawn terminal --
    Key([mod], "Return", lazy.spawn(terminal), desc="Spawn a terminal"),

    # -- Lock the screen --
    Key([mod], "Escape", lazy.spawn('slock'), desc="Lock the screen"),
]

# --- Groups ---

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # -- Switch groups --
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # -- Move window to group --
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

# --- Layouts ---

layout_options = {
    'margin': 10,
    'border_width': 0
}

layouts = [
    layout.Bsp(fair=False, **layout_options),
]

# --- Bar and screens ---

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

bar_options = {
    'background': colors[0],
    'margin': [0, 10, 10, 10]
}

group_box_options = {
    'active': colors[7],
    'inactive': colors[2],
    'spacing': 10,
    'rounded': True,
    'this_current_screen_border': colors[7],
    'this_screen_border': colors[7],
    'other_screen_border': colors[2],
    'font': 'FiraCodeNerdFont'
}

text_options = {
    'foreground': colors[7],
    'font': 'FiraCodeNerdFont'
}

quick_exit_options = {
    'default_text': '',
    'countdown_format': '',
    'countdown_start': 1
}

def shutdown():
    os.system('shutdown now')

def reboot():
    os.system('reboot')

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(**group_box_options),
                widget.Prompt(**text_options),
                widget.WindowName(**text_options),
                widget.Clock(format='%I:%M:%S', **text_options),
                widget.TextBox(text='', padding=10, mouse_callbacks={'Button1': shutdown}, **text_options),
                widget.TextBox(text='', padding=10, mouse_callbacks={'Button1': reboot}, **text_options),
                widget.QuickExit(padding=10, **text_options, **quick_exit_options),
            ],
            30,
            **bar_options,
        ),
    ),
# A second screen for my dual-monitor setup
#    Screen(
#        bottom=bar.Bar(
#            [
#                widget.GroupBox(**group_box_options),
#                widget.Prompt(**text_options),
#                widget.WindowName(**text_options),
#                widget.Clock(format='%I:%M:%S', **text_options),
#                widget.TextBox(text='', padding=10, mouse_callbacks={'Button1': shutdown}, **text_options),
#                widget.TextBox(text='', padding=10, mouse_callbacks={'Button1': reboot}, **text_options),
#                widget.QuickExit(padding=10, **text_options, **quick_exit_options),
#            ],
#            30,
#            **bar_options,
#        ),
#   )
]

# --- Floating layout keybinds ---

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# --- Misc settings ---

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_width=0, float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'), 
    Match(wm_class='maketag'),
    Match(wm_class='ssh-askpass'),
    Match(title='branchdialog'),
    Match(title='pinentry'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

# Left this here just in case

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
