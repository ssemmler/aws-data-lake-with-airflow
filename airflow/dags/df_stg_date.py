"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/incubator-airflow/blob/master/airflow/example_dags/tutorial.py
"""
import random

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': ['stephan.semmler@axelspringer.de'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('df_stg_date', default_args=default_args, schedule_interval=None)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='df_stg_date',
    bash_command='aws glue start-job-run  --job-name df_stg_date --region eu-west-1 --output text --arguments EFFECTIV_DATE=2018-11-12',
    xcom_push=True,
    dag=dag)

t2 = BashOperator(
  task_id='df_stg_date_job_id',
  bash_command="echo {{ ti.xcom_pull('df_stg_date') }}",
  retries=0,
  dag=dag)

t2.set_upstream(t1)
