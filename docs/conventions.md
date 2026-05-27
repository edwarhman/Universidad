# Convenciones de código

> Homogeneidad extrema. La IA predice mejor cuando el repositorio se parece
> a sí mismo en todas partes.

## Python

- **Versión:** Python 3.9+ (3.12 para LIE II).
- **Formato:** PEP 8. Líneas máximo 100 caracteres.
- **Imports:** stdlib primero, luego terceros, luego locales. Una línea por módulo.
- **Strings:** comillas dobles `"..."` siempre. Comillas simples solo para
  escapar comillas dobles dentro.
- **f-strings** para interpolación. Nada de `.format()` ni `%`.
- **Nombres:**
  - Clases: `PascalCase` (`SistemaLineal`)
  - Funciones: `CamelCase` (`resolverEcuacionBiseccion`)
  - Variables: `snake_case`
  - Constantes: `UPPER_SNAKE`
- **Tests:** Un archivo de test por módulo, pytest. Usar `tmp_path` o
  `TemporaryDirectory`, no mocks del filesystem.
- **Errores:** Excepciones nombradas para el dominio, no `return None`.
- **Comentarios:** Solo para explicar *por qués* no obvios. Los nombres deben
  hacer el resto.

## C (ESP-IDF / PlatformIO)

- **Nombres:** CamelCase español (`ControlMovimientoConfig`, `maquinaDeEstados`).
- **Estilo:** ESP-IDF style guide. Incluir headers completos, no forward-declares
  innecesarios.
- **Estructura:** Librerías modulares en `lib/`, ejemplos separados.
- **Tests:** `pio test` cuando existan.

## LaTeX

- **Estructura de informes:** portada → resumen → introducción → marco teórico
  → instrumentos → metodología → resultados → cálculos → conclusiones → anexos.
- **Estilo:** Usar `informes-electronica/utils/laboratorio.sty` para informes de
  Electrónica. Para el resto, estilo minimalista sin paquetes innecesarios.
- **Compilación:** `pdflatex + biber + pdflatex + pdflatex`.
- **Archivos:** `main.tex` como punto de entrada, secciones en archivos
  separados. Evitar un solo archivo monolítico.
- **Figuras:** En subdirectorio `Imagenes/` o `img/`. Solo PNG, JPG, PDF.

## Git

- **Commits:** Mensajes en español, presente imperativo.
- **Submódulos:** `micromouse/` es submódulo externo. No tocar sin preguntar.
- **Archivos generados:** No commitear artefactos LaTeX (`*.aux`, `*.log`,
  `*.pdf`), ni de PlatformIO (`.pio/`, `build/`), ni entornos virtuales
  (`.venv/`).
- **Una feature por commit.** No mezclar cambios no relacionados.
