# Data Cataloging
The earliest challenges that inhibited building a data lake were keeping track of all of the raw assets as they were loaded into the data lake, and then tracking all of the new data assets and versions that were created by data transformation, data processing, and analytics. Thus, an essential component of an Amazon S3-based data lake is the data catalog. The data catalog provides a query-able interface of all assets stored in the data lake’s S3 buckets. The data catalog is designed to provide a single source of truth about the contents of the data lake.

There are two general forms of a data catalog: a comprehensive data catalog that contains information about all assets that have been ingested into the S3 data lake, and a Hive Metastore Catalog (HCatalog) that contains information about data assets that have been transformed into formats and table definitions that are usable by analytics tools like Amazon Athena, Amazon Redshift, Amazon Redshift Spectrum, and Amazon EMR. The two catalogs are not mutually exclusive and both may exist. The comprehensive data catalog can be used to search for all assets in the data lake, and the HCatalog can be used to discover and query data assets in the data lake.

## Comprehensive Data Catalog
The comprehensive data catalog can be created by using standard AWS services like AWS Lambda, Amazon DynamoDB, and Amazon Elasticsearch Service (Amazon ES). At a high level, Lambda triggers are used to populate DynamoDB tables with object names and metadata when those objects are put into Amazon S3 then Amazon ES is used to search for specific assets, related metadata, and data classifications. The following figure shows a high-level architectural overview of this solution.

![Comprehensive-Data-Catalog](https://github.com/ssemmler/aws-data-lake-with-airflow/blob/master/docs/img/Comprehensive-Data-Catalog.png "Comprehensive-Data-Catalog")

###### Figure: Comprehensive data catalog using AWS Lambda, Amazon DynamoDB, and Amazon Elasticsearch Service

## HCatalog with AWS Glue
AWS Glue (now in beta) can be used to create a Hive-compatible Metastore Catalog of data stored in an Amazon S3-based data lake. To use AWS Glue to build your data catalog, register your data sources with AWS Glue in the AWS Management Console. AWS Glue will then crawl your S3 buckets for data sources and construct a data catalog using pre-built classifiers for many popular source formats and data types, including JSON, CSV, Parquet, and more. You may also add your own classifiers or choose classifiers from the AWS Glue community to add to your crawls to recognize and catalog other data formats. The AWS Glue-generated catalog can be used by Amazon Athena, Amazon Redshift, Amazon Redshift Spectrum, and Amazon EMR, as well as third-party analytics tools that use a standard Hive Metastore Catalog. The following figure shows a sample screenshot of the AWS Glue data catalog interface.

![HCatalog with AWS Glue](https://github.com/ssemmler/aws-data-lake-with-airflow/blob/master/docs/img/HCatalog-with-AWS-Glue.png "HCatalog with AWS Glue")

######Figure: Sample AWS Glue data catalog interface

### Defining a Database in Your Data Catalog
When you define a table in the AWS Glue Data Catalog, you add it to a database. A database is used to organize tables in AWS Glue. You can organize your tables using a crawler or using the AWS Glue console. A table can be in only one database at a time.
Your database can contain tables that define data from many different data stores. This data can include objects in Amazon Simple Storage Service (Amazon S3) and relational tables in Amazon Relational Database Service.
For more information about defining a database using the AWS Glue console, see Working with Databases on the AWS Glue Console (https://docs.aws.amazon.com/glue/latest/dg/console-databases.html).

## Planning a Data Lake Data Cataloge
The planning of a Data Lake Data Cataloge is closely linked to the planning of a Data Lake.
[Planning a Data Lake](https://github.com/ssemmler/aws-data-lake-with-airflow/blob/master/s3/data-lake-zones/README.md#planning-a-data-lake)

## Organizing the Data Lake
The individual databases have a similar structure to the Data Lake Zones.
[Organizing the Data Lake Data Cataloge](https://github.com/ssemmler/aws-data-lake-with-airflow/blob/master/s3/data-lake-zones/README.md#organizing-the-data-lake)

### The Data Lake Data Cataloge and his Databases:
```
├─Databases
│
├── A-Transient-DB         <- Useful when data quality or validity checks are required before data can land in the raw zone.
│
├── B-Raw-DB               <- The Raw or Persisted area of your Data Lake is where data is kept indefinitely
│                             in its raw format.
│   
├── C-User-Drop-DB         <- Manually generated data
│   
├── D1-Curated-Stage-DB    <- Transit storage for data in the ETL process
├── D2-Curated-Cleanse-DB  <- Cleansing storage for data in the ETL process
├── D3-Curated-Core-DB     <- The Core represents the central database within the Data Lake.
├── D4-Curated-Mart-DB     <- Data marts are sections of data warehouses, smaller data pools for applications
├── D5-Curated-Export-DB   <- Data staged for a specific purpose
├── D6-Curated-Transfer-DB <- Data staged for a specific application (data warehouse etc.)
│
├── E-Sandbox-DB           <- The Sandbox is designed to be used by deep analysts and scientists as an unmanaged area.
│
├── F-Log-DB               <- Amazon EMR, Hadoop and Glue produce log files that report status on the cluster.
│   
├── G-Archive-DB           <- Active archive of aged data, available for querying when needed
│   
└── H-Master-DB            <- Reference data
```
