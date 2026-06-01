# AGENTS.md — Mapa de navegación para agentes

> Este archivo es el **punto de entrada** para cualquier agente que trabaje en
> este repositorio. NO es una biblia de reglas: es un **mapa**. Lee solo lo
> que necesites cuando lo necesites (divulgación progresiva).

---

## 1. Antes de empezar (obligatorio)

1. Lee `progress/current.md` para saber dónde quedó la sesión anterior.
2. Ejecuta `./init.sh` y verifica que termina sin errores. Si falla, **para**
   y resuelve el entorno antes de tocar código.
3. Identifica en qué proyecto vas a trabajar. Lee su `feature_list.json` y
   elige **una** tarea con estado `pending`.
4. No trabajes en más de una feature a la vez.

## 2. Mapa del repositorio

| Archivo / carpeta | Qué contiene | Cuándo leerlo |
|---|---|---|
| `docs/architecture.md` | Estructura del repo, lenguajes, principios | Antes de implementar |
| `docs/conventions.md` | Reglas de estilo, nombres, estructura por lenguaje | Antes de escribir código |
| `docs/verification.md` | Cómo demostrar que el trabajo funciona | Antes de declarar `done` |
| `CHECKPOINTS.md` | Criterios objetivos de "estado final correcto" | Para auto-evaluarse |
| `feature_list.json` (en cada proyecto) | Tareas con estado machine-readable | Siempre, al empezar |
| `progress/current.md` | Sesión activa | Siempre |
| `progress/history.md` | Bitácora de sesiones anteriores | Contexto histórico |
| `.opencode/agents/` | Definiciones de subagentes (líder, implementador, revisor) | Si orquestas trabajo |
| `opencode.json` | Configuración de opencode (hooks, permisos) | No tocar manualmente |

## 3. Proyectos del repositorio

| Proyecto | Lenguaje | Verificación |
|---|---|---|
| `calculo-num-rico/` | Python | `pytest`, `flake8` |
| `comunicaciones/` | LaTeX | Compilar `main.tex` |
| `informes-electronica/` | LaTeX + Python | `pytest`, compilar LaTeX |
| `LIE II/` | Python (3.12) | `python` scripts |
| `sistemas-de-control-II/` | C (ESP-IDF) + Python + LaTeX | `pio run`, compilar LaTeX |
| `teoria-electromagnetica/` | LaTeX | Compilar `.tex` |
| `servicio/` | LaTeX | Compilar `.latex` |
| `micromouse/` (submódulo) | C (ESP-IDF) | `pio run` — preguntar antes de tocar |

## 4. Reglas duras

- **Una sola feature a la vez.** No mezcles cambios de varias tareas.
- **No declares `done` sin verificación.** Ejecuta `./init.sh` primero.
- **Escribe tus resultados en disco.** Usa `progress/` del proyecto. Tu
  respuesta en chat debe ser solo una referencia al archivo.
- **Si te bloqueas**, documenta en `progress/current.md` con estado
  `blocked` y termina la sesión. No inventes workarounds.
- **Tareas y parciales nunca pasan a `done` sin aprobación del usuario.** 
  El agente solo puede dejarlos en `awaiting_review`.

## 5. Cierre de sesión

1. Ejecuta `./init.sh` — todo verde.
2. Si la feature está acabada: marca `status: "done"` en `feature_list.json`.
3. Mueve el resumen de `progress/current.md` al final de `progress/history.md`.
4. Vacía `progress/current.md` dejando solo la plantilla.
5. No dejes archivos temporales, prints de debug ni TODOs.

## 6. Preferencias del usuario

- **Abrir archivos**: cuando el usuario pida abrir un archivo, usa
  `nohup xdg-open "<ruta_absoluta>" &>/dev/null &` para lanzarlo con la
  aplicación predeterminada del sistema en segundo plano (sin bloquear el chat).
