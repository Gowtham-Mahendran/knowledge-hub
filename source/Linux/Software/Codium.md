# VSCodium

Here is the official guide from the VSCodium [website](https://vscodium.com/)

1. Add the GPG key of the repository:
```bash
wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg \
   | gpg --dearmor \
   | sudo dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg
```

2. Add the repository:
```bash
echo 'deb [arch=amd64,arm64 signed-by=/usr/share/keyrings/vscodium-archive-keyring.gpg] https://download.vscodium.com/debs vscodium main' \
   | sudo tee /etc/apt/sources.list.d/vscodium.list
```
3. Update then install vscodium (if you want vscodium-insiders, then replace codium by codium-insiders):
```bash
sudo apt update && sudo apt install codium
```

4. To open VSCodium, execute `codium` in terminal

