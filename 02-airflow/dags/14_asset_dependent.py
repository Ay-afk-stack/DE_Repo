from airflow.sdk import dag, task, asset
from pendulum import datetime
import os
from assets_13 import fetch_data

@asset(
    schedule = fetch_data,
    # This is optional but good to include for clarity about the asset's location where data will be stored.
    uri = '/opt/airflow/logs/data/data_process.txt',
    name = 'process_data'
)
def process_data(self):
    os.makedirs(os.path.dirname(self.uri), exist_ok = True)
    
    with open(self.uri, 'w') as f:
        f.write(f"Data processed successfully!!!\n")
    
    print(f"Data Processed to {self.uri}")