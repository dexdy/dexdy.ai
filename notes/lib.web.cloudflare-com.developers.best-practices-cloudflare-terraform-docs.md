---
id: e27356a0-c592-4280-8203-6f420bd590f4
title: Best practices · Cloudflare Terraform docs (developers.cloudflare.com)
updated: 1703580026205
created: 1703580026205
---

URL :: https://developers.cloudflare.com/terraform/advanced-topics/best-practices/

The key concepts from Cloudflare's best practices for Terraform include:

1. **Managing Terraform Resources in Terraform:** Ensuring Terraform manages all changes and lifecycle of resources.
2. **Directory Structure:** Using a structured directory setup for accounts, zones, and products.
3. **Avoiding or Sparingly Using Modules:** Caution against over-reliance on modules which might lead to sync issues.
4. **Migrating Resources into Terraform:** Utilizing tools like cf-terraforming for integrating existing resources.
5. **Managing Some Resources Outside of Terraform:** Balancing resource management between Terraform and other tools.
6. **Using Separate Environments:** Keeping environments like staging and production separate for safety.
7. **Storing Credentials Safely:** Secure storage of Cloudflare credentials.

For a detailed understanding of these concepts, you can visit the webpage [here](https://developers.cloudflare.com/terraform/advanced-topics/best-practices/).