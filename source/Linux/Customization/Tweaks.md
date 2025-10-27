# Tweaks

## De-encrypt a pdf

1. Download `xpdf-utils' using `sudo apt-get install xpdf-utils`

```
gowtham@deb-gowarc  ~  sudo apt-get install xpdf-utils
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Note, selecting 'poppler-utils' instead of 'xpdf-utils'
poppler-utils is already the newest version (22.12.0-2+deb12u1).
poppler-utils set to manually installed.
The following packages were automatically installed and are no longer required:
  libslirp0 pigz slirp4netns
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

2. Debian is telling you that `xpdf-utils` has been replaced by `poppler-utils`, so when you try to install `xpdf-utils`, it just installs (or confirms you already have) `poppler-utils`.

3. Go to the directory. To decrypt a PDF and create a postscript file

```
pdftops -upw YOURPASSWORD-HERE input.pdf
```

This will create `input.ps` file. 

4. To convert `.ps` file (postscript) back to a `PDF`:
```
ps2pdf input.ps
```

PDF will be created without a encrypt password.

**qpdf**

```bash
qpdf --decrypt restricted-input.pdf unrestricted-output.pdf
```

## UV - astral

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

## Emoji

[Link](https://gist.github.com/rxaviers/7360908)

[admonitons](https://jimandreas.github.io/mkdocs-material/reference/admonitions/) for putting notes in markdown