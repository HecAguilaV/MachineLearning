# 🤖 ML-Análisis-Ecosistema-Dev

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-habilitado-blue.svg)](https://www.docker.com/)
[![Kedro](https://img.shields.io/badge/desarrollado_con-kedro-ffc900?logo=kedro)](https://kedro.org)
[![Airflow](https://img.shields.io/badge/orquestado_con-airflow-red.svg)](https://airflow.apache.org/)

**Proyecto del curso de Machine Learning para construir un sistema MLOps de nivel profesional que analiza, modela y predice tendencias en el ecosistema de desarrolladores.**

---

## 📋 Resumen Ejecutivo

Este proyecto implementa un pipeline de Machine Learning de principio a fin utilizando **Kedro**, **Docker** y **Apache Airflow**. El objetivo es transformar datos crudos de encuestas globales (Stack Overflow y JetBrains) en un modelo predictivo capaz de estimar la categoría salarial de un desarrollador.

Además, este pipeline busca validar y automatizar los hallazgos del siguiente informe de análisis preliminar:
* **Informe de Contexto**: [Informe Ejecutivo del Mercado Tech Chileno](./docs/referencias/Informe_Mercado_Tech_Chile.md)

---

git clone [https://github.com/HecAguilaV/ML-Analisis-Ecosistema-Dev.git](https://github.com/HecAguilaV/ML-Analisis-Ecosistema-Dev.git)
## 🚀 Cómo Empezar (con Docker)

Este proyecto está diseñado para ser completamente reproducible gracias a Docker.

### Prerrequisitos

- Docker Desktop (20.10+)
- Docker Compose (2.0+)

### Instalación Rápida

```bash
# 1. Clona este repositorio
git clone https://github.com/HecAguilaV/ML-Analisis-Ecosistema-Dev.git
cd ML-Analisis-Ecosistema-Dev

# 2. Inicia el entorno de desarrollo (script de arranque)
# (Asegúrate de darle permisos de ejecución primero: chmod +x start.sh)
./start.sh development
```

¡Listo! Tu entorno MLOps estará preparado. Accede a los servicios:

- **JupyterLab** (para exploración): [http://localhost:8888](http://localhost:8888)
- **Kedro Viz** (para visualizar pipelines): [http://localhost:4141](http://localhost:4141)

---

## ⚙️ Pipelines del Proyecto

El proyecto está organizado en pipelines modulares:

- **procesamiento_de_datos** 🧼: Carga los datos crudos de `data/01_raw/`, los limpia, selecciona columnas, maneja valores nulos y los guarda en `data/03_primary/`.
- **ciencia_de_datos** 🤖: Toma los datos limpios, los divide, entrena un modelo predictivo (ej. RandomForest) y lo guarda en `data/06_models/`.
- **reporte_de_resultados** 📊 (Futuro): Genera automáticamente los gráficos y métricas clave (ej. `feature_importance.png`) en `data/08_reporting/`.

---

## 📁 Estructura de Directorios

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