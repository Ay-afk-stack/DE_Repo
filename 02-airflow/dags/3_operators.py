from airflow.sdk import dag, task

@dag(
    dag_id = "bash_dag"
)
def bash_dag():
    @task.python
    def first_task():
        print("This is the first task")
        
    @task.python
    def second_task():
        print("This is the second task")
        
    @task.python
    def third_task():
        print("This is the third task")
    
    @task.bash
    def bash_task():
        return "echo https://airflow.apache.org"
        
    first = first_task()
    second = second_task()
    third = third_task()
    bash_task = bash_task() 
    
    first >> second >> third >> bash_task

bash_dag()