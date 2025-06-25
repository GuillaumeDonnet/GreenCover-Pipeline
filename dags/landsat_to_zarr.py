from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from ingest import stac_to_zarr

default_args = {"retries": 1, "retry_delay": 300}
with DAG("landsat_to_zarr", start_date=datetime(2025,1,1), schedule_interval="@daily", default_args=default_args):
    PythonOperator(task_id="ingest", python_callable=stac_to_zarr)
