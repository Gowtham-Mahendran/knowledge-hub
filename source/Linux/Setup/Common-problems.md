
## NVIDIA Driver

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
nvidia-detect
```
The output list the device driver compatible for your PC

```bash
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
