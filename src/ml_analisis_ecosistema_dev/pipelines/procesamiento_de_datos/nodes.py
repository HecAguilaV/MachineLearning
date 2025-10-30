"""
Nodos para el pipeline de procesamiento de datos, con un enfoque robusto y controlado por una "allowlist".
"""

import pandas as pd
import numpy as np
import logging
from sklearn.preprocessing import StandardScaler
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

def cargar_datos(
    so_2023: pd.DataFrame,
    jb_external: pd.DataFrame,
    jb_narrow: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Carga los datos crudos desde el catálogo."""
    return so_2023, jb_external, jb_narrow

def analizar_y_limpiar_nulos(
    so_2023: pd.DataFrame,
    jb_external: pd.DataFrame,
    jb_narrow: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Analiza y elimina columnas con un alto porcentaje de valores nulos."""
    logger.info("--- Análisis y Limpieza de Nulos por Columna ---")
    def _limpiar_df(df: pd.DataFrame, nombre: str) -> pd.DataFrame:
        nan_percentages = df.isnull().sum() / len(df)
        cols_to_drop = nan_percentages[nan_percentages > 0.5].index
        if len(cols_to_drop) > 0:
            logger.info(f"En '{nombre}', eliminando {len(cols_to_drop)} columnas con >50% de nulos.")
            df = df.drop(columns=cols_to_drop)
        return df

    so_2023_clean = _limpiar_df(so_2023, "Stack Overflow 2023")
    jb_external_clean = _limpiar_df(jb_external, "JetBrains External")
    jb_narrow_clean = _limpiar_df(jb_narrow, "JetBrains Narrow")
    return so_2023_clean, jb_external_clean, jb_narrow_clean

def eliminar_filas_sin_salario(df_so: pd.DataFrame, target_col: str) -> pd.DataFrame:
    """Elimina las filas del dataset de Stack Overflow donde el salario es nulo."""
    logger.info(f"--- Eliminando filas sin datos de '{target_col}' ---")
    df_cleaned = df_so.dropna(subset=[target_col])
    logger.info(f"Se eliminaron {len(df_so) - len(df_cleaned)} filas donde '{target_col}' era nulo.")
    return df_cleaned

def filtrar_outliers_salario(df_so: pd.DataFrame, target_col: str) -> pd.DataFrame:
    """Filtra outliers de la columna de salarios usando el método IQR."""
    logger.info(f"--- Filtrando outliers de '{target_col}' ---")
    Q1 = df_so[target_col].quantile(0.25)
    Q3 = df_so[target_col].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    df_filtered = df_so[(df_so[target_col] >= limite_inferior) & (df_so[target_col] <= limite_superior)]
    logger.info(f"Se eliminaron {len(df_so) - len(df_filtered)} filas consideradas outliers.")
    return df_filtered

def preprocesamiento_final_con_allowlist(df: pd.DataFrame, params: Dict[str, Any]) -> pd.DataFrame:
    """
    Realiza el preprocesamiento final basándose en una "allowlist" de columnas para evitar errores de memoria y tipo.
    """
    logger.info("--- Iniciando Preprocesamiento Final con Allowlist --- ")
    
    target_col = params["target_col"]
    if target_col not in df.columns:
        raise ValueError(f"La columna objetivo '{target_col}' no se encuentra.")

    y = df[target_col]
    features_df = df.drop(columns=[target_col])

    # 1. Definir la "Allowlist" de columnas categóricas que queremos procesar
    multi_answer_cols = params.get("multi_answer_cols", [])
    standard_categorical_cols = params.get("standard_categorical_cols", [])
    allowlist = set(multi_answer_cols + standard_categorical_cols)

    # 2. Identificar y eliminar todas las columnas de texto que NO están en la allowlist
    all_object_cols = features_df.select_dtypes(include=['object', 'category']).columns.tolist()
    cols_to_drop = [col for col in all_object_cols if col not in allowlist]
    if cols_to_drop:
        logger.warning(f"Eliminando {len(cols_to_drop)} columnas de texto no incluidas en la allowlist: {cols_to_drop}")
        features_df = features_df.drop(columns=cols_to_drop)

    # 3. Procesar columnas de respuesta múltiple de la allowlist
    for col in multi_answer_cols:
        if col in features_df.columns:
            dummies = features_df[col].fillna('').str.get_dummies(sep=';')
            dummies = dummies.add_prefix(f"{col}_")
            features_df = pd.concat([features_df.drop(columns=[col]), dummies], axis=1)

    # 4. Procesar columnas categóricas estándar de la allowlist
    cols_to_encode = [col for col in standard_categorical_cols if col in features_df.columns]
    if cols_to_encode:
        features_df = pd.get_dummies(features_df, columns=cols_to_encode, dummy_na=False)

    # 5. Escalar todas las características numéricas resultantes
    numeric_features = features_df.select_dtypes(include=np.number).columns.tolist()
    if numeric_features:
        scaler = StandardScaler()
        features_df[numeric_features] = scaler.fit_transform(features_df[numeric_features])
    
    final_df = pd.concat([features_df, y], axis=1)
    logger.info(f"--- Preprocesamiento Final Completado. Dimensiones: {final_df.shape} ---")
    
    return final_df