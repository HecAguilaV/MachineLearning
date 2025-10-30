@echo off
REM Activar entorno virtual
call .venv\Scripts\activate.bat
REM Versionar todos los archivos nuevos en la carpeta de datos crudos
call dvc add data\01_raw\
git add .
git commit -m "Nuevos datos versionados en data/01_raw/"
call dvc push
REM (Opcional) Asegura acceso público a todo el bucket:
REM gsutil iam ch allUsers:objectViewer gs://ml-ecosistema-dev-2025
git push
