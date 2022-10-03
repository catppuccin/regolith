#!/usr/bin/python3

import getopt
import sys

flavours = ['mocha', 'macchiato', 'frappe', 'latte']
accents = [
    'color_rosewater',
    'color_flamingo',
    'color_pink',
    'color_mauve',
    'color_red',
    'color_maroon',
    'color_peach',
    'color_yellow',
    'color_green',
    'color_teal',
    'color_sky',
    'color_sapphire',
    'color_blue',
    'color_lavender',
    'color_text',
    'color_subtext1',
    'color_subtext0',
    'color_overlay2',
    'color_overlay1',
    'color_overlay0',
    'color_surface2',
    'color_surface1',
    'color_surface0',
    'color_base',
    'color_mantle',
    'color_crust',
]

possible_accents = [
    'rosewater',
    'flamingo',
    'pink',
    'mauve',
    'red',
    'maroon',
    'peach',
    'yellow',
    'green',
    'teal',
    'sky',
    'sapphire',
    'blue',
    'lavender',
    'text',
    'subtext1',
    'subtext0',
    'overlay2',
    'overlay1',
    'overlay0',
    'surface2',
    'surface1',
    'surface0',
    'base',
    'mantle',
    'crust'
]

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hflavour:accent:", ["flavour=", "accent="])
    except getopt.GetoptError:
        print('test.py --flavour <flavour> --accent <accent>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py --flavour <flavour> --accent <accent>')
            sys.exit()
        elif opt in ("-f", "--flavour"):
            if arg in flavours:
                flavour = arg
            else:
                print('Invalid flavour')
                sys.exit(2)
        elif opt in ("-a", "--accent"):
            if arg in possible_accents:
               accent = arg
            else:
                print('Accent not found')
                sys.exit(2)
    FILE_PATH = '/usr/share/regolith-look/catppuccin/root'

    print('Flavour is ', flavour)
    print('Accent is ', accent)



    with open(FILE_PATH, 'r') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            for known_flavour in flavours:
                if known_flavour in line:
                    print('Found {} in line {}, changing for {}'.format(known_flavour, i, flavour))
                    lines[i] = line.replace(known_flavour, flavour)

            for known_accent in accents:
                if known_accent in line:
                    print('Found {} in line {}, changing for {}'.format(known_accent, i, accent))
                    lines[i] = line.replace(known_accent, f"color_{accent}")

    with open(FILE_PATH, 'w') as file:
        file.writelines(lines)

if __name__ == '__main__':
    main(argv=sys.argv[1:])
