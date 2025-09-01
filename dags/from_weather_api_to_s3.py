from airflow import DAG
import pendulum

from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
import json
import duckdb


OWNER = 'k.bogatyrev'