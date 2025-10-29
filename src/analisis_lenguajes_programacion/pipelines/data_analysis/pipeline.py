"""
Pipeline de análisis de datos de Stack Overflow Survey
"""

from kedro.pipeline import Pipeline, node

from .nodes import (
    load_and_inspect_survey,
    analyze_programming_languages,
    extract_salary_data,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        # Nodo 1: Inspección inicial del dataset
        node(
            func=load_and_inspect_survey,
            inputs="stack_overflow_survey",
            outputs="survey_basic_stats",
            name="inspect_survey_data",
        ),
        
        # Nodo 2: Análisis de lenguajes de programación
        node(
            func=analyze_programming_languages,
            inputs="stack_overflow_survey",
            outputs="languages_analysis",
            name="analyze_languages",
        ),
        
        # Nodo 3: Extracción de datos de salario
        node(
            func=extract_salary_data,
            inputs="stack_overflow_survey",
            outputs="salary_data",
            name="extract_salary_data",
        ),
    ])
