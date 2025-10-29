---
# 📄 Licencias de Datos y Atribuciones

Este repositorio **separa la licencia del código** (ver `LICENSE` en la raíz) de las licencias que rigen los datasets y recursos externos utilizados. A continuación se listan las licencias, enlaces oficiales, identificadores SPDX y la atribución requerida para los datos usados en el proyecto.

---

## 1. Encuesta a Desarrolladores Stack Overflow 2023

- **Licencia:** [Open Database License (ODbL) 1.0](https://opendatacommons.org/licenses/odbl/1-0/) (SPDX: ODbL-1.0)
- **Atribución requerida:** Atribuir a Stack Overflow / Stack Exchange según los términos de ODbL.
- **Página oficial de la encuesta:** [https://survey.stackoverflow.co/2023/](https://survey.stackoverflow.co/2023/)
- **Documentación/Esquema local:** `docs/stackoverflow_2023/`
- **Notas:** Si produces una base de datos derivada, ODbL puede requerir que la compartas bajo la misma licencia (*share‑alike*). Verifica los requisitos específicos si publicas o distribuyes derivados.

> **Atribución lista para copiar (Stack Overflow):**
>
> "Stack Overflow Developer Survey 2023" — Stack Overflow (ODbL 1.0). Fuente: https://survey.stackoverflow.co/2023/

---

## 2. Encuesta Ecosistema de Desarrolladores JetBrains 2025

- **Licencia:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) (SPDX: CC-BY-4.0)
- **Atribución requerida:** Atribuir a JetBrains s.r.o.
- **Página oficial / fuente del dataset:** [https://www.jetbrains.com/lp/devecosystem-2025/](https://www.jetbrains.com/lp/devecosystem-2025/)
- **Documentación/Esquema local:** `docs/jetbrains_2025/`
- **Notas:** Este repositorio incluye el archivo de licencia original (`LICENSE.txt`) junto al dataset correspondiente en `data/01_raw/jetbrains_2025/`.

> **Atribución lista para copiar (JetBrains):**
>
> "Developer Ecosystem Survey 2025" — JetBrains s.r.o. (CC BY 4.0). Fuente: https://www.jetbrains.com/lp/devecosystem-2025/

---

## ✅ Recomendaciones Prácticas de Atribución

- Mantén los archivos de licencia originales junto a los datasets en la carpeta `data/` (ya incluidos en este repositorio).
- En el `README.md` principal y en cualquier informe público, incluye al menos la atribución mínima (ver ejemplos arriba) y enlaza a este archivo (`DATA_LICENSES.md`) para más detalles.
- Si publicas derivados (tablas procesadas, subsets, visualizaciones que contienen datos), añade una nota describiendo los cambios realizados y la licencia aplicable al derivado (teniendo en cuenta las cláusulas *share-alike* si aplica).

---

## ⚠️ Notas Legales y de Privacidad

- La licencia ODbL (Stack Overflow) puede imponer obligaciones adicionales para bases de datos derivadas (*share‑alike*). Si piensas publicar un dataset derivado públicamente, revisa las obligaciones de ODbL en detalle.
- Revisa y asegúrate de eliminar cualquier dato que pueda identificar a personas antes de publicar resultados si existiera riesgo de fuga de información personal. Aunque este repositorio utiliza datasets públicos anonimizados, es responsabilidad del publicador verificar el cumplimiento de las normativas de privacidad y protección de datos aplicables.