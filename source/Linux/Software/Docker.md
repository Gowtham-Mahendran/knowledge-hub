
# Docker Desktop


## Docker

Install using the official [Documentation](https://docs.docker.com/engine/install/debian/#install-using-the-repository)

Follow [this](https://docs.docker.com/engine/install/linux-postinstall/) after installation

**Here is a guide**

1. KVM virtualization support - [Refer](https://docs.docker.com/desktop/setup/install/linux/)

Docker Desktop runs a VM that requires [KVM support](https://www.linux-kvm.org/). The kvm module should load automatically if the host has virtualization support.

KVM (Kernel-based Virtual Machine) is a Linux kernel module that enables your system to act as a hypervisor — allowing you to run virtual machines (VMs) with near-native performance. KVM lets your Linux system use the CPU's hardware virtualization features to run other operating systems or environments efficiently. It’s built into the Linux kernel (kvm, kvm_intel, or kvm_amd modules). Unlike Docker Engine (which runs containers natively on Linux), Docker Desktop for Linux, Runs Docker inside a virtual machine (VM) for isolation and consistency (like it does on Windows/macOS). That VM is powered by QEMU/KVM. So, Docker Desktop requires KVM to:

* Create and run that internal VM efficiently
* Use hardware-accelerated virtualization

To Check if your CPU supports virtualization:

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

If output is 0: your CPU doesn’t support virtualization or it’s disabled in BIOS. If >0: your CPU supports virtualization. Also, make sure virtualization is enabled in BIOS/UEFI.


To check if the KVM modules are enabled, run:
```bash
lsmod | grep kvm
```

```bash
kvm_amd               163840  0
kvm                  1146880  1 kvm_amd
irqbypass              16384  1 kvm
ccp                   118784  1 kvm_amd
```

[Set up KVM device user permissions](https://docs.docker.com/desktop/setup/install/linux/#set-up-kvm-device-user-permissions)
To check ownership of /dev/kvm, run :

```bash
$ ls -al /dev/kvm
crw-rw----+ 1 root kvm 10, 232 Jun 29 11:54 /dev/kvm
```

Add your user to the kvm group in order to access the kvm device:

```bash
sudo usermod -aG kvm $USER
```

Sign out and sign back in so that your group membership is re-evaluated.

Check and verify,
```bash
groups gowtham
```

It will show 
```bash
gowtham : gowtham cdrom floppy sudo audio dip video plugdev users kvm netdev bluetooth lpadmin scanner
```

2. GNOME terminal - [Refer](https://docs.docker.com/desktop/setup/install/linux/debian/)

If you're not using GNOME, you must install gnome-terminal to enable terminal access from Docker Desktop:

```bash
sudo apt install gnome-terminal
```
3. [Uninstall old versions](https://docs.docker.com/engine/install/debian/#uninstall-old-versions)
Before you can install Docker Engine, you need to uninstall any conflicting packages.

Your Linux distribution may provide unofficial Docker packages, which may conflict with the official packages provided by Docker. You must uninstall these packages before you install the official version of Docker Engine.

The unofficial packages to uninstall are:
* docker.io
* docker-compose
* docker-doc
* podman-docker
Moreover, Docker Engine depends on `containerd` and `runc`. Docker Engine bundles these dependencies as one bundle: `containerd.io`. If you have installed the `containerd` or `runc` previously, uninstall them to avoid conflicts with the versions bundled with Docker Engine.

Run the following command to uninstall all conflicting packages:
```bash
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

This will uninstall all the packages if anything is present.

4. [Install using the apt repository](https://docs.docker.com/engine/install/debian/#install-using-the-repository)

Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker apt repository. Afterward, you can install and update Docker from the repository.
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
```

To install Docker packages, use
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Verify that the installation is successful by running the hello-world image:

```bash
sudo docker run hello-world
```
This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits.

```bash
gowtham@deb-gowarc:~$ sudo docker run hello-world
[sudo] password for gowtham: 
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
e6590344b1a5: Pull complete 
Digest: sha256:940c619fbd418f9b2b1b63e25d8861f9cc1b46e3fc8b018ccfe8b78f19b8cc4f
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
1. The Docker client contacted the Docker daemon.
2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
   (amd64)
3. The Docker daemon created a new container from that image which runs the
   executable that produces the output you are currently reading.
4. The Docker daemon streamed that output to the Docker client, which sent it
   to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
$ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
https://hub.docker.com/

For more examples and ideas, visit:
https://docs.docker.com/get-started/


You have now successfully installed and started Docker Engine.
```

## Resolving Docker duplicate installations

If there are 2 docker versions, they may conflict with each other. To check,
```bash
gowtham@deb-gowarc:~/Documents/Gitlab/python-course-platform$ docker context ls
NAME            DESCRIPTION                               DOCKER ENDPOINT                                    ERROR
default *       Current DOCKER_HOST based configuration   unix:///var/run/docker.sock                        
desktop-linux   Docker Desktop                            unix:///home/gowtham/.docker/desktop/docker.sock   
```

The star* next to desktop-linux was there before you switched. After `docker context use default`, the “*” moves to default, meaning all CLI commands now talk to /var/run/docker.sock (the system daemon) instead of the Desktop socket. Now you can safely uninstall docker desktop if you are okay working with CLI (Command Line Interface).

To simply delete the named “desktop-linux” context from your local Docker CLI configuration.
```bash
docker context rm desktop-linux
```
Stop & disable the Desktop service 
```bash
systemctl --user stop docker-desktop
systemctl --user disable docker-desktop
```
Uninstall the Docker Desktop package using
```bash
sudo apt remove docker-desktop
sudo apt autoremove
```