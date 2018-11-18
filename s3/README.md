# S3-Data-Engineering
This project transforms and stores data for each unit into a useful format for analysis.

## S3-Directory-Structure
Two buckets are created for each unit or for the global profile. The Application Bucket contains all the scripts required to start the cluster and execute the transformations.
The data bucket (data lake) contains all data, from the raw data to the curated data including its processing steps. In addition, all logs etc. are stored here.

<Units:> unit_1, ... , unit_n

<Evironment:> test, dev, prod

# Links
[Data Lake Zones](https://github.com/ssemmler/aws-data-lake-with-airflow/tree/master/s3/data-lake-zones)

[Data Lake Scripts](https://github.com/ssemmler/aws-data-lake-with-airflow/tree/master/s3/data-lake-scripts)
