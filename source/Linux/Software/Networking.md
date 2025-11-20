
## 1. VPN

Install the [GlobalProtect-openconnect](https://github.com/yuezk/GlobalProtect-openconnect) client `.deb package` 

Verify installation using 
```bash
gpclient --version
```
To connect, use `sudo` and authenticate the login.

```bash
sudo gpclient connect <gateway>
```

## 2. Tor

Install `tor` using

```bash
sudo aptitude install tor
```

For GUI, install [torbrowser-launcher](https://github.com/torproject/torbrowser-launcher)

```bash
flatpak install flathub org.torproject.torbrowser-launcher
```

## 3. Others

To find the ip address,

```bash
nmcli device show
```

```bash
hostname -I
```

```bash
ip addr show
```

## 4. Proxychains

```bash
sudo aptitude install proxychains
```

To use proxychains,

```bash
sudo proxychains <browser-name>
```