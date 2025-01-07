from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
    'retires': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(name, age):
    print(f"hello world my name is {name} and i am {age} years old!")
        
with DAG(
    dag_id='dag_python_operator_v02',
    default_args=default_args,
    description='my first dag using python operator',
    start_date=datetime(2025, 1, 7, 13),
    schedule_interval='@daily'
    ) as dag:
        task1 = PythonOperator(
            task_id='greet_task',
            python_callable=greet,
            op_kwargs={
                'name': 'john doe',
                'age': 30
            }
        )
        task1 
        