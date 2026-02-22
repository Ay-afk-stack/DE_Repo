from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.trigger import CronTriggerTimetable

@dag(
    dag_id = 'schedule_cron',
    start_date = datetime(year=2026, month=2, day=16, tz = 'Asia/Kathmandu'),
    schedule = CronTriggerTimetable("0 16 * * MON-FRI", timezone='Asia/Kathmandu'),
    end_date = datetime(year=2026, month= 2, day= 28, tz = 'Asia/Kathmandu'),
    is_paused_upon_creation= False,
    catchup=True
)
def cron_schedule_dag():
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

cron_schedule_dag()