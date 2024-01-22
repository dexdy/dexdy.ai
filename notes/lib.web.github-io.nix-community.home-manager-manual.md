---
id: fa2c1374-498c-485d-aa76-9958e9aadadd
title: Home Manager Manual (nix-community.github.io)
updated: 1705659028455
created: 1705659028455
---

URL :: https://nix-community.github.io/home-manager/

- **Home Manager**: A tool that allows you to manage your user environment using Nix.
- **Installation methods**: There are three ways to install Home Manager: as a standalone tool, as a module within a NixOS system configuration, or as a module within a nix-darwin configuration.
- **Configuration file**: The main file where you specify your Home Manager options, typically found at ~/.config/home-manager/home.nix or ~/.config/home-manager/flake.nix.
- **Build and activation**: The steps to apply your configuration to your user environment, which also perform validity checks and collision detection.
- **Home Manager configuration**: You can run the Home Manager command directly from its flake to create an initial configuration in ~/.config/home-manager. You can override the default configuration directory with the --home-dir option.
- **Flake inputs**: You need to use the standard nix flake update command to update the flake inputs. The Home Manager nix-darwin module is similar to the NixOS module and uses the same flake URI.
- **Module system**: The Home Manager module system is based on the NixOS module system and supports the same basic option types. Some Home Manager options use custom types, such as hm.types.gvariant, which are described in more detail.
- **Contributions**: Contributions to Home Manager are welcome and should follow the guidelines in the page. The guidelines cover topics such as licensing, formatting, testing, documentation, and news entries.
- **Home Manager module system**: Home Manager uses the same module system as NixOS, but with some custom types and functions.
- **GVariant types**: Home Manager provides a set of functions to construct GVariant values, which are used by some programs like dconf.
- **Contributing to Home Manager**: Home Manager welcomes contributions that follow the guidelines, such as licensing, formatting, testing, and documenting.
- **News system**: Home Manager has a system for presenting news to the user, which should be used for noteworthy changes.