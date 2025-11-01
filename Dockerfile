# Dockerfile para extender la imagen de Airflow con las dependencias de Kedro

# Usa la imagen oficial de Airflow como base
FROM apache/airflow:3.1.1

# Instala dependencias del sistema para lightgbm
USER root
RUN apt-get update && apt-get install -y libgomp1
USER airflow

# Establece el directorio de trabajo
WORKDIR /opt/airflow

# Copia el archivo requirements.txt de tu proyecto Kedro
COPY requirements.txt .

# Instala las dependencias de Kedro
# Usa --no-cache-dir para ahorrar espacio en la imagen
# Usa --constraint para asegurar la compatibilidad con las versiones de Python de Airflow
RUN pip install --no-cache-dir -r requirements.txt \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.1.1/constraints-3.10.txt"

# Copia el proyecto Kedro al contenedor
# Esto es necesario para que los DAGs puedan ejecutar 'kedro run'
# El contenido del proyecto estará disponible en /opt/airflow/kedro_project
COPY . /opt/airflow/kedro_project

# Establece la variable de entorno para la ruta del proyecto Kedro
ENV KEDRO_PROJECT_PATH=/opt/airflow/kedro_project

# Puedes añadir más configuraciones si es necesario
