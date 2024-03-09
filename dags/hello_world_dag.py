from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',                     # Owner of the DAG
    'depends_on_past': False,               # DAG does not depend on past executions
    'start_date': days_ago(1),              # Start date of the DAG (1 day ago)
    'email': ['example@airflow.com'],       # Notification email address
    'email_on_failure': False,              # Do not send email on task failure
    'email_on_retry': False,                # Do not send email on task retry
    'retries': 1,                           # Number of retries if task fails
    'retry_delay': timedelta(minutes=1)     # Delay between retries
}

dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='Our first DAG',            # Description of the DAG
    schedule_interval=timedelta(days=1),    # Execution interval
)

hello_world_task = PythonOperator(
    task_id='hello_world',
    python_callable=lambda: print("♪ La, la, la, laaah, Hello World! ♪"), 
    dag=dag,
)

# Define the task execution order
hello_world_task 