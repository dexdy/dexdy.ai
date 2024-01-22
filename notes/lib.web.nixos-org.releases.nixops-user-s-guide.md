---
id: e655ec4a-00e7-4ace-afda-ee2db8fa0dcd
title: NixOps User's Guide (releases.nixos.org)
updated: 1705658727041
created: 1705658727041
---

URL :: https://releases.nixos.org/nixops/latest/manual/manual.html

- **NixOps**: A tool for deploying NixOS machines in a network or cloud, based on a declarative specification of logical and physical aspects of a deployment.
- **Nix**: A package manager that supports multiple versions, atomic upgrades, rollbacks, dependency completeness, and more.
- **NixOS**: A Linux distribution that uses Nix for system configuration management, with features such as nearly atomic upgrades, rollbacks, and more.
- **Deployment examples**: The page provides examples of how to deploy NixOS machines to various environments, such as VirtualBox, Amazon EC2, Google Compute Engine, Microsoft Azure, and others.
- **Logical machine specification**: A logical machine is a Nix expression that describes the desired configuration of a machine, such as the Apache web server¹[1].
- **Physical specification**: A physical specification is a Nix expression that tells NixOps to what environment the logical machines should be deployed, such as VirtualBox, EC2, GCE, or Azure.
- **NixOps commands**: NixOps provides various commands to create, deploy, modify, and destroy networks of machines, such as nixops create, nixops deploy, nixops destroy, etc.
- **Deployment examples**: The page shows several examples of deploying the same network of machines to different environments, such as VirtualBox, EC2, GCE, and Azure, and explains the differences and limitations of each environment.
- **NixOps deployment on Hetzner machines**: You can order machines from Hetzner's web interface and reference them by their main IP address in the NixOps network expression.
- **Partitioning and installing NixOS**: You can use Anaconda's format to partition the disks and use RAID1 for redundancy. You can also customize the partition layout by using deployment.hetzner.partitions option.
- **Robot credentials**: You need to provide the credentials for the Robot account to manage the machines. You can use environment variables or configuration options, but the former is recommended for security reasons.
- **Other deployment backends**: The page also briefly mentions how to use other backends such as libvirtd, GCE, and Azure. It provides some examples and links to more details.
- **Azure Directory**: A resource that allows creating a directory in an Azure storage service.
- **Azure DNS Record Set**: A resource that allows creating a DNS record set in an Azure DNS zone.
- **Azure DNS Zone**: A resource that allows creating a DNS zone in Azure.
- **Azure ExpressRoute Circuit**: A resource that allows creating a dedicated network connection between Azure and an on-premises location.
- **Service provider**: The name of the service provider that offers the ExpressRoute circuit. This must match the provider name returned by "azure network express-route provider list".
- **Bandwidth**: The bandwidth of the ExpressRoute circuit in Mbps. This must match one of the bandwidths offered by the chosen service provider.
- **Peering location**: The peering location for the ExpressRoute circuit. This must match one of the peering locations for the chosen service provider.
- **SKU**: The family and tier of the SKU of the ExpressRoute circuit. The family can be MeteredData or UnlimitedData, and the tier can be Standard or Premium.
- **BGP peering properties**: An attribute set of BGP peering properties, such as ASN, peer IP address, and primary/secondary prefix. The property list and allowed values depend on the peering type, which can be AzurePrivatePeering, AzurePublicPeering, or MicrosoftPeering.
- **Datadog Screenboard Resource**: This section explains how to define a Datadog screenboard by setting resources.dataogScreenboards. to an attribute set containing values for the Datadog API Key, APP Key, and the name of the dashboard.
- **Notes on hacking NixOps**: This section provides some instructions on how to get the latest version of NixOps from GitHub, and how to run some tests involving EC2 resources.
- **Release notes**: This section lists the changes and improvements made in various versions of NixOps, such as new features, bug fixes, documentation updates, and contributors. Some of the notable changes include:
    - Support for GCE routes, IPv6 on Digital Ocean, CloudWatch metrics and alarms, and separate Route53 resources.
    - Support for custom kernel/initrd/cmdline, and --dry-activate and --max-jobs options for the deploy command.
    - Support for deployment.keys.*.keyFile and deployment.keys.*.destDirdeployment.keys.*.path options to provide keys from local files and control where they are stored on the deployed machine.
    - Support for creating "persistent" domains for libvirt backend, and using images from nixpkgs for Azure and GCE backends.
