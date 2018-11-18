# Data Lake Scripts

```
├─s3://unit-data-lake-prod-01/
├── README.md          <- The top-level README for developers using this project.
├── aws                <- AWS scripts
│   └── bin            <- Shell scripts to start AWS Cluster manually or via Crontab and AWS CLI with Json-Configuration
│
├── emr                <- Shell scripts to start EMR clusters
│   ├── bin            <- Single shell scripts to execute the steps and actions
│   │   ├── action     <- You can use a bootstrap action to install additional software or
│   │   │                 customize the configuration of cluster instances.
│   │   └── step       <- Submitting Work to a Cluster
│   │
│   └── config         <- A list of configurations to apply to this configuration.
│                         You can nest configurations so that a single configuration can have its own configurations.
│
├── hive               <- Hive is an open-source, data warehouse, and analytic package that runs on top of a Hadoop cluster.
│   ├── libs           <- a collection of UDF's like brickhouse ot json serde (https://github.com/klout/brickhouse)
│   └── sql            <- Hive scripts use an SQL-like language called Hive QL (query language) that abstracts programming
│                         models and supports typical data warehouse interactions.
│
├── oozie              <- Use the Apache Oozie Workflow Scheduler to manage and coordinate Hadoop jobs.
│   │                     For more information, see http://oozie.apache.org/.
│   ├── dataflow       <- Corresponds to a transformation in the workflow
│   │   ├── stage      <- Transit storage for data in the ETL process
│   │   ├── cleanse    <- Cleansing storage for data in the ETL process
│   │   ├── core       <- The Core represents the central database within the Data Lake.
│   │   ├── mart       <- Data marts are sections of data warehouses, smaller data pools for applications
│   │   │                 that serve specific user groups such as specific departments or task areas.
│   │   ├── bin        <- optional
│   │   └── export     <- optional
│   │                     
│   └── workflow       <- Aggregates multiple dataflows
│
├── jupyter/emr        <- JupyterHub allows you to host multiple instances of a single-user Jupyter notebook server. When
│   │                     you create a cluster with JupyterHub, Amazon EMR creates a Docker container on the cluster's
│   │                     master node. JupyterHub, all the components required for Jupyter, and Sparkmagic run within the
│   │                     container.
│   ├── config         <- config files
│   ├── libs           <- Python Scripts
│   └── user           <- User
│       └── notebook   <- Jupyter-Notebooks for each user
│
├── zeppelin/emr       <- Use Apache Zeppelin as a notebook for interactive data exploration. For more information about
│   │                     Zeppelin, see https://zeppelin.apache.org/. Zeppelin is included in Amazon EMR release version
│   │                     5.0.0 and later. Earlier release versions include Zeppelin as a sandbox application. For more
│   │                     information, see Amazon EMR 4.x Release Versions.
│   ├── apps           <- Scripts to download or generate data
│   ├── config         <- config files
│   ├── img            <- Images for visualistion
│   └── notebook       <- Notebooks
│
├── rstudio/emr        <- Running sparklyr – RStudio’s R Interface to Spark on Amazon EMR
│   └── user           <- User
│       └── notebook   <- R-Notebooks for each user
│
├── sagemaker          <- Amazon SageMaker is a fully managed machine learning service.
│   └── user           <- user directory
│       └── notebook   <- Sagemaker Notebooks
│
├── glue               <- AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for
│   │                     customers to prepare and load their data for analytics.
│   ├── notebook       <- Glue Notebooks
│   │   └── user       <- user directory
│   │       └── notebook   
│   └── scripts        <- AWS Glue supports an extension of the PySpark Python dialect for scripting ETL - jobs. 
|                         **--scriptLocation**  —  The S3 location where your ETL script is located (in a form like
|                         s3://path/to/my/script.py). This overrides a script location set in the JobCommand object.
│
└── references         <- Data dictionaries, manuals, and all other explanatory materials.
```

# Links
