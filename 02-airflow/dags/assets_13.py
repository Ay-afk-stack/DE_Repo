from airflow.sdk import dag, task, asset
from pendulum import datetime
import os

@asset(
    schedule = '@daily',
    # This is optional but good to include for clarity about the asset's location where data will be stored.
    uri = '/opt/airflow/logs/data/data_extract.txt',
    name = 'fetch_data'
)
def fetch_data(self):
    os.makedirs(os.path.dirname(self.uri), exist_ok = True)
    
    with open(self.uri, 'w') as f:
        f.write(f"Data Fetched on successfully!!!\n")
    
    print(f"Data writtent to {self.uri}")