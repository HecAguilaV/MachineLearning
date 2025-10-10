## Análisis de Lenguajes de Programación

Proyecto Kedro para analizar la popularidad de lenguajes y su relación con salarios usando la Stack Overflow Developer Survey 2023. Enfoque simple, reproducible y honesto.

### Lo esencial
- Dataset: Stack Overflow Developer Survey 2023 (CSV ~158 MB). Se trabaja con una muestra de ~1.000 filas para desarrollo.
- Alcance: CRISP-DM (fases 1–3). Sin modelado ni despliegue.
- Outputs clave:
  - data/02_intermediate/survey_basic_stats.json (estadísticas básicas)
  - data/02_intermediate/languages_analysis.parquet (popularidad de lenguajes)
  - data/02_intermediate/salary_data.parquet (columnas salariales + país si existe)
- Dónde ver el código:
  - Pipeline: `src/analisis_lenguajes_programacion/pipelines/data_analysis/pipeline.py`
  - Nodos: `src/analisis_lenguajes_programacion/pipelines/data_analysis/nodes.py`
  - Notebook: `notebooks/01_exploratory_analysis.ipynb`

## Pipeline (nodos)
- load_and_inspect_survey(df): inspección y métricas básicas → survey_basic_stats.json
- analyze_programming_languages(df): conteos/porcentajes por columnas de lenguajes → languages_analysis.parquet
- extract_salary_data(df): columnas salariales y país (si aplica) → salary_data.parquet

## Cómo ejecutarlo
```bash
# Ejecutar todo
kedro run

# Ejecutar un nodo
kedro run --nodes="load_and_inspect_survey"

# Visual del pipeline (luego abrir http://localhost:4141)
kedro viz --no-browser --host=0.0.0.0 --port=4141

# Notebooks con contexto
kedro jupyter notebook
```

## Por qué un solo dataset
- Basta para responder popularidad y salarios sin complejidad extra.
- Más fácil de revisar y reproducir; menos puntos de fallo.
- Menor consumo de memoria/tiempo: práctico para un primer entregable.

## Limitaciones
- Muestra de ~1.000 registros; no se procesa el CSV completo en memoria.
- Visualizaciones y EDA básicos; CRISP-DM fases 4–6 fuera de alcance.

## Proyecto
- Autor: Héctor Aguila — Duoc UC, Machine Learning (4º semestre)
- Repositorio: https://github.com/HecAguilaV/MachineLearning.git
- Última actualización: 10 de octubre de 2025
## Análisis de Lenguajes de Programación

Proyecto Kedro para analizar la popularidad de lenguajes y su relación con salarios usando la Stack Overflow Developer Survey 2023. El enfoque es intencionalmente simple y reproducible.

### Lo esencial
- Dataset: Stack Overflow Developer Survey 2023 (CSV ~158 MB). Se trabaja con una muestra de ~1.000 filas para desarrollo.
- Alcance: Fases 1–3 de CRISP-DM (Business Understanding, Data Understanding, Data Preparation). Sin modelado ni despliegue.
- Entradas/Salidas clave:
  - data/02_intermediate/survey_basic_stats.json (estadísticas básicas)
  - data/02_intermediate/languages_analysis.parquet (popularidad de lenguajes)
  - data/02_intermediate/salary_data.parquet (columnas salariales + país si existe)
- Dónde revisar el código:
  - Pipeline: `src/analisis_lenguajes_programacion/pipelines/data_analysis/pipeline.py`
  - Nodos: `src/analisis_lenguajes_programacion/pipelines/data_analysis/nodes.py`
  - Notebook: `notebooks/01_exploratory_analysis.ipynb`

## Pipeline
Nodos implementados (archivo `nodes.py`):
- load_and_inspect_survey(df): inspección y métricas básicas → survey_basic_stats.json
- analyze_programming_languages(df): columnas de lenguajes, conteos/porcentajes → languages_analysis.parquet
- extract_salary_data(df): columnas salariales y país (si aplica) → salary_data.parquet

## Cómo ejecutarlo
```bash
# Ejecutar todo el pipeline
kedro run

# Ejecutar un nodo específico
kedro run --nodes="load_and_inspect_survey"

# Visual del pipeline (abrir luego http://localhost:4141)
kedro viz --no-browser --host=0.0.0.0 --port=4141

# Notebooks con contexto Kedro
kedro jupyter notebook
```

## Por qué un solo dataset
- Suficiente para responder popularidad y salarios sin agregar complejidad innecesaria.
- Menos puntos de fallo; más fácil de revisar y reproducir.
- Ahorro de memoria/tiempo, adecuado para un primer entregable honesto.

## Limitaciones
- Muestra de 1.000 registros para desarrollo; no se usa el dataset completo en memoria.
- Visualizaciones y análisis exploratorio básicos; sin fases 4–6 de CRISP-DM.

## Proyecto
- Autor: Héctor Aguila — Duoc UC, Machine Learning (4º semestre)
- Repositorio: https://github.com/HecAguilaV/MachineLearning.git
- Última actualización: 10 de octubre de 2025

## Análisis de Lenguajes de Programación

Proyecto de análisis con Kedro que estudia popularidad de lenguajes y relación con salarios usando la encuesta Stack Overflow Developer Survey 2023. Se prioriza simplicidad y reproducibilidad: un solo dataset, tres nodos claros y comandos mínimos.

### Por qué un solo dataset
- Suficiente para responder preguntas del problema (lenguajes y salarios están en la misma fuente).
- Reduce complejidad y errores; facilita reproducibilidad y corrección.
- Consume menos memoria/tiempo y es más adecuado para un primer entregable.

### Metodología (CRISP-DM, fases 1-3)
1) Business Understanding: objetivos y métricas claras. 2) Data Understanding: exploración y validación básica. 3) Data Preparation: limpieza y estandarización necesarias para análisis.

## Pipeline
Nodos implementados en `src/analisis_lenguajes_programacion/pipelines/data_analysis/nodes.py`:
- load_and_inspect_survey(df) → `data/02_intermediate/survey_basic_stats.json`
- analyze_programming_languages(df) → `data/02_intermediate/languages_analysis.parquet`
- extract_salary_data(df) → `data/02_intermediate/salary_data.parquet`

## Uso rápido
- Ejecutar todo: kedro run
- Ejecutar por nodo: kedro run --nodes="load_and_inspect_survey" (o el nombre del nodo)
- Notebooks con contexto: kedro jupyter notebook
- Visual del pipeline: kedro viz --no-browser --host=0.0.0.0 --port=4141

## Dataset
- Stack Overflow Developer Survey 2023 (CSV ~158 MB). Para desarrollo se usó una muestra de 1,000 filas.
- Contiene ~85 columnas con información sobre tecnologías, salarios y demografía.

## Outputs
- data/02_intermediate/survey_basic_stats.json: estadísticas básicas del dataset.
- data/02_intermediate/languages_analysis.parquet: popularidad de lenguajes.
- data/02_intermediate/salary_data.parquet: columnas salariales y país (si existe).

## Limitaciones
- Muestra de 1,000 registros para desarrollo; no incluye modelado ni despliegue (fases 4-6 CRISP-DM).
- Visualizaciones mínimas en notebooks; se puede profundizar.

## Proyecto
- Autor: Héctor Aguila — Duoc UC, Machine Learning (4to semestre)
- Repositorio: https://github.com/HecAguilaV/MachineLearning.git
- Última actualización: 9 de octubre de 2025



### Ejecución del Pipeline2. **Instalar dependencias principales**:

```bash

```bashpip install kedro==1.0.0 pandas numpy matplotlib seaborn pyarrow

# Pipeline completo```

kedro run

3. **Verificar instalación**:

# Nodos específicos```bash

kedro run --nodes="inspect_survey_data"kedro --version

kedro run --nodes="analyze_programming_languages"python -c "import kedro; print(f'Kedro {kedro.__version__} instalado correctamente')"

kedro run --nodes="extract_salary_data"```



# Pipeline específico## Cómo Ejecutar el Proyecto

kedro run --pipeline="data_analysis"

```### Pipeline Completo

```bash

### Visualización# Activar entorno virtual

source kedro-env/bin/activate

```bash

# Abrir Kedro Viz# Navegar al directorio del proyecto

kedro viz --no-browser --host=0.0.0.0 --port=4141cd analisis-lenguajes-programacion

```

# Ejecutar pipeline completo

## Estructura del Proyectokedro run

```

```

analisis-lenguajes-programacion/### Ejecución de Nodos Específicos

├── conf/                    # Configuración```bash

│   ├── base/# Solo inspección de datos

│   │   ├── catalog.yml     # Catálogo de datoskedro run --nodes="inspect_survey_data"

│   │   └── parameters.yml  # Parámetros

│   └── local/              # Config local (git-ignored)# Solo análisis de lenguajes

├── data/                   # Datos organizados por etapakedro run --nodes="analyze_programming_languages"

│   ├── 01_raw/            # Datos sin procesar

│   ├── 02_intermediate/   # Datos en procesamiento# Solo análisis salarial  

│   └── ...                # Etapas adicionaleskedro run --nodes="extract_salary_data"

├── deliverable/           # Entregable del proyecto

├── notebooks/             # Jupyter notebooks# Pipeline de análisis completo

├── src/                   # Código fuentekedro run --pipeline="data_analysis"

│   └── analisis_lenguajes_programacion/```

│       └── pipelines/

│           └── data_analysis/### Visualización del Pipeline

└── tests/                 # Tests unitarios```bash

```# Abrir interfaz web de Kedro Viz

kedro viz --no-browser --host=0.0.0.0 --port=4141

## Outputs del Análisis```



### survey_basic_stats.json## Estructura del Proyecto

Estadísticas descriptivas del dataset:

- Dimensiones y tipos de datos```

- Valores faltantesanalisis-lenguajes-programacion/

- Distribuciones básicas├── 📁 conf/                          # Archivos de configuración

│   ├── base/

### languages_analysis.parquet│   │   ├── catalog.yml              # Configuración del catálogo de datos

Análisis de lenguajes:│   │   ├── logging.yml              # Configuración de logging

- Popularidad relativa│   │   └── parameters.yml           # Parámetros del proyecto

- Distribución por experiencia│   └── local/                       # Configuraciones locales (git-ignored)

- Tendencias de adopción├── 📁 data/                         # Datos del proyecto (organizados por kedro)

│   ├── 01_raw/                     # 📥 Datos crudos (Stack Overflow CSV)

### salary_data.parquet│   ├── 02_intermediate/            # 🔄 Datos en procesamiento

Datos de compensación:│   ├── 03_primary/                 # ✅ Datos limpios y validados

- Rangos salariales por tecnología│   ├── 04_feature/                 # 🎯 Features engineered (outputs actuales)

- Correlaciones lenguaje-remuneración│   ├── 05_model_input/             # 📊 Input preparado para modelos

- Análisis de factores determinantes│   ├── 06_models/                  # 🤖 Modelos entrenados

│   ├── 07_model_output/            # 📈 Predicciones y resultados

## Stack Tecnológico│   └── 08_reporting/               # 📋 Datos para reportes y dashboards

├── 📁 notebooks/                    # 📓 Jupyter notebooks para análisis interactivo

- **Kedro 1.0.0**: Framework de pipeline├── 📁 src/analisis_lenguajes_programacion/

- **Pandas**: Procesamiento de datos│   ├── pipelines/

- **NumPy**: Operaciones numéricas│   │   └── data_analysis/          # 🔧 Pipeline principal de análisis

- **Matplotlib/Seaborn**: Visualización│   │       ├── __init__.py

- **PyArrow**: Almacenamiento eficiente│   │       ├── nodes.py            # Funciones de procesamiento

│   │       └── pipeline.py         # Definición del pipeline

## Trabajo con Notebooks│   └── settings.py                  # Configuraciones del proyecto

├── 📁 tests/                       # 🧪 Tests unitarios

```bash├── requirements.txt                 # 📦 Dependencias de Python

# Iniciar Jupyter con contexto Kedro└── README.md                       # 📖 Este archivo

kedro jupyter notebook```



# Acceso a catálogo y pipelines## Resultados y Outputs

# Variables disponibles: catalog, context, pipelines, session

```### Estadísticas Generales del Dataset

- **Total de registros procesados**: 1,000 (muestra de desarrollo)

## Información del Proyecto- **Columnas analizadas**: 85 variables completas

- **Lenguajes identificados**: 8 columnas específicas de tecnologías

- **Autor**: Héctor Aguila- **Variables salariales**: 2 columnas de compensación

- **Institución**: Duoc UC - Puerto Montt

- **Curso**: Machine Learning - 4to Semestre### Archivos de Salida

- **Fecha**: Septiembre 2025

- **Propósito**: Evaluación académica#### 📊 `survey_basic_stats.json`

Estadísticas descriptivas básicas del dataset:

## Contacto- Número de registros y columnas

- Tipos de datos identificados

- **Repositorio**: https://github.com/HecAguilaV/MachineLearning.git- Porcentaje de valores faltantes

- Resumen de variables numéricas y categóricas

---

#### 📈 `languages_analysis.parquet`

**Última actualización**: 9 de octubre de 2025Análisis detallado de lenguajes de programación:

- Popularidad relativa de cada lenguaje
- Distribución de uso por experiencia
- Trends de adopción identificados

#### 💰 `salary_data.parquet`
Datos de compensación procesados:
- Rangos salariales por tecnología
- Correlaciones entre lenguajes y remuneración
- Análisis de factores determinantes de salario

## Tecnologías y Herramientas

### Herramientas que usamos
- **🐍 Python 3.13.7**: El lenguaje en el que programamos todo
- **🔧 Kedro 1.0.0**: La herramienta que organiza nuestro proyecto
- **🐼 Pandas**: Para trabajar con tablas de datos (como Excel, pero en código)
- **🔢 NumPy**: Para hacer cálculos matemáticos
- **📊 Matplotlib/Seaborn**: Para crear gráficas bonitas
- **🏹 PyArrow**: Para guardar archivos de datos de manera eficiente

### Metodologías que seguimos
- **📋 CRISP-DM**: La receta paso a paso para proyectos de datos
- **🎯 Organización Kedro**: Una forma estándar de ordenar archivos y carpetas
- **🔄 Investigación Reproducible**: Que cualquiera pueda repetir nuestro trabajo

## Trabajo con Notebooks

### Configuración de Jupyter
```bash
# Instalar Jupyter (si no está instalado)
pip install jupyter jupyterlab

# Iniciar notebook server con contexto Kedro
kedro jupyter notebook

# Alternativamente, JupyterLab
kedro jupyter lab
```

### Variables Disponibles en Notebooks
Al usar `kedro jupyter`, tienes acceso automático a:
- `catalog`: Catálogo de datos del proyecto
- `context`: Contexto del proyecto Kedro
- `pipelines`: Todos los pipelines definidos
- `session`: Sesión activa de Kedro

### Ejemplo de Uso en Notebook
```python
# Cargar datos directamente desde el catálogo
survey_data = catalog.load("stack_overflow_survey")
basic_stats = catalog.load("survey_basic_stats")

# Ejecutar nodos específicos
session.run(node_names=["inspect_survey_data"])
```

## Próximos Desarrollos

### Fase Inmediata (Corto Plazo)
- [ ] **Notebooks CRISP-DM**: Crear notebooks detallados para cada fase
- [ ] **EDA Completo**: Análisis exploratorio exhaustivo con visualizaciones
- [ ] **Data Cleaning Pipeline**: Pipeline dedicado a limpieza de datos
- [ ] **Feature Engineering**: Creación de variables derivadas

### Fase de Expansión (Mediano Plazo)
- [ ] **Modelado Predictivo**: Modelos de ML para predicción salarial
- [ ] **Dashboard Interactivo**: Visualizaciones dinámicas con Plotly/Streamlit
- [ ] **API de Consulta**: Endpoint REST para consultar resultados
- [ ] **Automatización CI/CD**: Pipeline de integración continua

### Fase de Optimización (Largo Plazo)
- [ ] **Escalabilidad**: Procesamiento de dataset completo (>90k registros)
- [ ] **MLOps**: Implementación de prácticas MLOps avanzadas
- [ ] **Monitoreo**: Sistema de monitoring y alertas
- [ ] **Versionado de Datos**: Data versioning con DVC

## Guía de Contribución

### Estándares de Código
- **PEP 8**: Seguir convenciones de estilo de Python
- **Docstrings**: Documentar todas las funciones y clases
- **Type Hints**: Usar anotaciones de tipo cuando sea posible
- **Testing**: Escribir tests para nuevas funcionalidades

### Estructura de Commits
```
tipo(alcance): descripción breve

- feat: nueva funcionalidad
- fix: corrección de bugs
- docs: cambios en documentación
- style: cambios de formato (no afectan funcionalidad)
- refactor: factorización de código
- test: agregar o modificar tests
```

## Licencia y Uso

Este proyecto está desarrollado como parte de una **evaluación académica de Machine Learning**. 

- **Propósito**: Educativo y de investigación
- **Autor**: Héctor Aguila
- **Institución**: Duoc UC - Perto Montt - 4to Semestre
- **Curso**: Machine Learning
- **Fecha**: Septiembre 2025

## Contacto y Soporte

Para preguntas, sugerencias o reportes de problemas:

- **Autor**: Héctor Aguila
- **Repositorio**: (https://github.com/HecAguilaV/MachineLearning.git)
- **Documentación**: Ver archivos en `/docs` (si existen)

---
