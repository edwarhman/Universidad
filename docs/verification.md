# Verificación — Cómo demostrar que el trabajo funciona

> Regla de oro: **el agente no dice "funciona", lo demuestra**.
> Toda feature termina con evidencia ejecutable, no con afirmaciones.

## Niveles de verificación

### Nivel 1 — Tests automáticos (obligatorio para Python)

```bash
pytest                           # calculo-num-rico, informes-electronica
python -m pytest                 # desde cualquier proyecto con pytest
```

### Nivel 2 — Linting (obligatorio para Python)

```bash
flake8                           # calculo-num-rico
```

### Nivel 3 — Compilación (obligatorio para LaTeX y C)

```bash
# LaTeX
pdflatex main.tex && biber main && pdflatex main.tex && pdflatex main.tex

# ESP-IDF / PlatformIO
pio run                          # compilar
```

### Nivel 4 — Smoke test (opcional, recomendado)

Ejecutar un flujo end-to-end manual para verificar que el cambio funciona
en contexto real. Por ejemplo:

- Para un script Python: `python script.py --test` con entrada conocida.
- Para un comando CLI: invocar con argumentos de prueba y verificar salida.
- Para un informe LaTeX: compilar y revisar que no hay warnings.

### Nivel 5 — Verificación final (obligatorio antes de cerrar)

```bash
./init.sh                        # debe terminar con [OK] Entorno listo
```

Si `init.sh` está rojo, **no** marcar nada como `done`. Anotar el bloqueo
en `progress/current.md` y en `feature_list.json`.

## Proyecto específico

| Proyecto | Verificación |
|----------|-------------|
| `calculo-num-rico/` | `pytest`, `flake8` |
| `informes-electronica/` | `pytest` (si hay tests), compilar LaTeX |
| `LIE II/` | `python practica_amplitud_y_fase.py --test` (o pytest) |
| `comunicaciones/` | Compilar LaTeX |
| `sistemas-de-control-II/` | `pio run` + compilar LaTeX |
| `teoria-electromagnetica/` | Compilar LaTeX |
| `servicio/` | Compilar LaTeX |

## Anti-patrones (no hacer)

- ❌ "He añadido el comando, debería funcionar." → falta test ejecutable.
- ❌ Test que solo verifica que la función no lanza excepción. → debe
  comprobar el resultado concreto.
- ❌ `mock` del filesystem cuando se puede usar `tmp_path`.
- ❌ Marcar feature como `done` sin pasar `./init.sh`.
- ❌ Ignorar warnings de compilación LaTeX (pueden indicar problemas).

## Compilación LaTeX en WSL

Si usas MiKTeX en WSL, los agentes deben filtrar las rutas `/mnt/c/` del PATH
para evitar errores de permiso en `WindowsApps/`. Usa el script `scripts/compile-latex.sh`:

```bash
./scripts/compile-latex.sh main.tex -interaction=nonstopmode
```

Esto equivale a:
```bash
PATH=$(echo "$PATH" | tr ':' '\n' | grep -v '/mnt/c/' | tr '\n' ':') pdflatex main.tex
```

### Criterios de cierre por tipo de actividad

| Tipo | Criterio | Estado final |
|------|----------|-------------|
| `informe` | Compila LaTeX, cálculos correctos, estructura completa | `done` |
| `prelaboratorio` | Compila LaTeX, cálculos correctos | `done` |
| `tarea` | Cálculos validados, PDF/material generado | `awaiting_review` |
| `parcial` | Guía de estudio, simulacro, fecha registrada | `awaiting_review` |

Para tareas y parciales, el usuario debe dar el visto bueno después de
comparar con su trabajo original para pasar de `awaiting_review` a `done`.
