from airflow.sdk import dag, task

@dag(
    dag_id = "xcom_manual_dag",
)
def xcom_manual_dag():
    
    @task.python
    def first_task(**kwargs):
        
        # Extracting 'ti' -> task instance variable from kwargs to push XCOMs manually 
        ti = kwargs['ti']
        print("Extracting data... This is the first task")
        fetched_data = {"data" : [1, 2, 3, 4, 5]}
        ti.xcom_push(key = 'return_result', value = fetched_data)
        
    @task.python
    def second_task(**kwargs):

        # Accessing the ti variable
        ti = kwargs['ti']
        print("Transforming data... This is the second task")
        transformed_data = ti.xcom_pull(task_ids = 'first_task', key = 'return_result')['data'] * 2
        transformed_data_dict = {"trans_data" : transformed_data}
        ti.xcom_push(key = 'return_result', value = transformed_data_dict)

    @task.python
    def third_task(**kwargs):
        ti = kwargs['ti']
        load_data = ti.xcom_pull(task_ids = 'second_task', key = 'return_result')['trans_data']
        return load_data
        
    # instantiation of task dependencies
    first = first_task()
    second = second_task()
    third = third_task()

    # assigning orders of task
    first >> second >> third

# instantiating the dag
xcom_manual_dag()