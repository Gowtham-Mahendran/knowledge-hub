# Trixie

In the starting, nothing can be installed. To install the packages we need to add debian repositories

```
deb http://deb.debian.org/debian trixie main contrib non-free non-free-firmware
deb http://security.debian.org/debian-security trixie-security main contrib non-free non-free-firmware
deb http://deb.debian.org/debian trixie-updates main contrib non-free non-free-firmware
deb http://deb.debian.org/debian trixie-backports main contrib non-free non-free-firmware
```
main → Free software (essential system & desktop packages)
contrib → Free software that depends on non-free packages
non-free → Non-free software (firmware, drivers, proprietary tools)
non-free-firmware → Firmware now separated in Bookworm+ (needed for Wi-Fi, GPU firmware, etc.)
security → Security updates for Trixie
updates → Regular bugfix updates between point releases
backports → Newer versions of packages (optional, but useful if you need fresh software)

Install aptitude package manager

```
sudo apt install aptitude
```

Install curl to install uv

```
sudo aptitude install curl
```

then

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```


To extract .xz file,
```
tar -xvf thunderbird-141.0.tar.xz
```
Install extensions to enable exchange calendar

<img width="761" height="181" alt="image" src="https://github.com/user-attachments/assets/2758093f-1d0c-49c2-8ef1-7a6e9e626ed1" />

Go to TbSync account manager and add an exchange account with the credentials.

sync calendar. It should now appear in Thunderbird calendar.


## Docker

Install using the official [Documentation](https://docs.docker.com/engine/install/debian/#install-using-the-repository)

Follow [this](https://docs.docker.com/engine/install/linux-postinstall/) after installation

## VPN

Install the [GlobalProtect-openconnect](https://github.com/yuezk/GlobalProtect-openconnect) client `.deb package` 

Verify installation using 
```
gowtham@debian:~$ gpclient --version
gpclient 2.4.5 (2025-07-16)
```
To connect, use `sudo` and authenticate the login.

```
gowtham@debian:~$ sudo gpclient connect <gateway>
```



## Git 

Clone the repo and set the url 

`git remote set-url origin https://github.com/Gowtham-Mahendran/operation_linux.git`

Then, use 

`git config credential.helper store`

and enter the user name. For password enter the PAT generated from the Github

Now you can push to the repo.

To view the passwords, use

`cat ~/.git-credentials` 


## Latex

`sudo aptitude install texlive-full`

and then use vscode as a IDE for latex

To verify,

```
(.venv)  gowtham@debian  ~/Documents/Git/Github/power-systems-lab   main  tex --version
TeX 3.141592653 (TeX Live 2025/dev/Debian)
kpathsea version 6.4.0/dev
Copyright 2024 D.E. Knuth.
There is NO warranty.  Redistribution of this software is
covered by the terms of both the TeX copyright and
the Lesser GNU General Public License.
For more information about these matters, see the file
named COPYING and the TeX source.
Primary author of TeX: D.E. Knuth.
(.venv)  gowtham@debian  ~/Documents/Git/Github/power-systems-lab   main  pdflatex --version

pdfTeX 3.141592653-2.6-1.40.26 (TeX Live 2025/dev/Debian)
kpathsea version 6.4.0/dev
Copyright 2024 Han The Thanh (pdfTeX) et al.
There is NO warranty.  Redistribution of this software is
covered by the terms of both the pdfTeX copyright and
the Lesser GNU General Public License.
For more information about these matters, see the file
named COPYING and the pdfTeX source.
Primary author of pdfTeX: Han The Thanh (pdfTeX) et al.
Compiled with libpng 1.6.47; using libpng 1.6.48
Compiled with zlib 1.3.1; using zlib 1.3.1
Compiled with xpdf version 4.04
```

This `pdflatex` is the one which is used by vscode to compile latex

Now in vscode install `latex workshop` extension by James-Yu.

