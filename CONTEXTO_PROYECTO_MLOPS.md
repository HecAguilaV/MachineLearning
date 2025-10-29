# Contexto del Proyecto MLOps para Asistente de IA Local (VS Code)

**Proyecto:** ML-Análisis-Ecosistema-Dev
**Fecha:** 29 de octubre de 2025
**Objetivo:** Servir como documento de contexto para un asistente de IA que opera localmente en el entorno de desarrollo. Este archivo contiene la visión, el estado actual, los próximos pasos y los requisitos clave del proyecto.

---

## 1. Misión del Proyecto

**Objetivo Principal:** Construir un pipeline MLOps completo, reproducible y automatizado que ingiera, procese, modele y evalúe datos de encuestas a desarrolladores (Stack Overflow 2023, JetBrains 2025) para cumplir con los requisitos de una asignatura de Machine Learning.

**Stack Tecnológico Clave:**
- **Pipeline:** Kedro (~1.0.0)
- **Contenerización:** Docker (20.10+) / Docker Compose (2.0+)
- **Orquestación:** Apache Airflow (~2.8.0)
- **Versionado de Datos/Modelos:** DVC
- **Lenguaje:** Python (3.11)
- **Idioma del Proyecto:** Español para la lógica de negocio (variables, comentarios); Inglés para términos técnicos universales.

---

## 2. Estado Actual del Proyecto: "Configuración Completa"

Hemos finalizado la Fase 0 (Limpieza y Configuración). El repositorio está ordenado y listo para el desarrollo de pipelines.

**Lo que SÍ se ha hecho:**
- ✅ **Limpieza del Repositorio:** Se eliminó la plantilla de ejemplo `spaceflights`.
- ✅ **Estructura de Carpetas:** Se crearon `data/` (con subcarpetas `01_raw` a `08_reporting`), `docs/`, `dags/`, `docker/`. La raíz del repositorio es la raíz del proyecto Kedro.
- ✅ **Datos Crudos:** Los datasets de Stack Overflow y JetBrains están ubicados en `data/01_raw/`.
- ✅ **Configuración Kedro (`catalog.yml`):** Se definieron en `conf/base/catalog.yml` los datasets crudos con nombres en español (ej. `datos_crudos_so_2023`) y se configuró la ingesta de archivos `.zip`.
- ✅ **Documentación Inicial:** `README.md` actualizado y `docs/LICENCIAS_DE_DATOS.md` creado.
- ✅ **`.gitignore`:** Configurado para ignorar artefactos como `*.egg-info/`.

**Lo que NO se ha hecho (y son los próximos pasos):**
- ❌ No se ha escrito ningún código de pipeline en `src/ml_analisis_ecosistema_dev/pipelines/`.
- ❌ No se ha inicializado ni configurado DVC (`dvc init`).
- ❌ No se han creado los archivos `docker/Dockerfile.kedro` ni `docker-compose.yml`.
- ❌ No se ha escrito el DAG de Airflow en `dags/`.

---

## 3. Roadmap de Desarrollo (Próximos Pasos)

El trabajo se divide en las siguientes fases:

### Fase 1: Pipeline `procesamiento_de_datos` 🧼
- **Objetivo:** Cargar datos de `01_raw`, limpiarlos y crear un dataset maestro en `data/03_primary` o `data/05_model_input`.
- **Tareas Clave:**
    1. **Cargar Datos:** Usar las definiciones del `catalog.yml`.
    2. **Gestionar NaNs:** Eliminar filas críticas (salario), imputar en otras.
    3. **Filtrar Outliers:** Analizar y filtrar salarios extremos.
    4. **Encoding de Categóricas:** Aplicar `One-Hot Encoding` (multietiqueta), `Ordinal Encoding` (ordinales), `Binary Encoding` (nominales de alta cardinalidad).
    5. **Selección de Características:** Aplicar métodos de filtro (Correlación, ANOVA, Chi-cuadrado).
    6. **Estandarización:** Preparar el pipeline para aplicar `StandardScaler`.

### Fase 2: Pipelines `clasificacion` 🤖 y `regresion` 💰
- **Objetivo:** Implementar los dos pipelines de modelado cumpliendo los requisitos académicos.
- **A. Pipeline de REGRESIÓN (`regresion`):**
    - **Target:** `salario_anual_usd` (continua).
    - **Modelos (≥5):** `LinearRegression`, `Ridge`, `Lasso`, `RandomForestRegressor`, `XGBRegressor`.
    - **Validación:** `GridSearchCV` con `K-Fold Cross Validation` (k=5).
    - **Métricas:** R², MAE, RMSE.
- **B. Pipeline de CLASIFICACIÓN (`clasificacion`):**
    - **Target:** Una variable categórica (ej. `salary_group`).
    - **Preprocesamiento:** Aplicar `SMOTE` en el set de entrenamiento si las clases están desbalanceadas.
    - **Modelos (≥5):** `LogisticRegression`, `SVC`, `RandomForestClassifier`, `XGBClassifier`, `LGBMClassifier`.
    - **Validación:** `GridSearchCV` con `Stratified K-Fold Cross Validation` (k=5).
    - **Métricas:** Accuracy, Matriz de Confusión, F1-Score (macro y weighted average).

### Fase 3: Implementación de Stack MLOps
1.  **DVC:** Inicializar (`dvc init`), añadir artefactos (`dvc add data/01_raw`, `data/06_models`, etc.) y crear `dvc.yaml` con `stages` que ejecuten los pipelines de Kedro.
2.  **Docker:** Escribir `docker/Dockerfile.kedro` y `docker-compose.yml`.
3.  **Airflow:** Escribir un DAG en `dags/` que use `DockerOperator` para orquestar la ejecución de los pipelines.

### Fase 4: Reporte y Defensa
- Crear `docs/reporte_experimentos.md` con tablas comparativas (media ± std de CV), gráficos y conclusiones.

---

## 4. Guía de Justificación para la Defensa Técnica

El asistente debe ayudar a razonar las decisiones, no solo a escribir código.
- **Justificar Modelos Baseline:** `LinearRegression` y `LogisticRegression` como punto de partida.
- **Justificar Preprocesamiento:** ¿Por qué `StandardScaler` es necesario para SVM/Regresión Logística? ¿Por qué `SMOTE` es necesario si hay desbalanceo y por qué `F1-Score` es mejor que `Accuracy` en ese caso?
- **Justificar Modelos Avanzados:** `Lasso` como método de feature selection. `Random Forest` por su robustez ante no linealidades.
- **Justificar Evaluación:** ¿Por qué `Stratified K-Fold` es crucial para clasificación?

---

## 5. Estructura de Directorios Relevante
ML-Analisis-Ecosistema-Dev/
│
├── conf/
│ └── base/
│ ├── catalog.yml
│ └── parameters.yml
├── data/
│ ├── 01_raw/
│ ├── 03_primary/
│ ├── 05_model_input/
│ ├── 06_models/
│ └── 08_reporting/
├── dags/
│ └── kedro_ml_pipeline_dag.py
├── docker/
│ └── Dockerfile.kedro
├── docs/
│ └── reporte_experimentos.md
├── src/
│ └── ml_analisis_ecosistema_dev/
│ ├── pipelines/
│ │ ├── init.py
│ │ ├── procesamiento_de_datos/
│ │ │ ├── init.py
│ │ │ ├── nodes.py
│ │ │ └── pipeline.py
│ │ ├── clasificacion/
│ │ └── regresion/
│ └── pipeline_registry.py
├── .gitignore
├── dvc.yaml
├── docker-compose.yml
├── pyproject.toml
└── README.md