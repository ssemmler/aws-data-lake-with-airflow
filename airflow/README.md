# Airflow
2
​
3
aws glue start-job-run  --job-name df_stg_date --region eu-west-1 --arguments EFFECTIV_DATE=2018-11-12
4
'''
chmod 400 airflow_key_pair.pem
ssh -i "airflow_key_pair.pem" ec2-user@ec2-your-public-ip.your-region.compute.amazonaws.com

airflow scheduler

# sudo as the root user
sudo su
# Navigate to the airflow directory which was created by the cloudformation template – Look at the user-data section.
cd ~/airflow
source ~/.bash_profile
'''

5
# Links
https://github.com/apache/incubator-airflow/tree/master/airflow
7
https://github.com/mikeghen/airflow-tutorial
9
10
https://github.com/hgrif/airflow-tutorial
11
12
https://sonra.io/2018/01/01/using-apache-airflow-to-build-a-data-pipeline-on-aws/
13
14
https://aws.amazon.com/blogs/big-data/build-a-concurrent-data-orchestration-pipeline-using-amazon-emr-and-apache-livy/
15
16
https://github.com/astronomer/airflow-guides
17
18
http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/
19
20
https://github.com/postrational/airflow_tutorial/tree/fc918909763eba0a1671ecda4629b4ffec45c441/airflow_home
21
