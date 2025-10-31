# Tweaks

## De-encrypt a pdf

1. Download `xpdf-utils' using 

```bash
sudo aptitude install xpdf-utils
```

2. Debian is telling you that `xpdf-utils` has been replaced by `poppler-utils`, so when you try to install `xpdf-utils`, it just installs (or confirms you already have) `poppler-utils`.

3. Go to the directory. To decrypt a PDF and create a postscript file

```bash
pdftops -upw YOURPASSWORD-HERE input.pdf
```

This will create `input.ps` file. 

4. To convert `.ps` file (postscript) back to a `PDF`:
```bash
ps2pdf input.ps
```

PDF will be created without a encrypt password.


## qpdf

```bash
qpdf --decrypt restricted-input.pdf unrestricted-output.pdf
```

## UV - astral


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

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

```bash
sudo aptitude install texlive-full
```

To verify,

```bash
tex --version
```

```bash
pdflatex --version
```

This `pdflatex` is the one which is used by vscode to compile latex

Now in vscode install `latex workshop` extension by James-Yu.

## Emoji

[Link](https://gist.github.com/rxaviers/7360908)

[admonitons](https://jimandreas.github.io/mkdocs-material/reference/admonitions/) for putting notes in markdown


## Anki

Please check the [instruction manual](https://docs.ankiweb.net/platform/linux/installing.html)