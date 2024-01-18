---
id: 1hygstjkos2ziz3x2ssnc0v
title: "ClickHouse's Storage Engines List"
desc: ''
updated: 1705052557812
created: 1705052029251
---

ClickHouse offers a variety of table engines, each tailored for specific use cases. Here's a list of some of the key table engines available in ClickHouse:

1. **MergeTree**: The default engine used for storing large amounts of data. It is optimized for read and write operations and supports data replication and partitioning.

2. **ReplacingMergeTree**: Similar to MergeTree but with an additional feature that allows it to replace rows during the merge process based on a specified version column.

3. **SummingMergeTree**: A variation of MergeTree that can automatically sum the numeric columns for rows with the same primary key during the merge process.

4. **AggregatingMergeTree**: This engine is used for incremental data aggregation. It stores data in an intermediate aggregated state which can be further merged and aggregated.

5. **CollapsingMergeTree**: Designed for implementing simple clickstream analysis systems. It marks rows for deletion by a special 'sign' column and deletes them during the merge process.

6. **VersionedCollapsingMergeTree**: A combination of the Versioned and Collapsing engines. It is useful for maintaining versions of rows and collapsing rows marked for deletion.

7. **GraphiteMergeTree**: Optimized for Graphite data. It can roll up data according to the specified rules which are compatible with Graphite.

8. **Log**: Intended for storing log data for a short period. It writes data in the order of insertion and does not support indexes.

9. **TinyLog**: Similar to the Log engine but for small tables.

10. **StripeLog**: Another engine for small tables, stores data in stripes.

11. **Memory**: Stores all data in RAM. Useful for temporary data or small reference tables that need to be very fast to read.

12. **Buffer**: Provides a buffer for another table engine. It stores data in memory and periodically flushes it to the underlying table engine.

13. **Distributed**: Used for distributed processing of data across multiple ClickHouse nodes. It doesn't store data itself but allows querying data distributed over several physical servers.

14. **Kafka**: Integrates with Apache Kafka for streaming data ingestion.

15. **MaterializedView**: Used to implement materialized views which store data transformed by a SELECT query.

16. **URL**: Allows reading data from HTTP(s)/FTP servers using GET requests.

Each engine has its own set of features and is optimized for specific tasks and scenarios. The choice of engine depends on the specific requirements of the data storage and the queries that will be run against it.