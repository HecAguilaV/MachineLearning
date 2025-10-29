"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # Detectar pipelines disponibles, pero definir como default únicamente el pipeline principal
    pipelines = find_pipelines()

    # Si existe data_analysis, usamos ese como default para evitar confusión con pipelines de plantilla
    if "data_analysis" in pipelines:
        pipelines["__default__"] = pipelines["data_analysis"]
    else:
        # Fallback: mantener comportamiento estándar si no existe data_analysis
        pipelines["__default__"] = sum(pipelines.values()) if pipelines else Pipeline([])
    return pipelines
