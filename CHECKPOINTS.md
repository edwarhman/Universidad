# CHECKPOINTS — Evaluación del estado final

> No se evalúa el camino, se evalúa el destino. Estos checkpoints son objetivos
> para que un revisor (humano o IA) decida si el proyecto está sano.

## C1 — El arnés está completo

- [ ] Existen los 4 archivos base: `AGENTS.md`, `init.sh`, `CHECKPOINTS.md`,
      `progress/current.md`.
- [ ] Existen los 3 docs: `docs/architecture.md`, `docs/conventions.md`,
      `docs/verification.md`.
- [ ] `./init.sh` termina con exit code 0.

## C2 — El estado es coherente

- [ ] Como mucho una feature `in_progress` en cada `feature_list.json`.
- [ ] Toda feature `done` tiene verificación asociada que pasa.
- [ ] `progress/current.md` está vacío o describe la sesión activa (sin basura
      de sesiones anteriores).

## C3 — El código respeta la arquitectura

- [ ] No hay archivos fuera de lugar (código en `docs/`, documentación en
      `src/`, etc.).
- [ ] No hay `print()` de debug, TODOs sin contexto ni archivos temporales.
- [ ] Las convenciones del lenguaje se respetan (ver `docs/conventions.md`).

## C4 — La verificación es real

- [ ] Los tests de Python pasan con `pytest` (donde aplica).
- [ ] Los documentos LaTeX compilan sin errores (donde aplica).
- [ ] Los proyectos C/ESP-IDF compilan con `pio run` (donde aplica).

## C5 — La sesión se cerró bien

- [ ] `progress/history.md` tiene una entrada por la última sesión.
- [ ] No hay archivos sin trackear sospechosos (`*.tmp`, `__pycache__`,
      artefactos LaTeX fuera del `.gitignore`).
- [ ] La última feature trabajada está reflejada en su estado correcto en
      `feature_list.json`.

---

**Cómo usar:** un agente revisor (`.opencode/agents/reviewer.md`) recorre cada
checkbox, marca `[x]` o `[ ]`, y rechaza el cierre si quedan boxes vacíos.
