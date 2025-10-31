
"""
Pipeline para el entrenamiento y evaluación de modelos de clasificación.
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    create_target_variable,
    split_data,
    train_classifier_with_grid_search,
    report_and_select_best_classifier,
)

def create_pipeline(**kwargs) -> Pipeline:
    
    classification_params = "params:classification_pipeline"
    
    model_names = [
        "LogisticRegression",
        # "SVC", # Eliminado permanentemente por alto costo computacional
        "RandomForestClassifier",
        "XGBClassifier",
        "LGBMClassifier",
    ]

    create_target_node = node(
        func=create_target_variable,
        inputs=["datos_para_modelado", classification_params],
        outputs="data_with_target",
        name="create_target_variable_node",
    )

    split_data_node = node(
        func=split_data,
        inputs=["data_with_target", classification_params],
        outputs=dict(
            X_train="X_train_clf",
            X_test="X_test_clf",
            y_train="y_train_clf",
            y_test="y_test_clf",
        ),
        name="split_data_clf_node",
    )

    training_nodes = []
    for model_name in model_names:
        training_nodes.append(
            node(
                func=train_classifier_with_grid_search,
                inputs=[
                    "X_train_clf",
                    "y_train_clf",
                    f"params:classification_pipeline.models.{model_name}.model_name",
                    classification_params,
                ],
                outputs=f"{model_name}_classifier",
                name=f"train_{model_name}_classifier_node",
            )
        )

    # Se crea un diccionario plano de inputs para el nodo final
    report_inputs = {f"{name}_classifier": f"{name}_classifier" for name in model_names}
    report_inputs["X_test"] = "X_test_clf"
    report_inputs["y_test"] = "y_test_clf"

    report_and_select_node = node(
        func=report_and_select_best_classifier,
        inputs=report_inputs,
        outputs={
            "best_classification_model": "best_classification_model",
            "classification_metrics_report": "classification_metrics_report",
            "classification_confusion_matrices": "classification_confusion_matrices",
        },
        name="report_and_select_best_classifier_node",
    )

    return pipeline(
        [
            create_target_node,
            split_data_node,
            *training_nodes,
            report_and_select_node,
        ]
    )
