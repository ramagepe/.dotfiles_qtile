from libqtile import bar, layout, hook, qtile
# from libqtile import widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration
from scripts import storage

MOD_KEY = "mod4"
terminal = guess_terminal()
scripts_dir = "/home/ramage/.config/qtile/scripts/"

keys = [
    # Switch between windows
    Key([MOD_KEY], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD_KEY], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD_KEY], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD_KEY], "k", lazy.layout.up(), desc="Move focus up"),
    Key([MOD_KEY], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD_KEY], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD_KEY], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([MOD_KEY], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([MOD_KEY], "space", lazy.window.toggle_floating(),
        desc="Move window focus to other window"),
    Key([MOD_KEY], "d", lazy.spawn("rofi -show drun")),
    Key([MOD_KEY, "shift"], "d", lazy.spawn("sudo rofi -show drun")),
    Key([MOD_KEY], "escape", lazy.spawn("i3lock-fancy-rapid 5 3")),
    Key([MOD_KEY], "f", lazy.window.toggle_fullscreen()),

    Key([MOD_KEY], "Prior", lazy.spawn(scripts_dir + "increment_brigthness.sh")),
    Key([MOD_KEY], "Next", lazy.spawn(scripts_dir + "decrement_brigthness.sh")),


    Key([], "Print", lazy.spawn('flameshot gui')),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([MOD_KEY, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([MOD_KEY, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([MOD_KEY, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([MOD_KEY, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([MOD_KEY, "shift"], "e", lazy.spawn(
        "pcmanfm -d"), desc="Open file explorer"),

    Key([MOD_KEY, "shift"], "space", lazy.spawn(
        scripts_dir + "toggle_keyboard_layout.sh"), desc="Toggle keyboard layout"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Key([mod, "control"], "h", lazy.layout.grow_left(),
    #    desc="Grow window to the left"),
    # Key([mod, "control"], "l", lazy.layout.grow_right(),
    #    desc="Grow window to the right"),
    # Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([MOD_KEY, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([MOD_KEY, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([MOD_KEY, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([MOD_KEY, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([MOD_KEY, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([MOD_KEY, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([MOD_KEY, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([MOD_KEY, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key(
    #     [MOD_KEY, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    Key([MOD_KEY], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Key([MOD_KEY, "shift"], "Return", lazy.spawn('tdrop -ma -w -4 -y "$PANEL_HEIGHT" -s dropdown kitty'), desc="Launch dropdown terminal"),

    # Toggle between different layouts as defined below
    Key([MOD_KEY], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD_KEY], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD_KEY, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD_KEY, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([MOD_KEY], "r", lazy.spawn(),
        desc="Spawn a command using a prompt widget"),

    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),

    # Play / pause / next audio
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Hide bar
    Key([MOD_KEY], "b", lazy.hide_show_bar("all")),
]


groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# group_labels = ["", "", "", "", "", "", "", "", "", ""]
# group_labels = [""] * 10
# group_labels = [""] * 10
group_labels = [""] * 10
group_layouts = ["monadtall" for _ in range(len(group_names))]

for i, _ in enumerate(group_names):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i]
        )
    )

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [MOD_KEY],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {format(i.name)}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [MOD_KEY, "shift"],
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

# def init_colors():
#     return [["#0f1418.7", "#0f1418.7"],     # 0 - blackground
#             ["#1a1b26", "#1a1b26"],     # 1 - dark 80
#             ["#24283b", "#24283b"],     # 2 - dark 70
#             ["#414868", "#414868"],     # 3 - dark 60
#             ["#565f89", "#565f89"],     # 4 - dark 50
#             ["#cfc9c2", "#cfc9c2"],     # 5 - light
#             ["#7dcfff", "#7dcfff"]]     # 6 - contrast color

def init_colors():
    return [["#0f1418.7", "#0f1418.7"],     # 0 - blackground
            ["#7aa2f7", "#7aa2f7"],     # 1 - blue
            ["#7dcfff", "#7dcfff"],     # 2 - cyan
            ["#9ece6a", "#9ece6a"],     # 3 - green
            ["#bb9af7", "#bb9af7"],     # 4 - magenta
            ["#f7768e", "#f7768e"],     # 5 - red
            ["#e0af68", "#e0af68"],     # 6 - yellow
            ["#cfc9c2", "#cfc9c2"],     # 7 - light dark (foreground)
            ["#414868", "#414868"],]    # 8 - grey


colors = init_colors()


# LAYOUTS

def init_layout_theme(border: int, margin: int):
    return {
        "border_width": border,
        "margin": margin,
        "font": "JetBrainsMonoNerdFont 15",
                "font_size": 15,
                "border_focus": colors[1],
                "border_normal": colors[8]
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

def nerd_icon(nerdfont_icon, bg_color, fg_color, powerline):
    return widget.TextBox(
        font="JetBrainsMono Nerd Font",
        fontsize=15,
        text=nerdfont_icon,
        background=bg_color,
        foreground=fg_color,
        **powerline
    )


def border_decoration(color):
    return {
        "decorations": [
            BorderDecoration(
                colour=color,
                border_width=[0, 0, 3, 0],
                padding_x=10
            )
        ]
    }


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
BAR_SIZE = 24

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
                    background=colors[0],
                    padding=10,
                    **left_powerline
                ),
                widget.GroupBox(
                    active=colors[7],
                    inactive=colors[8],
                    block_highlight_text_color=colors[2],
                    highlight_method='text',
                    this_current_screen_border=colors[2],
                    padding=6,
                    background=colors[0],
                    **left_powerline
                ),
                widget.Spacer(
                    background=colors[0],
                    length=bar.STRETCH,
                ),
                widget.Memory(
                    padding=10,
                    format="  {MemUsed:.2f}{mm}",
                    measure_mem='G',
                    background=colors[0],
                    foreground=colors[7],
                    update_interval=2,
                    mouse_callbacks={
                        'Button1': lambda: qtile.spawn(f"{terminal} -e btm")
                    },
                    **border_decoration(colors[6])
                ),
                widget.GenPollText(
                    fmt='  {}',
                    padding=15,
                    background=colors[0],
                    foreground=colors[7],
                    update_interval=5,
                    func=lambda: storage.diskspace('FreeSpace'),
                    mouse_callbacks={
                        'Button1': lambda: qtile.spawn(f"{terminal} -e btm")
                    },
                    **border_decoration(colors[3])
                ),
                widget.GenPollText(
                    fmt='  {}',
                    padding=15,
                    background=colors[0],
                    foreground=colors[7],
                    update_interval=5,
                    func=lambda: storage.diskspace('FreeSpace', media=True),
                    mouse_callbacks={
                        'Button1': lambda: qtile.spawn(f"{terminal} -e btm")
                    },
                    **border_decoration(colors[5])
                ),
                widget.CPU(
                    padding=10,
                    format="  {load_percent}%",
                    background=colors[0],
                    foreground=colors[7],
                    update_interval=2,
                    mouse_callbacks={
                        'Button1': lambda: qtile.spawn(f"{terminal} -e btm")
                    },
                    **border_decoration(colors[4])
                ),
                widget.Spacer(
                    background=colors[0],
                    length=bar.STRETCH,
                    **right_powerline
                ),
                widget.Clock(
                    format="%I:%M %p",
                    padding=10,
                    background=colors[0],
                    foreground=colors[7],
                    **border_decoration(colors[1])
                ),
                widget.Clock(
                    format="%d-%m-%Y",
                    padding=10,
                    background=colors[0],
                    foreground=colors[7],
                    **border_decoration(colors[2])
                ),
                widget.Systray(
                    icon_size=18,
                    background=colors[0],
                    foreground=colors[7],
                    padding=20,
                    **right_powerline
                ),
                widget.QuickExit(
                    default_text="   ",
                    countdown_format='[{}]',
                    background=colors[0],
                    foreground=colors[7]
                ),
            ],
            BAR_SIZE,
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
              "bitwig-studio",
              "Bitwig-studio"]
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
    d["5"] = ["Discord", "discord"]
    d["6"] = ["Steam",
              "steam",
              "Steam-runtime",
              "steam-runtime"]
    d["7"] = ["Bitwarden",
              "bitwarden"]
    d["8"] = ["Pcmanfm",
              "pcmanfm",
              "Pcmanfm-qt",
              "pcmanfm-qt"]
    d["9"] = ["Carla",
              "carla"]
    d["0"] = ["Spotify",
              "spotify",
              "Music",
              "music"]
    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.toscreen()

#########################################################
###############         end             #################
#########################################################


# Drag floating layouts.
mouse = [
    Drag([MOD_KEY], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD_KEY], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD_KEY], "Button2", lazy.window.bring_to_front()),
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
        Match(title='kitty'),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"
