from airflow.sdk import dag, task
from pendulum import datetime

@dag(
    dag_id = 'schedule_preset',
    start_date = datetime(year=2026, month=2, day=20, tz = 'Asia/Kathmandu'),
    schedule='@daily',
    is_paused_upon_creation= False,
    catchup=True
)
def first_schedule_dag():
    @task.python
    def first_task():
        print("This is the first task")
        
    @task.python
    def second_task():
        print("This is the second task")
        
    @task.python
    def third_task():
        print("This is the third task")
        
    @task.python
    def fourth_task():
        print("This is the fourth task. First Dag run complete!!!")
    
    # instantiation of task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    fourth = fourth_task()

    # assigning orders of task
    
    first >> second >> third >> fourth

first_schedule_dag()