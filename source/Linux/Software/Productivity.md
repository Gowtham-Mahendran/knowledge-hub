## 1. Zotero - citation management software

The Git repo is [here](https://github.com/retorquere/zotero-deb) for deb. It is reccognized officially by [zotero](https://www.zotero.org/support/installation).

Install the `zotero connector` extension in the browser, so that the papers can be directly added to zotero

create an account and setup in zotero for cloud sync

A list of [plugins](https://www.zotero.org/support/plugins) can be found here.

For network visualization, use [cita](https://github.com/diegodlh/zotero-cita). Unfortunaltely it does not support Zotero 7

You can choose upto 9 colors for tags. Use this.


## 2. PDF tools

### 2.1 xpdf-utils

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


### 2.2 qpdf

```bash
qpdf --decrypt restricted-input.pdf unrestricted-output.pdf
```

### 2.3 pdftk

```bash
sudo aptitude install pdftk
```

To rewrite document outline to a pdf document:

1. Read internal PDF info and Export it as editable text
```bash
pdftk book.pdf dump_data > meta.txt
```

2. In the end of `meta.txt` file, add bookmarks:
```bash
BookmarkBegin
BookmarkTitle: Chapter 1 Introduction
BookmarkLevel: 1
BookmarkPageNumber: 5
```

3. Level-2 must come after Level-1
```bash
BookmarkBegin
BookmarkTitle: 3.1 Line Parameters
BookmarkLevel: 2
BookmarkPageNumber: 85
```

4. Rewrite and save back
```bash
pdftk book.pdf update_info meta.txt output book_with_outline.pdf
```

## 3. Latex

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

## 4. Anki

Please check the [instruction manual](https://docs.ankiweb.net/platform/linux/installing.html)

