"""Tests básicos para el pipeline `data_analysis`.

Cobertura mínima para validar:
- Que el pipeline se construye sin errores.
- Que los nodos principales reciben/retornan los tipos esperados con datos de ejemplo.
"""

import pandas as pd
from kedro.pipeline import node, Pipeline
from analisis_lenguajes_programacion.pipelines.data_analysis.nodes import (
	load_and_inspect_survey,
	analyze_programming_languages,
	extract_salary_data,
)


def test_pipeline_builds():
	"""El pipeline se construye correctamente."""
	p = Pipeline([
		node(load_and_inspect_survey, inputs="df", outputs="stats"),
		node(analyze_programming_languages, inputs="df", outputs="languages"),
		node(extract_salary_data, inputs="df", outputs="salaries"),
	])
	assert isinstance(p, Pipeline)


def test_nodes_with_small_df():
	"""Validar que las funciones operan con un DataFrame mínimo."""
	df = pd.DataFrame(
		{
			"LanguageHaveWorkedWith": ["Python; SQL", "JavaScript", None],
			"ConvertedComp": [50000, None, 30000],
			"Country": ["ES", "MX", "AR"],
		}
	)

	stats = load_and_inspect_survey(df)
	assert isinstance(stats, dict)
	assert {"total_filas", "total_columnas", "porcentaje_nulos"} <= set(stats.keys())

	lang_df = analyze_programming_languages(df)
	assert isinstance(lang_df, pd.DataFrame)
	assert {"columna", "respuestas_validas", "valores_unicos", "porcentaje_respuestas"} <= set(
		lang_df.columns
	)

	sal_df = extract_salary_data(df)
	assert isinstance(sal_df, pd.DataFrame)
