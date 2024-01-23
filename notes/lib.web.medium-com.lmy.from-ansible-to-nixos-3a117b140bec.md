---
id: 9cea0f0d-228b-4749-b24a-6960d2582dc3
title: From Ansible To Nixos (lmy.medium.com)
updated: 1705999280404
created: 1705999280404
---

URL :: https://lmy.medium.com/from-ansible-to-nixos-3a117b140bec

- **The problem**: The author frequently bricked their Raspberry Pi with system updates and wanted a way to restore a working state without reinstalling the OS or using a backup image.
- **The solution**: The author used Ansible, a tool for Infrastructure as Code (IaC), to automate the setup process and install various services on their Raspberry Pi.
- **The drawbacks**: Ansible was slow, verbose, and platform-dependent. It also did not guarantee atomicity of system updates, meaning the system could break halfway.
- **The alternative**: The author considered using NixOS, a Linux distribution that supports snapshots and atomic updates, to avoid rebuilding the system from scratch.
- **Cross-compiling NixOS packages for RPi**: The author plans to write about how to use a more powerful machine to compile NixOS packages for Raspberry Pi in a future post.
- **Rolling back to a last-known good configuration with NixOS**: The author also intends to explore how to use NixOS to revert to a previous system state, but faces a problem with the USB keyboard not working on the boot menu.
- **Reference to another article**: The author recommends reading the post from Michael Lynch, who also migrated from Ansible to NixOS this year, and invites feedback from other readers who have done the same.
