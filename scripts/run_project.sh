#!/usr/bin/env bash
set -euo pipefail

# Configuración
PYTHON_VERSION_MIN="3.8"
VENV_DIR=".venv"
JUPYTER_PORT=8888
KEDRO_VIZ_PORT=4141
HOST=127.0.0.1

log() { echo "[run] $*"; }
err() { echo "[run][error] $*" >&2; }

# 0) Cargar variables de entorno si existe .env
if [ -f .env ]; then
  # shellcheck disable=SC2046
  export $(grep -v '^#' .env | xargs) || true
fi

# 1) Crear/activar entorno virtual
if [ ! -d "$VENV_DIR" ]; then
  log "Creando entorno virtual en $VENV_DIR"
  python3 -m venv "$VENV_DIR"
fi

# shellcheck disable=SC1091
# Asegurar que usamos el Python del venv de forma explícita al lanzar procesos
source "$VENV_DIR/bin/activate"
PY_BIN="$VENV_DIR/bin/python"
KEDRO_BIN="$VENV_DIR/bin/kedro"

# 2) Instalar dependencias
if [ -f "requirements.txt" ]; then
    log "Instalando dependencias desde requirements.txt"
    pip install --upgrade pip
    pip install -r requirements.txt
else
  log "requirements.txt no encontrado; instalando dependencias mínimas"
  pip install kedro==1.0.0 pandas numpy pyarrow
fi

# 3) Ejecutar pipeline
log "Ejecutando pipeline completo: kedro run"
"$PY_BIN" -m kedro run || err "Fallo en kedro run (continuo con los siguientes pasos)"

# 4) Levantar Kedro Viz (en background)
log "Levantando Kedro Viz en http://localhost:${KEDRO_VIZ_PORT}"
nohup "$PY_BIN" -m kedro viz --no-browser --host="$HOST" --port="$KEDRO_VIZ_PORT" >/tmp/kedro_viz.log 2>&1 &
VIZ_PID=$!
log "Kedro Viz PID: $VIZ_PID (logs: /tmp/kedro_viz.log)"

# 5) Iniciar Jupyter Notebook (en background)
log "Iniciando Jupyter Notebook en http://localhost:${JUPYTER_PORT}"
nohup "$PY_BIN" -m kedro jupyter notebook --NotebookApp.token='' --NotebookApp.password='' --port="$JUPYTER_PORT" --ip="$HOST" >/tmp/jupyter.log 2>&1 &
JUPYTER_PID=$!
log "Jupyter PID: $JUPYTER_PID (logs: /tmp/jupyter.log)"

# 6) Abrir URLs en el navegador por defecto (macOS/Linux)
VIZ_URL="http://localhost:${KEDRO_VIZ_PORT}"
NB_URL="http://localhost:${JUPYTER_PORT}/notebooks/notebooks/01_exploratory_analysis.ipynb"

open_url() {
  if command -v open >/dev/null 2>&1; then
    open "$1" || true
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$1" || true
  else
    log "Abrir manualmente: $1"
  fi
}

# Dar tiempo a que los servicios arranquen
sleep 5 || true
log "Abriendo Kedro Viz: $VIZ_URL"
open_url "$VIZ_URL"
log "Abriendo Notebook: $NB_URL"
open_url "$NB_URL"

log "Listo. Servicios activos:"
log "- Kedro Viz:     http://localhost:${KEDRO_VIZ_PORT}"
log "- Jupyter:       http://localhost:${JUPYTER_PORT}"
log "Para detenerlos: kill ${VIZ_PID} ${JUPYTER_PID} && deactivate"
