---
id: 1b92d2ac-da5f-450c-987c-89f14067dd18
title: Use natural language to execute SQL queries | Semantic Kernel (devblogs.microsoft.com)
updated: 1701878820803
created: 1701878820803
---

URL :: https://devblogs.microsoft.com/semantic-kernel/use-natural-language-to-execute-sql-queries/

**NL2SQL Sandbox** : This is a tool that allows users to query their
relational database using natural language expressions. It uses GPT-4 to
generate SQL queries from natural language objectives and schema meta-data.

**Schema Meta-Data** : This is a YAML format that describes the table and
column names, references, descriptions and platform of the database. It helps
the model to reason over the schema and produce the correct SQL variant.

**Query Generation** : This is a low/no-shot approach that uses two sequential
prompts: IsQuery and GenerateQuery. The model responds to semantic nuance and
clarity of the objectives, but cannot reason over the data itself.

**Best Practices** : These are some guidelines to ensure security, privacy and
validity of the data access and query generation. They include least
privilege, credential management, injection prevention and design-time schema
capture.

