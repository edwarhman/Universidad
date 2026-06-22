# Implementación Feature 2 — prelab_2

Se han agregado dos nuevas tablas a `maquinas-electricas-i/entregables/prelaboratorios/prelab-2/tablas.tex` para registrar los datos del ciclo de histéresis del núcleo macizo (Tabla 3) y laminado (Tabla 4).

## Detalles de la implementación
- **Archivo modificado**: `maquinas-electricas-i/entregables/prelaboratorios/prelab-2/tablas.tex`
- **Tablas añadidas**:
  - `tab:histeresis_macizo` (Tabla 3: Ciclo de histéresis para el Núcleo Macizo)
  - `tab:histeresis_laminado` (Tabla 4: Ciclo de histéresis para el Núcleo Laminado)
- **Estructura**:
  - Columnas: `Tensión (V)`, `Corriente (A)`, `$B_{\text{max}}$ (Tesla)`, `$H_{\text{max}}$ (A/m)`, `Ancho del ciclo (T)`, `Área del ciclo (T $\cdot$ A/m)`.
  - Definición de columnas: `\begin{tabularx}{\textwidth}{| c | c | Y | Y | Y | Y |}`.
  - Filas: 9 filas correspondientes a niveles de tensión de 40 a 120 V de 10 en 10.
  - Formato: Rejilla completa con `|` y `\hline`, usando `\small` y especificador `[H]`.

## Verificación
- El documento LaTeX compila correctamente usando el PATH de WSL filtrado (`pdflatex main.tex`).
- El script `./init.sh` se ejecutó con éxito.
