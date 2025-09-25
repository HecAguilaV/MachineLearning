Evaluación Parcial 1 - Machine Learning
Proyecto con Framework Kedro
 
Información General
Sigla	Nombre Asignatura	Tiempo Asignado	% Ponderación
MLY0100	Machine Learning	4 semanas	40% de la asignatura
Tipo de Evaluación	Modalidad	Entorno de Trabajo
✅ Entrega de proyecto	Parejas	Laboratorio / Remoto
 
📋 Descripción de la Evaluación
Esta evaluación parcial se compone de dos partes:
Parte 1: Prueba Teórica Individual (30%)
•	Evaluación de conocimientos técnicos y teóricos
•	Modalidad individual
•	Ponderación: 30% de la nota parcial 1
Parte 2: Proyecto Práctico con Kedro (70%)
•	Desarrollo de proyecto de Machine Learning usando el framework Kedro
•	Implementación de las primeras 3 fases de la metodología CRISP-DM
•	Trabajo con mínimo 3 datasets diferentes
•	Modalidad en parejas
•	Ponderación: 70% de la nota parcial 1
 
🎯 Objetivos de Aprendizaje
Al completar esta evaluación, los estudiantes serán capaces de:
1.	Implementar un proyecto profesional de Machine Learning usando el framework Kedro
2.	Aplicar la metodología CRISP-DM en un contexto real
3.	Desarrollar pipelines modulares y reutilizables para procesamiento de datos
4.	Gestionar múltiples fuentes de datos usando el catálogo de Kedro
5.	Documentar procesos técnicos siguiendo estándares de la industria
6.	Crear código reproducible y mantenible siguiendo mejores prácticas
 
📚 Metodología CRISP-DM - Fases a Desarrollar
Fase 1: Comprensión del Negocio
•	Definir objetivos del proyecto
•	Evaluar la situación actual
•	Determinar objetivos de Machine Learning
•	Producir plan del proyecto
Fase 2: Comprensión de los Datos
•	Recolectar datos iniciales (mínimo 3 datasets)
•	Describir los datos
•	Explorar los datos (EDA)
•	Verificar calidad de los datos
Fase 3: Preparación de los Datos
•	Seleccionar los datos relevantes
•	Limpiar los datos (missing values, outliers)
•	Construir nuevas variables (feature engineering)
•	Integrar datos de múltiples fuentes
•	Formatear y transformar datos
 
🛠️ Requisitos Técnicos
Framework y Herramientas
•	Framework principal: Kedro (versión 0.18.x o superior)
•	Lenguaje: Python 3.8+
•	IDE recomendado: VS Code o PyCharm
•	Control de versiones: Git
Librerías Requeridas
# Data manipulation
pandas>=1.3.0
numpy>=1.21.0

# Visualization
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0

# Machine Learning
scikit-learn>=1.0.0

# Kedro ecosystem
kedro>=0.18.0
kedro-viz>=6.0.0
kedro-datasets>=1.0.0

# Utilities
jupyter>=1.0.0
ipykernel>=6.0.0
Estructura del Proyecto Kedro
proyecto-ml-parejas/
├── conf/
│   ├── base/
│   │   ├── catalog.yml        # Configuración de datasets
│   │   ├── parameters.yml     # Parámetros del proyecto
│   │   └── logging.yml
│   └── local/
│       └── credentials.yml    # Credenciales (no subir a Git)
├── data/
│   ├── 01_raw/                # Datos originales (mínimo 3 archivos)
│   ├── 02_intermediate/       # Datos procesados parcialmente
│   ├── 03_primary/            # Datos limpios
│   ├── 04_feature/           # Features para modelado
│   └── 05_model_input/       # Datos listos para entrenar
├── docs/
│   └── source/                # Documentación del proyecto
├── notebooks/
│   ├── 01_business_understanding.ipynb
│   ├── 02_data_understanding.ipynb
│   └── 03_data_preparation.ipynb
├── src/
│   └── proyecto_ml/
│       ├── pipelines/
│       │   ├── data_engineering/
│       │   │   ├── nodes.py
│       │   │   └── pipeline.py
│       │   ├── data_science/
│       │   │   ├── nodes.py
│       │   │   └── pipeline.py
│       │   └── reporting/
│       │       ├── nodes.py
│       │       └── pipeline.py
│       └── pipeline_registry.py
├── README.md
├── requirements.txt
└── .gitignore
 
📊 Rúbrica de Evaluación Detallada
Escala de Evaluación
Nivel de Desempeño	% Logro	Nota	Descripción
Muy buen desempeño	100%	7.0	Logro completo de todos los aspectos
Buen desempeño	80%	5.6	Alto desempeño con mínimas omisiones
Desempeño aceptable	60%	4.2	Logro de elementos básicos
Desempeño incipiente	40%	2.8	Importantes omisiones o errores
Desempeño insuficiente	20%	1.4	Desempeño incorrecto
No logrado	0%	1.0	No cumple requisitos mínimos
Criterios de Evaluación (10 indicadores)
1. Estructura y Configuración del Proyecto Kedro (10%)
•	100%: Proyecto Kedro perfectamente estructurado, configuración completa en conf/, README detallado, estructura modular clara
•	80%: Proyecto bien estructurado, configuración funcional, documentación adecuada
•	60%: Estructura básica funcional, configuración mínima operativa
•	40%: Errores en estructura, configuración incompleta
•	20%: No usa Kedro o estructura incorrecta
2. Implementación del Catálogo de Datos (10%)
•	100%: 3+ datasets correctamente configurados, múltiples formatos (CSV, Excel, Parquet), parametrización, versionado
•	80%: 3 datasets bien configurados, formatos apropiados
•	60%: 3 datasets básicos funcionales
•	40%: Menos de 3 datasets o errores significativos
•	20%: Sin catálogo o mal configurado
3. Desarrollo de Nodos y Funciones (10%)
•	100%: Nodos altamente modulares, funciones puras, docstrings completos, manejo de errores, principios SOLID
•	80%: Nodos bien estructurados, buena documentación
•	60%: Nodos funcionales con modularidad básica
•	40%: Baja modularidad, funciones acopladas
•	20%: Sin nodos o mal estructurados
4. Construcción de Pipelines (10%)
•	100%: Pipelines organizados por fase CRISP-DM, uso de namespaces, dependencias claras, componibles
•	80%: Pipelines funcionales bien conectados
•	60%: Pipelines básicos operativos
•	40%: Problemas en dependencias o estructura
•	20%: Sin pipelines o incorrectos
5. Análisis Exploratorio de Datos - EDA (10%)
•	100%: EDA exhaustivo (univariado, bivariado, multivariado), visualizaciones interactivas, análisis de patrones en 3+ datasets
•	80%: EDA completo con buenos análisis y visualizaciones
•	60%: EDA básico con estadísticos descriptivos
•	40%: EDA superficial o incompleto
•	20%: Sin EDA o extremadamente básico
6. Limpieza y Tratamiento de Datos (10%)
•	100%: Estrategias diferenciadas por tipo de variable, manejo sofisticado de outliers/missing values, validación de integridad
•	80%: Buen tratamiento con estrategias justificadas
•	60%: Limpieza básica implementada
•	40%: Limpieza superficial o con errores
•	20%: Sin limpieza o mal implementada
7. Transformación y Feature Engineering (10%)
•	100%: Transformaciones avanzadas justificadas, feature engineering creativo, PCA si aplica, pipelines parametrizables
•	80%: Buenas transformaciones (scaling, encoding), features derivadas
•	60%: Transformaciones básicas (normalización/estandarización)
•	40%: Transformaciones limitadas o mal aplicadas
•	20%: Sin transformaciones necesarias
8. Identificación de Targets para ML (10%)
•	100%: Múltiples targets correctos para regresión y clasificación, justificación sólida basada en negocio, análisis de viabilidad
•	80%: Targets principales correctos con buena justificación
•	60%: Targets básicos correctos
•	40%: Identificación confusa o parcialmente incorrecta
•	20%: Sin identificación o completamente mal definidos
9. Documentación y Notebooks (10%)
•	100%: Documentación excepcional, notebooks estructurados por CRISP-DM, markdown detallado, docstrings, README completo
•	80%: Buena documentación, notebooks claros, código comentado
•	60%: Documentación básica, notebooks funcionales
•	40%: Documentación escasa o confusa
•	20%: Sin documentación
10. Reproducibilidad y Mejores Prácticas (10%)
•	100%: Completamente reproducible, requirements.txt, parameters.yml, logging, tests, PEP8, .env para credenciales
•	80%: Reproducible con buenas prácticas implementadas
•	60%: Básicamente reproducible, algunas buenas prácticas
•	40%: Problemas de reproducibilidad
•	20%: No reproducible
 
📦 Entregables Requeridos
Entregables Obligatorios
1.	✅ Repositorio Git con el proyecto Kedro completo
2.	✅ Mínimo 3 datasets diferentes en data/01_raw/
3.	✅ Catálogo de datos configurado (conf/base/catalog.yml)
4.	✅ Pipelines implementados para las 3 fases CRISP-DM
5.	✅ 3 Notebooks de análisis (uno por fase)
6.	✅ README.md con instrucciones de instalación y ejecución
7.	✅ requirements.txt actualizado
8.	✅ Documentación en código (docstrings)
Entregables Opcionales (Puntos Extra)
•	🌟 Visualización interactiva con kedro viz
•	🌟 Tests unitarios básicos
•	🌟 CI/CD con GitHub Actions
•	🌟 Containerización con Docker
•	🌟 Dashboard interactivo con Streamlit/Dash
 
🚀 Guía de Inicio Rápido
Paso 1: Instalación de Kedro
# Crear ambiente virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar Kedro
pip install kedro kedro-viz

# Verificar instalación
kedro info
Paso 2: Crear Proyecto
# Crear nuevo proyecto Kedro
kedro new

# Responder las preguntas:
# Project Name: Proyecto ML [Nombres]
# Repo Name: proyecto-ml-parejas
# Python Package: proyecto_ml
Paso 3: Configurar Datasets
# conf/base/catalog.yml
raw_data:
  type: pandas.CSVDataSet
  filepath: data/01_raw/dataset_principal.csv
  
reference_data:
  type: pandas.ExcelDataSet
  filepath: data/01_raw/datos_referencia.xlsx
  
supplementary_data:
  type: pandas.ParquetDataSet
  filepath: data/01_raw/datos_complementarios.parquet
Paso 4: Crear Primer Pipeline
# src/proyecto_ml/pipelines/data_engineering/nodes.py
def load_and_validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Valida y retorna el dataset cargado.
    
    Args:
        df: DataFrame raw
    
    Returns:
        DataFrame validado
    """
    assert not df.empty, "Dataset vacío"
    logger.info(f"Dataset cargado: {df.shape}")
    return df
Paso 5: Ejecutar Pipeline
# Ejecutar todos los pipelines
kedro run

# Ejecutar pipeline específico
kedro run --pipeline=data_engineering

# Visualizar pipeline
kedro viz
 
📚 Recursos de Apoyo
Documentación Oficial
•	Kedro Documentation
•	Kedro Tutorial - Spaceflights
•	CRISP-DM Guide
Videos Tutoriales Recomendados
•	Getting Started with Kedro
•	Building ML Pipelines with Kedro
Plantillas y Ejemplos
•	Kedro Starter Templates
•	Ejemplo de Proyecto ML con Kedro
Cheat Sheets
# Comandos Kedro más usados
kedro new                    # Crear proyecto
kedro run                    # Ejecutar pipelines
kedro run --pipeline=<name>  # Ejecutar pipeline específico
kedro viz                    # Visualizar DAG
kedro jupyter notebook       # Abrir Jupyter con Kedro
kedro catalog list          # Listar datasets
kedro pipeline create <name> # Crear nuevo pipeline
kedro test                   # Ejecutar tests
 
⚠️ Consideraciones Importantes
Manejo de Datos Sensibles
•	NUNCA subir datos reales a GitHub
•	Usar .gitignore para excluir carpeta data/
•	Credenciales en conf/local/ (nunca en conf/base/)
•	Considerar datos sintéticos para el repositorio público
Control de Versiones
# .gitignore recomendado
data/
conf/local/
*.log
.ipynb_checkpoints/
__pycache__/
*.pyc
.pytest_cache/
docs/build/
Trabajo en Equipo
•	Usar branches para desarrollo paralelo
•	Pull requests para revisar código
•	Commits descriptivos y frecuentes
•	Documentar decisiones importantes en README
 
📅 Cronograma Sugerido
Semana	Actividades	Entregables
Semana 1	- Formar parejas<br>- Instalar Kedro<br>- Configurar proyecto<br>- Cargar datasets	Proyecto iniciado, datasets cargados
Semana 2	- Comprensión del negocio<br>- EDA inicial<br>- Primeros pipelines	Notebook fase 1, pipeline básico
Semana 3	- Comprensión profunda datos<br>- Limpieza de datos<br>- Feature engineering	Notebook fase 2, pipeline limpieza
Semana 4	- Preparación final datos<br>- Documentación<br>- Testing y validación	Proyecto completo, documentación
 
✅ Checklist de Entrega
Antes de entregar, verificar:
•	[ ] Proyecto Kedro ejecuta sin errores con kedro run
•	[ ] Mínimo 3 datasets diferentes configurados
•	[ ] Pipelines para las 3 fases CRISP-DM
•	[ ] Notebooks documentados (1 por fase)
•	[ ] README con instrucciones claras
•	[ ] requirements.txt actualizado
•	[ ] Código con docstrings
•	[ ] Repositorio Git con commits descriptivos
•	[ ] .gitignore configurado correctamente
•	[ ] Sin datos sensibles en el repositorio
 
🎯 Criterios de Éxito
Un proyecto exitoso deberá:
1.	Demostrar dominio del framework Kedro
2.	Aplicar correctamente la metodología CRISP-DM
3.	Procesar eficientemente múltiples fuentes de datos
4.	Documentar claramente todas las decisiones
5.	Ser completamente reproducible por terceros
6.	Seguir mejores prácticas de ingeniería de software
 
¡Éxito en su proyecto! 🚀
Recuerden: La calidad del código y la documentación son tan importantes como los resultados del análisis.
 
Fecha de entrega: 24-09-2025
Formato de entrega: Link al repositorio GitHub/GitLab
Modalidad: Digital a través del AVA 
