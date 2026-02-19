from airflow.sdk import dag, task

@dag(
    dag_id = 'parallel_tasks'
)
def parallel_tasks():
    @task.python
    def extract_task(**kwargs):
        print("Extracting Data...")
        ti = kwargs['ti']
        extracted_data = {
                            'api_data': [1, 2, 3, 4, 5],
                            'db_data': [6, 7, 8, 9, 10],
                            's3_data': [11, 12, 13, 14, 15],
                        }
        ti.xcom_push(key = 'extracted_data', value = extracted_data)
    
    @task.python
    def transform_api_data(**kwargs):
        ti = kwargs['ti']
        extracted_api_data = ti.xcom_pull(task_ids = 'extract_task', key = 'extracted_data')['api_data']
        print(f"Transforming API data: {extracted_api_data}")
        transformed_api_data = [i * 10 for i in extracted_api_data]
        ti.xcom_push(key = 'return_transformed_api_data', value = {'transformed_api_data' : transformed_api_data})
    
    @task.python
    def transform_db_data(**kwargs):
        ti = kwargs['ti']
        extracted_db_data = ti.xcom_pull(task_ids = 'extract_task', key = 'extracted_data')['db_data']
        print(f"Transforming DB data: {extracted_db_data}")
        transformed_db_data = [i * 10 for i in extracted_db_data]
        ti.xcom_push(key = 'return_transformed_db_data', value = {'transformed_db_data' : transformed_db_data})
    
    @task.python
    def transform_s3_data(**kwargs):
        ti = kwargs['ti']
        extracted_s3_data = ti.xcom_pull(task_ids = 'extract_task', key = 'extracted_data')['s3_data']
        print(f"Transforming s3 data: {extracted_s3_data}")
        transformed_s3_data = [i * 10 for i in extracted_s3_data]
        ti.xcom_push(key = 'return_transformed_s3_data', value = {'transformed_s3_data' : transformed_s3_data})
    
    @task.bash
    def load_task(**kwargs):
        print("loading Data to the destination...")
        ti = kwargs['ti']
        api_data = ti.xcom_pull(task_ids = 'transform_api_data', key = 'return_transformed_api_data')
        db_data = ti.xcom_pull(task_ids = 'transform_db_data', key = 'return_transformed_db_data')
        s3_data = ti.xcom_pull(task_ids = 'transform_s3_data', key = 'return_transformed_s3_data')
        
        return f"echo 'Loaded Data: {api_data}, {db_data}, {s3_data}' "
        
    extract = extract_task()
    transform_api = transform_api_data()
    transform_db = transform_db_data()
    transform_s3 = transform_s3_data()
    load = load_task()
    
    extract >> [transform_api, transform_db, transform_s3] >> load


parallel_tasks()
