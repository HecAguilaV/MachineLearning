# ML-Análisis-Ecosistema-Dev

**Motor de backend MLOps para una futura herramienta de inteligencia de mercado, diseñada para ayudar a los desarrolladores a tomar decisiones estratégicas sobre su carrera profesional.**

---

## 1. Visión y Misión

### La Visión (Nuestro Norte)

El objetivo final es construir una **herramienta web interactiva** que permita a los desarrolladores analizar tendencias, obtener predicciones salariales personalizadas y tomar decisiones informadas sobre qué tecnologías estudiar.

### La Misión (Este Repositorio)

Este proyecto construye el **cerebro y la sala de máquinas (backend)** que alimentará esa futura aplicación. Implementamos un pipeline de Machine Learning de principio a fin utilizando un stack MLOps moderno para transformar datos crudos de encuestas globales (Stack Overflow 2023, JetBrains 2025) en modelos predictivos robustos y reproducibles.

---

## 2. Arquitectura y Stack Tecnológico

- **Pipeline:** Kedro
- **Contenerización:** Docker / Docker Compose
- **Orquestación:** Apache Airflow
- **Versionado de Datos/Modelos:** DVC
- **Lenguaje:** Python 3.10+

---

## 3. Roadmap del Proyecto (Brújula del Equipo)

El trabajo se divide en las siguientes fases. **Actualmente estamos en la Fase 1.**

### Fase 1: Pipeline `procesamiento_de_datos` 🧼
*   **Objetivo:** Cargar datos crudos, limpiarlos y generar un dataset maestro listo para el modelado.
*   **Tareas:**
    *   [X] **Cargar Datos:** Usar las definiciones del `catalog.yml`.
    *   [X] **Gestionar NaNs:** Eliminar columnas con >50% de nulos y filas críticas (salario).
    *   [X] **Filtrar Outliers:** Filtrar salarios extremos usando el método IQR.
    *   [X] **Encoding de Categóricas (Básica):** Aplicar `One-Hot Encoding` a variables de baja cardinalidad.
    *   [X] **Selección de Características:** Aplicar métodos de filtro (correlación) para seleccionar los mejores predictores.
    *   [X] **Estandarización:** Aplicar `StandardScaler` a las variables numéricas.
    *   [X] **Guardado Final:** Generar el artefacto `data/05_model_input/datos_para_modelado.parquet`.

### Fase 2: Pipelines de Modelado (`regresion` 💰 y `clasificacion` 🤖)
*   **Objetivo:** Implementar los dos pipelines de modelado cumpliendo los requisitos académicos.
*   **A. Pipeline de REGRESIÓN:**
    *   **Target:** `ConvertedCompYearly`.
    *   **Modelos:** `LinearRegression`, `Ridge`, `Lasso`, `RandomForestRegressor`, `XGBRegressor`.
    *   **Validación:** `GridSearchCV` con `K-Fold CV (k≥5)`.
*   **B. Pipeline de CLASIFICACIÓN:**
    *   **Target:** Una variable categórica (ej. `salary_group`).
    *   **Preprocesamiento:** `SMOTE` si hay desbalanceo.
    *   **Modelos:** `LogisticRegression`, `SVC`, `RandomForestClassifier`, `XGBClassifier`, `LGBMClassifier`.
    *   **Validación:** `GridSearchCV` con `Stratified K-Fold CV (k≥5)`.

### Fase 3: Implementación de Stack MLOps
*   **Objetivo:** Versionar, empaquetar y orquestar el pipeline completo.
*   **Tareas:** DVC (`dvc init`, `dvc add`), Docker (`Dockerfile`, `docker-compose.yml`), Airflow (crear el DAG).

### Fase 4: Reporte y Defensa
*   **Objetivo:** Crear `docs/reporte_experimentos.md` con tablas, gráficos y conclusiones.

---

## 4. Guía de Inicio Rápido y Reproducibilidad

### Opción A: Entorno Local (Recomendado para desarrollo)

1.  **Prerrequisitos:** Git, Python 3.10+.
2.  **Clonar:** `git clone <URL_DEL_REPOSITORIO_GIT> && cd ML-Analisis-Ecosistema-Dev`
3.  **Entorno Virtual:** `py -m venv .venv && .\.venv\Scripts\activate` (en Windows)
4.  **Instalar Dependencias:** `pip install -r requirements.txt`
5.  **Instalar Proyecto:** `pip install -e .`
6.  **Verificar:** `kedro run`

### Opción B: Entorno Docker (Recomendado para ejecución)
1.  **Prerrequisitos:** Docker Desktop, Docker Compose, Git.
2.  **Clonar:** `git clone <URL_DEL_REPOSITORIO_GIT> && cd ML-Analisise-Ecosistema-Dev`
3.  **Iniciar:** `./start.sh` (o el comando equivalente en `docker-compose.yml`).

---

## 5. Guía de Justificación para la Defensa Técnica

Este proyecto no solo ejecuta código, sino que justifica cada decisión. Puntos clave a defender:
- **¿Por qué `StandardScaler`?** Esencial para modelos sensibles a la escala como `Lasso`, `Ridge` y `SVC`.
- **¿Por qué `SMOTE` y `F1-Score`?** Si las clases están desbalanceadas, `Accuracy` es engañoso. `SMOTE` balancea los datos de entrenamiento y `F1-Score` es una métrica más robusta en este escenario.
- **¿Por qué `Lasso`?** No solo es un buen regresor, sino que su regularización L1 funciona como un método de selección de características "embebido".
- **¿Por qué `Stratified K-Fold`?** Asegura que la proporción de clases se mantenga

- ## 📁 Estructura de Directorios

El proyecto sigue una estructura estándar para mantener todo organizado:

```text
.
├── conf/         # Configuración de Kedro (catálogo, parámetros)
├── data/         # Datos (raw, intermediate, models, etc.)
├── dags/         # Definiciones de DAGs para Apache Airflow
├── docker/       # Dockerfiles para los diferentes servicios
├── docs/         # Documentación de apoyo (esquemas, PDFs)
├── notebooks/    # Notebooks de Jupyter para análisis exploratorio
├── src/          # Código fuente del proyecto (pipelines y nodos)
└── README.md     # Este archivo
```

---

## 📄 Licenciamiento

Este proyecto tiene un licenciamiento dual, separando el código fuente de los datos utilizados.

**Código Fuente**

El código fuente de este proyecto (todo lo contenido en `src/`, `docker/`, `dags/`, etc.) está licenciado bajo la Licencia MIT. Ver detalles en el archivo [LICENSE](./LICENSE).

**Datos Utilizados**

Los datasets de las encuestas se utilizan bajo sus licencias públicas específicas, las cuales requieren atribución:

- Encuesta Stack Overflow 2023: Licenciada bajo ODbL 1.0.
- Encuesta JetBrains 2025: Licenciada bajo CC BY 4.0.

Para ver los detalles completos de atribución, enlaces y notas legales, por favor consulta el archivo: [DATA_LICENSES.md](./docs/DATA_LICENSES.md)

---

## 👨‍💻 Autor

**Héctor Águila** — Un Soñador con poca RAM
**Asignatura:** Machine Learning - Duoc UC
**Repositorio:** [PROYECTO MACHINE LEARNING](https://github.com/HecAguilaV/ML_Analisis_Ecosistema_Dev.git)
**Última actualización: 29 de octubre de 2025**


