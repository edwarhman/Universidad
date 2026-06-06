# Implementación Feature 5 — prelab_3: Circuito Magnético de un Contactor

Se ha agregado la referencia bibliográfica de Wikipedia solicitada y se ha citado en el marco teórico.

## Detalles de los cambios

1. **`main.tex`**: Se añadió la siguiente entrada bibliográfica al final del entorno `thebibliography`:
   ```latex
   \bibitem{wikipedia}
   Wikipedia, \textit{Contactor --- Wikipedia, la enciclopedia libre}, \url{https://es.wikipedia.org/wiki/Contactor}, 2026.
   ```

2. **`marco_teorico.tex`**: Se citó la referencia en el primer párrafo de la definición de contactor mediante `\cite{wikipedia}`.

3. **Verificación**:
   - Se ejecutó `./init.sh` con éxito.
   - Debido a las políticas del entorno, la compilación de LaTeX mediante comandos de consola externos dio timeout (esperando aprobación del usuario), pero los archivos `.tex` fueron modificados correctamente cumpliendo con la convención.
