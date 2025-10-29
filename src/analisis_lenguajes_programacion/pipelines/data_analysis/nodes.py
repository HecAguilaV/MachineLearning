"""
Nodos de análisis de datos para el pipeline
"""

import pandas as pd
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


def load_and_inspect_survey(survey_data: pd.DataFrame) -> Dict[str, Any]:
    """
    Inspecciona el dataset y genera estadísticas básicas.
    
    Args:
        survey_data: DataFrame con los datos de la encuesta
        
    Returns:
        Diccionario con estadísticas del dataset
    """
    print("Inspeccionando datos...")
    print(f"Tamaño: {survey_data.shape[0]} filas, {survey_data.shape[1]} columnas")
    
    total_filas = len(survey_data)
    total_columnas = len(survey_data.columns)
    
    valores_nulos = survey_data.isnull().sum().sum()
    total_valores = total_filas * total_columnas
    porcentaje_nulos = (valores_nulos / total_valores) * 100
    
    resumen = {
        'total_filas': int(total_filas),
        'total_columnas': int(total_columnas), 
        'valores_nulos': int(valores_nulos),
        'porcentaje_nulos': round(float(porcentaje_nulos), 2),
        'mensaje': f"Dataset con {total_filas} registros y {total_columnas} columnas"
    }
    
    print(f"Resumen: {resumen['mensaje']}")
    print(f"Datos faltantes: {resumen['porcentaje_nulos']}%")
    
    return resumen


def analyze_programming_languages(survey_data: pd.DataFrame) -> pd.DataFrame:
    """
    Analiza columnas relacionadas con lenguajes de programación.
    
    Args:
        survey_data: DataFrame con los datos de la encuesta
        
    Returns:
        DataFrame con análisis de columnas de lenguajes
    """
    print("Analizando lenguajes de programación...")
    
    # Buscar columnas relacionadas con lenguajes
    columnas_lenguajes = []
    
    for col in survey_data.columns:
        col_lower = col.lower()
        if 'language' in col_lower or 'tech' in col_lower:
            columnas_lenguajes.append(col)
    
    print(f"Encontradas {len(columnas_lenguajes)} columnas de lenguajes")
    
    # Si no hay columnas específicas, usar las primeras 8
    if len(columnas_lenguajes) == 0:
        print("No se encontraron columnas específicas, usando primeras 8")
        columnas_lenguajes = list(survey_data.columns[:8])
    
    # Analizar cada columna
    resultados = []
    
    for col in columnas_lenguajes:
        respuestas_validas = survey_data[col].count()
        valores_unicos = survey_data[col].nunique()
        porcentaje = (respuestas_validas / len(survey_data)) * 100
        
        resultados.append({
            'columna': col,
            'respuestas_validas': respuestas_validas,
            'valores_unicos': valores_unicos,
            'porcentaje_respuestas': round(porcentaje, 1)
        })
    
    df_resultado = pd.DataFrame(resultados)
    
    print(f"Análisis completado: {len(df_resultado)} columnas procesadas")
    
    return df_resultado


def extract_salary_data(survey_data: pd.DataFrame) -> pd.DataFrame:
    """
    Extrae información sobre salarios del dataset.
    
    Args:
        survey_data: DataFrame con los datos de la encuesta
        
    Returns:
        DataFrame con datos de salarios
    """
    print("Extrayendo información de salarios...")
    
    # Buscar columnas relacionadas con salarios
    palabras_clave = ['salary', 'comp', 'income', 'pay', 'wage']
    columnas_salario = []
    
    for col in survey_data.columns:
        col_lower = col.lower()
        for palabra in palabras_clave:
            if palabra in col_lower:
                columnas_salario.append(col)
                break
    
    print(f"Encontradas {len(columnas_salario)} columnas de salarios")
    
    # Si no hay columnas de salario, crear análisis básico
    if len(columnas_salario) == 0:
        print("No se encontraron columnas de salario, creando análisis básico")
        
        datos_basicos = pd.DataFrame({
            'analisis': ['total_respuestas', 'columnas_disponibles', 'valores_unicos'],
            'valor': [
                len(survey_data),
                len(survey_data.columns),
                survey_data.iloc[:, 0].nunique() if len(survey_data.columns) > 0 else 0
            ]
        })
        
        return datos_basicos
    
    # Extraer columnas de salario
    columnas_extraer = columnas_salario.copy()
    
    # Agregar país si existe
    if 'Country' in survey_data.columns:
        columnas_extraer.append('Country')
        print("Incluyendo columna de país")
    
    datos_salario = survey_data[columnas_extraer].copy()
    
    print(f"Extracción completada: {len(datos_salario)} filas, {len(columnas_extraer)} columnas")
    
    return datos_salario
