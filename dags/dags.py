import logging

from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonVirtualenvOperator

args = {
    'owner': 'marian',
    'start_date': days_ago(1)
}

logger = logging.getLogger(__name__)

dag = DAG(dag_id='etl_pipeline',
          default_args=args,
          schedule_interval=None,
          is_paused_upon_creation=True)


def download_data():
    import requests
    url = "http://data-ingestor:5000"
    response = requests.get(url)
    print("_____________RESPONSE_____________")
    print(response.__dict__)


with dag:
    read_data = PythonVirtualenvOperator(
        task_id="read_data_step",
        requirements="requests==2.31.0",
        python_callable=download_data,
    )

    read_data
