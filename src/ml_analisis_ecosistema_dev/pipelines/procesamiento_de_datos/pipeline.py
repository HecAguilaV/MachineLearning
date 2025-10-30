"""
Pipeline de procesamiento de datos robusto y controlado por una "allowlist".
"""

from kedro.pipeline import Pipeline, node
from .nodes import (
    cargar_datos, 
    analizar_y_limpiar_nulos, 
    eliminar_filas_sin_salario,
    filtrar_outliers_salario,
    preprocesamiento_final_con_allowlist # Importar la nueva función final
)

def create_pipeline(**kwargs) -> Pipeline:
    """Crea el pipeline de procesamiento de datos.

    Returns:
        El pipeline de procesamiento de datos.
    """
    return Pipeline([
        node(
            func=cargar_datos,
            inputs=[
                "datos_crudos_so_2023",
                "datos_crudos_jb_2025_external",
                "datos_crudos_jb_2025_narrow",
            ],
            outputs=[
                "datos_intermedios_so_2023",
                "datos_intermedios_jb_external",
                "datos_intermedios_jb_narrow",
            ],
            name="cargar_datos_crudos",
        ),
        node(
            func=analizar_y_limpiar_nulos,
            inputs=[
                "datos_intermedios_so_2023",
                "datos_intermedios_jb_external",
                "datos_intermedios_jb_narrow",
            ],
            outputs=[
                "datos_primarios_so_2023",
                "datos_primarios_jb_external",
                "datos_primarios_jb_narrow",
            ],
            name="analizar_y_limpiar_nulos_por_columna",
        ),
        node(
            func=eliminar_filas_sin_salario,
            inputs={"df_so": "datos_primarios_so_2023", "target_col": "params:preprocessing_params.target_col"},
            outputs="datos_con_salario_so_2023",
            name="eliminar_filas_sin_salario_so",
        ),
        node(
            func=filtrar_outliers_salario,
            inputs={"df_so": "datos_con_salario_so_2023", "target_col": "params:preprocessing_params.target_col"},
            outputs="datos_sin_outliers_so_2023",
            name="filtrar_outliers_salario_so",
        ),
        node(
            func=preprocesamiento_final_con_allowlist,
            inputs={
                "df": "datos_sin_outliers_so_2023",
                "params": "params:preprocessing_params"
            },
            outputs="datos_para_modelado",
            name="preprocesamiento_final_node",
        ),
    ])