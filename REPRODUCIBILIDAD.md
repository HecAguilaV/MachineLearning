# Checklist de Reproducibilidad del Proyecto

Esta guía te permitirá clonar y configurar el entorno del proyecto en un nuevo equipo para continuar el trabajo desde el punto actual.

## 1. Prerrequisitos

Asegúrate de tener instalado lo siguiente en el nuevo equipo:
- [ ] **Git:** Para control de versiones.
- [ ] **Python:** Versión 3.10 o superior. Asegúrate de que esté añadido al PATH.
- [ ] **Tu editor de código preferido** (ej. Visual Studio Code).

## 2. Pasos de Configuración

1.  **Clonar el Repositorio:**
    Abre una terminal y clona el repositorio. (Deberás subir tus cambios a un repositorio remoto como GitHub primero).
    ```sh
    git clone <URL_DEL_REPOSITORIO_GIT>
    cd ML_Analisis_Ecosistema_Dev
    ```

2.  **Crear y Activar el Entorno Virtual:**
    Es crucial para aislar las dependencias del proyecto.
    ```sh
    # Crear el entorno virtual
    py -m venv .venv

    # Activar el entorno (Windows)
    .\.venv\Scripts\activate
    ```

3.  **Instalar Dependencias:**
    Instala todas las librerías necesarias para el proyecto.
    ```sh
    pip install -r requirements.txt
    ```

4.  **Instalar el Paquete del Proyecto:**
    Esto hace que tu proyecto Kedro sea un paquete instalable y que los comandos `kedro` funcionen correctamente.
    ```sh
    pip install -e .
    ```

## 3. Verificación

Para asegurarte de que todo está configurado correctamente, ejecuta el pipeline principal. Debería completarse sin errores.

```sh
# En Windows, para evitar errores de codificación en la consola
set PYTHONIOENCODING=utf-8

# Ejecutar el pipeline
kedro run
```

Si el comando `kedro run` se ejecuta y completa todos los nodos exitosamente, ¡has replicado el entorno y estás listo para continuar!
