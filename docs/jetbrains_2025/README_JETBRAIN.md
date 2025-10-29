# Developer Ecosystem Survey 2025 - Open Raw Data

> **Nota:** Los datos del reporte están ponderados. Para replicar los resultados del informe, aplica el multiplicador de la columna `"weight"` en tus cálculos. De lo contrario, los resultados diferirán. Los pesos se aplican para reducir sesgos y ofrecer una imagen más representativa.

---

## Archivos incluidos en la carpeta

- **`developer_ecosystem_2025_external.csv`**  
  Archivo CSV con 4740 columnas y 24,534 filas.  
  - Cada fila representa un encuestado individual.
  - Cada columna corresponde a una respuesta de pregunta de opción única o a una opción de pregunta de opción múltiple.
  - Columnas especiales:  
    - `response_id`: Identificador único del encuestado.  
    - `weight`: Peso para ajustar sesgos de muestreo por país, preferencia de lenguaje y relación con JetBrains.

- **`developer_ecosystem_2025_external_narrow.csv.zip`**  
  Archivo CSV comprimido que presenta los datos en un formato más estandarizado (tipo base de datos).  
  - Cada fila corresponde a una respuesta individual de pregunta de opción única o a una opción seleccionada en preguntas de opción múltiple.
  - Si un encuestado selecciona varias opciones, se generan varias filas.
  - Contiene 4 columnas: `respondent ID`, `weight`, `question ID`, y `answer`.
  - Más de seis millones de filas.

- **`developer_ecosystem_2025_external_questions.csv`**  
  Archivo CSV que lista todas las preguntas de la encuesta con sus nombres cortos, tal como se usan en el dataset.
  - Incluye el campo `parent_question_id` para preguntas tabulares (grillas de radio/checkbox), conectando cada ítem con su pregunta "padre".

- **`Developer_Ecosystem_2025_Survey_questions_logic.pdf`**  
  Documento PDF con el texto completo de las preguntas y opciones de respuesta, así como la lógica detrás de cada pregunta.  
  - Ejemplo: Explica que las preguntas sobre Java solo se hicieron a quienes declararon usar Java.

- **`LICENSE.txt`**  
  Archivo de texto con los términos de la licencia (CC-BY-4.0) para el uso de los datos.

---

## Detalles adicionales sobre preguntas "Fiction" en el dataset

- **primary y rank:**  
  Versiones ajustadas de las preguntas `primary_proglang` y `proglang_rank`, modificadas para casos donde solo se seleccionó un lenguaje y no se preguntó por ranking.

- **main:**  
  Derivada de `proglang_rank`, representa el lenguaje más importante elegido por el encuestado.

- **region:**  
  Columna para reportes que agrupa países individuales en regiones más amplias.

- **salary_group:**  
  Clasificación dentro de cada región que segmenta a los individuos en tres grupos según su rango salarial (alto, medio, bajo).  
  - La pregunta de salario real fue excluida por ser sensible.

---

## ¿Qué significa que los datos estén bajo la licencia CC-BY-4.0?

Con la licencia Creative Commons Attribution 4.0 International (CC BY 4.0):

- Puedes compartir (copiar y redistribuir en cualquier medio o formato) y adaptar (remezclar, transformar y construir a partir de los datos) para cualquier propósito, incluso comercialmente.
- Debes dar crédito adecuado al origen, enlazar la licencia e indicar si realizaste cambios.
- No puedes añadir términos legales o medidas tecnológicas que restrinjan a otros de hacer lo que la licencia permite.

Para artículos científicos y publicaciones basadas en estos datos (aunque no los incluyan directamente):

- Debes reconocer a JetBrains s.r.o. como fuente, indicar el uso bajo CC BY 4.0 y describir cómo usaste los datos.
- Esto fomenta la transparencia y el intercambio de conocimiento, sin importar el medio de publicación.