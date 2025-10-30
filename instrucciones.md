# Documento Integrado de Requisitos y Evaluación — Entrega Parcial 2

## 1. Objetivo General

Implementar y documentar un flujo completo de Machine Learning siguiendo la metodología CRISP-DM, con pipelines modulares de clasificación y regresión, versionado de datos y modelos, orquestación, reproducibilidad y defensa técnica, usando las mejores prácticas de MLOps.

---

## 2. Requisitos Técnicos y Académicos

### CRISP-DM y Análisis Exploratorio
- El notebook debe cubrir todas las fases de CRISP-DM, con explicaciones en markdown y justificación de cada decisión.
- Incluir análisis estadístico, visualizaciones, correlaciones y fundamentos matemáticos.
- Justificar la selección de features y modelos, y explicar diferencias entre regresión y clasificación.

### Modelado Supervisado
- **Regresión:**  
  - Target continuo justificado.
  - Al menos 5 modelos distintos.
  - GridSearchCV + CrossValidation (k≥5).
  - Métricas estándar (RMSE, MAE, R²).
  - Selección y justificación del mejor modelo.
- **Clasificación:**  
  - Target discreto (“target”).
  - Al menos 5 modelos distintos.
  - GridSearchCV + CrossValidation (k≥5).
  - Métricas estándar (accuracy, F1, ROC-AUC, etc.).
  - Análisis de matriz de confusión y métricas derivadas.
  - Balanceo de clases (ej: SMOTE).
  - Selección y justificación del mejor modelo.

### MLOps y Reproducibilidad
- **Kedro:** Dos pipelines independientes y modulares (clasificación y regresión).
- **DVC:** Versionado de datasets, features, modelos y métricas. Stages en dvc.yaml.
- **Airflow:** DAG que ejecute ambos pipelines y consolide resultados.
- **Docker:** Imagen funcional y reproducible, con instrucciones claras.
- **Git:** Todo el código y configuración versionados.
- **README:** Instrucciones, arquitectura, cómo correr todo (local, Docker, Airflow), enlaces a datos y reporte.
- **Reporte de experimentos:** Comparación, discusión y conclusiones (notebook o markdown).
- **Defensa técnica:** Explicación clara del flujo Kedro–Airflow–DVC–Docker y justificación de decisiones.

---

## 3. Rúbrica y Checklist

| Criterio                                 | %  | Evidencias de logro                                                                 |
|-------------------------------------------|----|-------------------------------------------------------------------------------------|
| Integración de Pipelines                  | 8  | Pipelines Kedro modulares y ejecutables                                             |
| DVC (datos, features, modelos, métricas)  | 7  | Stages en dvc.yaml, artefactos y métricas versionadas                               |
| Airflow (DAG orquestado)                  | 7  | DAG ejecuta ambos pipelines y consolida resultados                                  |
| Docker (portabilidad)                     | 7  | Imagen funcional, reproducible, con instrucciones de ejecución                      |
| Métricas y visualizaciones                | 10 | Métricas correctas y análisis gráfico                                               |
| Cobertura de modelos + Tuning + CV        | 24 | ≥5 modelos por tipo, GridSearch + CV (k≥5), tabla comparativa                       |
| Reproducibilidad (Git+DVC+Docker)         | 7  | Ejecución determinística y documentada                                              |
| Documentación técnica                     | 5  | README con instrucciones y arquitectura                                             |
| Reporte de experimentos                   | 5  | Comparación final, discusión y conclusiones                                         |
| Defensa técnica (oral)                    | 20 | 10’ + 5’ preguntas, explicación del flujo Kedro–Airflow–DVC–Docker                 |

---

## 4. Análisis de Estado Actual

### ¿Qué tienes ya implementado?
- Estructura de proyecto MLOps moderna (Kedro, DVC, Docker, Airflow).
- Pipeline de procesamiento de datos funcional y reproducible.
- Versionado de datos con DVC (aunque con limitaciones de Drive).
- README detallado y documentación de arquitectura.
- Automatización parcial (falta integración total de Airflow y Docker para todo el flujo).
- Análisis exploratorio y justificación de decisiones en notebooks previos.

### ¿Qué falta o debe mejorarse?
- Separar y modularizar los pipelines de clasificación y regresión en Kedro.
- Implementar al menos 5 modelos distintos en cada pipeline, con GridSearchCV y k-fold.
- Orquestar ambos pipelines con un DAG de Airflow funcional.
- Versionar no solo datos, sino también features, modelos y métricas con DVC.
- Crear una imagen Docker que ejecute todo el flujo (incluyendo Airflow).
- Completar el notebook de informe con todas las fases de CRISP-DM, justificaciones, visualizaciones y comparativas.
- Subir manualmente los datos a Drive (por las restricciones de OAuth) y dejarlo documentado.
- Preparar la defensa técnica, con explicación clara de cada decisión y del flujo MLOps.

---

## 5. Proyección y Siguiente Paso

### Objetivo final
- Entregar un proyecto reproducible, defendible y bien documentado, que permita ejecutar y comparar modelos de clasificación y regresión, versionar todos los artefactos y orquestar el flujo completo con Airflow y Docker.

### Siguiente paso recomendado
1. **Estructura de pipelines Kedro:** Modulariza y separa los pipelines de clasificación y regresión.
2. **Implementa los modelos y experimentos:** Añade los 5+ modelos por pipeline, tuning y validación.
3. **Orquestación:** Crea el DAG de Airflow que ejecute ambos pipelines.
4. **Versionado:** Asegúrate de versionar datasets, features, modelos y métricas con DVC.
5. **Docker:** Prepara la imagen Docker y verifica que todo el flujo sea ejecutable.
6. **Notebook de informe:** Completa el notebook con todas las fases, justificaciones, visualizaciones y comparativas.
7. **Documentación:** Actualiza el README y deja claro el acceso a los datos y la reproducibilidad.
8. **Defensa técnica:** Prepara una presentación clara del flujo y las decisiones.

---

Este documento debe ser tu guía de referencia para asegurar que tu entrega cumple con todos los requisitos técnicos y académicos, y maximiza tu puntaje en la evaluación.
