# Arquitectura del Repositorio

```mermaid
graph TB
    subgraph Universidad["universidad/"]
        direction TB
        ROOT["Raíz del repo"]
    end

    subgraph Python["Python"]
        CN["calculo-num-rico/<br/>Métodos numéricos<br/>numpy, sympy, pytest"]
        IE_py["informes-electronica/<br/>Análisis de datos<br/>matplotlib, pandas"]
        L2["LIE II/<br/>Python ≥3.12"]
        PID["sistemas-de-control-II/<br/>control-pendulo/pid_tuner.py<br/>Tkinter + pyserial"]
    end

    subgraph C_ESP32["C (ESP-IDF / PlatformIO)"]
        MM["micromouse/<br/>Robot laberinto<br/>Submódulo git"]
        CP["sistemas-de-control-II/<br/>control-pendulo/<br/>Librerías modulares"]
    end

    subgraph LaTeX["LaTeX"]
        CO["comunicaciones/<br/>Informes Comunicaciones I"]
        IE_tex["informes-electronica/<br/>Informes Electrónica<br/>utils/laboratorio.sty"]
        SC["servicio/<br/>Plantilla Servicio Comunitario"]
        TE["teoria-electromagnetica/<br/>Formularios"]
        SC2["sistemas-de-control-II/<br/>Informes varios"]
    end

    subgraph PDFs["PDFs"]
        PR["programas/<br/>~85 pensums"]
    end

    ROOT --> CN
    ROOT --> IE_py
    ROOT --> IE_tex
    ROOT --> L2
    ROOT --> PID
    ROOT --> MM
    ROOT --> CP
    ROOT --> CO
    ROOT --> SC
    ROOT --> TE
    ROOT --> SC2
    ROOT --> PR

    MM -.-> |Submódulo<br/>git@github.com:edwarhman/micromouse.git| GIT["GitHub"]
```

## Resumen

| Dimensión | Detalle |
|---|---|
| **Dueño** | Emerson Warhman — Escuela de Ing. Eléctrica, UCV |
| **Propósito** | Trabajos académicos: informes, código fuente, fórmulas, pensums |
| **Lenguajes** | Python (3.12), C (ESP-IDF), LaTeX |
| **Build systems** | PlatformIO (ESP32), pytest (Python), pdflatex/biber (LaTeX) |
| **CI/CD** | Ninguno |
| **Submódulos** | `micromouse` → `git@github.com:edwarhman/micromouse.git` |
| **Convención clave** | Todo en español: docs, comentarios, identificadores |

## Estilo de código por lenguaje

| Lenguaje | Convención |
|---|---|
| Python | CamelCase para clases (`SistemaLineal`), CamelCase para funciones (`resolverEcuacionBiseccion`) |
| C | CamelCase español (`ControlMovimientoConfig`, `maquinaDeEstados`), estilo ESP-IDF |
| LaTeX | `portada → resumen → introducción → marco teórico → instrumentos → metodología → resultados → cálculos → conclusiones → anexos` |
