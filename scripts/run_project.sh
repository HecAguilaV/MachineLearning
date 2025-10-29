
# Script adaptado para Windows PowerShell
# Ejecutar este script desde PowerShell: powershell -ExecutionPolicy Bypass -File .\scripts\run_project.ps1

$ErrorActionPreference = "Stop"

# Configuración
$VENV_DIR = ".venv"
$JUPYTER_PORT = 8888
$KEDRO_VIZ_PORT = 4141
$HOST = "127.0.0.1"

function Log($msg) { Write-Host "[run] $msg" }
function Err($msg) { Write-Host "[run][error] $msg" -ForegroundColor Red }

# 1) Crear entorno virtual si no existe
if (-Not (Test-Path $VENV_DIR)) {
    Log "Creando entorno virtual en $VENV_DIR"
    py -3.11 -m venv $VENV_DIR
}

# 2) Activar entorno virtual
$env:VIRTUAL_ENV = (Resolve-Path $VENV_DIR).Path
$activateScript = Join-Path $VENV_DIR "Scripts\Activate.ps1"
if (Test-Path $activateScript) {
    Log "Activando entorno virtual"
    . $activateScript
} else {
    Err "No se encontró el script de activación: $activateScript"
    exit 1
}

# 3) Instalar dependencias
if (Test-Path "requirements.txt") {
    Log "Instalando dependencias desde requirements.txt"
    pip install --upgrade pip
    pip install -r requirements.txt
} else {
    Log "requirements.txt no encontrado; instalando dependencias mínimas"
    pip install kedro==1.0.0 pandas numpy pyarrow
}

# 4) Ejecutar pipeline Kedro
Log "Ejecutando pipeline completo: kedro run"
try {
    kedro run
} catch {
    Err "Fallo en kedro run (continuo con los siguientes pasos)"
}

# 5) Levantar Kedro Viz
Log "Levantando Kedro Viz en http://localhost:$KEDRO_VIZ_PORT"
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "-m kedro viz --no-browser --host=$HOST --port=$KEDRO_VIZ_PORT"

# 6) Iniciar Jupyter Notebook
Log "Iniciando Jupyter Notebook en http://localhost:$JUPYTER_PORT"
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "-m kedro jupyter notebook --NotebookApp.token='' --NotebookApp.password='' --port=$JUPYTER_PORT --ip=$HOST"

# 7) Abrir URLs en el navegador por defecto
Start-Sleep -Seconds 5
$vizUrl = "http://localhost:$KEDRO_VIZ_PORT"
$nbUrl = "http://localhost:$JUPYTER_PORT/notebooks/01_exploratory_analysis.ipynb"
Log "Abriendo Kedro Viz: $vizUrl"
Start-Process $vizUrl
Log "Abriendo Notebook: $nbUrl"
Start-Process $nbUrl

Log "Listo. Servicios activos:"
Log "- Kedro Viz:     $vizUrl"
Log "- Jupyter:       http://localhost:$JUPYTER_PORT"
Log "Para detenerlos: cierra las ventanas de PowerShell o finaliza los procesos desde el Administrador de tareas."
