"""Configuración de pytest para incluir `src` en el PYTHONPATH durante los tests.

Esto evita errores de importación cuando el paquete local aún no está instalado
o cuando pytest no está ejecutándose con el entorno esperado.
"""

import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_DIR = os.path.join(ROOT_DIR, "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)
