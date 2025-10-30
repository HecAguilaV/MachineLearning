"""Project pipelines."""

from kedro.pipeline import Pipeline

from ml_analisis_ecosistema_dev.pipelines.procesamiento_de_datos import (
    create_pipeline as dp_pipeline,
)
from ml_analisis_ecosistema_dev.pipelines.regresion.pipeline import (
    create_pipeline as regresion_pipeline,
)
from ml_analisis_ecosistema_dev.pipelines.clasificacion.pipeline import (
    create_pipeline as clasificacion_pipeline,
)


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    processing_pipeline = dp_pipeline()
    reg_pipeline = regresion_pipeline()
    clasif_pipeline = clasificacion_pipeline()

    return {
        "__default__": processing_pipeline,
        "procesamiento_de_datos": processing_pipeline,
        "regresion": reg_pipeline,
        "clasificacion": clasif_pipeline,
    }
