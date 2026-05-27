# Arquitectura del Repositorio

> Define qué significa "hacer un buen trabajo". Los agentes revisores evalúan
> código contra este archivo. Si no está aquí, no es un requisito.

## Estructura general

```
universidad/
├── calculo-num-rico/           # Python — métodos numéricos (numpy, sympy, pytest)
├── comunicaciones/             # LaTeX — informes Comunicaciones I
├── informes-electronica/       # LaTeX + Python — informes de laboratorio de Electrónica
├── LIE II/                     # Python — Laboratorio de Ing. Eléctrica II
├── micromouse/                 # C (ESP-IDF, PlatformIO) — submódulo git
├── programas/                  # PDFs del pensum de Ingeniería Eléctrica UCV
├── servicio/                   # LaTeX — plantilla Servicio Comunitario
├── sistemas-de-control-II/     # C (ESP-IDF, PlatformIO) + Python + LaTeX
├── teoria-electromagnetica/    # LaTeX — formularios
├── docs/                       # Documentación del harness (arquitectura, convenciones, verificación)
├── progress/                   # Bitácora de sesiones global
├── .opencode/                  # Configuración de opencode (agentes, skills)
├── opencode.json               # Configuración principal de opencode
├── AGENTS.md                   # Mapa de navegación para agentes
├── CHECKPOINTS.md              # Criterios de "estado final correcto"
└── init.sh                     # Verificación ejecutable del entorno
```

## Lenguajes y build systems

| Lenguaje | Proyectos | Build / test |
|----------|-----------|--------------|
| Python | `calculo-num-rico/`, `informes-electronica/`, `LIE II/`, `sistemas-de-control-II/` | pytest, flake8 |
| C (ESP-IDF) | `micromouse/`, `sistemas-de-control-II/control-pendulo/` | PlatformIO (`pio run`) |
| LaTeX | `comunicaciones/`, `informes-electronica/`, `sistemas-de-control-II/`, `teoria-electromagnetica/`, `servicio/` | pdflatex + biber |

## Principios de diseño

1. **Una feature a la vez.** Cada `feature_list.json` por proyecto define el
   alcance. Nunca trabajar en dos features simultáneas.
2. **Estado en disco, no en chat.** `progress/` y `feature_list.json` son la
   fuente de verdad. Los agentes escriben resultados en archivos, no en chat.
3. **Verificación ejecutable.** `init.sh` corre tests reales. No confiar en lo
   que el agente "dice" que funciona.
4. **Sin dependencias innecesarias.** Cada proyecto usa solo lo que necesita.
   No introducir librerías sin documentar la razón.
5. **Todo en español.** READMEs, comentarios, nombres de variables, documentos.

## Principio de capas (aplica a proyectos Python)

```
CLI / interfaz  →  lógica de dominio  →  persistencia
     │                   │                     │
  cli.py            proyecto.py          storage.py
```

Para proyectos LaTeX: `portada → resumen → introducción → marco teórico →
instrumentos → metodología → resultados → cálculos → conclusiones → anexos`.

Para proyectos C/ESP-IDF: librerías modulares en `lib/`, ejemplos en
directorios `NN_Nombre_Demo/`, aplicación principal en `src/`.

## Proyectos y submódulos

- `micromouse/` es un submódulo → `git submodule update --init --recursive`
  después de clonar.
- `control-pendulo/` NO es submódulo, es un proyecto PlatformIO independiente
  dentro de `sistemas-de-control-II/`.
