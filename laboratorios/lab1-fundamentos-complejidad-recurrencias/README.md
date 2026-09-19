# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias

## Parte 1 — Analizar el algoritmo antes de comprar hardware

El que un algoritmo haya funcionado por 8 años consecutivos no implica que su comportamiento sea el más eficiente respecto al  tiempo de procesamiento (CPU) y el límite de operaciones que un hardware pueda procesar, lo cuál a su vez puede afectar la experiencia del usuario en tiempo real, y aunque bajo el concepto de corrección el sistema Tamiza entrega una lista de datos ordenados de forma exacta y sin ningún error lógico, cuando hablamos de eficiencia este algoritmo puede generar un reproceso cada vez mayor dependiendo la cantidad de datos que ingresan al sistema ya que la forma en que usa los recursos no es la mejor, lo cuál implica que Tamiza incumpla la ventana de tiempo de 4 horas que es estrictamente obligatoria, si para este caso se duplica la velocidad del servidor sin mejorar el algoritmo, esto podría desencadenar que en un futuro ocurra el mismo problema, ya que un hardware ofrece un crecimiento lineal, mientras que un algoritmo mal estructurado (que en este caso siendo un algoritmo de ordenamiento por inserción) es cuadrático, lo que quiere decir que si en unos años se duplican los datos el trabajo del servidor no se duplicará sino que se cuadruplicará, por ejemplo, para un sistema de automatizaciones como power automate, si se debe evaluar diariamente la indemnización de los empleados de una compañía (que tiene potencial de crecimiento) se debe considerar que debe procesar un cálculo de antigüedad, días de vacaciones pendientes y salario actual, suponiendo que actualmente se encuentran 1000 empleados activos, el flujo encargado de procesarlo debe iterar (por medio de un ciclo for) cada uno de ellos, y dentro del buble debe realizar las consultas y cálculos respectivos, generando un proceso que puede tardar 2 segundos por usuario, es decir que el flujo tarda en total 33,3 minutos en ejecutar todo el proceso. Con el pasar de los años la compañía incrementa el número de empleados de 1000 a 5000 usuarios, lo cuál genera un incremento del tiempo de ejecución a 2:46 horas, lo cuál implica que el flujo deba ejecutarse en la madrugada, suponiendo que un futuro la compañía tenga a 20.000 empleados, podría incrementar a 11 horas de ejecución, y esto podría intervenir en la ventana de tiempo que tiene Microsoft, lo que podría llevar a que el proceso exceda el límite del plan y el flujo se cancele a mitad del proceso, dejando a la mitad de la compañía sin evaluar.

## Parte 2 — Responsabilidad ambiental y ética de la implementación

Como responsable técnico de Tamiza, la selección de un algoritmo no es solo una decisión de ingeniería de software, conlleva un impacto directo en el entorno ecológico y en la vida de miles de personas. En primer lugar, respecto a la dimensión ambiental, el tiempo de ejecución en el servidor se traduce directamente en consumo de energía eléctrica, ya que cuando el procesador (CPU) trabaja a su máxima capacidad ejecutando un algoritmo de ordenamiento por inserción de naturaleza cuadrática sobre 1,200,000 pacientes, demanda una gran cantidad de vatios por cada segundo extra que se queda encendido intentando resolver el problema. Si el servidor debe procesar un volumen masivo con un algoritmo mal estructurado, este consumo no es un evento aislado, sino que al multiplicarse todas las madrugadas consecutivamente durante años, la ineficiencia algorítmica genera una huella de carbono gigantesca y un desperdicio energético acumulado innecesario que podría evitarse, pues optimizar el algoritmo reduciría el tiempo de horas a segundos, disminuyendo de forma directa las emisiones de gases de efecto invernadero del centro de datos a largo plazo.Por otro lado, en la dimensión ética, cuando el algoritmo falla o excede su ventana de tiempo por ser ineficiente respecto al procesamiento, se generan perjuicios concretos para personas reales; el primer escenario ocurre cuando hay un retraso en la atención crítica, ya que si el proceso de ordenamiento de la madrugada no termina a tiempo antes de que empiece la jornada, la lista de pacientes del día no se genera, retrasando las llamadas de asignación de citas prioritarias o tratamientos urgentes, un error cuyo costo asume directamente el paciente, quien paga el precio más alto con el deterioro de su estado de salud, su bienestar o su tranquilidad emocional debido a la espera. El segundo escenario se presenta en forma de colapso y estrés laboral, puesto que si el algoritmo se congela o arroja datos incompletos a mitad del proceso, el sistema de llamadas fallará por la mañana y provocará una avalancha de reclamos e insultos por parte de ciudadanos frustrados que no aparecen en el sistema, siendo el operador del centro de contacto quien asume el costo del error al tener que absorber el estrés emocional, la sobrecarga laboral y el desgaste psicológico de dar la cara por una falla de software que él no provocó.Finalmente, existe una tensión propia en este caso debido a que el orden de la lista decide a quién se llama primero, lo cual impone una obligación ética muy estricta sobre la corrección del ordenamiento que va mucho más allá de qué tan rápido termine el proceso en el tiempo de CPU. Si el algoritmo ordena mal debido a una falla lógica, una persona en estado crítico de salud podría quedar al final de la cola de llamadas mientras que alguien con menor prioridad sería atendido primero; por lo tanto, la corrección aquí no es solo un indicador técnico, sino una garantía de justicia y equidad médica donde modificar la posición de un registro por un error en las directrices del código altera los criterios de asignación y puede vulnerar la vida de un paciente, obligándonos a asegurar que la lógica de priorización sea siempre exacta, transparente y auditable.


## Parte 3 — Peor caso, mejor caso y caso promedio, demostrados en Python

### 3.1 — Explicación

Considerando que la entrada del sistema es igual a n = 1'200.000 registros, se deben definir 3 casos de análisis; 

1. Mejor caso: Representa el tiempo mínimo de procesamiento que requiere el algoritmo entre todas las entradas posibles de tamaño n. En este caso, los datos de entrada ya vienen organizados de la mejor manera posible, lo que le ahorra a la CPU un montón de comparaciones e intercambios. Para el algoritmo Insertion Sort, este caso ocurre cuando la lista ya viene completamente ordenada en el sentido deseado, logrando una complejidad lineal de \(O(n)\).

2. Peor Caso: Representa el tiempo máximo de procesamiento que requiere el algoritmo considerando todas las combinaciones posibles de datos de tamaño n. Aquí la entrada de datos obliga a la CPU a realizar el límite máximo de operaciones permitidas por su estructura. Para Insertion sort ocurre cuando los datos se encuentran en orden totalmente inverso, forzando una complejidad cuadrática de  \(O(n^2)\).

3. Caso promedio: Representa el tiempo esperado o promedio que tardará el algoritmo en procesar el conjunto total de todas las entradas posibles de tamaño n. asumiendo que cualquier permutación de los datos tienen la misma probabilidad de ocurrir. En Insertion Sort, esto implica que cada elemento debe compararse con al mitad de los elementos anteriores, manteniendo un comportamiento cuadrático de  \(O(n^2)\).

para saber si el algoritmo de Tamiza entra en producción sabiendo que la ventana de cuatro horas es estricta y obligatoria, se debe utilizar el peor caso. En sistemas con restricciones de tiempo crítico (ventanas operativas no negociables), no podemos depender de la suerte o de un comportamiento promedio. Diseñar o aprobar un sistema basados en el mejor caso o en el promedio dejaría la plataforma vulnerable a colapsar e incumplir la ventana de tiempo si los datos llegan en una disposición desfavorable, tal como ya ha ocurrido en las últimas semanas. Debemos grantizar que, incluso en el escenario más caótico y exigente de los datos, el algoritmo termine antes de las 6:00 am.


Antes de realizar las mediciones experimentales, predigo que los escenarios de la plataforma representan los siguientes casos de análisis para el algoritmo insertion sort;

- Escenario C (Orden inverso) es el peor caso, debido a que el sistema legado exporta los registros de menos a mayor riesgo (Es exáctamente lo contrario a lo que Tamiza necesita), cada nuevo elemento evaluado por insertion sort tendrá que recorrer la lista completa hacia atrás hasta el primer lugar para ser acomodado, lo cuál obliga al procesador a ejecutar el número máximo absoluto de comparaciones y movimientos de memoria, reflejando el comportamiento cuadrático  \(O(n^2)\).

- Escenario B (Casi ordenado) es el mejor caso, como el 98% del lote se encuentra ordenado por riesgo gracias a la lista del día anterior, el algoritmo encontrará rápidamente la posición correcta para la gran mayoría de los riesgos con un mínimo de comparaciones. Solo el 2% final requerirá un esfuerzo de ordenamiento por lo que el tiempo de procesamiento se mantendrá muy cercano al óptimo lineal  \(O(n)\).

- El Escenario A (Aleatorio) representa el caso promedio: Al no existir ninguna relación entre el orden en que los laboratorios subieron los datos y su índice de riesgo, los elementos estarán distribuidos al azar. El algoritmo tendrá que mover cada registro, en promedio, hasta la mitad de la sublista ya ordenada, lo que se traducirá experimentalmente en un comportamiento cuadrático \(O(n^2)\), tardando aproximadamente la mitad del tiempo que registrará el peor caso (Escenario C).


### Análisis de Resultados Empíricos (Parte 3)

#### Gráficas de Rendimiento
![Comparaciones vs Tamaño](laboratorios/Lab_Fundamentos_Complejidad_Recurrencia/graficas/parte3_comparaciones.png)
![Tiempo de Ejecución vs Tamaño](laboratorios/Lab_Fundamentos_Complejidad_Recurrencia/graficas/parte3_tiempo.png)


#### Diagnóstico de los Escenarios de Tamiza

Tras ejecutar las pruebas experimentales controladas incrementando el volumen de datos desde $n=100$ hasta $n=6400$, el comportamiento del algoritmo *Insertion Sort* reflejó las siguientes características empíricas:

*   **El peor caso resultó ser el Escenario C (Orden inverso):** Al ingresar los datos ordenados de menor a mayor (exactamente al revés de lo que requiere la plataforma), el algoritmo registró el crecimiento parabólico más pronunciado en ambas gráficas. Con $n=6400$, alcanzó el máximo absoluto de operaciones de comparación ($20,476,800$ comparaciones) y el mayor tiempo en CPU.
*   **El mejor caso resultó ser el Escenario B (Casi ordenado):** Al tener un 98% del lote previamente ordenado de forma decreciente, el algoritmo requirió un número mínimo de operaciones en su ciclo interno, registrando apenas $10,314$ comparaciones para $n=6400$. Su comportamiento gráfico se mantuvo asintóticamente plano y cercano a cero en tiempo de procesamiento.
*   **El escenario que se aproxima al caso promedio es el Escenario A (Aleatorio):** Al procesar registros sin relación alguna con el índice de riesgo, el volumen de comparaciones ($10,279,781$ comparaciones para $n=6400$) se situó de manera consistente en una magnitud equivalente a la mitad del peor caso ($\approx \frac{n^2}{4}$), validando la tendencia cuadrática esperada en entradas aleatorias.

#### Contraste con la Predicción Inicial

Al confrontar las mediciones experimentales con las predicciones planteadas en la sección 3.1, se concluye que **los resultados empíricos coinciden con la predicción teórica**. 

El experimento confirmó que el canal de origen de migración desde el sistema legado (Escenario C) representa el peor entorno operativo para Tamiza, mientras que el reproceso diario (Escenario B) mitiga el impacto del algoritmo permitiéndole actuar de manera casi lineal. Esto demuestra con datos matemáticos por qué el sistema colapsó en producción en las últimas semanas: al abrirse la cobertura de salud a nivel departamental, ingresaron flujos masivos con comportamiento aleatorio (Escenario A) e inverso (Escenario C), detonando la naturaleza cuadrática del código e incumpliendo de forma definitiva la ventana crítica de cuatro horas, lo cual confirma que el software no puede permanecer sin optimizarse.


## Parte 4 — Complejidad de merge sort e insertion sort: cálculo y validación

### 4.1 — Cálculo teórico 

La ecuación de recurrencia para Merge Sort clásica: 
    $$T(n) = 2T(n/2) + \Theta(n)$$

Donde sale cada cosa: 

- 2: Porque en cada páso partimos el arreglo en dos mitades. 
- $T(n/2)$: Es el tamaño de esos dos nuevos subproblemas (cada mitad tiene la mitad de los datos, lógicamente).
- $\Theta(n)$: Es lo que nos cuesta la fase de "combinar". Para mezclar dos listas ordenadas, el algoritmo tiene que recorrer todos los $n$ elementos comparándolos uno a uno.

Para resolverla elegí el método maestro. Identificamos los valores:

- $a = 2$ (las dos llamadas recursivas)
- $b = 2$ (el factor por el que dividimos el problema)
- $f(n) = \Theta(n)$ (el costo de la mezcla)

Calculamos $n^{\log_b(a)}$, que sería $n^{\log_2(2)} = n^1 = n$.Al comparar, vemos que $f(n)$ es exactamente igual a $n^{\log_b(a)}$. Esto significa que caemos directo en la condición del Caso 2 del teorema maestro. Siguiendo la regla de este caso, simplemente multiplicamos el resultado por $\log n$, concluyendo que la complejidad final es:

$T(n) = \Theta(n \log n)$

Calculando a mano el costo pensando en el peor caso para Tamiza (que sería el Escenario C, donde todos los registros llegan exactamente al revés, de menor a mayor riesgo):

| Línea | Código | Veces que se ejecuta en el peor caso |
|---:|---|---:|
| 1 | `for i in range(1, n):` | `n` |
| 2 | `key = datos[i]` | `n - 1` |
| 3 | `j = i - 1` | `n - 1` |
| 4 | `while j >= 0 and datos[j] < key:` | `n(n - 1) / 2` |
| 5 | `datos[j + 1] = datos[j]` | `n(n - 1) / 2` |
| 6 | `j -= 1` | `n(n - 1) / 2` |
| 7 | `datos[j + 1] = key` | `n - 1` |


La clave de todo este cálculo está en el ciclo while de la línea 4. Como los datos están al revés, por cada elemento i que el algoritmo revisa, tiene que devolverse hasta el principio del arreglo para encontrar su posición correcta.
Esa sumatoria desde $1$ hasta $n-1$ da matemáticamente $\frac{n(n-1)}{2}$, que es lo mismo que $\frac{n^2}{2} - \frac{n}{2}$.Si multiplicamos cada línea por una constante de tiempo imaginaria y sumamos todo, el término de mayor grado (el que crece más rápido y absorbe al resto) es el $n^2$. Omitiendo las constantes, el resultado final es $O(n^2)$.

La complejidad esperada: 

| Algoritmo | Mejor Caso | Caso Promedio | Peor Caso |
|---|---|---|---|
| Insertion Sort | `O(n)` | `O(n²)` | `O(n²)` |
| Merge Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` |


### 4.3 — Concepto técnico a la Secretaría de Salud


El que un algoritmo de ordenamiento por inserción haya funcionado por 8 años consecutivos en Tamiza no implica que su comportamiento siga siendo el más eficiente respecto al tiempo de procesamiento (CPU) y el límite de operaciones que el hardware pueda procesar, y aunque bajo el concepto de corrección el sistema actual entrega una lista de datos ordenados de forma exacta, cuando hablamos de eficiencia este algoritmo está generando un reproceso cada vez mayor dependiendo la cantidad de registros que ingresan al sistema, ya que la forma en que usa los recursos no es la mejor. Respecto a la propuesta del área de infraestructura de simplemente duplicar la velocidad del servidor sin mejorar el código, considero que esto no va a solucionar el problema de fondo, ya que un hardware ofrece un crecimiento lineal, mientras que el algoritmo mal estructurado que tenemos actualmente es cuadrático ($O(n^2)$), lo que quiere decir que, como se evidencia en la gráfica de medición generada (parte4_tiempo.png) evaluando un tamaño de entrada de 10.000 registros, el tiempo de Insertion Sort ya se empieza a disparar, por lo que si se duplica la capacidad de la máquina solo bajaremos el tiempo a la mitad por ahora, pero si en unos años se duplican los datos el trabajo del servidor se cuadruplicará y volveremos a desencadenar el mismo problema, afectando el centro de contacto en tiempo real.Para saber si el proceso cabe en la ventana de tiempo de 4 horas que es estrictamente obligatoria con los 1.200.000 registros actuales, debemos hacer una extrapolación matemática (aclarando que esto es una estimación proyectada y no una medición directa en el equipo). Tomando el dato medido en la gráfica donde 10.000 registros tardaron aproximadamente 2.5 segundos con Insertion Sort, escalar esto a 1.2 millones implica multiplicar el tamaño de entrada por 120, y por su naturaleza cuadrática el tiempo se multiplica por $120^2$ (es decir 14.400 veces), lo cual implica que el flujo tardaría en total unas 10 horas de ejecución, excediendo el límite de la madrugada y provocando que el proceso se cancele a la mitad. Por el contrario, Merge Sort para esos mismos 10.000 registros tardó solo 0.04 segundos, y por su crecimiento logarítmico ($O(n \log n)$), la extrapolación indica que procesar el millón de registros tomaría apenas unos 10 segundos, entrando perfectamente en la ventana de tiempo.Por lo anterior, recomiendo explícitamente que Tamiza debe ejecutar el algoritmo Merge Sort como solución definitiva. Sabemos que el canal de entrada puede cambiar sin aviso, y aunque Insertion Sort es muy rápido cuando los datos llegan casi ordenados (Escenario B), el sistema colapsa si entra un lote aleatorio del portal web o si migran datos al revés desde el sistema legado, y el equipo de ingeniería no debería mantener tres implementaciones distintas del código dependiendo la procedencia de los datos ya que esto aumenta la complejidad y el costo de mantenimiento, por lo cual unificar el proceso bajo Merge Sort nos garantiza un rendimiento óptimo y estable sin importar cómo lleguen los registros.Finalmente, se debe considerar una métrica distinta del tiempo puro, ya que a diferencia de Insertion Sort, Merge Sort no ordena los datos en la misma lista sino que consume memoria adicional al crear nuevas sublistas temporales para dividir y mezclar los registros, lo cual implica un mayor uso de RAM en el servidor, pero teniendo en cuenta que solo estamos ordenando números enteros (los índices de riesgo), este consumo será de unos pocos megabytes adicionales, lo cual es un impacto totalmente marginal para los servidores actuales y justifica por completo asegurar que el centro de llamadas tenga su lista completa todos los días a las 6:00 a. m.