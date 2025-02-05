from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from clean import pre_process
from filter import filter_function
from airflow.operators.email_operator import EmailOperator
default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 2, 4),
}

with DAG(dag_id='test_dag', default_args=default_args, schedule_interval='@daily') as dag:

    # Task 1: Check if file exists
    check_file = BashOperator(
        task_id='check_file',
        bash_command='ls ~/in_file/Athletes.csv',  # Corrected command
        retries=2,
        retry_delay=timedelta(seconds=15)
    )

    # Task 2: Pre-process data
    pre_process_task = PythonOperator(
        task_id='pre_process',
        python_callable=pre_process
    )

    #task--3 --- FIlter the data

    Filter_data=PythonOperator(
        task_id="Filter_data",
        python_callable=filter_function
    )

    #Task--4 Email
    Send_Email=EmailOperator(
        task_id="Email",
        to="*********@gmail.com",
        subject="hello",
        html_content="<h1> Yoyr Reports are generated Sucessfully,Thanks"
    )


    check_file >> pre_process_task >> Filter_data >> Send_Email