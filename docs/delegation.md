# Delegation Harness — Arnés de Delegación

> No todas las tareas merecen un subagente. Invocar un subagente tiene costo:
> preparar prompt, enviar, esperar que explore, que implemente, que reporte.
> Para cambios triviales, el líder hace inline.

## Principio

Delegar es una **decisión de arquitectura**, no el comportamiento por defecto.
El líder evalúa la tarea y decide según tres niveles:

| Nivel | Costo | Acción |
|-------|-------|--------|
| 🟢 Inline | ~2s | Cambio directo del líder |
| 🟡 Delegar | ~30-120s | Subagente especializado |
| 🔴 Dividir | ~2-5min | Líder divide + múltiples subagentes |

## Matriz de decisión

```
¿La tarea cambia 1-2 archivos?
├── No → Delegar o Dividir
└── Sí
    ├── ¿Agrega lógica nueva (Python/C/LaTeX)?
    │   ├── Sí → Delegar
    │   └── No
    │       ├── ¿Requiere investigación?
    │       │   ├── Sí → Delegar (explorer primero)
    │       │   └── No → ✅ Inline
    │       └──
    └──
```

## Operaciones inline permitidas

| Operación | Ejemplo |
|-----------|---------|
| Cambiar fecha | `"due": "2026-06-10"` → `"due": "2026-06-12"` |
| Cambiar estado | `"status": "pending"` → `"status": "done"` |
| Corregir typo | Texto en markdown |
| Agregar entrada en tabla | Nueva fila en `semestres/2026-1.md` |
| Actualizar docs factual | Sin análisis ni decisión de diseño |
| Renombrar archivo | Simple `mv` |

## Operaciones que siempre delegan

| Operación | Subagente |
|-----------|-----------|
| Implementar código Python | implementer |
| Escribir informe LaTeX | implementer |
| Resolver ejercicios | implementer (con explorer previo) |
| Investigar tema | explorer |
| Refactorizar | explorer → implementer → reviewer |
| Revisar calidad | reviewer |

## Auto-regulación del líder

Si el líder empieza un inline y descubre complejidad inesperada:
1. Descarta cambios inline
2. Delega al subagente correspondiente
3. Anota en progress/current.md el escalamiento

### Ciclo de vida por tipo de feature

**Informes y prelaboratorios:**
\[
\text{pending} \rightarrow \text{in\_progress} \rightarrow \text{done}
\]

**Tareas y parciales:**
\[
\text{pending} \rightarrow \text{in\_progress} \rightarrow \text{awaiting\_review} \xrightarrow{\text{aprobación del usuario}} \text{done}
\]

Las tareas requieren comparación con el original hecho a mano. Los parciales
requieren visto bueno del usuario. Los agentes nunca pasan estos tipos a
`done` directamente.
