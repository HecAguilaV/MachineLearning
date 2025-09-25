# Demo rápida del análisis de datos - Ejecutable directamente
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("🎓 DEMO: ¿QUÉ HACE EL ANÁLISIS DE DATOS?")
print("=" * 50)

# Crear datos de ejemplo
np.random.seed(42)
n_programadores = 100

# Características de programadores
experiencia = np.random.normal(5, 2.5, n_programadores)
experiencia = np.clip(experiencia, 0, 15)
python = np.random.binomial(1, 0.6, n_programadores)
javascript = np.random.binomial(1, 0.7, n_programadores)

# Calcular salario basado en características
salario = (40000 + 
          experiencia * 3000 + 
          python * 8000 + 
          javascript * 6000 + 
          np.random.normal(0, 5000, n_programadores))

# Crear dataset
datos = pd.DataFrame({
    'experiencia_anos': np.round(experiencia, 1),
    'conoce_python': python,
    'conoce_javascript': javascript,
    'salario_usd': np.round(salario, 0).astype(int)
})

print("📊 DATOS CREADOS:")
print(f"   - {len(datos)} programadores simulados")
print(f"   - {len(datos.columns)} características por programador")
print("\n📋 Primeras 5 filas:")
print(datos.head())

print("\n📈 ESTADÍSTICAS BÁSICAS:")
print(f"   💰 Salario promedio: ${datos['salario_usd'].mean():,.0f}")
print(f"   📊 Salario mínimo: ${datos['salario_usd'].min():,.0f}")
print(f"   📈 Salario máximo: ${datos['salario_usd'].max():,.0f}")
print(f"   🐍 % que conoce Python: {datos['conoce_python'].mean():.1%}")
print(f"   💛 % que conoce JavaScript: {datos['conoce_javascript'].mean():.1%}")

print("\n🔍 ANÁLISIS DE CORRELACIONES:")
correlacion_exp_salario = datos['experiencia_anos'].corr(datos['salario_usd'])
print(f"   📈 Experiencia vs Salario: {correlacion_exp_salario:.3f}")

salario_python_si = datos[datos['conoce_python']==1]['salario_usd'].mean()
salario_python_no = datos[datos['conoce_python']==0]['salario_usd'].mean()
diferencia_python = salario_python_si - salario_python_no

print(f"   🐍 Salario con Python: ${salario_python_si:,.0f}")
print(f"   📝 Salario sin Python: ${salario_python_no:,.0f}")
print(f"   💡 Diferencia por saber Python: ${diferencia_python:,.0f}")

print("\n🤖 SIMULACIÓN DE MACHINE LEARNING:")
print("   (Prediciendo salario de un nuevo programador)")

# Ejemplo simple de predicción
nuevo_programador = {
    'experiencia': 7,
    'python': True, 
    'javascript': True
}

# Buscar programadores similares (KNN manual simple)
similar_mask = (
    (abs(datos['experiencia_anos'] - nuevo_programador['experiencia']) <= 2) &
    (datos['conoce_python'] == (1 if nuevo_programador['python'] else 0)) &
    (datos['conoce_javascript'] == (1 if nuevo_programador['javascript'] else 0))
)

programadores_similares = datos[similar_mask]

if len(programadores_similares) > 0:
    salario_predicho = programadores_similares['salario_usd'].mean()
    print(f"\n👤 NUEVO PROGRAMADOR:")
    print(f"   🎯 Experiencia: {nuevo_programador['experiencia']} años")
    print(f"   🐍 Python: {'Sí' if nuevo_programador['python'] else 'No'}")
    print(f"   💛 JavaScript: {'Sí' if nuevo_programador['javascript'] else 'No'}")
    print(f"\n🔮 PREDICCIÓN:")
    print(f"   💰 Salario estimado: ${salario_predicho:,.0f}")
    print(f"   👥 Basado en {len(programadores_similares)} programadores similares")
else:
    print("   ❌ No se encontraron programadores similares")

print(f"\n🎯 ¿QUÉ ACABAS DE VER?")
print("=" * 35)
print("✅ 1. CARGA DE DATOS - Creamos un dataset de programadores")
print("✅ 2. EXPLORACIÓN - Calculamos estadísticas básicas")
print("✅ 3. ANÁLISIS - Encontramos patrones (correlaciones)")
print("✅ 4. MACHINE LEARNING - Predijimos salario de alguien nuevo")
print("✅ 5. INTERPRETACIÓN - Entendimos qué afecta los salarios")

print(f"\n🚀 TU PROYECTO DE KEDRO HACE EXACTAMENTE ESTO:")
print("   📊 Pero con datos reales de Stack Overflow")
print("   🔧 De forma más organizada y profesional")
print("   ⚡ Automatizado para ejecutarse solo")
print("   📈 Con visualizaciones más sofisticadas")

print(f"\n💡 ¿PARA QUÉ SIRVE EN LA VIDA REAL?")
print("   🏢 Empresas: Decidir salarios, contratar talento")
print("   🎓 Estudiantes: Elegir qué tecnologías aprender")
print("   💼 Profesionales: Negociar mejores salarios")
print("   📊 Investigadores: Entender tendencias del mercado")