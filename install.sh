#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

sudo cp -r "$DIR/catppuccin" "/usr/share/regolith-look/"
sudo cp "$DIR/wrapper.sh" "/usr/bin/regolith-catppuccin"
