# airflow/dags/elt_dag.py

from datetime import datetime
from airflow import DAG
from docker.types import Mount
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.docker.operators.docker import DockerOperator
import subprocess

CONN_ID = '5c82b98e-7eba-445c-9851-da48fffe7a8c'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
#    'retries': 1,
#    'retry_delay': timedelta(minutes=5)
}

# def run_elt_script():
#     script_path = "/opt/airflow/elt/elt_script.py"
#     result = subprocess.run(['python', script_path],
#                             capture_output=True, text=True)
    
#     if result.returncode != 0:
#         raise Exception(f"Script failed with error: {result.stderr}")
#     else:
#         print(result.stdout)

dag = DAG(
    'elt_and_dbt',
    default_args=default_args,
    description='An ELT workflow with dbt',
    start_date=datetime(2024,7,30),
    catchup=False
)

t1 = AirbyteTriggerSyncOperator(
    task_id="airbyte_postgres_postgres",
    airbyte_conn_id='airbyte',
    connection_id=CONN_ID,
    asynchronous=False,
    timeout=3600,
    wait_seconds=3,
    dag=dag
)

t2 = DockerOperator(
    task_id="dbt_run",
    image='ghcr.io/dbt-labs/dbt-postgres:1.8.2',
    command=[
        "run",
        "--profiles-dir",
        "/app/.dbt",
        "--project-dir",
        "/dbt"
    ],
    auto_remove=True,
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    mounts=[
        Mount(source='/home/amrit/data-projects/data-engineering/elt-demo/custom_postgres',
              target='/dbt', type='bind'),
        Mount(source='/home/amrit/.dbt',
              target='/app/.dbt', type='bind')
    ],
    dag=dag
)

t1 >> t2