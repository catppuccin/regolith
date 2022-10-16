#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

[[ $(command -v unzip) ]] || exit 1

git submodule update --init --recursive

FLAVOURS=(
"Mocha"
"Macchiato"
"Frappe"
"Latte"
)

for flavour in "${FLAVOURS[@]}"; do
  sudo unzip -o -d /usr/share/themes/ "$DIR/gtk/Releases/Catppuccin-${flavour}.zip" >/dev/null
done

sudo cp -r "$DIR/catppuccin" "/usr/share/regolith-look/"
sudo cp "$DIR/wrapper.sh" "/usr/bin/regolith-catppuccin"
