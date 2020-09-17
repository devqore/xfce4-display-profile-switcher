Why?
---

I need this script because I want to switch easily between display profiles using keyboard shortcuts. Display profiles are already configured in [xfce display settings](https://docs.xfce.org/xfce/xfce4-settings/display) so script it's only used to display currently configured profiles (`-l` or `--list-profiles`) and then set proper command with option `-s` or `--set-profile` `PROFILE_ID` in [applications shortcuts](https://docs.xfce.org/xfce/xfce4-settings/keyboard). 

Usage
-----

```
usage: xfce_display_profile_switcher.py [-h] [-s PROFILE_ID] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -s PROFILE_ID, --set-profile PROFILE_ID
                        set profile with given id
  -l, --list-profiles   list profiles
```

Requirements
------------

Python 3 and xfconf-query in the PATH.
