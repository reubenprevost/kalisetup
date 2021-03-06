#!/usr/bin/python3

import os

# Check admin priviledges
if os.geteuid() != 0:
    exit("You must run this program as root")

os.chdir("~/")

# Create tmux conf
with open("~/.tmux.conf", "w+") as f:
    conftext = '''
    # switch panes using Alt-Arrow without prefix
    bind -n M-Left select-pane -L
    bind -n M-Right select-pane -R
    bind -n M-Up select-pane -U
    bind -n M-Down select-pane -D

    # zoom pane using Alt-Z without prefix
    bind -n M-z resize-pane -Z
    '''

    f.write(conftext)

# Create hackthebox and pentestit directories
os.mkdir("~/hackthebox")
os.mkdir("~/htbacademy")
os.mkdir("~/pentestit")

# Install GoBuster
os.system("/usr/bin/apt -y install gobuster")

# Install SecLists
os.chdir("/opt")
os.system("/usr/bin/apt -y install seclists")