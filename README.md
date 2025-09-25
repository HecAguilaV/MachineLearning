# Análisis de Lenguajes de Programación

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## ¿Qué hace este proyecto?

Este proyecto analiza **qué lenguajes de programación son más populares y cuáles pagan mejor**. Es como hacer una investigación de mercado, pero con datos reales de más de 90,000 programadores que respondieron una encuesta en Stack Overflow (una página web muy famosa entre desarrolladores).

Usamos dos herramientas principales:
- **CRISP-DM**: Una metodología (como una receta paso a paso) para hacer proyectos de análisis de datos
- **Kedro**: Un programa que nos ayuda a organizar nuestro código y datos de forma ordenada

### ¿Qué queremos lograr?

- **Objetivo Principal**: Descubrir cuáles son los lenguajes de programación más usados hoy en día
- **Objetivos Específicos**:
  - Ver qué lenguajes están más de moda
  - Descubrir qué lenguajes te pueden ayudar a ganar más dinero
  - Crear información útil para decidir qué tecnologías aprender
  - Hacer todo esto de manera organizada y que otros puedan repetir el proceso

## Metodología CRISP-DM (La receta que seguimos)

CRISP-DM es como una receta de cocina, pero para proyectos de datos. Tiene 6 pasos, pero nosotros hicimos los primeros 3:

### 1. 🎯 Entender el Problema
- **¿Qué queremos saber?**: ¿Qué lenguajes de programación son más populares y pagan mejor?
- **¿Para qué nos sirve?**: Para ayudar a estudiantes y programadores a decidir qué aprender
- **¿Cómo sabemos si lo hicimos bien?**: Si encontramos patrones claros y útiles

### 2. 📊 Conocer los Datos
- **¿De dónde vienen los datos?**: Encuesta de Stack Overflow 2023
- **¿Cuántos datos tenemos?**: Más de 90,000 respuestas (usamos 1,000 para practicar)
- **¿Qué información importante hay?**: Lenguajes que usa cada persona, cuánto gana, cuánta experiencia tiene

### 3. 🔧 Preparar los Datos
- Limpiar información que falta o está mal escrita
- Organizar todo en el mismo formato
- Crear nuevas variables que nos ayuden a entender mejor
- Separar los datos en grupos más fáciles de analizar

## Dataset Principal

### Stack Overflow Developer Survey 2023
- **Formato**: CSV (~158 MB)
- **Registros**: Muestra de 1,000 respuestas para desarrollo
- **Características principales**:
  - 85 columnas con información completa del desarrollador
  - 8 columnas específicas de lenguajes de programación
  - 2 columnas relacionadas con información salarial
  - Datos demográficos y de experiencia profesional

## ¿Cómo funciona nuestro proyecto? (Los 3 pasos principales)

Nuestro proyecto hace el trabajo en **3 pasos automáticos**:

### 🔍 Paso 1: `inspect_survey_data` (Revisar los datos)
- **¿Qué hace?**: Abre el archivo de datos y mira qué contiene
- **¿Para qué sirve?**: Para saber con qué estamos trabajando (cuántas personas, qué preguntas, etc.)
- **¿Qué produce?**: Un archivo con estadísticas básicas (`survey_basic_stats.json`)

### 📈 Paso 2: `analyze_programming_languages` (Analizar lenguajes)
- **¿Qué hace?**: Cuenta cuáles lenguajes son más populares
- **¿Para qué sirve?**: Para ver qué tecnologías está usando más gente
- **¿Qué produce?**: Un archivo con el análisis de lenguajes (`languages_analysis.parquet`)

### 💰 Paso 3: `extract_salary_data` (Analizar salarios)
- **¿Qué hace?**: Busca información sobre cuánto ganan los programadores
- **¿Para qué sirve?**: Para ver qué lenguajes dan mejores salarios
- **¿Qué produce?**: Un archivo con datos de salarios (`salary_data.parquet`)

## Instalación y Configuración

### Requisitos del Sistema
- **Python**: 3.8 o superior
- **Sistema operativo**: macOS, Linux, Windows
- **Memoria RAM**: Mínimo 4GB (recomendado 8GB)

### Configuración del Entorno

1. **Crear entorno virtual**:
```bash
python -m venv kedro-env
source kedro-env/bin/activate  # macOS/Linux
# kedro-env\Scripts\activate  # Windows
```

2. **Instalar dependencias principales**:
```bash
pip install kedro==1.0.0 pandas numpy matplotlib seaborn pyarrow
```

3. **Verificar instalación**:
```bash
kedro --version
python -c "import kedro; print(f'Kedro {kedro.__version__} instalado correctamente')"
```

## Cómo Ejecutar el Proyecto

### Pipeline Completo
```bash
# Activar entorno virtual
source kedro-env/bin/activate

# Navegar al directorio del proyecto
cd analisis-lenguajes-programacion

# Ejecutar pipeline completo
kedro run
```

### Ejecución de Nodos Específicos
```bash
# Solo inspección de datos
kedro run --nodes="inspect_survey_data"

# Solo análisis de lenguajes
kedro run --nodes="analyze_programming_languages"

# Solo análisis salarial  
kedro run --nodes="extract_salary_data"

# Pipeline de análisis completo
kedro run --pipeline="data_analysis"
```

### Visualización del Pipeline
```bash
# Abrir interfaz web de Kedro Viz
kedro viz --no-browser --host=0.0.0.0 --port=4141
```

## Estructura del Proyecto

```
analisis-lenguajes-programacion/
├── 📁 conf/                          # Archivos de configuración
│   ├── base/
│   │   ├── catalog.yml              # Configuración del catálogo de datos
│   │   ├── logging.yml              # Configuración de logging
│   │   └── parameters.yml           # Parámetros del proyecto
│   └── local/                       # Configuraciones locales (git-ignored)
├── 📁 data/                         # Datos del proyecto (organizados por kedro)
│   ├── 01_raw/                     # 📥 Datos crudos (Stack Overflow CSV)
│   ├── 02_intermediate/            # 🔄 Datos en procesamiento
│   ├── 03_primary/                 # ✅ Datos limpios y validados
│   ├── 04_feature/                 # 🎯 Features engineered (outputs actuales)
│   ├── 05_model_input/             # 📊 Input preparado para modelos
│   ├── 06_models/                  # 🤖 Modelos entrenados
│   ├── 07_model_output/            # 📈 Predicciones y resultados
│   └── 08_reporting/               # 📋 Datos para reportes y dashboards
├── 📁 notebooks/                    # 📓 Jupyter notebooks para análisis interactivo
├── 📁 src/analisis_lenguajes_programacion/
│   ├── pipelines/
│   │   └── data_analysis/          # 🔧 Pipeline principal de análisis
│   │       ├── __init__.py
│   │       ├── nodes.py            # Funciones de procesamiento
│   │       └── pipeline.py         # Definición del pipeline
│   └── settings.py                  # Configuraciones del proyecto
├── 📁 tests/                       # 🧪 Tests unitarios
├── requirements.txt                 # 📦 Dependencias de Python
└── README.md                       # 📖 Este archivo
```

## Resultados y Outputs

### Estadísticas Generales del Dataset
- **Total de registros procesados**: 1,000 (muestra de desarrollo)
- **Columnas analizadas**: 85 variables completas
- **Lenguajes identificados**: 8 columnas específicas de tecnologías
- **Variables salariales**: 2 columnas de compensación

### Archivos de Salida

#### 📊 `survey_basic_stats.json`
Estadísticas descriptivas básicas del dataset:
- Número de registros y columnas
- Tipos de datos identificados
- Porcentaje de valores faltantes
- Resumen de variables numéricas y categóricas

#### 📈 `languages_analysis.parquet`
Análisis detallado de lenguajes de programación:
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
- refactor: refactorización de código
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

## 📚 Glosario (Diccionario de Términos)

*Si encuentras una palabra que no entiendes, búscala aquí:*

### Términos de Programación
- **Pipeline**: Es como una cadena de montaje en una fábrica. Los datos entran por un lado, pasan por varios procesos, y salen transformados por el otro lado
- **Dataset**: Un conjunto de datos, como una hoja de Excel gigante con mucha información
- **CSV**: Un tipo de archivo que guarda datos en filas y columnas, como Excel pero más simple
- **Parquet**: Otro tipo de archivo para guardar datos, pero más eficiente que CSV
- **JSON**: Un formato para guardar información de manera organizada, fácil de leer por computadoras

### Términos de Kedro
- **Nodo**: Una función que hace una tarea específica (como limpiar datos o hacer cálculos)
- **Catálogo**: Una lista de todos los archivos de datos que usa el proyecto
- **Pipeline**: La secuencia completa de pasos que sigue el proyecto
- **Kedro Viz**: Una herramienta que muestra gráficamente cómo está conectado todo el proyecto

### Términos de Análisis de Datos
- **CRISP-DM**: Una metodología (receta) estándar para hacer proyectos de análisis de datos
- **EDA (Análisis Exploratorio)**: El proceso de explorar los datos para entender qué contienen
- **Feature Engineering**: Crear nuevas variables a partir de las que ya tenemos
- **Insights**: Descubrimientos o conclusiones interesantes que sacamos de los datos

### Términos Técnicos
- **Entorno Virtual**: Un espacio aislado donde instalamos las herramientas del proyecto, sin afectar el resto de la computadora
- **Framework**: Un conjunto de herramientas pre-hechas que nos facilita el trabajo
- **API**: Una forma de que diferentes programas se comuniquen entre sí
- **Git**: Una herramienta para llevar control de cambios en el código

### Términos de Machine Learning
- **Correlación**: Cuando dos cosas están relacionadas (por ejemplo: más experiencia = mejor salario)
- **Modelado Predictivo**: Usar datos del pasado para predecir qué pasará en el futuro
- **Variables**: Las características que medimos (edad, salario, lenguajes que conoce, etc.)
- **MLOps**: Prácticas para mantener modelos de machine learning funcionando en producción

### Términos de la Industria
- **Stack Overflow**: La página web más famosa donde programadores hacen preguntas y comparten conocimiento
- **Open Source**: Software gratuito que cualquiera puede usar y modificar
- **CI/CD**: Prácticas para automatizar el proceso de desarrollo y despliegue de software

---

## Estado del Proyecto

🟢 **Activo** - En desarrollo y mejora continua

**Última actualización**: 24 de septiembre de 2025

**Próximo paso**: Completar notebooks con análisis básico y visualizaciones

---

## 💡 Consejos para Estudiantes

### Si eres nuevo en esto:
1. **No te preocupes si no entiendes todo** - Esto es normal al comenzar
2. **Ejecuta el código paso a paso** - No trates de hacer todo de una vez
3. **Lee los mensajes de error** - Aunque parezcan confusos, te dan pistas
4. **Busca en Google** - Los programadores hacemos esto TODO el tiempo
5. **Pide ayuda** - La comunidad de programadores suele ser muy útil

### Para tu evaluación:
- **Documenta todo lo que hagas** - Explica por qué hiciste cada cosa
- **Haz capturas de pantalla** - Los profesores aman las evidencias visuales
- **Explica con tus propias palabras** - Demuestra que entendiste, no solo copiaste
- **Menciona las dificultades** - Es normal tener problemas, compártelos

---

*Este README es un documento que se actualiza conforme aprendemos y mejoramos el proyecto.*
