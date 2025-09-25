# Prueba simple de nuestras funciones para principiantes

import pandas as pd
import sys
import os

# Agregar el path del proyecto para poder importar nuestras funciones
sys.path.append('/Users/hector/Desktop/4 SEMESTRE/MachineLearning/analisis-lenguajes-programacion/src')

# Importar nuestras funciones
from analisis_lenguajes_programacion.pipelines.data_analysis.nodes import (
    load_and_inspect_survey,
    analyze_programming_languages, 
    extract_salary_data
)

def main():
    print("="*60)
    print("🎓 PRUEBA DE FUNCIONES PARA PRINCIPIANTES")
    print("="*60)
    
    # Crear datos de ejemplo para probar
    print("\n📋 Creando datos de ejemplo...")
    
    # Simular datos de encuesta
    datos_ejemplo = pd.DataFrame({
        'LanguageHaveWorkedWith': ['Python;JavaScript', 'Java;C++', 'Python;R'],
        'LanguageWantToWorkWith': ['Python;Go', 'JavaScript;Python', 'Python;Scala'],
        'CompTotal': [75000, 85000, 95000],
        'CompFreq': ['Yearly', 'Yearly', 'Monthly'],
        'Country': ['United States', 'Germany', 'Canada'],
        'YearsCodePro': [5, 8, 3],
        'Employment': ['Employed full-time', 'Employed full-time', 'Student'],
        'Age': [28, 35, 24]
    })
    
    print(f"✅ Creé {len(datos_ejemplo)} filas de ejemplo con {len(datos_ejemplo.columns)} columnas")
    
    # Probar función 1: Inspección básica
    print("\n" + "="*50)
    print("🔍 PASO 1: INSPECCIÓN BÁSICA DE DATOS")
    print("="*50)
    
    try:
        resultado1 = load_and_inspect_survey(datos_ejemplo)
        print(f"\n📊 Resultado de la inspección:")
        for clave, valor in resultado1.items():
            print(f"   {clave}: {valor}")
    except Exception as e:
        print(f"❌ Error en paso 1: {e}")
    
    # Probar función 2: Análisis de lenguajes
    print("\n" + "="*50)
    print("💻 PASO 2: ANÁLISIS DE LENGUAJES")
    print("="*50)
    
    try:
        resultado2 = analyze_programming_languages(datos_ejemplo)
        print(f"\n📈 Resultado del análisis de lenguajes:")
        print(resultado2.to_string(index=False))
    except Exception as e:
        print(f"❌ Error en paso 2: {e}")
    
    # Probar función 3: Análisis de salarios
    print("\n" + "="*50)
    print("💰 PASO 3: ANÁLISIS DE SALARIOS")
    print("="*50)
    
    try:
        resultado3 = extract_salary_data(datos_ejemplo)
        print(f"\n💵 Resultado del análisis de salarios:")
        print(resultado3.to_string(index=False))
    except Exception as e:
        print(f"❌ Error en paso 3: {e}")
    
    print("\n" + "="*60)
    print("🎉 ¡PRUEBA COMPLETADA!")
    print("="*60)
    print("✅ Todas las funciones están diseñadas para principiantes")
    print("✅ Los mensajes explican qué hace cada paso")
    print("✅ El código es fácil de entender y seguir")

if __name__ == "__main__":
    main()