## Test Suites for niri

# Installation and Running
Use these commands to install niri with DankMaterialShell for a fairly out-of-the-box experience or check [this](https://github.com/niri-wm/niri/wiki/Getting-Started).

Fedora:
```bash
sudo dnf copr enable avengemedia/dms
sudo dnf install niri dms
systemctl --user add-wants niri.service dms
```

Arch Linux:
```bash
sudo pacman -Syu niri xwayland-satellite xdg-desktop-portal-gnome xdg-desktop-portal-gtk alacritty dms-shell-niri matugen cava qt6-multimedia-ffmpeg
systemctl --user add-wants niri.service dms
```

Ubuntu 25.10 and above:
```bash
sudo add-apt-repository ppa:avengemedia/danklinux
sudo add-apt-repository ppa:avengemedia/dms
sudo apt install niri dms
```

NixOS: check [nixpkgs](https://github.com/NixOS/nixpkgs) or [niri-flake](https://github.com/sodiboo/niri-flake)  

After running these commands, log out, choose Niri in your display manager, and log back in. Or, if not using a display manager, run niri-session on a TTY.
