from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.events import EventsTimetable

special_dates = EventsTimetable(event_dates = [
    datetime(year = 2026, month = 1, day = 1, tz = 'Asia/Kathmandu'),
    datetime(year = 2026, month = 1, day = 15, tz = 'Asia/Kathmandu'),
    datetime(year = 2026, month = 1, day = 26, tz = 'Asia/Kathmandu'),
    datetime(year = 2026, month = 1, day = 30, tz = 'Asia/Kathmandu'),
])

@dag(
    schedule = special_dates,
    start_date = datetime(year = 2026, month = 1, day = 1, tz = 'Asia/Kathmandu'),
    end_date = datetime(year = 2026, month = 1, day = 31, tz = 'Asia/Kathmandu'),
    catchup = True
)
def special_dates_dag():
    
    @task.python
    def special_event_task(**kwargs):
        execution_date = kwargs['logical_date']
        print(f"Running task for special event on {execution_date}")
    
    special_dates = special_event_task()

special_dates_dag()