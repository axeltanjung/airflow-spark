import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator


with DAG(
    dag_id="test_pipeline",
    start_date=datetime.datetime(2024, 2, 13),
    schedule_interval="5 7 * * *",
) as dag:
    start = DummyOperator(
        task_id = "start",
        dag = dag
    )

    extract = DummyOperator(
        task_id = "extract",
        dag = dag
    )

    load = DummyOperator(
        task_id = "load",
        dag = dag
    )

    transform = DummyOperator(
        task_id = "transform",
        dag = dag
    )

    end = DummyOperator(
        task_id = "end",
        dag = dag
    )

    start >> extract >> load >> transform >> end
