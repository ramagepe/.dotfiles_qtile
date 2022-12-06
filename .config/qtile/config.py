from libqtile import bar, layout, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras import widget

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    Key([mod, "shift"], "d", lazy.spawn("sudo dmenu_run -fn 'JetBrainsMono Nerd Font-16'")),
    Key([mod], "escape", lazy.spawn("i3lock-fancy-rapid 5 3")),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),

    # Play / pause / next audio
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
]

groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_labels = ["", "", "", "", "", "", "", "漣", "", ""]
group_layouts = ["monadtall" for _ in range(len(group_names))]

for i, _ in enumerate(group_names):
    groups.append(
            Group(
                name = group_names[i],
                layout = group_layouts[i].lower(),
                label = group_labels[i]
                )
            )

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {format(i.name)}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {format(i.name)}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


# COLORS

def init_colors():
    return [["#0f1418", "#0f1418"],     # 0 - blackground
            ["#1a1b26", "#1a1b26"],     # 1 - dark 80
            ["#24283b", "#24283b"],     # 2 - dark 70
            ["#414868", "#414868"],     # 3 - dark 60
            ["#565f89", "#565f89"],     # 4 - dark 50
            ["#cfc9c2", "#cfc9c2"],     # 5 - light
            ["#7dcfff", "#7dcfff"]]     # 6 - contrast color


colors = init_colors()


# LAYOUTS

def init_layout_theme(border: int, margin: int):
    return {
                "border_width": border,
                "margin": margin,
                "font": "JetBrainsMono Nerd Font 15",
                "font_size": 15,
                "border_focus": colors[4],
                "border_normal": colors[2]
            }


border_layout = init_layout_theme(2, 6)
borderless_layout = init_layout_theme(0, 0)

layouts = [
    layout.MonadTall(**border_layout),
    layout.Max(**border_layout),
    # layout.MonadTall(**borderless_layout),
    # layout.Max(**borderless_layout),
]


# BAR

def nerd_icon(nerdfont_icon, fg_color):
    return widget.TextBox(
        font="JetBrainsMono Nerd Font",
        fontsize=15,
        text=nerdfont_icon,
        foreground=fg_color,
        **right_powerline,
        background=colors[4],
        padding=0)


left_powerline = {
    "decorations": [
        PowerLineDecoration()
    ]
}

right_powerline = {
    "decorations": [
        PowerLineDecoration(path='arrow_right')
    ]
}

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()
bar_size = 24

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background=colors[1],
                    padding=10,
                    **left_powerline
                ),
                widget.GroupBox(
                    active=colors[5],
                    inactive=colors[3],
                    block_highlight_text_color=colors[6],
                    highlight_method='text',
                    this_current_screen_border=colors[6],
                    padding=12,
                    background=colors[2],
                    **left_powerline
                ),
                widget.Spacer(
                    background=colors[0],
                    **right_powerline
                ),
                widget.PulseVolume(
                    fmt='墳  {}',
                    background=colors[4],
                    foreground=colors[5],
                    padding=20,
                    **right_powerline
                ),
                widget.Clock(
                    format="%Y-%m-%d",
                    padding=20,
                    background=colors[3],
                    foreground=colors[5],
                    **right_powerline
                ),
                widget.Clock(
                    format="%I:%M %p",
                    padding=20,
                    background=colors[2],
                    foreground=colors[5],
                    **right_powerline
                ),
                widget.Systray(
                    icon_size=18,
                    background=colors[1],
                    foreground=colors[5],
                    padding=20,
                    **right_powerline
                ),
                widget.QuickExit(
                    default_text="   ",
                    countdown_format='[{}]',
                    background=colors[1],
                    foreground=colors[5]
                ),
            ],
            bar_size,
        ),
    ),
]


#########################################################
################ assgin apps to groups ##################
#########################################################


@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    d["1"] = ["Terminal",
              "terminal",
              "Alacritty",
              "alacritty",
              "Code",
              "code",
              "Fleet",
              "fleet"]
    d["2"] = ["Navigator",
              "navigator",
              "Firefox",
              "firefox",
              "Chromium",
              "chromium",
              "Google-chrome",
              "google-chrome",
              "Brave",
              "brave",
              "Brave-browser",
              "brave-browser"]
    d["3"] = ["Obsidian", 
              "obsidian"]
    d["4"] = ["Thunderbird", 
              "thunderbird", 
              "Mail"]
    # d["5"] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
    # d["6"] = ["Vlc","vlc", "Mpv", "mpv" ]
    d["7"] = ["1Passsword", 
              "1password"]
    d["8"] = ["Pcmanfm",
              "pcmanfm",
              "Pcmanfm-qt",
              "pcmanfm-qt"]
    d["9"] = ["Carla", 
              "carla"]
    d["0"] = ["Spotify",
              "spotify",
              "Clementine",
              "clementine",
              "Audacious",
              "audacious",
              "Music",
              "music"]
    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen()

#########################################################
###############         end             #################
#########################################################


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=colors[4],
    border_normal=colors[2],
    border_width=2,
    float_rules=[
        # Run `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="calf"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title='Open File'),
        Match(title='galculator'),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"
