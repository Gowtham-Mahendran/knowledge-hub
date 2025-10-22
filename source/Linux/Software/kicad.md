# KiCAD - Debian Backports

**For Bookworm:**

Debian’s Backports archive is an official way to get newer (“back-ported”) versions of packages on your stable system without sacrificing its overall stability. Backports is a separate APT repository (e.g. bookworm-backports for Debian 12) that Debian maintainers populate with newer releases of software originally built for Debian Testing or Unstable. Stable’s main archive often has older releases (e.g. KiCad 6 in Debian 12). Backports let you get KiCad 9 (or other up-to-date software) without waiting for the next Debian release. [Refer](https://www.kicad.org/download/linux/)

To use backports, we need to enable the backports repo,

```bash
echo "deb http://deb.debian.org/debian bookworm-backports main contrib non-free" \
  | sudo tee /etc/apt/sources.list.d/bookworm-backports.list
```

Then update apt using

```bash
sudo aptitude update
```

Now install KiCAD using,

```bash
sudo aptitude install -t bookworm-backports kicad
```
The -t flag in APT stands for “target release” (it’s shorthand for --target-release). It tells APT which release (or suite) you want to pull a package from, rather than using the default “stable” archive.

**For Trixie:**

Install KiCAD using,

```bash
sudo aptitude install kicad
```