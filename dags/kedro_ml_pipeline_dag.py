from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime
import os

# Define la ruta base de tu proyecto Kedro
# Asegúrate de que esta ruta sea la correcta en tu entorno
KEDRO_PROJECT_PATH = "/opt/airflow/kedro_project"

with DAG(
    dag_id="kedro_ml_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule=None,  # Ejecución manual o programada externamente
    catchup=False,
    tags=["kedro", "mlops"],
    description="DAG para orquestar los pipelines de Kedro ML_Analisis_Ecosistema_Dev",
) as dag:
    # Tarea para ejecutar el pipeline de procesamiento de datos
    run_processing = BashOperator(
        task_id="run_processing_pipeline",
        bash_command=f"cd {KEDRO_PROJECT_PATH} && kedro run --pipeline=procesamiento_de_datos",
        dag=dag,
    )

    # Tarea para ejecutar el pipeline de regresión
    run_regression = BashOperator(
        task_id="run_regression_pipeline",
        bash_command=f"cd {KEDRO_PROJECT_PATH} && kedro run --pipeline=regresion",
        dag=dag,
    )

    # Tarea para ejecutar el pipeline de clasificación
    run_classification = BashOperator(
        task_id="run_classification_pipeline",
        bash_command=f"cd {KEDRO_PROJECT_PATH} && kedro run --pipeline=clasificacion",
        dag=dag,
    )

    # Definir las dependencias de las tareas:
    # El procesamiento debe terminar antes de que los modelos de regresión y clasificación puedan ejecutarse.
    run_processing >> [run_regression, run_classification]
