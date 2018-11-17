# aws-datalake-with-airflow
This code demonstrates the architecture featured of a datalake orchestrated by Apache Airflow.

## The Datalake Bucket:
```
├─s3://unit-datalake-prod-01/
├── README.md          <- The top-level README for developers using this project.
│
├── 01-raw-data-zone   <- The Raw or Persisted area of your Data Lake is where data is kept indefinitely in its raw format.#
│   │                       ✓ Exact copy of source data in native format (aka master dataset in the batch layer)
│   │                       ✓ Immutable to change
│   │                       ✓ History retained indefinitely
│   │                       ✓ Data access is highly limited to few people
│   │                       ✓ Everything downstream can be regenerated from raw
│   │
│   ├── tealium        <- example of raw-data
│   └── google         <- example of raw-data
│
├── 02-transient-zone  <- Useful when data quality or validity checks are required before data can land in the raw zone.
│   │                       ✓ Selectively utilized
│   │                       ✓ Separation of “new data” from “raw data” to ensure data consistency
│   │                       ✓ Transient low-latency data (speed layer)
│   │                       ✓ Data quality validations
│   │
│   ├── 01-athena       <- Athena stores query results in Amazon S3. Each User has his own S3OutputDirectory.
│   └── 02-glue         <- Specifies an S3 path to a bucket that can be used as a temporary directory for the Job.
│   
├── 03-master-data-zone <- Reference data
│   
├── 04-user-drop-zone   <- Manually generated data
│
├── data               <- The Sandbox is designed to be used by deep analysts and scientists as an unmanaged area.
│   └── user           <- user directory
│
├── log                <- Amazon EMR, Hadoop and Glue produce log files that report status on the cluster.
│   ├── emr            <- optinonal
│   ├── hadoop         <- optinonal
│   └── glue           <- optinonal
│

│
├── warehouse          <- Analytic or Curated. In this section of the Data Lake, the data has been heavily processed.
│   │                     Sometimes it is aggregated and stored in a star schema-like format to conform with different
│   │                     reporting and analysis tools.
│   ├── stage          <- Transit storage for data in the ETL process
│   ├── cleanse        <- Cleansing storage for data in the ETL process
│   ├── core           <- The Core represents the central database within the Data Lake.
│   └── mart           <- Data marts are sections of data warehouses, smaller data pools for applications
│
└──references          <- Data dictionaries, manuals, and all other explanatory materials.
```


# Links
https://github.com/aws/aws-cli/tree/develop/scripts

https://github.com/aws-samples/aws-concurrent-data-orchestration-pipeline-emr-livy

https://medium.com/@fartashh/scalable-data-engineering-platform-on-cloud-a557026aa02e

https://developer.okta.com/blog/2018/07/31/use-aws-cloudformation-to-automate-static-site-deployment-with-s3
