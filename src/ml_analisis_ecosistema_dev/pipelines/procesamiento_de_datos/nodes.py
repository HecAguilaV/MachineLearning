"""
Nodos para el pipeline de procesamiento de datos.
"""

import pandas as pd
import numpy as np
import io
from sklearn.preprocessing import StandardScaler


def cargar_datos(
    so_2023: pd.DataFrame,
    jb_external: pd.DataFrame,
    jb_narrow: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Carga los datos crudos desde el catálogo.

    Args:
        so_2023: DataFrame de la encuesta de Stack Overflow 2023.
        jb_external: DataFrame de la encuesta externa de JetBrains 2025.
        jb_narrow: DataFrame de la encuesta reducida de JetBrains 2025.

    Returns:
        Una tupla con los tres DataFrames cargados.
    """
    return so_2023, jb_external, jb_narrow


def analizar_y_limpiar_nulos(
    so_2023: pd.DataFrame,
    jb_external: pd.DataFrame,
    jb_narrow: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Analiza y elimina columnas con un alto porcentaje de valores nulos.

    Args:
        so_2023: DataFrame de Stack Overflow.
        jb_external: DataFrame de JetBrains (externo).
        jb_narrow: DataFrame de JetBrains (reducido).

    Returns:
        Una tupla con los tres DataFrames sin las columnas con demasiados nulos.
    """
    print("--- Análisis y Limpieza de Nulos por Columna ---")

    def _limpiar_df(df: pd.DataFrame, nombre: str) -> pd.DataFrame:
        nan_percentages = df.isnull().sum() / len(df)
        cols_to_drop = nan_percentages[nan_percentages > 0.5].index

        if len(cols_to_drop) > 0:
            print(
                f"En '{nombre}', eliminando {len(cols_to_drop)} columnas con >50% de nulos:"
            )
            for col in cols_to_drop:
                print(f"  - {col} ({nan_percentages[col]:.2%})")
            df = df.drop(columns=cols_to_drop)
        else:
            print(f"En '{nombre}', no se encontraron columnas con >50% de nulos.")

        return df

    so_2023_clean = _limpiar_df(so_2023, "Stack Overflow 2023")
    jb_external_clean = _limpiar_df(jb_external, "JetBrains External")
    jb_narrow_clean = _limpiar_df(jb_narrow, "JetBrains Narrow")

    print("--- Fin de la limpieza de nulos por columna ---")

    return so_2023_clean, jb_external_clean, jb_narrow_clean


def eliminar_filas_sin_salario(df_so: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina las filas del dataset de Stack Overflow donde el salario anual
    convertido a USD ('ConvertedCompYearly') es nulo.
    """
    print("--- Eliminando filas sin datos de salario (Stack Overflow) ---")

    columna_salario = "ConvertedCompYearly"

    if columna_salario not in df_so.columns:
        print(
            f"ADVERTENCIA: La columna '{columna_salario}' no se encontró. No se eliminaron filas."
        )
        return df_so

    rows_before = len(df_so)
    df_cleaned = df_so.dropna(subset=[columna_salario])
    rows_after = len(df_cleaned)

    print(
        f"Se eliminaron {rows_before - rows_after} filas donde '{columna_salario}' era nulo."
    )
    print("--- Fin de la eliminación de filas sin salario ---")

    return df_cleaned


def filtrar_outliers_salario(df_so: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra outliers de la columna de salarios usando el método IQR.
    """
    print("--- Filtrando outliers de salario (Stack Overflow) ---")

    columna_salario = "ConvertedCompYearly"

    if columna_salario not in df_so.columns:
        print(
            f"ADVERTENCIA: La columna '{columna_salario}' no se encontró. No se filtraron outliers."
        )
        return df_so

    Q1 = df_so[columna_salario].quantile(0.25)
    Q3 = df_so[columna_salario].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    rows_before = len(df_so)
    df_filtered = df_so[
        (df_so[columna_salario] >= limite_inferior)
        & (df_so[columna_salario] <= limite_superior)
    ]
    rows_after = len(df_filtered)

    print(
        f"Se eliminaron {rows_before - rows_after} filas consideradas outliers de salario."
    )
    print(
        f"Límites de salario considerados: ${limite_inferior:,.2f} - ${limite_superior:,.2f}"
    )
    print("--- Fin del filtrado de outliers ---")

    return df_filtered


def analizar_tipos_de_datos(
    so_2023: pd.DataFrame,
    jb_external: pd.DataFrame,
    jb_narrow: pd.DataFrame,
):
    """
    Analiza y muestra información sobre los tipos de datos de las columnas
    de los dataframes.
    """
    print("\n" + "=" * 50)
    print("--- ANÁLISIS DE TIPOS DE DATOS ---")
    print("=" * 50)

    datasets = {
        "Stack Overflow (limpio)": so_2023,
        "JetBrains External": jb_external,
        "JetBrains Narrow": jb_narrow,
    }

    for nombre, df in datasets.items():
        print(f"\n--- Dataset: {nombre} ---")
        print(f"Dimensiones: {df.shape}")

        buffer = io.StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        print(info_str)

    print("=" * 50)
    print("--- FIN DEL ANÁLISIS DE TIPOS DE DATOS ---")
    print("=" * 50 + "\n")


def codificar_variables_categoricas(df_so: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica One-Hot Encoding a un conjunto seleccionado de variables categóricas.
    """
    print("--- Codificando variables categóricas (One-Hot Encoding) ---")

    columnas_a_codificar = [
        "MainBranch",
        "Age",
        "Employment",
        "RemoteWork",
        "EdLevel",
        "DevType",
    ]

    columnas_existentes = [col for col in columnas_a_codificar if col in df_so.columns]
    print(f"Columnas a codificar: {columnas_existentes}")

    df_encoded = pd.get_dummies(
        df_so, columns=columnas_existentes, prefix=columnas_existentes
    )

    print(
        f"El número de columnas aumentó de {len(df_so.columns)} a {len(df_encoded.columns)}."
    )
    print("--- Fin de la codificación ---")

    return df_encoded


def seleccionar_caracteristicas(
    df: pd.DataFrame, target_col: str = "ConvertedCompYearly"
) -> pd.DataFrame:
    """
    Selecciona características basadas en la correlación.

    1. Elimina características altamente correlacionadas entre sí (multicolinealidad).
    2. Elimina características con baja correlación con la variable objetivo.

    Args:
        df: DataFrame con datos codificados.
        target_col: Nombre de la columna objetivo.

    Returns:
        DataFrame con un conjunto reducido de características.
    """
    print("--- Iniciando selección de características por correlación ---")

    if target_col not in df.columns:
        print(
            f"ADVERTENCIA: La columna objetivo '{target_col}' no se encuentra. Omitiendo selección."
        )
        return df

    # Asegurarse de que solo se usan columnas numéricas
    df_numeric = df.select_dtypes(include=["number"])

    # 1. Eliminar multicolinealidad
    corr_matrix = df_numeric.corr().abs()
    upper_tri = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

    to_drop_multi = [
        column for column in upper_tri.columns if any(upper_tri[column] > 0.90)
    ]

    df_reduced = df.drop(columns=to_drop_multi)

    print(
        f"Se eliminaron {len(to_drop_multi)} columnas por alta multicolinealidad (> 0.90)."
    )

    # 2. Eliminar características con baja correlación con el target
    correlations_with_target = (
        df_reduced.select_dtypes(include=["number"]).corr()[target_col].abs()
    )

    # Mantener solo las que superan el umbral, y siempre mantener el target
    cols_to_keep = correlations_with_target[
        correlations_with_target >= 0.05
    ].index.tolist()
    if target_col not in cols_to_keep:
        cols_to_keep.append(target_col)

    # Identificar columnas no numéricas para mantenerlas siempre
    non_numeric_cols = df.select_dtypes(exclude=["number"]).columns.tolist()
    final_cols_to_keep = list(set(cols_to_keep + non_numeric_cols))

    to_drop_low_corr = [
        col
        for col in df_reduced.select_dtypes(include=["number"]).columns
        if col not in final_cols_to_keep
    ]

    df_final = df_reduced.drop(columns=to_drop_low_corr)

    print(
        f"Se eliminaron {len(to_drop_low_corr)} columnas numéricas por baja correlación (< 0.05) con '{target_col}'."
    )
    print(
        f"El número de columnas se redujo de {len(df.columns)} a {len(df_final.columns)}."
    )
    print("--- Fin de la selección de características ---")

    return df_final


def escalar_variables_numericas(
    df: pd.DataFrame, target_col: str = "ConvertedCompYearly"
) -> pd.DataFrame:
    """
    Estandariza las columnas numéricas de un DataFrame usando StandardScaler,
    excluyendo la columna objetivo.

    Args:
        df: DataFrame a escalar.
        target_col: Nombre de la columna objetivo a excluir del escalado.

    Returns:
        DataFrame con las columnas numéricas escaladas.
    """
    print("--- Iniciando estandarización de variables numéricas ---")

    # Identificar columnas numéricas, excluyendo el target
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if target_col in numeric_cols:
        numeric_cols.remove(target_col)

    if not numeric_cols:
        print("No se encontraron columnas numéricas para escalar.")
        return df

    print(f"Se escalarán {len(numeric_cols)} columnas numéricas.")

    scaler = StandardScaler()
    df_scaled = df.copy()
    df_scaled[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    print("--- Fin de la estandarización ---")

    return df_scaled
