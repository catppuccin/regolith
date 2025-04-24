#!/usr/bin/env bash
sudo python3 /usr/share/regolith-look/catppuccin/theme-switcher.py --flavour "${1:-mocha}" --accent "${2:-blue}"
regolith-look refresh
