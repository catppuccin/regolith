<h3 align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/logos/exports/1544x1544_circle.png" width="100" alt="Logo"/><br/>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
	Catppuccin for <a href="https://regolith-desktop.com/">Regolith</a>
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/misc/transparent.png" height="30" width="0px"/>
</h3>

<p align="center">
	<a href="https://github.com/catppuccin/regolith/stargazers"><img src="https://img.shields.io/github/stars/catppuccin/regolith?colorA=363a4f&colorB=b7bdf8&style=for-the-badge"></a>
	<a href="https://github.com/catppuccin/regolith/issues"><img src="https://img.shields.io/github/issues/catppuccin/regolith?colorA=363a4f&colorB=f5a97f&style=for-the-badge"></a>
	<a href="https://github.com/catppuccin/regolith/contributors"><img src="https://img.shields.io/github/contributors/catppuccin/regolith?colorA=363a4f&colorB=a6da95&style=for-the-badge"></a>
</p>

<p align="center">
	<img src="./assets/preview.webp"/>
</p>

## Previews

<details>
<summary>🌻 Latte</summary>
<img src="assets/latte.webp"/>
</details>
<details>
<summary>🪴 Frappé</summary>
<img src="assets/frappe.webp"/>
</details>
<details>
<summary>🌺 Macchiato</summary>
<img src="assets/macchiato.webp"/>
</details>
<details>
<summary>🌿 Mocha</summary>
<img src="assets/mocha.webp"/>
</details>

## Usage

1. Clone this repository locally
2. Copy the content of the `catppuccin` folder to `/usr/share/regolith-look/catppuccin`
3. Run `sudo python3 /usr/share/regolith-look/catppuccin/theme-switcher.py --flavour <flavour> --accent <accent>`
4. Run `regolith-look set catppuccin`

## Variables
```shell
! --------------------------------------------
! -- Selected flavour
! --------------------------------------------
#include "/usr/share/regolith-look/catppuccin/config/latte"

! --------------------------------------------
! -- Selected accent
! --------------------------------------------
#define color_accent      color_pink
```
## Dependencies
- [GTK](https://github.com/catppuccin/gtk)
- [Gnome-Terminal](https://github.com/catppuccin/gnome-terminal)

## 📝 TODO

- Gnome terminal themes are still missing.
- Fix the issue regarding GTK3 themes. (The theme is not applied correctly)
- When changing flavours on the fly, workspaces glyph don't update their colours accordingly until logging out / back in

## 💝 Thanks to

- [taka0o](https://github.com/taka0o)

&nbsp;

<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>

<p align="center">
	Copyright &copy; 2021-present <a href="https://github.com/catppuccin" target="_blank">Catppuccin Org</a>
</p>

<p align="center">
	<a href="https://github.com/catppuccin/catppuccin/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a>
</p>
