# Implementación de Feature 1 — prelab_1

Se han modificado las tablas en `maquinas-electricas-i/entregables/prelaboratorios/prelab-1/tablas.tex` de la siguiente manera:

1. **Tablas 1 y 2**:
   - Se reordenaron las columnas para que después de "Instrumento empleado" vayan "Valor Medido" y "Error Absoluto ($\varepsilon$)".
   - Se eliminó completamente la columna "Valor Real".
   - Se adaptaron los anchos de columnas en tabularx a 6 columnas:
     `\begin{tabularx}{\textwidth}{| >{\hsize=1.5\hsize}Y | >{\hsize=1.3\hsize}Y | >{\hsize=0.8\hsize}Y | >{\hsize=0.8\hsize}Y | >{\hsize=0.8\hsize}Y | >{\hsize=0.8\hsize}Y |}`
   - Se actualizaron los separadores de celdas `&` (dejando 5 ampersands por fila) y los comandos `\cline{2-6}` para concordar con las 6 columnas resultantes.

2. **Tabla 3**:
   - Se modificó el cuerpo de la tabla para que tenga exactamente 13 filas vacías con la estructura ` & & & \\ \hline`.

3. **Verificación**:
   - Se compiló con éxito a PDF dos veces usando el script `scripts/compile-latex.sh` (que filtra el PATH de WSL).
   - Se ejecutó `./init.sh` satisfactoriamente.
