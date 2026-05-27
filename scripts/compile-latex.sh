#!/usr/bin/env bash
# compile-latex.sh — Compilar LaTeX en WSL filtrando rutas /mnt/c/
#
# En WSL con MiKTeX, las rutas /mnt/c/WINDOWS/... dan errores de permiso.
# Este script filtra esas rutas del PATH antes de compilar.

set -u

if [ $# -lt 1 ]; then
    echo "Uso: $0 <archivo.tex> [argumentos extra para pdflatex]"
    echo "Ej:  $0 main.tex"
    echo "     $0 main.tex -interaction=nonstopmode"
    exit 1
fi

TEX_FILE="$1"
shift

# Limpiar PATH de rutas /mnt/c/ que dan problemas con MiKTeX en WSL
CLEAN_PATH=$(echo "$PATH" | tr ':' '\n' | grep -v '/mnt/c/' | tr '\n' ':')
export PATH="$CLEAN_PATH"

echo "[compile-latex] PATH filtrado (sin /mnt/c/)"
echo "[compile-latex] Compilando: $TEX_FILE ..."

# Primera pasada
pdflatex "$@" "$TEX_FILE"
EXIT_CODE=$?

# Verificar si el PDF se generó
PDF_NAME="${TEX_FILE%.tex}.pdf"
if [ -f "$PDF_NAME" ]; then
    echo "[compile-latex] ✅ $PDF_NAME generado correctamente"
else
    echo "[compile-latex] ❌ No se generó $PDF_NAME"
fi

exit $EXIT_CODE
