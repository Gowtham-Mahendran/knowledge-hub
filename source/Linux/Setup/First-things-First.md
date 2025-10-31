## 1. Easyroam config

The certificate is only valid for **90 days** and must be replaced after this period.

To configure **eduroam** using a script, follow these steps:

1. Open [https://www.easyroam.de](https://www.easyroam.de) in your web browser.
2. In the search field, enter your institution name, e.g., `UOL`.
3. Log in using your institutional credentials.


## 2. Installing Thunderbird

Thunderbird is my favourite mail manager. Thunderbird could be installed normally form the apt repositary:

```bash
sudo aptitude install thunderbird 
```
This downloads the package from online mirrors. Customizing thunderbird is detailed in Customization section.

## 3. Brave Browser

Here is the linux [download](https://brave.com/linux/) page of Brave browser

```bash
aptitude install curl
curl -fsS https://dl.brave.com/install.sh | sh
```

## 4. External Monitor

You can preview the current setup by just running:
```bash
xrandr
```

The below script will list available GPU output providers.
```bash
xrandr --listproviders
```

To place the monitor to the right of laptop screen.
```bash
xrandr --output HDMI-1-0 --auto --right-of eDP
```

To duplicate,
```bash
xrandr --output HDMI-1-0 --mode 1920x1080 --same-as eDP
```

## 5. Mounting Network Drives

1. Make a new folder in the user directory

```bash
mkdir name
```

2. Check the uid and gid of the user using

```bash
id
```

3. To mount CIFS file systems under Linux, you may need to install additional packages. Install cifs-utils using,

```bash
apt install cifs-utils
```

4. Edit the fstab file to mount permanently and let it be there automatically on boot. To open, we need to be in the root.

```bash
sudo nano /etc/fstab   
```

5. You can add entries to /etc/fstab (you must be root for that or use sudo). The entries should have the form: [Refer](https://hpcwiki.uni-oldenburg.de/en/hpc-usage/data-storage/mounting-file-systems)

```bash
//server_address/share <mount_point> cifs vers=3.0,workgroup=W2KROOT,username=<user>,file_mode=0600,dir_mode=0700,uid=<linux_username>,gid=<linux_group>,noauto,users 0 0
```

6. Then, to mount the directories, you can use the following command as a user without root-privileges:

```bash
$ mount <mount_point>
```

There will be a warning message,

```bash
mount: (hint) your fstab has been modified, but systemd still uses
      the old version; use 'systemctl daemon-reload' to reload.
```

It means, if you've recently edited `/etc/fstab`, `systemd` is still using a cached version, and to fully apply the new changes, you should run:

```bash
systemctl daemon-reload
```

