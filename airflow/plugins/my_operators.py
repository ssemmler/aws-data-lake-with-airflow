import logging
import boto3
from datetime import datetime
from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin
from airflow.utils.decorators import apply_defaults
from airflow.operators.sensors import BaseSensorOperator


glue = boto3.client(service_name='glue', region_name='eu-west-1',
              endpoint_url='https://glue.eu-west-1.amazonaws.com')

log = logging.getLogger(__name__)

class MyFirstOperator(BaseOperator):

    @apply_defaults
    def __init__(self, my_operator_param, *args, **kwargs):
        self.operator_param = my_operator_param
        super(MyFirstOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        response = glue.start_job_run(JobName='df_stg_date',Arguments={'--region': 'eu-west-1','--EFFECTIV_DATE': '2018-11-13'})
        log.info("Hello World!")
        log.info('JobRunId: %s', response['JobRunId'])
        log.info('operator_param: %s', self.operator_param)
        task_instance = context['task_instance']
        task_instance.xcom_push('glue_start_job_run_id', response['JobRunId'])

class MyFirstSensor(BaseSensorOperator):
    template_fields = tuple()
    ui_color = '#b5f2ff'

    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(MyFirstSensor, self).__init__(*args, **kwargs)

    def poke(self, context):
        task_instance = context['task_instance']
        job_run_id = task_instance.xcom_pull('my_first_operator_task', key='glue_start_job_run_id')
        log.info('JobRunId: %s', job_run_id)
        status = glue.get_job_run(JobName='df_stg_date', RunId=job_run_id)
        log.info("The glue_get_job_run_status (Sensor) Begin: %s", status['JobRun']['JobRunState'])
        if status['JobRun']['JobRunState'] != 'SUCCEEDED':
            log.info("The glue_get_job_run_status (Sensor) Loop: %s", format(status['JobRun']['JobRunState']))
            return False

        log.info("The glue_get_job_run_status (Sensor) End: %s", format(status['JobRun']['JobRunState']))
        task_instance = context['task_instance']
        task_instance.xcom_push('glue_get_job_run_status', status['JobRun']['JobRunState'])
        return True


class MyFirstPlugin(AirflowPlugin):
    name = "my_first_plugin"
    operators = [MyFirstOperator, MyFirstSensor]
    
