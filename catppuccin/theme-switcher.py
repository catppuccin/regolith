#!/usr/bin/env python3

import argparse
import sys

FLAVOURS = ["mocha", "macchiato", "frappe", "latte"]
ACCENTS = [
    "rosewater", "flamingo", "pink", "mauve", "red", "maroon",
    "peach", "yellow", "green", "teal", "sky", "sapphire", "blue", "lavender"
]
ACCENT_KEYS = [f"color_{accent}" for accent in ACCENTS]

ROOT_FILE_PATH = "/usr/share/regolith-look/catppuccin/root"
CONFIG_DIR = "/usr/share/regolith-look/catppuccin/config"

def parse_args():
    parser = argparse.ArgumentParser(description="Apply Catppuccin flavour and accent.")
    parser.add_argument(
        "--flavour",
        choices=FLAVOURS,
        default="mocha",
        help="Flavour of Catppuccin to use"
    )
    parser.add_argument(
        "--accent",
        choices=ACCENTS,
        default="blue",
        help="Accent to use"
    )
    return parser.parse_args()

def update_root_file(flavour, accent):
    with open(ROOT_FILE_PATH, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        for known_flavour in FLAVOURS:
            if known_flavour in line:
                print(f"Found {known_flavour} in line {i}, changing to {flavour}")
                lines[i] = line.replace(known_flavour, flavour)

        for known_accent in ACCENT_KEYS:
            if known_accent in line:
                print(f"Found {known_accent} in line {i}, changing to color_{accent}")
                lines[i] = line.replace(known_accent, f"color_{accent}")

    with open(ROOT_FILE_PATH, "w") as file:
        file.writelines(lines)

def update_config_file(flavour):
    config_path = f"{CONFIG_DIR}/{flavour}"
    with open(config_path, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("gtk.theme_name:"):
            theme_name = f"Catppuccin-{flavour.capitalize()}"
            lines[i] = f"gtk.theme_name: {theme_name}\n"
            # TODO: update to include accent when GTK themes support it
            print(f"Updated GTK theme name to {theme_name}")

    with open(config_path, "w") as file:
        file.writelines(lines)

def main():
    args = parse_args()
    update_root_file(args.flavour, args.accent)
    update_config_file(args.flavour)

if __name__ == "__main__":
    main()

