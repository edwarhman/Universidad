#!/usr/bin/env bash
# init.sh — Verificación e inicialización del entorno
#
# Lo ejecuta el agente al COMENZAR una sesión y antes de declarar cualquier
# tarea como `done`. Si falla, la sesión no debe avanzar.

set -u
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

ok()    { printf "${GREEN}[OK]${NC}    %s\n" "$1"; }
warn()  { printf "${YELLOW}[WARN]${NC}  %s\n" "$1"; }
fail()  { printf "${RED}[FAIL]${NC}  %s\n" "$1"; }

EXIT_CODE=0

echo "── 1. Verificando entorno base ────────────────────────"

# Bash
if ! command -v bash >/dev/null 2>&1; then
  fail "bash no está instalado"
  exit 1
fi
ok "bash disponible"

# Python
if ! command -v python3 >/dev/null 2>&1; then
  fail "python3 no está instalado"
  exit 1
fi
ok "python3 -> $(python3 --version)"

# Git
if ! command -v git >/dev/null 2>&1; then
  fail "git no está instalado"
  exit 1
fi
ok "git -> $(git --version 2>&1 | head -1)"

echo ""
echo "── 2. Verificando archivos base del arnés ──────────────"

BASE_FILES=(
  "AGENTS.md"
  "CHECKPOINTS.md"
  "docs/architecture.md"
  "docs/conventions.md"
  "docs/verification.md"
  "progress/current.md"
  "progress/history.md"
  "opencode.json"
)
for f in "${BASE_FILES[@]}"; do
  if [ ! -f "$f" ]; then
    fail "Falta archivo base: $f"
    EXIT_CODE=1
  else
    ok "Existe $f"
  fi
done

echo ""
echo "── 3. Verificando herramientas por lenguaje ────────────"

# LaTeX
if command -v pdflatex >/dev/null 2>&1; then
  ok "pdflatex disponible"
else
  warn "pdflatex no instalado (no podrás compilar LaTeX)"
fi

if command -v biber >/dev/null 2>&1; then
  ok "biber disponible"
else
  warn "biber no instalado (no podrás compilar bibliografía LaTeX)"
fi

# PlatformIO
if command -v pio >/dev/null 2>&1; then
  ok "PlatformIO disponible -> $(pio --version 2>&1 | head -1)"
else
  warn "pio no instalado (no podrás compilar proyectos ESP32)"
fi

# Flake8
if command -v flake8 >/dev/null 2>&1; then
  ok "flake8 disponible -> $(flake8 --version 2>&1 | head -1)"
else
  warn "flake8 no instalado (no podrás lintear Python)"
fi

echo ""
echo "── 4. Validando feature_list.json de cada proyecto ─────"

python3 - <<'PY'
import json, os, sys, glob

proyectos_con_feature_list = []
for f in glob.glob("*/feature_list.json"):
    proyecto = f.split("/")[0]
    try:
        data = json.load(open(f))
        valid = {"pending", "in_progress", "awaiting_review", "done", "blocked"}
        in_progress = [feat for feat in data.get("features", []) if feat.get("status") == "in_progress"]
        if len(in_progress) > 1:
            print(f"[FAIL]  {proyecto}: {len(in_progress)} features en in_progress (máximo 1)")
            sys.exit(1)
        for feat in data.get("features", []):
            if feat.get("status") not in valid:
                print(f"[FAIL]  {proyecto}: estado inválido en feature {feat.get('id')}: {feat.get('status')}")
                sys.exit(1)
        print(f"[OK]    {proyecto}/feature_list.json válido ({len(data.get('features', []))} features)")
        proyectos_con_feature_list.append(proyecto)
    except Exception as e:
        print(f"[FAIL]  {proyecto}/feature_list.json inválido: {e}")
        sys.exit(1)

if not proyectos_con_feature_list:
    print("[WARN]  No hay ningún feature_list.json en los proyectos")
PY

PY_EXIT=$?
if [ $PY_EXIT -ne 0 ]; then EXIT_CODE=1; fi

echo ""
echo "── 5. Ejecutando tests de proyectos Python ─────────────"

# Test calculo-num-rico if it exists
if [ -d "calculo-num-rico" ] && [ -f "calculo-num-rico/requirements.txt" ]; then
  echo "   → calculo-num-rico..."
  (cd calculo-num-rico && pip install -q -r requirements.txt 2>/dev/null && python -m pytest -q 2>&1 | tail -3)
  if [ $? -eq 0 ]; then
    ok "calculo-num-rico: tests pasan"
  else
    warn "calculo-num-rico: tests no ejecutados o fallan (revisar manualmente)"
  fi
fi

echo ""
echo "── 6. Resumen ──────────────────────────────────────────"

if [ $EXIT_CODE -eq 0 ]; then
  ok "Entorno listo. Puedes empezar a trabajar."
else
  fail "Entorno NO está listo. Resuelve los errores antes de avanzar."
fi

exit $EXIT_CODE
