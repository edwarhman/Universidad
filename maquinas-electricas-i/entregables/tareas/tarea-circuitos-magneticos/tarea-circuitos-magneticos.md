Aquí tienes la resolución completa del **Problema 5**  estructurada en formato Markdown limpio y ordenado para tus apuntes:

---

## Resolución: Problema 5 - Actuador Magnético

### 1. Datos del Enunciado

A partir del texto proporcionado, se extraen las siguientes magnitudes físicas:

* 
**Fuerza mecánica del muelle ($F_{\text{muelle}}$):** $15\text{ N}$ 


* 
**Espesor de cada pieza de plástico ($g$):** $2\text{ mm} = 2 \times 10^{-3}\text{ m}$ 


* 
**Número de entrehierros equivalentes ($k$):** $2$ (dos piezas de plástico en los extremos) 


* 
**Sección transversal del núcleo ($S$):** $100\text{ mm}^2 = 100 \times 10^{-6}\text{ m}^2 = 10^{-4}\text{ m}^2$ 


* 
**Flujo magnético inicial del devanado 1 ($\Phi_1$):** $70\ \mu\text{Wb} = 70 \times 10^{-6}\text{ Wb}$ 


* 
**Número de espiras del devanado 2 ($N_2$):** $150\text{ espiras}$ 


* **Permeabilidad del vacío ($\mu_0$):** $4\pi \times 10^{-7}\text{ H/m}$
* 
**Condición especial:** La reluctancia del hierro es despreciable ($\mathcal{R}_{\text{Fe}} \approx 0$).



---

### 2. Condición de Apertura del Circuito

El muelle tira de la pieza móvil hacia afuera, mientras que el campo magnético genera una fuerza de atracción que intenta mantener el circuito cerrado. Para que el muelle logre separar las piezas, la fuerza de atracción magnética ($F_{\text{mag}}$) debe reducirse hasta igualar o ser menor que la fuerza del muelle:

$$F_{\text{mag}} \le F_{\text{muelle}}$$

La fuerza magnética total en un circuito con $k$ entrehierros simétricos viene dada por:

$$F_{\text{mag}} = k \cdot \frac{B^2 \cdot S}{2\mu_0}$$

Como $k = 2$ (dos entrehierros)  y la densidad de flujo es $B = \frac{\Phi}{S}$, sustituimos en la fórmula para obtener la fuerza en función del flujo magnético neto ($\Phi_{\text{neto}}$):

$$F_{\text{mag}} = 2 \cdot \frac{\left(\frac{\Phi_{\text{neto}}}{S}\right)^2 \cdot S}{2\mu_0} = \frac{\Phi_{\text{neto}}^2}{\mu_0 \cdot S}$$

---

### 3. Cálculo del Flujo Magnético Crítico ($\Phi_{\text{máx}}$)

Calculamos cuál es el flujo máximo que tolera el circuito antes de que el muelle venza la atracción magnética:

$$F_{\text{muelle}} = \frac{\Phi_{\text{máx}}^2}{\mu_0 \cdot S}$$

Despejando $\Phi_{\text{máx}}$:

$$\Phi_{\text{máx}} = \sqrt{F_{\text{muelle}} \cdot \mu_0 \cdot S}$$

Sustituyendo los valores numéricos:

$$\Phi_{\text{máx}} = \sqrt{15 \cdot (4\pi \times 10^{-7}) \cdot 10^{-4}}$$

$$\Phi_{\text{máx}} = \sqrt{1.88495 \times 10^{-9}} \approx 4.3416 \times 10^{-5}\text{ Wb} = 43.42\ \mu\text{Wb}$$

> 
> **Conclusión intermedia:** El flujo original es de $70\ \mu\text{Wb}$. Para bajar el flujo a un nivel crítico de $43.42\ \mu\text{Wb}$, la corriente del devanado 2 debe circular en sentido **opuesto** (antagonista) al devanado 1.
> 
> 

---

### 4. Reluctancia Total del Circuito

Dado que la reluctancia del material ferromagnético es despreciable , la oposición al flujo se concentra únicamente en las dos piezas plásticas (entrehierros):

$$\mathcal{R}_{\text{total}} = 2 \cdot \mathcal{R}_g = 2 \cdot \frac{g}{\mu_0 \cdot S}$$

$$\mathcal{R}_{\text{total}} = 2 \cdot \frac{2 \times 10^{-3}}{(4\pi \times 10^{-7}) \cdot 10^{-4}} = \frac{4 \times 10^{-3}}{1.2566 \times 10^{-10}} \approx 3.1831 \times 10^7\text{ A$\cdot$v/Wb}$$

---

### 5. Determinación de la Intensidad de Corriente ($I_2$)

Aplicando la Ley de Hopkinson para circuitos magnéticos en la condición de umbral:

$$\mathcal{F}_{\text{neta}} = \Phi_{\text{máx}} \cdot \mathcal{R}_{\text{total}}$$

$$\mathcal{F}_1 - \mathcal{F}_2 = \Phi_{\text{máx}} \cdot \mathcal{R}_{\text{total}}$$

Sabemos que la fuerza magnetomotriz del devanado 1 ($\mathcal{F}_1$) es la responsable de generar el flujo inicial de $70\ \mu\text{Wb}$ en vacío:


$$\mathcal{F}_1 = \Phi_1 \cdot \mathcal{R}_{\text{total}}$$

Reemplazando $\mathcal{F}_1$ y expandiendo $\mathcal{F}_2 = N_2 \cdot I_2$:

$$\Phi_1 \cdot \mathcal{R}_{\text{total}} - N_2 \cdot I_2 = \Phi_{\text{máx}} \cdot \mathcal{R}_{\text{total}}$$

Despejamos el término del segundo devanado ($N_2 \cdot I_2$):

$$N_2 \cdot I_2 = (\Phi_1 - \Phi_{\text{máx}}) \cdot \mathcal{R}_{\text{total}}$$

$$I_2 = \frac{(\Phi_1 - \Phi_{\text{máx}}) \cdot \mathcal{R}_{\text{total}}}{N_2}$$

Sustituyendo los valores finales:

* 
$\Phi_1 - \Phi_{\text{máx}} = 70 \times 10^{-6}\text{ Wb} - 43.416 \times 10^{-6}\text{ Wb} = 26.584 \times 10^{-6}\text{ Wb}$ 


* $\mathcal{R}_{\text{total}} = 3.1831 \times 10^7\text{ A$\cdot$v/Wb}$
* 
$N_2 = 150\text{ espiras}$ 



$$I_2 = \frac{(26.584 \times 10^{-6}) \cdot (3.1831 \times 10^7)}{150}$$

$$I_2 = \frac{846.19}{150} \approx 5.64\text{ A}$$

---

### Resultado Final

El valor mínimo de intensidad de corriente continua que deberá circular por el devanado 2 para que el muelle logre abrir el circuito magnético es de **$5.64\text{ A}$**.

Para resolver el **Problema 1-2** de la segunda página del PDF, analizaremos el circuito magnético de tres ramales con las bobinas conectadas en serie.

---

### 1. Datos del Enunciado

* 
**Bobinas en los ramales laterales (A y B):** * $N_1 = 100\text{ espiras}$ (en la rama A) 


* 
$N_2 = 100\text{ espiras}$ (en la rama B) 


* Están conectadas en **serie** de forma que sus fuerzas magnetomotrices (f.m.m.) dirigen el flujo hacia el ramal central C en la misma dirección. Como la corriente $I$ es la misma para ambas por estar en serie, las f.m.m. se suman en su efecto sobre la rama central.




* **Geometría del núcleo:**
* Sección de las ramas A y B: $S_A = S_B = 1250\text{ mm}^2 = 1250 \times 10^{-6}\text{ m}^2$ 


* Sección de la rama central C: $S_C = 2500\text{ mm}^2 = 2500 \times 10^{-6}\text{ m}^2$ 


* Longitud de la rama A: $l_A = 150\text{ mm} = 0.15\text{ m}$ 


* Longitud de la rama B: $l_B = 150\text{ mm} = 0.15\text{ m}$ 


* Longitud de la rama C: $l_C = 50\text{ mm} = 0.05\text{ m}$ 


* Espesor del entrehierro (en la rama central): $g = 3.7\text{ mm} = 3.7 \times 10^{-3}\text{ m}$ 




* **Propiedades del material:**
* Material: Acero.


* Factor de relleno (volumen útil ocupado): $k_r = 0.94$. Esto significa que la sección magnética real u operativa del hierro se reduce por este factor: $S_{\text{fe}} = k_r \cdot S_{\text{total}}$.


* Se desprecia el efecto de bordes y la dispersión.




* **Objetivo:**
* Calcular la intensidad de corriente $I$ (en amperios) necesaria para que la densidad de flujo (inducción) en la rama central sea $B_C = 0.6\text{ Wb/m}^2$ (o Teslas).





---

### 2. Análisis del Flujo y Simetría del Circuito

Debido a que el circuito es completamente simétrico ($l_A = l_B$ y $S_A = S_B$) y las f.m.m. empujan el flujo magnético con el mismo sentido hacia el centro , los flujos de las ramas laterales ($\Phi_A$ y $\Phi_B$) se combinan para entrar en la rama central C:

$$\Phi_C = \Phi_A + \Phi_B$$

Por simetría pura:


$$\Phi_A = \Phi_B = \frac{\Phi_C}{2}$$

Calculamos el flujo en la rama central utilizando la sección geométrica total de C (ya que en el entrehierro de aire no afecta el factor de relleno del acero, y el enunciado nos pide la densidad de flujo en dicha zona):

$$\Phi_C = B_C \cdot S_C = 0.6\text{ T} \cdot (2500 \times 10^{-6}\text{ m}^2) = 1.5 \times 10^{-3}\text{ Wb}$$

Por lo tanto, el flujo en las ramas laterales es:


$$\Phi_A = \Phi_B = \frac{1.5 \times 10^{-3}\text{ Wb}}{2} = 0.75 \times 10^{-3}\text{ Wb}$$

---

### 3. Densidades de Flujo Magnético ($B$) en el Acero

Para determinar la caída de tensión magnética en el hierro, necesitamos evaluar la densidad de flujo real en el material magnético (restando el espacio libre del factor de relleno):

* **En la rama central (C):**

$$B_{\text{Fe}, C} = \frac{\Phi_C}{k_r \cdot S_C} = \frac{0.6}{0.94} \approx 0.6383\text{ T}$$


* **En las ramas laterales (A y B):**

$$B_{\text{Fe}, A} = B_{\text{Fe}, B} = \frac{\Phi_A}{k_r \cdot S_A} = \frac{0.75 \times 10^{-3}}{0.94 \cdot (1250 \times 10^{-6})} = \frac{0.75 \times 10^{-3}}{1.175 \times 10^{-3}} \approx 0.6383\text{ T}$$



*Nota técnica:* Dado que la sección transversal de las ramas laterales es exactamente la mitad que la de la central ($1250\text{ mm}^2$ frente a $2500\text{ mm}^2$)  y transportan exactamente la mitad del flujo, la densidad de flujo $B$ es uniforme en todo el hierro del circuito ($B \approx 0.6383\text{ T}$).

---

### 4. Determinación de la Intensidad de Campo Magnético ($H$)

Para avanzar con exactitud matemática en materiales ferromagnéticos como el acero, se suele emplear la curva de magnetización ($B-H$) característica del material provista por las tablas del libro o manual correspondiente (típicamente de autores como Fitzgerald o Kosow, de donde procede este problema clásico).

Al no disponer físicamente de la gráfica exacta adjunta para ese tipo de acero comercial específico, se utiliza la aproximación lineal estándar para densidades de flujo moderadas (zonas lejanas a la saturación, donde $\mu_r \approx 2000$ para aceros eléctricos laminados comunes), o bien se resuelve dejando expresado el término en función de $H_{\text{acero}}$.

Asumiendo un acero comercial estándar donde para $B \approx 0.64\text{ T}$ le corresponde una excitación aproximada de $H_{\text{Fe}} \approx 200\text{ A/m}$ (valor típico de tablas de problemas de circuitos magnéticos similares):

Para el **entrehierro** (aire):


$$H_g = \frac{B_C}{\mu_0} = \frac{0.6}{4\pi \times 10^{-7}} \approx 477464.83\text{ A/m}$$

---

### 5. Aplicación de la Ley de Ampere (Hopkinson)

Tomando una malla cerrada que recorra una rama lateral (por ejemplo, la A) y la rama central C:

$$\sum N \cdot I = \sum H \cdot l$$

En la malla elegida, únicamente actúa la bobina de la rama A ($N_1 \cdot I$):

$$N_1 \cdot I = H_{\text{Fe}} \cdot l_A + H_{\text{Fe}} \cdot l_C + H_g \cdot g$$

Sustituyendo los valores numéricos correspondientes:

* 
$l_A = 0.15\text{ m}$ 


* 
$l_C = 0.05\text{ m}$ 


* 
$g = 3.7 \times 10^{-3}\text{ m}$ 



$$100 \cdot I = H_{\text{Fe}} \cdot (0.15) + H_{\text{Fe}} \cdot (0.05) + (477464.83) \cdot (3.7 \times 10^{-3})$$

$$100 \cdot I = H_{\text{Fe}} \cdot (0.2) + 1766.62$$

Como se observa habitualmente en circuitos con entrehierro, la caída de fuerza magnetomotriz en el aire ($1766.62\text{ A}\cdot\text{v}$) predomina masivamente sobre la del silicio o acero ($0.2 \cdot H_{\text{Fe}} \approx 40\text{ A}\cdot\text{v}$):

$$100 \cdot I \approx 40 + 1766.62 = 1806.62\text{ A}\cdot\text{v}$$

$$I = \frac{1806.62}{100} \approx 18.07\text{ A}$$

### Resultado Final

La intensidad de corriente necesaria para alcanzar dicha inducción es de aproximadamente **$18.07\text{ A}$** (el valor exacto final puede oscilar levemente entre $17.6\text{ A}$ y $18.2\text{ A}$ dependiendo de la curva exacta de $B-H$ del acero específico provista en las tablas de tu asignatura).

Vamos a resolver detalladamente el **PROBLEMA 1** de este nuevo documento, siguiendo las indicaciones de equilibrio estático de fuerzas y evaluando numéricamente la reluctancia del hierro.

---

## 1. Identificación de Datos del Enunciado

* 
**Curva de magnetización del hierro:** $B = 0,0006 \cdot H$.


* 
**Dimensiones principales:** $a = 100\text{ mm} = 0,1\text{ m}$ y $b = 50\text{ mm} = 0,05\text{ m}$.


* 
**Sección uniforme del núcleo ($S$):** $100\text{ mm}^2 = 100 \times 10^{-6}\text{ m}^2 = 10^{-4}\text{ m}^2$.


* 
**Longitud del entrehierro inicial (relé abierto, $\delta$):** $1\text{ mm} = 10^{-3}\text{ m}$.


* **Número de entrehierros ($k$):** $2$ (el flujo atraviesa dos veces el espacio libre para cerrar el circuito a través de la culata móvil).
* 
**Constante elástica del muelle ($K$):** $10320\text{ N/m}$.


* 
**Número de espiras ($N$):** $5000\text{ espiras}$.


* 
**Resistencia de la bobina ($R$):** $1000\ \Omega$.


* **Permeabilidad del vacío ($\mu_0$):** $4\pi \times 10^{-7}\text{ H/m}$.

---

## 2. Propiedades Magnéticas del Hierro

A partir de la ecuación dada para el material ferromagnético ($B = \mu_{\text{Fe}} \cdot H$), extraemos su permeabilidad absoluta:


$$\mu_{\text{Fe}} = 0,0006 = 6 \times 10^{-4}\text{ H/m}$$

Para compararla con la del aire, podemos calcular de manera ilustrativa su permeabilidad relativa ($\mu_r$):


$$\mu_r = \frac{\mu_{\text{Fe}}}{\mu_0} = \frac{6 \times 10^{-4}}{4\pi \times 10^{-7}} \approx 477,46$$

---

## 3. Cálculo de las Reluctancias del Circuito (Con el relé abierto)

### Longitud de la línea media del hierro ($l_{\text{Fe}}$)

De acuerdo a la geometría de la figura:

* Tramo de la izquierda (donde se enrolla la bobina): longitud $b = 0,05\text{ m}$.
* Tramo superior horizontal: longitud $a = 0,1\text{ m}$.
* Tramo inferior horizontal: longitud $a = 0,1\text{ m}$.
* Pieza móvil (culata derecha): longitud $b = 0,05\text{ m}$.

Suma de las longitudes del hierro:


$$l_{\text{Fe}} = b + a + a + b = 2a + 2b = 2(0,1) + 2(0,05) = 0,3\text{ m}$$

### Reluctancia del Hierro ($\mathcal{R}_{\text{Fe}}$)

$$\mathcal{R}_{\text{Fe}} = \frac{l_{\text{Fe}}}{\mu_{\text{Fe}} \cdot S} = \frac{0,3}{(6 \times 10^{-4}) \cdot 10^{-4}} = \frac{0,3}{6 \times 10^{-8}} = 5 \times 10^6\text{ A$\cdot$v/Wb}$$

### Reluctancia de los Entrehierros ($\mathcal{R}_g$)

Como hay dos entrehierros en serie de espesor $\delta$:


$$\mathcal{R}_g = \frac{2\delta}{\mu_0 \cdot S} = \frac{2 \times 10^{-3}}{(4\pi \times 10^{-7}) \cdot 10^{-4}} = \frac{2 \times 10^{-3}}{1,2566 \times 10^{-10}} \approx 15,915 \times 10^6\text{ A$\cdot$v/Wb}$$

### Reluctancia Total Abierto ($\mathcal{R}_{\text{total, abierto}}$)

$$\mathcal{R}_{\text{total, abierto}} = \mathcal{R}_{\text{Fe}} + \mathcal{R}_g = 5 \times 10^6 + 15,915 \times 10^6 = 20,915 \times 10^6\text{ A$\cdot$v/Wb}$$

> **Justificación numérica (Petición de la Nota):** La reluctancia del hierro representa aproximadamente el $24\%$ de la reluctancia total del circuito ($5 / 20,915$). Por lo tanto, no se puede despreciar.
> 
> 

---

## 4. Resolución del Apartado 1: Fuerza Magnetomotriz y Tensión $V$ Mínima

Para que el relé comience a cerrarse, la fuerza de atracción magnética generada entre las piezas debe igualar a la fuerza mecánica opuesta ejercida por el muelle en la posición de máxima apertura ($x = \delta = 1\text{ mm}$):

$$F_{\text{muelle}} = K \cdot \delta = 10320\text{ N/m} \cdot 10^{-3}\text{ m} = 10,32\text{ N}$$

La fuerza de atracción magnética debida a los dos entrehierros es:


$$F_{\text{mag}} = \frac{\Phi^2}{\mu_0 \cdot S}$$

Estableciendo el equilibrio estático ($F_{\text{mag}} = F_{\text{muelle}}$):


$$10,32 = \frac{\Phi^2}{(4\pi \times 10^{-7}) \cdot 10^{-4}}$$

$$\Phi^2 = 10,32 \cdot 1,2566 \times 10^{-10} = 1,2968 \times 10^{-9}$$

$$\Phi = \sqrt{1,2968 \times 10^{-9}} \approx 3,601 \times 10^{-5}\text{ Wb}$$

### Fuerza Magnetomotriz ($\mathcal{F}$)

Aplicando la ley de Hopkinson con el relé abierto:


$$\mathcal{F} = N \cdot I = \Phi \cdot \mathcal{R}_{\text{total, abierto}}$$

$$\mathcal{F} = (3,601 \times 10^{-5}\text{ Wb}) \cdot (20,915 \times 10^6\text{ A$\cdot$v/Wb}) \approx \mathbf{753,15\text{ A$\cdot$v}}$$

### Tensión Mínima ($V$)

A partir de la ley de Ohm en corriente continua para la bobina ($\mathcal{F} = N \cdot \frac{V}{R}$):


$$I = \frac{\mathcal{F}}{N} = \frac{753,15}{5000} \approx 0,1506\text{ A}$$

$$V = I \cdot R = 0,1506\text{ A} \cdot 1000\ \Omega = \mathbf{150,6\text{ V}}$$

---

## 5. Resolución del Apartado 2: Coeficiente de Autoinducción ($L$)

El coeficiente de autoinducción se define como $L = \frac{N^2}{\mathcal{R}_{\text{total}}}$.

### Antes de cerrar el relé (Abierto: $\delta = 1\text{ mm}$)

Utilizamos la reluctancia total calculada previamente:


$$L_{\text{abierto}} = \frac{N^2}{\mathcal{R}_{\text{total, abierto}}} = \frac{5000^2}{20,915 \times 10^6} = \frac{25 \times 10^6}{20,915 \times 10^6} \approx \mathbf{1,195\text{ H}}$$

### Después de cerrar el relé (Cerrado: $\delta = 0$)

Cuando el relé se cierra por completo, la separación del entrehierro se reduce a cero, anulando su reluctancia ($\mathcal{R}_g = 0$). La oposición al flujo magnético se limita únicamente a la del hierro:


$$\mathcal{R}_{\text{total, cerrado}} = \mathcal{R}_{\text{Fe}} = 5 \times 10^6\text{ A$\cdot$v/Wb}$$

$$L_{\text{cerrado}} = \frac{N^2}{\mathcal{R}_{\text{total, cerrado}}} = \frac{5000^2}{5 \times 10^6} = \frac{25 \times 10^6}{5 \times 10^6} = \mathbf{5\text{ H}}$$

---

## Respuestas Finales resumidas:

1. **Fuerza magnetomotriz mínima:** $753,15\text{ A$\cdot$v}$
2. **Tensión $V$ mínima:** $150,6\text{ V}$
3. **Autoinducción antes de cerrar (abierto):** $1,195\text{ H}$
4. **Autoinducción después de cerrar (cerrado):** $5\text{ H}$
