#!/usr/bin/python3

import argparse
import sys
from subprocess import check_output as run

flavours = ["mocha", "macchiato", "frappe", "latte"]
possible_accents = [
    "rosewater",
    "flamingo",
    "pink",
    "mauve",
    "red",
    "maroon",
    "peach",
    "yellow",
    "green",
    "teal",
    "sky",
    "sapphire",
    "blue",
    "lavender"
]
accents = [f"color_{accent}" for accent in possible_accents]

parser = argparse.ArgumentParser()
parser.add_argument(
    "--flavour",
    help="Flavour of Catppuccin to use",
    choices=flavours,
    default="mocha"
)
parser.add_argument(
    "--accent",
    help="Accent to use",
    choices=possible_accents,
    default="blue"
)
args = parser.parse_args()

def main(argv):
    FILE_PATH = "/usr/share/regolith-look/catppuccin/root"
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            for known_flavour in flavours:
                if known_flavour in line:
                    print(
                        "Found {} in line {}, changing for {}".format(
                            known_flavour, i, args.flavour
                        )
                    )
                    lines[i] = line.replace(known_flavour, args.flavour)

            for known_accent in accents:
                if known_accent in line:
                    print(
                        "Found {} in line {}, changing for {}".format(
                            known_accent, i, args.accent
                        )
                    )
                    lines[i] = line.replace(known_accent, f"color_{args.accent}")

    with open(FILE_PATH, "w") as file:
        file.writelines(lines)

    FILE_PATH = f"/usr/share/regolith-look/catppuccin/config/{args.flavour}"
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line.startswith("gtk.theme_name:"):
                flavour = args.flavour.capitalize()
                # TODO: replace this with {args.accent}, once GTK has all accents
                lines[i] = f"gtk.theme_name: Catppuccin-{flavour}\n"

    with open(FILE_PATH, "w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    main(argv=sys.argv[1:])
