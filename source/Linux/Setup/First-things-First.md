## 1. Easyroam config

The certificate is only valid for **90 days** and must be replaced after this period.

To configure **eduroam** using a script, follow these steps:

1. Open [https://www.easyroam.de](https://www.easyroam.de) in your web browser.
2. In the search field, enter your institution name, e.g., `UOL`.
3. Log in using your institutional credentials.


## 2. Installing Thunderbird

Once the sources were fixed, Thunderbird could be installed normally:

```bash
sudo aptitude install thunderbird 
```
This downloaded the package from online mirrors instead of prompting for the DVD.

## 3. Brave Browser

Here is the linux [download](https://brave.com/linux/) page of Brave browser

```
aptitude install curl
curl -fsS https://dl.brave.com/install.sh | sh
```

## 4. NVIDIA Driver

```bash
[ 0.259410] ACPI BIOS Error (bug): Failure creating named object [_SB.PCI0.GPP0.VGA], AE_ALREADY_EXISTS (20220331/dswload2-326)
[ 0.259421] ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20220331/psobject-220)
[ 0.259492] ACPI BIOS Error (bug): Failure creating named object [_SB.PCI0.GPP0.HDAU], AE_ALREADY_EXISTS (20220331/dswload2-326)
[ 0.259436] ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20220331/psobject-220)
[ 0.909192] blacklist: Problem blacklisting hash (-13)
[ 0.909414] blacklist: Problem blacklisting hash (-13)
[ 0.909528] blacklist: Problem blacklisting hash (-13)
[ 0.909560] blacklist: Problem blacklisting hash (-13)
[ 0.909787] blacklist: Problem blacklisting hash (-13)
[ 1.998245] nouveau 0000:01:00.0: firmware: failed to load nvidia/ga107/nvdec/scrubber.bin (-2)
[ 1.998271] firmware_class: See https://wiki.debian.org/Firmware for information about missing firmware
[ 1.998307] nouveau 0000:01:00.0: firmware: failed to load nvidia/ga107/nvdec/scrubber.bin (-2)
```

The last three errors shows that the nvidia driver is failed to load. The nvidia-detect script (found in the [nvidia-detect](https://packages.debian.org/nvidia-detect) package in the [non-free](https://www.debian.org/doc/debian-policy/ch-archive#s-non-free) section) can also be used to identify the GPU and the recommended driver package to install. Refer the nvidia debian page [here](https://wiki.debian.org/NvidiaGraphicsDrivers)

Install the detect driver
```bash
apt install nvidia-detect
```

Detect the driver using  
```bash
nvidia-detect
```

The output is as follows

```bash
gowtham@deb-gowarc:~$ nvidia-detect
Detected NVIDIA GPUs:
01:00.0 VGA compatible controller [0300]: NVIDIA Corporation GA107M [GeForce RTX 3050 Mobile] [10de:25a2] (rev a1)

Checking card:  NVIDIA Corporation GA107M [GeForce RTX 3050 Mobile] (rev a1)
Your card is supported by all driver versions.
Your card is also supported by the Tesla 470 drivers series.
It is recommended to install the
nvidia-driver
package.
```

Install the nvidia-driver
```bash
apt install nvidia-driver
```

During installation, it prompted saying NVIDIA proprietary driver is conflicting with the open-source Nouveau driver. It asked for reboot after installation. Once installed, Reboot in `su`
```bash
reboot
```

verify the installation using 
```bash
nvidia-smi
```

The output is as follows

```bash
gowtham@deb-gowarc:~$ nvidia-smi
Thu Jun 26 17:13:29 2025       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.247.01             Driver Version: 535.247.01   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA GeForce RTX 3050 ...    On  | 00000000:01:00.0 Off |                  N/A |
| N/A   47C    P3              17W /  30W |      8MiB /  4096MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|    0   N/A  N/A       949      G   /usr/lib/xorg/Xorg                            4MiB |
+---------------------------------------------------------------------------------------+
```

while rebooting, the nvidia driver error got resolved.

```bash
[ 0.259410] ACPI BIOS Error (bug): Failure creating named object [_SB.PCI0.GPP0.VGA], AE_ALREADY_EXISTS (20220331/dswload2-326)
[ 0.259421] ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20220331/psobject-220)
[ 0.259492] ACPI BIOS Error (bug): Failure creating named object [_SB.PCI0.GPP0.HDAU], AE_ALREADY_EXISTS (20220331/dswload2-326)
[ 0.259436] ACPI Error: AE_ALREADY_EXISTS, During name lookup/catalog (20220331/psobject-220)
[ 0.909192] blacklist: Problem blacklisting hash (-13)
[ 0.909414] blacklist: Problem blacklisting hash (-13)
[ 0.909528] blacklist: Problem blacklisting hash (-13)
[ 0.909560] blacklist: Problem blacklisting hash (-13)
[ 0.909787] blacklist: Problem blacklisting hash (-13)
```
## 5. Miniforge

- Download conda-forge installer from the [website](https://conda-forge.org/download/)

- Go to the directory and run

```bash
bash Miniforge3-$(uname)-$(uname -m).sh
```

Since `uname` outputs `Linux` and `uname -m` outputs `x86_64`, running the command `Miniforge3-$(uname)-$(uname -m).sh` is similar to mentioning the actual file name `Miniforge3-Linux-x86_64.sh`.


- It will ask to read the license agreement and now it will show `end`. Now type `yes` and the installation will begin.

```bash
Miniforge3 will now be installed into this location:
/home/gowtham/miniforge3

- Press ENTER to confirm the location
- Press CTRL-C to abort the installation
- Or specify a different location below
```

Press `ENTER`


- Once installation is done, it prompts

```bash
Do you wish to update your shell profile to automatically initialize conda?
This will activate conda on startup and change the command prompt when activated.
If you'd prefer that conda's base environment not be activated on startup,
run the following command when conda is activated:

conda config --set auto_activate_base false

You can undo this by running `conda init --reverse $SHELL`? [yes|no]
```

If `yes` - Adds Conda to your shell startup file. conda is ready every time. 
If `no` - You’ll have to manually source `~/miniforge3/bin/activate` each time.

press `yes` in this case. 


- Successfully installed

```bash
no change     /home/gowtham/miniforge3/condabin/conda
no change     /home/gowtham/miniforge3/bin/conda
no change     /home/gowtham/miniforge3/bin/conda-env
no change     /home/gowtham/miniforge3/bin/activate
no change     /home/gowtham/miniforge3/bin/deactivate
no change     /home/gowtham/miniforge3/etc/profile.d/conda.sh
no change     /home/gowtham/miniforge3/etc/fish/conf.d/conda.fish
no change     /home/gowtham/miniforge3/shell/condabin/Conda.psm1
no change     /home/gowtham/miniforge3/shell/condabin/conda-hook.ps1
no change     /home/gowtham/miniforge3/lib/python3.12/site-packages/xontrib/conda.xsh
no change     /home/gowtham/miniforge3/etc/profile.d/conda.csh
modified      /home/gowtham/.bashrc

==> For changes to take effect, close and re-open your current shell. <==

Running `shell init`, which:
 - modifies RC file: "/home/gowtham/.bashrc"
 - generates config for root prefix: "/home/gowtham/miniforge3"
 - sets mamba executable to: "/home/gowtham/miniforge3/bin/mamba"
The following has been added in your "/home/gowtham/.bashrc" file

# >>> mamba initialize >>>
# !! Contents within this block are managed by 'mamba shell init' !!
export MAMBA_EXE='/home/gowtham/miniforge3/bin/mamba';
export MAMBA_ROOT_PREFIX='/home/gowtham/miniforge3';
__mamba_setup="$("$MAMBA_EXE" shell hook --shell bash --root-prefix "$MAMBA_ROOT_PREFIX" 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__mamba_setup"
else
    alias mamba="$MAMBA_EXE"  # Fallback on help from mamba activate
fi
unset __mamba_setup
# <<< mamba initialize <<<

Thank you for installing Miniforge3!
```

- Close terminal window (Konsole) and open a new one. *conda env base* can be seen.

```bash
(base) gowtham@deb-gowarc:~$ conda --version
conda 25.3.0
```

- To prevent the automatic activation of the conda base environment when you open a new terminal
```bash
conda config --set auto_activate_base false
```

Once again, reopen the terminal. Conda can still be accessed in Konsole but we need to activate the environment when needed.
```bash
gowtham@deb-gowarc:~$ conda --version
conda 25.3.0
gowtham@deb-gowarc:~$ conda activate base
(base) gowtham@deb-gowarc:~$ conda deactivate
gowtham@deb-gowarc:~$ conda env list

# conda environments:
#
base                   /home/gowtham/miniforge3
```

## 6. External Monitor

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

