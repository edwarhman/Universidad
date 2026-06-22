# Implementación de Solución para Desbordamiento Horizontal en Tabla de Mediciones

Se ha resuelto el problema de desbordamiento horizontal en `tablas.tex` para el Prelaboratorio 3 de Máquinas Eléctricas I aplicando los siguientes cambios:

1. **Preámbulo (`main.tex`)**:
   - Se añadió el paquete `array`.
   - Se definió el tipo de columna personalizado centrado y auto-ajustable:
     ```latex
     \newcolumntype{Y}{>{\centering\arraybackslash}X}
     ```

2. **Tabla de Mediciones (`tablas.tex`)**:
   - Se modificó la definición de columnas del entorno `tabularx`:
     ```latex
     \begin{tabularx}{\textwidth}{X c Y Y c}
     ```
   - Se agregaron cortes suaves `\allowbreak` en las cabeceras `Valor Medido/\allowbreak Experimental` y `Valor Nominal/\allowbreak Catálogo` para asegurar un ajuste correcto en múltiples líneas sin generar desbordamientos.

3. **Compilación y Verificación**:
   - El documento fue compilado exitosamente con `pdflatex`.
   - Se ejecutó `./init.sh` constatando que todo el entorno y configuración del proyecto están correctos.
