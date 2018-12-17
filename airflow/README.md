# Airflow
```
# Starts a job run using a job definition.
aws glue start-job-run  --job-name df_stg_date --region eu-west-1 --output json --arguments EFFECTIV_DATE=2018-11-12 | jq -r ".JobRunId"

# Contains information about a job run.
aws glue get-job --job-name df_stg_date --region eu-west-1

# Retrieves metadata for all runs of a given job definition.
aws glue get-job-run --job-name df_stg_date --run-id jr_8e9e19b85f3fcc1e21cee9f3763e62030547e4b9611abde33e781accc790fda7 --region eu-west-1 --output  json | jq -r ".JobRun.JobRunState"
SUCCEEDED
```

```
chmod 400 airflow_key_pair.pem
ssh -i "airflow_key_pair.pem" ec2-user@ec2-your-public-ip.your-region.compute.amazonaws.com

# sudo as the root user
sudo su
# Navigate to the airflow directory which was created by the cloudformation template – Look at the user-data section.
cd ~/airflow
source ~/.bash_profile

airflow scheduler

```
## Airflow date macros, ds and execution_date
A very common pattern when developing ETL workflows in any technology is to parameterize tasks with the execution date, so that tasks can, for example, work on the right data partition. Apache Airflow allows the usage of Jinja templating when defining tasks, where it makes available multiple helpful variables and macros to aid in date manipulation.

A simple task that executes a run.sh bash script with the execution date as a parameter might look like the following:

```
task = BashOperator(
    task_id='bash_script',
    bash_command='./run.sh {{ ds }}',
    dag=dag)
```

The {{ }} brackets tell Airflow that this is a Jinja template, and ds is a variable made available by Airflow that is replaced by the execution date in the format YYYY-MM-DD. Thus, in the dag run stamped with 2018-06-04, this would render to:

```
./run.sh 2018-06-04

```

For more Information see this [Link]( https://diogoalexandrefranco.github.io/about-airflow-date-macros-ds-and-execution-date/).

# Links
https://github.com/apache/incubator-airflow/tree/master/airflow

https://github.com/mikeghen/airflow-tutorial

https://github.com/hgrif/airflow-tutorial

https://sonra.io/2018/01/01/using-apache-airflow-to-build-a-data-pipeline-on-aws/

https://aws.amazon.com/blogs/big-data/build-a-concurrent-data-orchestration-pipeline-using-amazon-emr-and-apache-livy/

https://github.com/astronomer/airflow-guides

http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/

https://github.com/postrational/airflow_tutorial/tree/fc918909763eba0a1671ecda4629b4ffec45c441/airflow_home

###### Use AWS CLI and jq to do some things
https://gist.github.com/brasey/088654b67cb00f88bbaf

###### About Airflow date macros, ds and execution_date
https://diogoalexandrefranco.github.io/about-airflow-date-macros-ds-and-execution-date/
https://airflow.apache.org/code.html#macros
