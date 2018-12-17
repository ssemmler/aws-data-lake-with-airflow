######################################################################################
##
## AWS Glue Tutorial DAG
## Example of an AWS Glue DAG that executes a glue job with the help of an operator
## and waits for the end with a sensor.
## Autor: Stephan Semmler 2018-12-04
## GitHub: https://github.com/ssemmler/aws-data-lake-with-airflow/blob/master/airflow/
#####################################################################################
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import AwsGlueOperator, AwsGlueSensor


dag = DAG('aws_glue_test_dag', description='AWS Glue tutorial DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

start_task = DummyOperator(task_id='start_task', dag=dag)

glue_sensor_task = AwsGlueSensor(task_id                = 'glue_sensor_task',
                                 glue_operator_taskname = 'glue_operator_task',
                                 poke_interval          = 30,
                                 dag                    = dag)

glue_operator_task = AwsGlueOperator(glue_operator_jobname        = 'df_stg_date',
                                     glue_operator_region         = 'eu-west-1',
                                     glue_operator_effectiv_date  = '2018-11-15',
                                     task_id                      = 'glue_operator_task',
                                     dag                          = dag)
end_task = DummyOperator(task_id = 'end_task',
                         dag     = dag)

start_task >> glue_operator_task >> glue_sensor_task >> end_task
