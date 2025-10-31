
"""
Pipeline para el entrenamiento y evaluación de modelos de regresión.
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    split_data,
    train_model_with_grid_search,
    report_and_select_best_model,
)

def create_pipeline(**kwargs) -> Pipeline:
    
    # Parámetros para todo el pipeline de regresión
    regression_params = "params:regression_pipeline"

    # Nombres de los modelos a entrenar
    model_names = [
        "LinearRegression",
        "Ridge",
        "Lasso",
        "RandomForestRegressor",
        "XGBRegressor",
    ]

    # 1. Nodo para dividir los datos
    split_data_node = node(
        func=split_data,
        inputs=["datos_para_modelado", regression_params],
        outputs=dict(
            X_train="X_train",
            X_test="X_test",
            y_train="y_train",
            y_test="y_test",
        ),
        name="split_data_node",
    )

    # 2. Nodos de entrenamiento para cada modelo
    training_nodes = []
    for model_name in model_names:
        training_nodes.append(
            node(
                func=train_model_with_grid_search,
                inputs=[
                    "X_train",
                    "y_train",
                    f"params:regression_pipeline.models.{model_name}.model_name", # Pasamos el nombre del modelo
                    regression_params,
                ],
                outputs=f"{model_name}_model", # Salida única para el modelo entrenado
                name=f"train_{model_name}_node",
            )
        )

    # 3. Nodo para evaluar, reportar y seleccionar el mejor modelo
    # Se crea un diccionario plano de inputs para el nodo final
    report_inputs = {f"{name}_model": f"{name}_model" for name in model_names}
    report_inputs["X_test"] = "X_test"
    report_inputs["y_test"] = "y_test"

    report_and_select_node = node(
        func=report_and_select_best_model,
        inputs=report_inputs,
        outputs={
            "best_regression_model": "regresion_model", # Coincide con catalog.yml
            "regression_metrics_report": "metrics", # Coincide con catalog.yml
        },
        name="report_and_select_best_model_node",
    )

    return pipeline(
        [
            split_data_node,
            *training_nodes,
            report_and_select_node,
        ]
    )

