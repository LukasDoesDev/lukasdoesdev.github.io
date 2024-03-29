---
title: "Arch Linux QEMU and KVM setup"
shortDescription: "How to use KVM, QEMU and virt-manager on Arch Linux."
tags: ["linux", "kvm", "qemu", "virt-manager", "arch linux"]
created: "2022-01-23"
author: "ThatOneLukas"
authorData:
    description: "Programmer, gamer, Arch user, open-source contributor"
    image: "https://www.thatonelukas.tk/pictureLogo.png"
    github: "https://github.com/LukasDoesDev"
    twitter: "thatonelukas"
---
How to use KVM, QEMU and `virt-manager` on Arch Linux.

## TL;DR

```bash
LC_ALL=C lscpu | grep Virtualization || exit 1
yay -S qemu virt-manager ebtables dmidecode --needed
sudo systemctl enable libvirtd
sudo systemctl start libvirtd
groups | grep libvirt || sudo usermod -G libvirt -a $USER
```

## Full explanation

The following line checks if we have virtualization enabled for the CPU and exits if we don't.

```bash
LC_ALL=C lscpu | grep Virtualization || exit 1
```

The following line installs QEMU, `virt-manager`, `ebtables` and `dmidecode` with Yay.

```bash
yay -S qemu virt-manager ebtables dmidecode --needed
```

The following lines enable and start the libvirtd systemd unit.

```bash
sudo systemctl enable libvirtd
sudo systemctl start libvirtd
```

The following line checks if we are in the libvirt group and adds us to it if we are not.

```bash
groups | grep libvirt || sudo usermod -G libvirt -a $USER
```
