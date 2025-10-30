
"""
Nodos para el pipeline de clasificación.
"""
import logging
import pandas as pd
from typing import Dict, Any
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import (
    accuracy_score, f1_score, precision_score, recall_score, roc_auc_score, confusion_matrix
)
from imblearn.pipeline import Pipeline as ImbPipeline
from imblearn.over_sampling import SMOTE

logger = logging.getLogger(__name__)

def create_target_variable(data: pd.DataFrame, params: Dict[str, Any]) -> pd.DataFrame:
    """Crea la variable objetivo binaria basada en un umbral de salario."""
    data_copy = data.copy()
    data_copy[params["target_col"]] = (data_copy[params["original_target_col"]] > params["salary_threshold"]).astype(int)
    data_copy = data_copy.drop(columns=[params["original_target_col"]])
    logger.info(f"Variable objetivo '{params['target_col']}' creada. Distribución:\n{data_copy[params['target_col']].value_counts(normalize=True)}")
    return data_copy

def split_data(data: pd.DataFrame, params: Dict[str, Any]) -> Dict[str, Any]:
    """Divide los datos en conjuntos de entrenamiento y prueba."""
    X = data.drop(columns=[params["target_col"]])
    y = data[params["target_col"]]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=params["test_size"], random_state=params["random_state"], stratify=y
    )
    return dict(X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)

def _get_model_instance(model_name: str, params: Dict[str, Any]):
    """Retorna una instancia del modelo de clasificación."""
    model_map = {
        "LogisticRegression": LogisticRegression(random_state=params.get("random_state"), max_iter=1000),
        "SVC": SVC(random_state=params.get("random_state"), probability=True),
        "RandomForestClassifier": RandomForestClassifier(random_state=params.get("random_state")),
        "XGBClassifier": XGBClassifier(random_state=params.get("random_state"), use_label_encoder=False, eval_metric='logloss'),
        "LGBMClassifier": LGBMClassifier(random_state=params.get("random_state")),
    }
    if model_name not in model_map:
        raise ValueError(f"Modelo '{model_name}' no soportado.")
    return model_map[model_name]

def train_classifier_with_grid_search(X_train: pd.DataFrame, y_train: pd.Series, model_name: str, params: Dict[str, Any]) -> Any:
    """Entrena un clasificador usando un pipeline con SMOTE y GridSearchCV."""
    model = _get_model_instance(model_name, params)
    param_grid = {f'model__{k}': v for k, v in params["models"][model_name]["param_grid"].items()}

    pipeline = ImbPipeline([
        ('smote', SMOTE(random_state=params.get("random_state"))),
        ('model', model)
    ])

    cv = StratifiedKFold(n_splits=params.get("cv_folds", 5), shuffle=True, random_state=params.get("random_state"))

    grid_search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        cv=cv,
        scoring=params.get("scoring", "f1"),
        n_jobs=-1,
        verbose=1
    )
    
    logger.info(f"Iniciando GridSearchCV para el clasificador {model_name}...")
    grid_search.fit(X_train, y_train)
    
    logger.info(f"Mejores parámetros para {model_name}: {grid_search.best_params_}")
    return grid_search.best_estimator_

def report_and_select_best_classifier(X_test: pd.DataFrame, y_test: pd.Series, **models) -> Dict[str, Any]:
    """Evalúa, reporta y selecciona el mejor modelo de clasificación."""
    metrics_report = {}
    best_model = None
    best_f1 = -1
    confusion_matrices = {}

    logger.info("--- Informe de Evaluación de Modelos de Clasificación ---")

    for model_name, model in models.items():
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]
        
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "f1_score": f1_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "roc_auc": roc_auc_score(y_test, y_proba),
        }
        metrics_report[model_name] = metrics
        cm = confusion_matrix(y_test, y_pred)
        confusion_matrices[model_name] = cm

        logger.info(f"Modelo: {model_name}")
        for metric, value in metrics.items():
            logger.info(f"  - {metric.replace('_', ' ').title()}: {value:.4f}")
        
        # Visualización de la Matriz de Confusión
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title(f'Matriz de Confusión - {model_name}')
        plt.ylabel('Etiqueta Real')
        plt.xlabel('Etiqueta Predicha')
        # Guardar la figura en un diccionario para que Kedro la pueda versionar
        # Esta es una forma de manejar artefactos visuales
        # La clave será el nombre del artefacto en el catalog.yml
        confusion_matrices[f"{model_name}_confusion_matrix_plot"] = plt

        if metrics["f1_score"] > best_f1:
            best_f1 = metrics["f1_score"]
            best_model = model

    logger.info("--- Fin del Informe ---")
    logger.info(f"Mejor modelo seleccionado: {type(best_model.named_steps['model']).__name__} (F1-Score: {best_f1:.4f})")

    return {
        "best_classification_model": best_model,
        "classification_metrics_report": metrics_report,
        "classification_confusion_matrices": confusion_matrices
    }
