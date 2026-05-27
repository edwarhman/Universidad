# AGENTS.md — Universidad

Repo personal de Emerson Warhman — Ingeniería Eléctrica, UCV.

## Estructura general

```
calculo-num-rico/           # Python — métodos numéricos (numpy, sympy, pytest)
comunicaciones/             # LaTeX — informes Comunicaciones I
informes-electronica/       # LaTeX + Python — informes de laboratorio de Electrónica
LIE II/                     # Python — Laboratorio de Ing. Eléctrica II
micromouse/                 # C (ESP-IDF, PlatformIO) — submodulo git
programas/                  # PDFs del pensum de Ingeniería Eléctrica UCV
servicio/                   # LaTeX — plantilla Servicio Comunitario
sistemas-de-control-II/     # C (ESP-IDF, PlatformIO) + Python + LaTeX
teoria-electromagnetica/   # LaTeX — formularios
```

## Comandos importantes

### Python (`calculo-num-rico/`, `informes-electronica/`)
```bash
pip install -r requirements.txt   # instalar dependencias
pytest                            # correr tests (calculo-num-rico)
flake8                            # lintear (calculo-num-rico)
```

### PlatformIO / ESP32 (`micromouse`, `control-pendulo`)
```bash
pio run                           # compilar
pio upload                        # flashear
pio device monitor                # serial a 115200 baud
pio test                          # correr tests embebidos
```

### LaTeX (todos los informes)
```bash
pdflatex main.tex && biber main && pdflatex main.tex && pdflatex main.tex
```

Clonar con submódulos:
```bash
git clone --recurse-submodules <url>
```

## Workflow obligatorio (gates de verificación)

Seguir este orden en cada sesión:

| # | Acción |
|---|--------|
| 1 | Leer `PICKUP.md` para saber dónde se quedó la sesión anterior |
| 2 | Leer `planning/architecture.md` si necesitas contexto del repo |
| 3 | Planificar los cambios antes de escribir código |
| 4 | Ejecutar lint/typecheck después de cada cambio |
| 5 | Al proponer el siguiente paso, detallar en qué consiste |
| 6 | Actualizar `PICKUP.md` al final de la sesión |

NO saltarse pasos. Si un gate de verificación falla, corregir antes de continuar.

## Boundaries

| Nivel | Incluye |
|---|---|
| **Siempre permitido** | `calculo-num-rico/`, `informes-electronica/`, `comunicaciones/`, `LIE II/`, `sistemas-de-control-II/`, `teoria-electromagnetica/`, `servicio/`, `planning/`, `opencode.json`, `AGENTS.md`, `PICKUP.md` |
| **Preguntar antes** | Modificar `AGENTS.md`, renombrar directorios, tocar `micromouse/` (submódulo externo) |
| **Nunca modificar** | `.env`, `.venv/`, `node_modules/`, `.pio/`, `build/`, `dist/`, PDFs commiteados, archivos generados por herramientas |

## Convenciones

- **Todo en español**: READMEs, comentarios, nombres de variables, documentos.
- Python: mezcla de inglés/español en identificadores (ej. `resolverEcuacionBiseccion`, `SistemaLineal`). C: CamelCase español (`ControlMovimientoConfig`, `maquinaDeEstados`).
- LaTeX: estructura consistente — portada, resumen, introducción, marco teórico, instrumentos, metodología, resultados, cálculos, conclusiones, anexos. Usa `laboratorio.sty` compartido en `informes-electronica/utils/`.
- El directorio `programas/` contiene ~85 PDFs del pensum (fuente de verdad sobre contenidos de materias).
- `micromouse` es un submodulo → `git submodule update --init --recursive` después de clonar.
- No hay CI/CD, ni Makefiles, ni top-level README.
- Varios `.gitignore` excluyen artefactos LaTeX (`*.aux`, `*.log`, `*.pdf`) y de PlatformIO (`.pio/`, `build/`).

## No obvio (decisiones que parecen bugs pero son intencionales)

- `calculo-num-rico/` se originó en Google Colab — algunas secuencias de celdas asumen ejecución interactiva, no ejecución headless.
- `informe-{2,3}/calculos/resultados.py` son casi idénticos y dependen de un módulo `incertidumbres` que **no está commiteado** en el repo.
- Python 3.12 requerido en `LIE II/` (`.python-version`), y para `pid_tuner.py` (tkinter + pyserial) en `control-pendulo`.
- `control-pendulo/` es un proyecto PlatformIO independiente (no un submódulo), y sus ejemplos (`01_*` a `05_*`) se compilan por separado desde cada directorio.
- El cron de `check-group-streaks` en game-habits **no aplica aquí** — este repo no tiene Edge Functions ni Supabase.

## Archivos de planificación

| Archivo | Contenido |
|---|---|
| `planning/architecture.md` | Diagrama Mermaid del repo, tabla de estilos de código |
| `PICKUP.md` | Estado actual de la sesión y próximos pasos |

## Específico por proyecto

### `control-pendulo/` (sistemas-de-control-II)
- Librerías modulares reutilizables para control de movimiento en ESP32.
- `pid_tuner.py`: GUI Tkinter para sintonización PID en tiempo real sobre UART.
- Comandos serie: `SETKP <val>`, `SETKI <val>`, `SETKD <val>` — puerto por defecto `COM8`.
- Ejemplo principal: `04_Inverted_Pendulum_Project/` integra encoder, stepper, LCD, PID.

### `micromouse/`
- Robot laberinto ESP32: sensores IR + HC-SR04, encoders, PWM motores DC, máquina de estados.
- Más monolítico que `control-pendulo` — todo en `src/`.
- Variante de placa: `upesy_wroom` (usa `sdkconfig.upesy_wroom`).
