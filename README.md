## Análisis de Lenguajes de Programación

Práctico de Machine Learning para analizar la popularidad de lenguajes y su relación con salarios usando la Stack Overflow Developer Survey 2023. Enfoque simple y reproducible.

### Esencial
- Dataset: Stack Overflow Developer Survey 2023 (CSV ~158 MB). Se trabaja con una muestra de ~1.000 filas para desarrollo.
- Alcance: CRISP-DM (fases 1–3). Sin modelado ni despliegue.
- Outputs clave:
  - `data/02_intermediate/survey_basic_stats.json` (estadísticas básicas)
  - `data/02_intermediate/languages_analysis.parquet` (popularidad de lenguajes)
  - `data/02_intermediate/salary_data.parquet` (columnas salariales + país si existe)
- Dónde ver el código:
  - Pipeline: `src/analisis_lenguajes_programacion/pipelines/data_analysis/pipeline.py`
  - Nodos: `src/analisis_lenguajes_programacion/pipelines/data_analysis/nodes.py`
  - Notebook: `notebooks/01_exploratory_analysis.ipynb`

### Pipeline
- `load_and_inspect_survey(df)`: inspección y métricas básicas → `survey_basic_stats.json`
- `analyze_programming_languages(df)`: conteos/porcentajes por columnas de lenguajes → `languages_analysis.parquet`
- `extract_salary_data(df)`: columnas salariales y país (si aplica) → `salary_data.parquet`

### Cómo ejecutarlo

#### Opción 1: Ejecución manual (paso a paso)
```bash
# Ejecutar todo el pipeline
kedro run

# Ejecutar un nodo específico
kedro run --nodes="load_and_inspect_survey"

# Visualizar el pipeline (requiere abrir http://localhost:4141)
kedro viz --no-browser --host=127.0.0.1 --port=4141

# Trabajar con notebooks que tienen contexto del proyecto
kedro jupyter notebook
```

#### Opción 2: Ejecución automatizada (recomendado)
Este proyecto incluye un script para automatizar todo el proceso desde la terminal.

**Para ejecutarlo:**
1.  Abre una terminal.
2.  Asegúrate de estar en la carpeta raíz de este proyecto.
3.  Ejecuta el siguiente comando:

```bash
./scripts/run_project.sh
```

<details>
<summary>Haz clic para ver los detalles del script y el comando de permisos</summary>

- **Inspeccionar el script**: Puedes ver el contenido del script aquí: [`scripts/run_project.sh`](./scripts/run_project.sh)
- **Permisos (solo la primera vez)**: Antes de usarlo por primera vez, dale permisos de ejecución con:
  ```bash
  chmod +x scripts/run_project.sh
  ```
- **¿Qué hace el script?**:
  1. Crea y activa un entorno virtual (`.venv`).
  2. Instala las dependencias desde `requirements.txt`.
  3. Ejecuta el pipeline completo (`kedro run`).
  4. Inicia `kedro viz` y `jupyter notebook` en segundo plano.
  5. Abre automáticamente las pestañas del navegador para ambos servicios.
- **Puertos (fijos)**:
  - Kedro Viz: `http://localhost:4141`
  - Jupyter: `http://localhost:8888`
</details>

### ¿Por qué usé solo un dataset?
Como este es mi primer proyecto con Kedro, quise mantener las cosas simples para enfocarme en aprender a usar la herramienta.
- **Todo en un solo lugar:** El archivo de la encuesta ya tenía los datos de lenguajes y salarios, así que no necesité buscar más.
- **Más fácil de manejar:** Trabajar con un solo archivo me ayudó a entender mejor el flujo de datos en el pipeline.
- **Más rápido:** Usar un solo dataset consume menos memoria y hace que todo corra más rápido, lo cual no destroza mi mac xD

### Cosas que no hice
Este proyecto se enfoca en las primeras etapas de un análisis de datos. Por eso, hay algunas cosas que quedaron fuera:
- **No usé el dataset completo:** Para que el proyecto corriera rápido en mi computador, trabajé con una muestra de ~1.000 filas. El archivo original tiene casi 90,000.
- **No hay modelos de Machine Learning:** El objetivo era preparar y limpiar los datos (fases 1-3 de CRISP-DM). No llegué a la parte de crear modelos predictivos (fases 4-6).
- **Análisis básico:** Las visualizaciones y el análisis son sencillos.

### Proyecto
- **Autor**: Héctor Aguila — Duoc UC, Machine Learning
- **Repositorio**: https://github.com/HecAguilaV/MachineLearning.git
- **Última actualización**: 10 de octubre de 2025
