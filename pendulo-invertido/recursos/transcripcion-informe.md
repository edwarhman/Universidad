# Informe de Laboratorio: Control de Péndulo Invertido

**Institución:** Universidad Central de Venezuela | Facultad de Ingeniería | Escuela de Ingeniería Eléctrica 

**Departamento:** Electrónica y Control 

**Profesor:** José Romero 

**Estudiante:** Emerson Warhman 

---

## Objetivos

* Modelar el sistema del prototipo de péndulo invertido.


* Estabilizar el sistema mediante el diseño de dos controladores PID en cascada.


* Estabilizar el sistema mediante realimentación de variables de estados utilizando observador identidad, observador de orden reducido y observador funcional lineal.


* Comparar el desempeño entre los controladores diseñados utilizando el tiempo de establecimiento y el sobre impulso.



---

## Modelo

### Análisis de la barra

El centro de gravedad de la barra está en el centro geométrico de la misma. Las coordenadas del centro de gravedad de la barra son:

$$X_{cg} = x + l \sin\theta$$



$$Y_{cg} = l \cos\theta$$



El movimiento rotacional de la barra viene dado por:

$$\tau = I \ddot{\theta}$$



donde $I$ es el momento de inercia de la barra alrededor de su centro de gravedad. El movimiento horizontal del centro de gravedad es:

$$m \frac{d^2}{dt^2}(x + l \sin\theta) = H$$



El movimiento vertical del centro de gravedad es:

$$m \frac{d^2}{dt^2}(l \cos\theta) = V - mg$$



Como se debe mantener el péndulo invertido en posición vertical se puede suponer $\theta$ pequeñas por lo que:

$$\sin\theta \approx \theta, \quad \cos\theta \approx 1, \quad \dot{\theta}^2 \approx 0$$



quedan:

$$(I + ml^2)\ddot{\theta} = mgl\theta - ml\ddot{x}$$



El momento de inercia en el centro de gravedad es:

$$\frac{1}{12}mL^2 = \frac{1}{12}m(2l)^2 = \frac{1}{3}ml^2$$



Sustituyendo en y:

$$\ddot{\theta} = \frac{3}{4l}g\theta - \frac{3}{4l}\ddot{x}$$



### Análisis del carro

Ya que el actuador es un sistema mecánico el movimiento del carro viene dado por y cuando no se suponen las pérdidas físicas del actuador el sistema está definido por el siguiente juego de ecuaciones:

$$\ddot{\theta} = \frac{3}{4l}g\theta - \frac{3}{4l}u$$



$$\ddot{x} = u$$



### Representación en variables de estado

Con $g = 9.8 \, \text{m/s}^2$:

$$\dot{\mathbf{x}} = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 14.7 & 0 \end{bmatrix} \mathbf{x} + \begin{bmatrix} 0 \\ 1 \\ 0 \\ -1.5 \end{bmatrix} u$$



$$\mathbf{y}(t) = \begin{bmatrix} 1 & 0 & 0 & 0 \end{bmatrix} \mathbf{x}(t)$$



### Discretizando el sistema con un retenedor de orden cero

$T = 0.01 \, \text{seg}$:

$$\mathbf{x}(n+1) = \begin{bmatrix} 1 & 0.01 & -0.0001 & 0 \\ 0 & 1 & -0.003 & -0.0001 \\ 0 & 0 & 1.0028 & 0.01 \\ 0 & 0 & 0.5659 & 1.0028 \end{bmatrix} \mathbf{x}(n) + \begin{bmatrix} 0.0001 \\ 0.01 \\ -0.0001 \\ -0.003 \end{bmatrix} u(n)$$



$$\mathbf{y}(n) = \begin{bmatrix} 1 & 0 & 0 & 0 \end{bmatrix} \mathbf{x}(n)$$



### Controlabilidad

$$\mathbf{M}_c = \begin{bmatrix} \mathbf{H} & \mathbf{G}\mathbf{H} & \mathbf{G}^2\mathbf{H} & \mathbf{G}^3\mathbf{H} \end{bmatrix}$$



$$\mathbf{M}_c = \begin{bmatrix} 0.0001 & 0.0002 & 0.0003 & 0.0004 \\ 0.01 & 0.01 & 0.01 & 0.0099 \\ -0.0001 & -0.0003 & -0.0006 & -0.0011 \\ -0.003 & -0.006 & -0.0091 & -0.0122 \end{bmatrix}$$



Rango $\mathbf{M}_c = 4$, es controlable.

### Observabilidad

$$\mathbf{M}_o = \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{G} \\ \mathbf{C}\mathbf{G}^2 \\ \mathbf{C}\mathbf{G}^3 \end{bmatrix}$$



Rango $\mathbf{M}_o = 4$.

---

## Diseño de Servosistema de Tipo 1

Para controlar la posición es necesario estructurar un sistema de tipo 1. El sistema del péndulo invertido montado en un carro no tiene un integrador natural, por lo tanto se realimenta la variable de posición a la entrada y se inserta un integrador en el camino directo como se muestra en la figura 2.

$$u = -\mathbf{K}\mathbf{x} + K_i e_I$$



$$\dot{e}_I = r - y = r - \mathbf{C}\mathbf{x}$$



El sistema ampliado queda:

$$\hat{\mathbf{A}} = \begin{bmatrix} \mathbf{G} & \mathbf{0} \\ -\mathbf{C} & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0.01 & -0.0001 & 0 & 0 \\ 0 & 1 & -0.003 & -0.0001 & 0 \\ 0 & 0 & 1.0028 & 0.01 & 0 \\ 0 & 0 & 0.5659 & 1.0028 & 0 \\ -1 & 0 & 0 & 0 & 1 \end{bmatrix}, \quad \hat{\mathbf{B}} = \begin{bmatrix} \mathbf{H} \\ 0 \end{bmatrix} = \begin{bmatrix} 0.0001 \\ 0.01 \\ -0.0001 \\ -0.003 \\ 0 \end{bmatrix}$$



Para la asignación de polos se utilizaron los siguientes polos comandados:


$$p = [0.9515, \, 0.9775 + j0.0257, \, 0.9775 - j0.0257, \, 0.742]$$



Para ello se utilizó la fórmula de Ackermann:


$$\mathbf{K}_{amp} = \begin{bmatrix} 0 & 0 & 0 & 0 & 1 \end{bmatrix} \mathbf{M}_c^{-1} \alpha(\hat{\mathbf{A}})$$



donde $\alpha$ es el polinomio característico deseado:


$$\alpha = z^5 - 4.714 z^4 + 8.846 z^3 - 8.365 z^2 + 3.946 z - 0.714$$



Se obtiene $\mathbf{K}_{amp}$  de donde:


$$\mathbf{K} = \begin{bmatrix} -28.8466 & -14.9071 & -54.4323 & -9.3951 \end{bmatrix}$$



$$K_i = -9.1010$$



### Observador Identidad

Para diseñar el observador identidad se seleccionan autovalores que sean más rápidos que los polos a lazo cerrado del sistema, en este caso se seleccionaron en:


$$\alpha_{obs} = z^4 - 2.8 z^3 + 2.9366 z^2 - 1.3536 z + 0.2315$$



Para encontrar la matriz de realimentación del observador se utilizó el sistema dual de la fórmula de Ackermann:


$$\mathbf{L} = \alpha_{obs}(\mathbf{G}) \begin{bmatrix} \mathbf{C} \\ \mathbf{C}\mathbf{G} \\ \mathbf{C}\mathbf{G}^2 \\ \mathbf{C}\mathbf{G}^3 \end{bmatrix}^{-1} \begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}$$



dando como resultado:


$$\mathbf{L} = \begin{bmatrix} 0.49 & 0.5 & 0.9997 & 26.3034 \end{bmatrix}^T$$



El observador se construye como:


$$\mathbf{A}_o = \mathbf{G} - \mathbf{L}\mathbf{C}, \quad \mathbf{B}_o = \mathbf{H} - \mathbf{L} D$$



### Observador de Orden Reducido

Utilizaremos solo la dinámica de la barra.


$$\mathbf{A}_{22} = \begin{bmatrix} 1.0028 & 0.01 \\ 0.5659 & 1.0028 \end{bmatrix}, \quad \mathbf{A}_{12} = \begin{bmatrix} -0.0001 & 0 \\ -0.003 & -0.0001 \end{bmatrix}^T$$



$$\mathbf{B}_2 = \begin{bmatrix} -0.0001 \\ -0.003 \end{bmatrix}$$



La matriz $\mathbf{C}$ ya está en la forma apropiada. La forma del observador es:

$$\tilde{\mathbf{x}}(n+1) = (\mathbf{A}_{22} - \mathbf{L}\mathbf{A}_{12})\tilde{\mathbf{x}}(n) + \mathbf{B}_2 u(n) + \dots$$



El autovalor del observador será colocado en 0.5.


$$\det(z\mathbf{I} - \mathbf{A}_{22} + \mathbf{L}\mathbf{A}_{12}) = z - 0.5$$



$$L = 20.28$$



Sustituyendo:


$$\tilde{\mathbf{x}}(n+1) = 0.5 \tilde{\mathbf{x}}(n) + \dots$$



### Funcional Lineal Simple

Cálculo del índice de observabilidad:


$$\text{Rango} \, \mathbf{M}_o = 4 \implies \text{índice de observabilidad} = 2$$



El observador puede construirse con un solo autovalor el cual es $z = 0.5$. Además se debe cumplir:


$$\mathbf{T}\mathbf{A} - \mathbf{F}\mathbf{T} = \mathbf{W} = \mathbf{G}_c \mathbf{C}$$



---

## Diseño de Controladores PID

### Análisis de la barra

$$\theta = \frac{3/4l}{s^2 - 3g/4l} u$$



### Análisis del carro

$$x = \frac{1}{s^2} u$$



Mediante proceso de ensayo y error se obtuvieron los siguientes controladores:


$$PID_1(z) = 0.4 + 0.02 \frac{1}{z} + 0.157 z$$



$$PID_2(z) = -18 - \frac{91}{z} - 0.02 z$$



---

## Procedimiento Experimental

El prototipo del péndulo invertido cuenta con una barra anclada a un carro el cual es desplazado a través de una correa de goma por un motor a pasos, mide aproximadamente 1 metro de largo y cuenta con dos finales de carreras que sirven para dar una referencia de la posición del carro y como apagador de emergencia del sistema en caso de que se rebase el límite del riel previniendo que se estropeen componentes del sistema. El péndulo es controlado por un microcontrolador ESP32 que toma las lecturas del ángulo del péndulo desde un encoder. El sistema también cuenta con una rutina de calibración la cual le permite buscar el cero de posición y el rango máximo del riel.

### Implementación de los controladores PID

Durante la implementación del los PID se observaron una serie de errores de códigos que impedían el correcto funcionamiento del sistema. Los comandos enviados al motor eran de los de una impresora lo cual bloqueaba el avance o causaba un movimiento errático del programa debido a los cambios abruptos de velocidad. Otro error era que la salida del PID interno es un comando de aceleración y se le pasaba directamente al motor que recibe comandos de velocidad, se corrigió esto integrando la salida de aceleración del motor para obtener una velocidad, haciendo los movimientos más suaves.

Otro problema que se identificó es que la ganancia del modelo asumido tenía que corregirse, se multiplicó por un factor de corrección en el código para que coincidiera con el comportamiento real del carro. Resueltos estos problemas el péndulo se mantuvo estable. A partir de aquí se realizó un proceso de ensayo y error en laboratorio para ajustar los valores de los PID que hicieran el sistema lo más robusto posible, obteniendo por resultado:

$$PID_{EXT} = 0.4 + 0.02 \frac{1}{z} + 0.157 z$$



$$PID_{INT} = -18 - \frac{91}{z} - 0.02 z$$



Es importante mencionar que se tomó una medida de seguridad con las salidas de los PID utilizados en el código, estas se limitaron para que su salida no pudiese superar a la transformada de grados a velocidad y aceleración del carro. Al momento de sintonizar los PID también se tomó en cuenta que el lazo del péndulo debe ser mucho más rápido que el lazo de posición.

### Implementación de controladores por realimentación de variables de estado utilizando observador

Se adaptó la rutina de gestión del PID para que funcionara con realimentación por variables de estados utilizando los tres observadores: Identidad, de orden reducido y funcional lineal simple. Se agregaron los valores de las matrices calculados en el estudio del modelo matemático de manera que el péndulo se mantuvo estable para cada uno de ellos.

### Comparación de los modelos y resultados

Se diseñó una prueba para evaluar los controladores. Esta consiste en cambiar la posición de referencia en intervalos de tiempo fijos y observar la respuesta del sistema a este cambio. Otra prueba consiste en perturbar al péndulo de manera que su ángulo cambie drásticamente respecto a la vertical y luego observar la capacidad del controlador para regresar el péndulo a su estado estable. Durante estas pruebas se guardaron los datos de la posición del carro, el ángulo del péndulo y las acciones de control del sistema durante el proceso. En esta última prueba se utilizó un ventilador para generar una corriente de aire en el camino del péndulo y evaluar el comportamiento de este al recibir una perturbación continua de viento. Las tres pruebas se realizaron para cada uno de los controladores bajo estudio.

---

## Análisis de Resultados

### Comparación entre la respuesta teórica y la real

Al observar los resultados gráficos se puede notar que para el observador identidad la posición oscila tres veces antes de estabilizarse, ambas curvas apuntan al mismo comportamiento. Los cambios de amplitudes son similares y los picos cambian en los mismos instantes de tiempo en ambas gráficas. Vemos que para ambos casos el error en estado estacionario es prácticamente 0. En los momentos en que el error estacionario no es cero en el prototipo real cuando debería serlo se debe a perturbaciones externas como el viento.

Al evaluar las respuestas del prototipo físico con los distintos observadores se nota que la respuesta de posición para el observador identidad es subamortiguada mientras que la del de orden reducido es más parecida a una respuesta críticamente amortiguada o sobreamortiguada ya que no tiene sobrepico. Por otro lado las respuestas del observador de orden completo y del funcional lineal parecen tener un pequeño sobreimpulso, sin embargo esto puede ser debido a la perturbación del viento. Por otro lado para el ángulo del péndulo vemos que se comportan prácticamente de la misma manera.

### Comparación entre los controladores

Se observa claramente en las gráficas que la respuesta de posición del PID tiene un comportamiento subamortiguado mientras que para los tres controladores por realimentación de estados es prácticamente sobreamortiguada. Vemos que en estado estable el PID mantiene pequeñas oscilaciones mientras que los demás se mantienen prácticamente con error 0. Esto se debe principalmente a que el PID no puede adaptarse de forma tan óptima a los modos acoplados del lazo cerrado como sí lo hacen los de variables de estado. Al observar el ángulo se nota que el PID llega a ángulos mayores llegando a registrar picos de hasta 5 grados mientras que los demás esquemas se mantuvieron alrededor de 1 grado.

En la velocidad del carro se observa que el PID llega a valores más altos de hasta 8 mientras que los demás tienen su pico mayor en 3. Se notó además que en estado estacionario la velocidad del PID se encuentra muy ruidosa mientras que los otros tienen una velocidad que oscila muy cerca de cero en estado estacionario. Esta puede ser la razón por la cual los controladores de variables de estado son más robustos que el PID, estos realizan más trabajo interno continuo para mantener el ángulo en 0. En la aceleración ocurre algo parecido que con la velocidad. Para el PID la aceleración es muy ruidosa en estado estable mientras que en los demás se mantiene en un rango estrecho de entre -5 y 5. Se observó también que la aceleración en el funcional lineal llega a 5 durante la prueba de cambio de referencia mientras que en estado estacionario se reduce a valores cercanos a cero.

Por otro lado el de orden reducido maneja valores de aceleración menores que el resto en estado estacionario tanto en el cambio de referencia como en estado estacionario. Esto podría indicar que es el más eficiente energéticamente de los tres. Cabe mencionar que los límites de saturación de velocidad y aceleración son los mismos para todos los controladores.

Las figuras muestran los resultados de las pruebas de condiciones iniciales para ángulos de 10°, 15°, 25° y 30° respectivamente. En la prueba de 10° se obtuvo que el PID tuvo la mayor sobreelongación luego le sigue el funcional lineal mientras que el identidad y el de orden reducido tuvieron una sobreelongación menor. Tanto el PID, identidad y el funcional lineal oscilaron al menos 2 veces antes de estabilizarse, mientras que el control con observador de orden reducido se estabilizó a través de la primera sobreelongación.

Para la prueba de 15° el PID no logró recuperarse y se cayó mientras que los otros lograron estabilizarse. En esta ocasión el que mostró una respuesta más suave fue el observador identidad que osciló una sola vez mientras que los otros oscilaron al menos dos veces. En las pruebas de 25° y 30° no se probó el PID ya que se probó antes que no es capaz de recuperarse de ángulos mayores a 15°. En esta ocasión los tres controladores por variables de estado se comportaron de manera similar lo que parece indicar que el comportamiento sobreamortiguado depende de las condiciones del sistema y de las perturbaciones al momento de hacer las pruebas.

En la prueba con el ventilador se notó que el PID no fue capaz de soportar la perturbación continua y terminó cayendo, mientras que los de variables de estado se mantuvieron estables. Entre estos últimos el funcional lineal es el que más esfuerzo hizo para mantener la estabilidad seguido por el de orden reducido y por último el identidad.

Durante la calibración del PID también se observó que aumentar la ganancia proporcional hacía que el carro se desplazara bruscamente generando vibraciones mecánicas. Esto limitó en gran medida el ajuste del PID. Esta dificultad parece ser debida al ruido en la lectura del ángulo del encoder.

---

## Conclusiones

* Se cumplió con el diseño e implementación del PID en cascada y de la realimentación de estados con los observadores identidad, de orden reducido y funcional lineal.


* El comportamiento real de los controladores respondió de forma muy aproximada al comportamiento teórico esperado, demostrando que las perturbaciones externas no afectaron de forma crítica la estabilidad, cumpliendo así el efecto de haber linealizado el sistema alrededor del punto inestable.


* Al comparar cada uno de los modelos utilizados se concluye que el PID posee un desempeño menos robusto ya que es más susceptible a las perturbaciones y tiene un rango de estabilidad más bajo. Por otro lado los controladores por realimentación del estado tienen un comportamiento muy superior, considerándose el funcional lineal como el más robusto frente a perturbaciones continuas.


* Esto se debe a que el funcional lineal fue diseñado ajustando un único polo acoplado para el lazo cerrado mientras que para los demás observadores el diseño de las variables de estado se hace de forma independiente para cada polo separado.


* Se evidenció la ventaja del control por realimentación del estado sobre el PID al permitir diseñar la ubicación exacta de los polos del sistema y forzar a que el sistema se comportara como se deseaba, a diferencia del PID en el cual se tuvo que depender de un ajuste empírico limitado por el ruido.



---

## Notas de Revisión Litográficas (Observaciones del Profesor)

> De acuerdo con las anotaciones en lápiz y marcas de revisión que el profesor José Romero plasmó sobre el manuscrito original, se extraen los siguientes puntos a tomar en cuenta en el documento digital:
> 1. **Puntuación por Secciones:** El primer bloque (modelado y análisis clásico) cuenta con una anotación de `6/10` , mientras que el desarrollo por variables de estado ostenta un `8/10`. La entrega cierra con la marca aprobatoria del docente.
> 2. **Base de Tiempo de Muestreo:** En los cálculos y gráficas de control digital, ratificar que el período de muestreo está fijado exactamente en $T_s = 0.01 \, \text{seg}$ (frecuencia de cálculo de la rutina a $1000 \, \text{Hz}$) para evitar desfases en las ecuaciones de diferencias de los observadores.
> 3. **Tratamiento Dinámico de la Barra:** Se destaca el recordatorio de tratar el sistema bajo la perspectiva rigurosa de un **péndulo físico** en lugar de una masa puntual (péndulo simple) al deducir el momento de inercia ($I = \frac{1}{3}ml^2$) y el centro geométrico de la masa, asegurando la concordancia entre los autovalores teóricos y el comportamiento real del prototipo.
> 4. **Aclaratoria en Gráfica de Validación:** El profesor identificó una discrepancia visual en los resultados temporales adjuntos, aclarando que el periodo real de la oscilación amortiguada del sistema físico es de **16 segundos**, corrigiendo la estimación inicial de 10 segundos.
