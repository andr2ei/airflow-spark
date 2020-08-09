from airflow import DAG
from datetime import timedelta
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': True,
    'start_date': days_ago(2),
    # 'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

_config = {
    'conn_id': 'spark_standalone',
    'conf': {
        'fs.defaultFS': 'file://'
    },
    'files': None,
    'py_files': None,
    'driver_classpath': None,
    'jars': None,
    'packages': None,
    'exclude_packages': None,
    'repositories': None,
    'total_executor_cores': 2,
    'executor_cores': 2,
    'executor_memory': '1g',
    'keytab': None,
    'principal': None,
    'name': '{{ task_instance.task_id }}',
    'num_executors': 1,
    'verbose': True,
    'application': '/root/airflow/jars/spark-on-aws-1_2.11-0.1.jar',
    'driver_memory': '1g',
    'java_class': 'com.tr.aws.emr.test.Test',
    'application_args': [
        '-f', 'foo',
        '--bar', 'bar',
        '--with-spaces', 'args should keep embdedded spaces'
    ]
}

dag = DAG(
    'spark_test',
    default_args=default_args,
    description='A simple spark DAG',
    schedule_interval=timedelta(days=1),
)

t1 = SparkSubmitOperator(
    task_id='print_spark_count',
    dag=dag,
    **_config
)