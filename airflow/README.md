# Airflow
```
aws glue start-job-run  --job-name df_stg_date --region eu-west-1 --arguments EFFECTIV_DATE=2018-11-12
aws glue get-job --job-name df_stg_date --region eu-west-1
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
