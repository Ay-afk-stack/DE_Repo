from dag_orchestrate_1 import orchestrate_first_dag
from dag_orchestrate_2 import orchestrate_second_dag
from airflow.sdk import dag, task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

@dag(
    dag_id = 'parent_dag'
)
def parent_dag():
    trigger_first_dag = TriggerDagRunOperator(
        task_id = 'trigger_first_orchestrator_dag',
        trigger_dag_id = 'orchestrate_first_dag',
        wait_for_completion = True
    )
    
    trigger_second_dag = TriggerDagRunOperator(
        task_id = 'trigger_second_orchestrator_dag',
        trigger_dag_id = 'orchestrate_second_dag',
        wait_for_completion = True
    )
    
    trigger_first_dag >> trigger_second_dag

parent_dag()