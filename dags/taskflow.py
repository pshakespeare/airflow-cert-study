# from airflow import DAG
from airflow.decorators import dag, task
# from airflow.operators.python import PythonOperator

from datetime import datetime


# def task_a():
#     print("Task A")
#     return 42

# def task_b(ti=None):
#     print("Task B")
#     print(ti.xcom_pull(task_ids="task_a"))

@dag(
    start_date=datetime(2023, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["taskflow"]
)
def taskflow():
    @task
    def task_a():
        print("Task A")
        return 42

    @task
    def task_b(value):
        print("Task B")
        print(value)

    task_b(task_a())

taskflow()
# with DAG(
#     dag_id="taskflow",
#     start_date=datetime(2023, 1, 1),
#     schedule="@daily",
#     catchup=False,
#     tags=["taskflow"]
# ):
#     task_a = PythonOperator(
#         task_id="task_a",
#         python_callable=_task_a
#     )

#     task_b = PythonOperator(
#         task_id="task_b",
#         python_callable=_task_b
#     )

#     task_a >> task_b