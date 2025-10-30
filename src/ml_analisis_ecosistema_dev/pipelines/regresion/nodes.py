
"""
Nodos para el pipeline de regresión.
"""
import logging
import pandas as pd
from typing import Dict, Any, List
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

logger = logging.getLogger(__name__)

def split_data(data: pd.DataFrame, params: Dict[str, Any]) -> Dict[str, Any]:
    """Divide los datos en conjuntos de entrenamiento y prueba, asegurando que solo
    se usen columnas numéricas para las características.

    Args:
        data: DataFrame de entrada.
        params: Diccionario de parámetros con test_size y random_state.

    Returns:
        Un diccionario con X_train, X_test, y_train, y_test.
    """
    X = data.drop(columns=[params["target_col"]])
    y = data[params["target_col"]]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=params["test_size"], random_state=params["random_state"]
    )
    
    logger.info(f"División de datos completada. Tamaño de X_train: {X_train.shape}")
    return dict(
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
    )

def _get_model_instance(model_name: str, params: Dict[str, Any]):
    """Retorna una instancia del modelo basado en el nombre."""
    model_map = {
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(),
        "Lasso": Lasso(),
        "RandomForestRegressor": RandomForestRegressor(random_state=params.get("random_state")),
        "XGBRegressor": XGBRegressor(random_state=params.get("random_state")),
    }
    if model_name not in model_map:
        raise ValueError(f"Modelo '{model_name}' no soportado.")
    return model_map[model_name]

def train_model_with_grid_search(
    X_train: pd.DataFrame, 
    y_train: pd.Series, 
    model_name: str, 
    params: Dict[str, Any]
) -> Any:
    """
    Entrena un modelo de regresión usando GridSearchCV para encontrar los mejores hiperparámetros.

    Args:
        X_train: DataFrame de características de entrenamiento.
        y_train: Serie del target de entrenamiento.
        model_name: Nombre del modelo a entrenar.
        params: Diccionario de parámetros que incluye la grilla para GridSearchCV.

    Returns:
        El mejor estimador encontrado por GridSearchCV.
    """
    model = _get_model_instance(model_name, params)
    param_grid = params["models"][model_name]["param_grid"]
    
    cv = KFold(n_splits=params.get("cv_folds", 5), shuffle=True, random_state=params.get("random_state"))
    
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=cv,
        scoring=params.get("scoring", "neg_root_mean_squared_error"),
        n_jobs=-1,
        verbose=1,
        error_score='raise' # Añadido para depuración
    )
    
    logger.info(f"Iniciando GridSearchCV para el modelo {model_name}...")
    grid_search.fit(X_train, y_train)
    
    logger.info(f"Mejores parámetros para {model_name}: {grid_search.best_params_}")
    
    return grid_search.best_estimator_

def report_and_select_best_model(
    X_test: pd.DataFrame,
    y_test: pd.Series,
    **models
) -> Dict[str, Any]:
    """
    Evalúa múltiples modelos, genera un informe de métricas, selecciona el mejor
    y lo guarda.

    Args:
        models: Un diccionario con los modelos entrenados.
        X_test: DataFrame de características de prueba.
        y_test: Serie del target de prueba.

    Returns:
        Un diccionario con el mejor modelo y las métricas de todos los modelos.
    """
    metrics_report = {}
    best_model = None
    best_r2 = -np.inf

    logger.info("--- Informe de Evaluación de Modelos de Regresión ---")
    
    for model_name, model in models.items():
        y_pred = model.predict(X_test)
        
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        metrics_report[model_name] = {"rmse": rmse, "mae": mae, "r2": r2}
        
        logger.info(f"Modelo: {model_name}")
        logger.info(f"  - R^2: {r2:.4f}")
        logger.info(f"  - RMSE: {rmse:.4f}")
        logger.info(f"  - MAE: {mae:.4f}")
        
        if r2 > best_r2:
            best_r2 = r2
            best_model = model
            
    logger.info("--- Fin del Informe ---")
    logger.info(f"Mejor modelo seleccionado: {type(best_model).__name__} (R^2: {best_r2:.4f})")

    return {
        "best_regression_model": best_model,
        "regression_metrics_report": metrics_report
    }
