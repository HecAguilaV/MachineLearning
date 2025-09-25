"""
Análisis Básico de Datos de Stack Overflow
Proyecto para principiantes - Análisis de Lenguajes de Programación
"""

import pandas as pd
import logging
from typing import Dict, Any

# Configuramos el logger para ver qué está pasando
logger = logging.getLogger(__name__)


def load_and_inspect_survey(survey_data: pd.DataFrame) -> Dict[str, Any]:
    """
    PASO 1: Revisar qué datos tenemos
    Esta función es como abrir una caja y contar qué hay adentro
    
    ¿Qué hace?
    - Cuenta cuántas filas (personas) y columnas (preguntas) tenemos
    - Ve cuántos datos faltan
    - Calcula cuánto espacio ocupa en la computadora
    
    Args:
        survey_data: Los datos de la encuesta (como una tabla de Excel gigante)
        
    Returns:
        Un diccionario con información básica sobre nuestros datos
    """
    print("📊 Revisando nuestros datos...")
    print(f"   Tamaño: {survey_data.shape[0]} personas, {survey_data.shape[1]} preguntas")
    
    # Contamos cuántas personas respondieron
    total_personas = len(survey_data)
    
    # Contamos cuántas preguntas hay
    total_preguntas = len(survey_data.columns)
    
    # Calculamos cuántos espacios están vacíos
    espacios_vacios = survey_data.isnull().sum().sum()
    total_espacios = total_personas * total_preguntas
    porcentaje_vacios = (espacios_vacios / total_espacios) * 100
    
    # Organizamos toda esta información
    resumen = {
        'total_personas': int(total_personas),
        'total_preguntas': int(total_preguntas), 
        'espacios_vacios': int(espacios_vacios),
        'porcentaje_vacios': round(float(porcentaje_vacios), 2),
        'mensaje': f"Tenemos datos de {total_personas} programadores con {total_preguntas} preguntas cada uno"
    }
    
    print(f"✅ Resumen: {resumen['mensaje']}")
    print(f"   Datos faltantes: {resumen['porcentaje_vacios']}%")
    
    return resumen


def analyze_programming_languages(survey_data: pd.DataFrame) -> pd.DataFrame:
    """
    PASO 2: Buscar información sobre lenguajes de programación
    Esta función es como un detective que busca pistas sobre qué lenguajes usa la gente
    
    ¿Qué hace?
    - Busca columnas que hablen de lenguajes (Python, Java, etc.)
    - Cuenta cuántas personas respondieron cada pregunta
    - Ve cuántos lenguajes diferentes mencionaron
    
    Args:
        survey_data: Los datos de la encuesta
        
    Returns:
        Una tabla con el análisis de lenguajes de programación
    """
    print("🔍 Buscando información sobre lenguajes de programación...")
    
    # Buscar columnas que hablen de lenguajes o tecnologías
    # Es como buscar palabras clave en un diccionario
    columnas_lenguajes = []
    
    for nombre_columna in survey_data.columns:
        nombre_minuscula = nombre_columna.lower()
        if 'language' in nombre_minuscula or 'tech' in nombre_minuscula:
            columnas_lenguajes.append(nombre_columna)
    
    print(f"   Encontré {len(columnas_lenguajes)} columnas sobre lenguajes:")
    for i, col in enumerate(columnas_lenguajes, 1):
        print(f"   {i}. {col}")
    
    # Si no encontramos nada, usemos las primeras 8 columnas como ejemplo
    if len(columnas_lenguajes) == 0:
        print("   No encontré columnas específicas, usando las primeras 8 como ejemplo")
        columnas_lenguajes = list(survey_data.columns[:8])
    
    # Crear un análisis simple de cada columna
    resultados = []
    
    for columna in columnas_lenguajes:
        # Contar cuántas respuestas válidas hay
        respuestas_validas = survey_data[columna].count()
        
        # Contar cuántos valores únicos hay
        valores_unicos = survey_data[columna].nunique()
        
        # Calcular el porcentaje de respuestas
        porcentaje_respuestas = (respuestas_validas / len(survey_data)) * 100
        
        resultados.append({
            'columna': columna,
            'respuestas_validas': respuestas_validas,
            'valores_unicos': valores_unicos,
            'porcentaje_respuestas': round(porcentaje_respuestas, 1)
        })
    
    # Convertir a DataFrame (tabla ordenada)
    tabla_analisis = pd.DataFrame(resultados)
    
    print("✅ Análisis completado!")
    print(f"   Analicé {len(tabla_analisis)} columnas de lenguajes")
    
    return tabla_analisis


def extract_salary_data(survey_data: pd.DataFrame) -> pd.DataFrame:
    """
    PASO 3: Buscar información sobre salarios
    Esta función es como buscar información sobre cuánto ganan los programadores
    
    ¿Qué hace?
    - Busca columnas que hablen de salarios o dinero
    - Extrae esa información para analizarla después
    - También incluye el país (si lo encuentra) porque los salarios cambian por país
    
    Args:
        survey_data: Los datos de la encuesta
        
    Returns:
        Una tabla con solo la información de salarios
    """
    print("💰 Buscando información sobre salarios...")
    
    # Buscar columnas que hablen de salarios, dinero, compensación
    # Palabras clave que podrían indicar salario
    palabras_salario = ['salary', 'comp', 'income', 'pay', 'wage']
    columnas_salario = []
    
    for nombre_columna in survey_data.columns:
        nombre_minuscula = nombre_columna.lower()
        for palabra in palabras_salario:
            if palabra in nombre_minuscula:
                columnas_salario.append(nombre_columna)
                break  # No agregar la misma columna dos veces
    
    print(f"   Encontré {len(columnas_salario)} columnas sobre salarios:")
    for i, col in enumerate(columnas_salario, 1):
        print(f"   {i}. {col}")
    
    # Si no encontramos columnas de salario, crear un análisis básico
    if len(columnas_salario) == 0:
        print("   No encontré columnas específicas de salario")
        print("   Creando análisis básico con información general...")
        
        # Crear un DataFrame simple con información básica
        datos_basicos = pd.DataFrame({
            'analisis': ['total_respuestas', 'columnas_disponibles', 'paises_mencionados'],
            'valor': [
                len(survey_data),
                len(survey_data.columns),
                survey_data.get('Country', survey_data.iloc[:, 0]).nunique() if len(survey_data.columns) > 0 else 0
            ]
        })
        
        return datos_basicos
    
    # Si encontramos columnas de salario, extraerlas
    columnas_a_extraer = columnas_salario.copy()
    
    # Agregar país si existe
    if 'Country' in survey_data.columns:
        columnas_a_extraer.append('Country')
        print("   ✅ También incluiré información del país")
    
    # Extraer solo las columnas que nos interesan
    datos_salario = survey_data[columnas_a_extraer].copy()
    
    # Contar cuántos datos válidos tenemos
    datos_validos = datos_salario.count().sum()
    
    print("✅ Extracción completada!")
    print(f"   Extraje {len(datos_salario)} filas con {len(columnas_a_extraer)} columnas")
    print(f"   Total de datos válidos: {datos_validos}")
    
    return datos_salario
