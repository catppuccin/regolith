#!/usr/bin/env bash
sudo python3 /usr/share/regolith-look/catppuccin/theme-switcher.py "${1:-mocha}" "${2:-blue}"
regolith-look refresh
