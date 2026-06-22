# Sesión actual — maquinas-electricas-i

## Proyecto: maquinas-electricas-i
## Feature: 9 — informe_3 (Estudio del Contactor o Conmutador electromagnéticos)
## Plan:
- [x] Extraer los integrantes de Informe 2 a partir del historial de git (Br. Daryari Molina, Br. Carla Fajardo, Br. Emerson Warhman, Br. Yonathan Reyes y docente Jesús Blondell).
- [x] Modificar la portada de Informe 3 (`maquinas-electricas-i/entregables/informes/Informe3/texto/portada.tex`) para listar a todos los integrantes y al docente con espaciado dinámico (`\vfill`) para evitar desbordes de página.
- [x] Agregar y refinar la descripción de las piezas del contactor en la Figura 7.3 a la sección 7.1 (`maquinas-electricas-i/entregables/informes/Informe3/texto/resultados.tex`), incluyendo la carcasa inferior y las observaciones sobre la identificación de las espiras de sombra y los orificios del entrehierro al acoplar el núcleo y el martillo.
- [x] Configurar en la segunda tabla (Tabla 7.2) de `resultados.tex` el valor de la tensión de mantenimiento como $54 \pm 2$ V.
- [x] Agregar la imagen de las espiras de sombra (`espiras-sombra.png`) a la sección 7.1 de resultados con su respectivo texto de referencia.
- [x] Anexar la ficha técnica (datasheet) del contactor `LC1D09.pdf` en la sección de Anexos (`maquinas-electricas-i/entregables/informes/Informe3/texto/anexos.tex`) importando sus páginas de manera gráfica.
- [x] Añadir una subsección de análisis de parámetros y conceptos operativos en `resultados.tex` haciendo referencia al marco teórico y explicando brevemente el significado de cada concepto (espiras de sombra, entrehierro, corriente de llamada, corriente de mantenimiento, tensión de mantenimiento), corrigiendo el análisis de la corriente de llamada de Contactor 1 para reflejar su medición real ($0,18$ A) y simplificando las referencias a la "Sección 3" para evitar advertencias de compilación por el espacio en el nombre del archivo del marco teórico.
- [x] Añadir en la sección 7.1 de `resultados.tex` la descripción técnica detallada del modelo de contactor identificado (\textbf{LC1 D09 01}) y la especificación de sus contactos principales (3 contactos NA) y auxiliares (1 contacto NC).
- [x] Compilar el documento de Informe 3 (`main.tex`) para verificar que compile correctamente y que la portada, el texto nuevo, las tablas, la nueva imagen y el datasheet se rendericen de forma adecuada.
- [x] Ubicar el análisis y discusión de resultados como una nueva sección independiente ("Análisis de Resultados y Discusión") en `texto/analisis de resultados.tex` en lugar de una subsección de Resultados, estructurando sus puntos como subsecciones.
- [x] Habilitar la inclusión de `texto/analisis de resultados.tex` en `main.tex` y recompilar de manera limpia.
- [x] Validar el entorno con `./init.sh`.

## Estado

- [ ] En progreso
- [x] Awaiting Review (Listo para revisión)

## Notas

- Los integrantes y el docente se agregaron de forma correcta basándose en el historial de `Informe 2`.
- Se agregó y actualizó en la sección 7.1 la descripción de los componentes de la Figura 7.3 (núcleo magnético, armadura móvil, carcasa inferior, bobina de control, resorte) y las observaciones sobre las espiras de sombra e identificación de los orificios del entrehierro al acoplar el núcleo y el martillo.
- Se añadió en la sección 7.1 el análisis detallado del modelo del contactor \textbf{LC1 D09 01} (LC1, D09, 01) y la identificación de sus terminales y contactos (3 contactos principales NA y 1 contacto auxiliar NC).
- Se configuró la tensión de mantenimiento como $96 \pm 2$ \si{\volt} y la tensión mínima de operación como $54 \pm 2$ \si{\volt} en la segunda tabla (Tabla 7.2) para el Contactor 2, alineando las descripciones teóricas y conceptuales a esta configuración.
- Se añadió la figura de las espiras de sombra (`espiras-sombra.png`) y su respectiva referencia en el texto de la sección 7.1.
- Se anexaron las 2 páginas de la ficha técnica `LC1D09.pdf` en la sección de Anexos.
- Se incluyó la subsección 7.4 (Análisis de Parámetros y Conceptos Operativos) resumiendo brevemente el significado físico y vinculándolo formalmente a la Sección 3 (Marco Teórico), con los valores corregidos de corriente de llamada para ambos contactores y sin advertencias de compilación.
- Se reestructuró el Análisis de Resultados y Discusión como la Sección 8 independiente en `texto/analisis de resultados.tex`, con sus subsecciones.
- Se estandarizó el formato de las cantidades físicas y unidades en la sección de análisis utilizando las macros del paquete `siunitx` (\qty) para garantizar coherencia en el informe.
- Se actualizó el análisis de las espiras de sombra para contrastar el comportamiento del Contactor 1 (sin vibración en estado estable) frente al Contactor 2 (con vibración presente en estado estable debido al desgaste o tamaño del circuito magnético).
- Se agregó el análisis del ensayo con obstáculo en el entrehierro, justificando el incremento de la corriente de mantenimiento a \qty{0,40}{\ampere} y el aumento severo en las vibraciones mecánicas y acústicas debido al incremento de reluctancia y pérdida de acoplamiento de las espiras de sombra por la hoja de papel doblada.
- Se redactaron y estructuraron las conclusiones formales del informe en `texto/conclusiones.tex`, sintetizando el impacto de los aspectos constructivos en las magnitudes eléctricas, eficiencia GB 21518, rol de las espiras de sombra, entrehierro permanente, los efectos del ensayo de obstrucción y el peligro de sobrecalentamiento y daño en la bobina por corrientes de mantenimiento elevadas bajo fallos mecánicos.
- El documento LaTeX compila de forma exitosa (`main.pdf` generado con todas las referencias cruzadas resueltas).
- Se agregó el Prelaboratorio 5 (entrega: 25-06-2026) y el Parcial 1 (entrega: 30-06-2026) como actividades pendientes en `maquinas-electricas-i/feature_list.json`.
- Se actualizó la fecha del Parcial 1 de Plantas y Subestaciones al 23-06-2026 en su respectivo `feature_list.json`.
- Se reemplazó la nota de la pinza amperimétrica por la nueva Tabla 7.2 de mediciones de referencia (corriente de llamada 0,18 A, mantenimiento 0,014 A, incertidumbre 0,01 A).

