"""Project pipelines."""
from kedro.pipeline import Pipeline
from ml_analisis_ecosistema_dev.pipelines.procesamiento_de_datos import create_pipeline as dp_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    processing_pipeline = dp_pipeline()

    return {
        "__default__": processing_pipeline,
        "procesamiento_de_datos": processing_pipeline,
    }
