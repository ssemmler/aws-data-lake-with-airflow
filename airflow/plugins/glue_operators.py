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

class AwsGlueOperator(BaseOperator):

    @apply_defaults
    def __init__(self, glue_operator_jobname, glue_operator_region, glue_operator_effectiv_date, *args, **kwargs):
        self.operator_jobname       = glue_operator_jobname
        self.operator_region        = glue_operator_region
        self.operator_effectiv_date = glue_operator_effectiv_date
        super(AwsGlueOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        response = glue.start_job_run(JobName=self.operator_jobname, Arguments={'--region': self.operator_region, '--EFFECTIV_DATE': self.operator_effectiv_date})
        log.info("Start Glue Job!")
        log.info('JobRunId     : %s', response['JobRunId'])
        log.info('JobName      : %s', self.operator_jobname)
        log.info('EffectivDate : %s', self.operator_effectiv_date)
        log.info('Region       : %s', self.operator_region)
        task_instance = context['task_instance']
        task_instance.xcom_push('glue_job_run_id', response['JobRunId'])
        task_instance.xcom_push('glue_job_name'  , self.operator_jobname)
class AwsGlueSensor(BaseSensorOperator):
    template_fields = tuple()
    ui_color = '#b5f2ff'

    @apply_defaults
    def __init__(self, glue_operator_taskname, *args, **kwargs):
        self.operator_taskname = glue_operator_taskname
        super(AwsGlueSensor, self).__init__(*args, **kwargs)

    def poke(self, context):
        task_instance = context['task_instance']
        glue_job_run_id     = task_instance.xcom_pull(self.operator_taskname, key='glue_job_run_id')
        glue_job_run_name   = task_instance.xcom_pull(self.operator_taskname, key='glue_job_name')
        log.info('JobRunId   : %s', glue_job_run_id)
        log.info('JobRunName : %s', glue_job_run_name)
        log.info('TaskName   : %s', self.operator_taskname)
        glue_job_run_status = glue.get_job_run(JobName=glue_job_run_name, RunId=glue_job_run_id)
        log.info("The glue_job_run_status (Sensor) Begin: %s", glue_job_run_status['JobRun']['JobRunState'])
        if glue_job_run_status['JobRun']['JobRunState'] != 'SUCCEEDED':
            log.info("The glue_job_run_status (Sensor) Loop: %s", format(glue_job_run_status['JobRun']['JobRunState']))
            return False

        log.info("The glue_job_run_status (Sensor) End: %s", format(glue_job_run_status['JobRun']['JobRunState']))
        task_instance = context['task_instance']
        task_instance.xcom_push('glue_job_run_status', glue_job_run_status['JobRun']['JobRunState'])
        return True


class MyFirstPlugin(AirflowPlugin):
    name = "aws_glue_plugin"
    operators = [AwsGlueOperator, AwsGlueSensor]
