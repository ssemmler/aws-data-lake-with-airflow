# Data Lake
A data lake is one piece of an overall data management strategy. Conceptually, a data lake is nothing more than a data repository. The data lake can store any type of data. Cost and effort are reduced because the data is stored in its original native format with no structure (schema) required of it initially.

# Planning a Data Lake
There's various things you want to consider as you're planning a data lake -- to prevent it from becoming the dreaded data swamp -- including things such as:

-  Ingestion needs (push / pull via streaming or batch)
-  Security around data access
-  Data retention and archival policies
-  Encryption requirements
-  Governance
-  Data quality
-  Master data management
-  Validity checks necessary
-  Metadata management
-  Organization of data for optimal data retrieval
-  Scheduling and job management
-  Logging and auditing
-  To what extent data federation will be utilized
-  Enrichment, standardization, cleansing, and curation needs
-  Technology choices comprising the overall data lake architecture (HDFS, Hadoop components, NoSQL DBs, relational DBs, etc.)
-  Modular approach to the overall design

You definitely want to spend some time planning out how the data will be organized so that finding the data is as straightforward as possible. Just like with planning anything where data is stored (for example, a regular file share, or a SharePoint document library, etc.), you usually want to consider subject areas along with user groups and security boundaries. 

# Organizing the Data Lake
There's many different ways to organize a data lake and there are a couple of organization examples. Above all else, the data lake should be organized for optimal data retrieval. Metadata capabilities of your data lake will greatly influence how you handle organization.

## The Data Lake Bucket:
```
├─s3://unit-data-lake-zones-prod-01/
├── README.md            <- The top-level README for developers using this project.
│
├── A-Transient-Zone     <- Useful when data quality or validity checks are required before data can land in the raw zone.
│   │                          ✓ Selectively utilized
│   │                          ✓ Separation of “new data” from “raw data” to ensure data consistency
│   │                          ✓ Transient low-latency data (speed layer)
│   │                          ✓ Data quality validations
│   │
│   ├── athena           <- Athena stores query results in Amazon S3. Each User has his own S3OutputDirectory.
│   └── glue             <- **--TempDir** — Specifies an S3 path to a bucket that can be used as a temporary 
|                           directory for the Job.
│
├── B-Raw-Data-Zone      <- The Raw or Persisted area of your Data Lake is where data is kept indefinitely 
│   │                        in its raw format.
│   │                          ✓ Exact copy of source data in native format (aka master dataset in the batch layer)
│   │                          ✓ Immutable to change
│   │                          ✓ History retained indefinitely
│   │                          ✓ Data access is highly limited to few people
│   │                          ✓ Everything downstream can be regenerated from raw
│   │
│   ├── tealium           <- example of raw-data
│   └── google            <- example of raw-data
│   
├── C-User-Drop-Zone      <- Manually generated data
│   
├── D-Curated-Data-Zone   <- Analytic or Curated. In this section of the Data Lake, the data has been heavily processed.
│   │                         Sometimes it is aggregated and stored in a star schema-like format to conform with different
│   │                         reporting and analysis tools.
│   │                           ✓ Cleansed and transformed data, organized for optimal data delivery (data warehouse)
│   │                           ✓ Supports self-service
│   │                           ✓ Standard security, change management, and governance
│   │                           ✓ Data staged for a specific purpose or application (data warehouse etc.)
│   ├── stage             <- Transit storage for data in the ETL process
│   ├── cleanse           <- Cleansing storage for data in the ETL process
│   ├── core              <- The Core represents the central database within the Data Lake.
│   ├── mart              <- Data marts are sections of data warehouses, smaller data pools for applications
│   ├── export            <- Data staged for a specific purpose
│   └── transfer          <- Data staged for a specific application (data warehouse etc.)
│
├── E-Sandbox-Zone        <- The Sandbox is designed to be used by deep analysts and scientists as an unmanaged area.
│   └── user.name         <- user directory
│
├── F-Log-Zone            <- Amazon EMR, Hadoop and Glue produce log files that report status on the cluster.
│   ├── emr               <- optinonal
│   ├── hadoop            <- optinonal
│   └── glue              <- optinonal
│   
├── G-Archive-Data-Zone   <- Active archive of aged data, available for querying when needed
│   
└── H-Master-Data-Zone    <- Reference data
```
# Links
https://www.sqlchick.com/
