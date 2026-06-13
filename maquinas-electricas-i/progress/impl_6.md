# Implementación Feature 6 — informe_2: Ciclo de Histéresis en Núcleos Ferromagnéticos Macizos y Laminados

Se agregaron las tablas de resultados experimentales correspondientes a los ensayos de núcleo macizo (Cuadro 1) y núcleo laminado (Cuadro 4) con formato `tabularx` centrado. Además, se añadió un cuadro detallado de parámetros de configuración y dimensiones físicas del núcleo ferromagnético.
También se agregaron las figuras experimentales al final de la sección de resultados.

## Detalles de los cambios

1. **`main.tex`**: Se definió el tipo de columna `Y` en el preámbulo para centrar automáticamente las celdas en las tablas que utilicen `tabularx`:
   ```latex
   \newcolumntype{Y}{>{\centering\arraybackslash}X}
   ```

2. **`texto/resultados.tex`**:
   - Se añadió un cuadro de parámetros de configuración experimental (`tab:parametros_config`).
   - Se agregaron las dos tablas de mediciones con los resultados experimentales.
   - Se agregaron las figuras experimentales:
     - **Ciclo de histéresis del núcleo macizo** (`fig:ciclo_histeresis_macizo`) como figura independiente.
     - **Ciclo de histéresis del núcleo laminado** (`fig:ciclo_histeresis_laminado`) como figura independiente.
     - **Formas de onda en núcleo macizo**: Voltaje (`fig:onda_voltaje_macizo`) y corriente (`fig:onda_corriente_macizo`) agrupadas en subfiguras.

3. **Verificación**:
   - Compilación exitosa del informe completo `main.tex` utilizando `pdflatex`.
   - Ejecución de `./init.sh` con salida completamente verde y válida.
