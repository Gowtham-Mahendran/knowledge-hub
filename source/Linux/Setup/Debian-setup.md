This guide documents the full process of replacing Windows with Debian 13 on an HP laptop, including BIOS setup, offline driver installation, and EasyRoam setup.

## 1. Booting Debian

**Downloading and creating Debian bootable drive**

Go to the [Debian](https://www.debian.org/distrib/) distribution page and download the **firmware-included ISO** for Debian 13. Example: `debian-13.1.0-amd64-DVD-1.iso`

Download and install [Rufus](https://rufus.ie) to write the ISO to a USB:
- Select your USB
- Choose the ISO file
- Use **GPT partition scheme**
- Use **UEFI (non-CSM)**

**BIOS/UEFI Configuration**

- Reboot and press F10 (On HP laptops) repeatedly to enter BIOS setup.
- Go to Security → Secure Boot Configuration → Disable Secure Boot
- Reboot and press F9 to enter Boot Device Options
- Choose UEFI: <your USB drive> (e.g., UEFI: SanDisk)

**Install Debian 13**

- Select **Graphical Install**
- When prompted for network drivers, skip if your hardware isn’t detected
- Choose Guided Partitioning
- Set **root password**
- Create a normal user

**Login Manager Selection**

If installing multiple desktops, you’ll be prompted to choose a display manager:

- `gdm3` → for GNOME desktop (default)
- `sddm` → for KDE Plasma
 
**Switching to superuser**

Once you are in the startup page, open terminal and Switch to root to get admin privileges for modifying system and installing apps:

```bash
su -
```
To update the system,
```bash
apt update 
apt upgrade
```

To add `user` to sudo list, go to `root` and execute
```bash
usermod -aG sudo <username>
```

To verify,

```bash
groups <username>
```

This will show something like, `<username> : <username> cdrom floppy sudo audio dip video plugdev users netdev bluetooth lpadmin scanner`. Now `<username>` is a `superuser` or use `sudo whoami`.


## 2. Setting Up Debian Package Sources


Once you boot into the system, you need to add repositories so that Debian can fetch and install software packages from official sources.

To install the packages, we need to add debian repositories to the `sources.list`.

**Open the sources list:**
```bash
sudo nano /etc/apt/sources.list
```

You’ll be prompted for your password when using sudo.

**Add the following sources to the list if not already there:**

```bash
deb http://deb.debian.org/debian trixie main contrib non-free non-free-firmware
deb http://security.debian.org/debian-security trixie-security main contrib non-free non-free-firmware
deb http://deb.debian.org/debian trixie-updates main contrib non-free non-free-firmware
deb http://deb.debian.org/debian trixie-backports main contrib non-free non-free-firmware
```

!!! info "Explanation of sources list"
    **main** → Free software (essential system & desktop packages)<br>
    **contrib** → Free software that depends on non-free packages<br>
    **non-free** → Non-free software (firmware, drivers, proprietary tools)<br>
    **non-free-firmware** → Firmware now separated in Bookworm+ (needed for Wi-Fi, GPU firmware, etc.)<br>
    **security** → Security updates for Trixie<br>
    **updates** → Regular bugfix updates between point releases<br>
    **backports** → Newer versions of packages (optional, but useful if you need fresh software)<br>

To save the changes, `Ctrl + O` and press `Enter` to save. To exit nano, press `Ctrl + X`.

**Once the sources are added, you can update the packages**

To fetch the updates from the repositories,

```bash
sudo apt update
```

To see the packages that needs update,

```bash
apt list --upgradable
```

To update
```bash
sudo apt upgrade
```

**To install softwares and tools, i personally prefer having a package manager,**

### Aptitude

Aptitude provides a user-friendly interface with more advanced features compared to the simple command-line interface of `apt-get`

Install `aptitude` package manager

```bash
sudo apt install aptitude
```

In the Aptitude interface, press `/` to search package. Navigate using the arrow keys. To install packages, use the `+` key to select the packages and press `g` to start the installation process.

### Curl

Sometimes, `curl` is needed to install packages. You can install it using the `aptitude`

```bash
sudo aptitude install curl
```

### Flatpak

[Flatpak](https://flatpak.org/) is another package management for Linux.

```bash
sudo apt install flatpak
```

Add the flatpak repo [refer](https://flatpak.org/setup/Debian)

```bash
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

Restart the system to apply the changes.