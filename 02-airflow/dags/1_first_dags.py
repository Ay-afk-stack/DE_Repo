from airflow.sdk import dag, task

@dag(
    dag_id = "first_dag",
)
def first_dag():
    
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

# instantiating the dag
first_dag()