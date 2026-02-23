from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.interval import CronDataIntervalTimetable

@dag(
    dag_id = 'incremental_load_dag',
    schedule = CronDataIntervalTimetable("@daily", timezone = 'Asia/Kathmandu'),
    start_date = datetime(year = 2026, month = 2, day = 1, tz = 'Asia/Kathmandu'),
    end_date = datetime(year = 2026, month = 2, day = 28, tz = 'Asia/Kathmandu'),
    catchup = True
)
def incremental_load_dag():
    
    @task.python
    def incremental_data_fetch(**kwargs):
        date_interal_start = kwargs['data_interval_start']
        date_interval_end = kwargs['data_interval_end']
        print(f"Fetching data from {date_interal_start} to {date_interval_end}")
    
    @task.bash
    def incremental_data_process():
        return "echo 'Processing Incremental data from {{ data_interval_start }} to {{ data_interval_end }}'"

    fetch_data = incremental_data_fetch()
    process_data = incremental_data_process()
    
    fetch_data >> process_data

incremental_load_dag()