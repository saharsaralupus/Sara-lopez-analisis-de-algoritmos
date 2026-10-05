# Retroalimentación — Laboratorio evaluativo 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Sara López Cardona · **Laboratorio:** Fundamentos, complejidad y recurrencias (Plataforma Tamiza)
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `3ce9c2a`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 25 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 11 / 20 |
| Calidad del análisis de las gráficas | 11 / 20 |
| Documentación y organización del informe | 5 / 10 |
| **Total** | **73 / 100** |
| **Nota (0–5)** | **3.65** |

## 1. Corrección conceptual (25 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que llegue a tiempo, y nombra la ventana de cuatro horas como la restricción que se incumple.
- Explica por qué duplicar el servidor solo gana tiempo: si los datos se duplican, el trabajo se cuadruplica.
- Su ejemplo propio (el flujo de indemnizaciones) trae cifras y una restricción concreta.
- En la Parte 2 relaciona tiempo con energía acumulada y señala dos perjuicios, indicando quién asume el costo (el paciente y el operador del centro de contacto).
- Reconoce que el orden de la lista exige una corrección estricta, porque decide a quién se llama primero.

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define mejor, peor y promedio indicando sobre qué entradas se toman, y justifica usar el peor caso por la ventana estricta.
- Escribió la predicción antes de medir y la contrastó después.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro (a = 2, b = 2, caso 2) hasta `Θ(n log n)`.
- Presenta la tabla línea a línea de insertion sort y la tabla de complejidades.

**Lo que puede mejorar:**
- En el método maestro conviene escribir la condición del caso de forma explícita (`f(n) = Θ(n^(log_b a))`) y no solo decir que "es igual".
- La tabla línea a línea tiene el código escrito distinto al que realmente entregó (por ejemplo, la condición del `while`), y solo cubre el peor caso. Debe corresponder a su implementación.

## 3. Corrección de la implementación (11 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no modifican la lista recibida y cuentan comparaciones entre elementos. Merge sort tiene su propia mezcla recursiva.
- Los generadores producen lotes del tamaño pedido, sin repetidos y con semilla.

**Lo que puede mejorar:**
- `parte3_casos.py` se detiene con un error al guardar la gráfica de comparaciones, porque escribe en una carpeta con otro nombre (`Lab_Fundamentos_Complejidad_Recurrencia`) que no existe. Hay que usar rutas relativas a la carpeta del propio archivo, como hizo en el tiempo.
- `generar_casi_ordenado` usa `list.sort()`; la regla pide no usar funciones de ordenamiento de Python, así que debe construir ese 98 % de otra forma.
- Los archivos de las partes 3 y 4 tienen funciones sin type hints ni docstrings, y hay varios avisos de estilo PEP 8 (espacios al final de línea, líneas en blanco de más, imports sin ordenar).

## 4. Calidad del análisis de las gráficas (11 / 20)
**Lo que hizo bien:**
- Las dos gráficas de la Parte 3 tienen título, ejes y leyenda, con los tres escenarios en los mismos ejes.
- Identifica con cifras el peor caso (C), el mejor (B) y el parecido al promedio (A), y lo contrasta con su predicción.
- El concepto técnico de 4.3 recomienda merge sort, responde a la propuesta del servidor, hace la extrapolación a 1.200.000 registros declarándola como estimación y discute la memoria extra.

**Lo que puede mejorar:**
- La gráfica de la Parte 4 solo muestra la curva de merge sort: falta la de insertion sort en los mismos ejes, que es justo la comparación que se pedía.
- Falta la sección 4.2: no hay conclusión leída desde la gráfica ni contraste con las complejidades de 4.1, ni explicación de qué pasa con tamaños pequeños.
- En 4.3 dice que insertion sort tardó 2,5 s con 10.000 registros, pero ese dato no aparece en su gráfica; todo dato citado debe poder verse en ella.
- La extrapolación de merge sort no explica el razonamiento con `n log n`; solo da un resultado.

## 5. Documentación y organización del informe (5 / 10)
**Lo que hizo bien:**
- Carpeta del laboratorio en una ubicación aceptada, con los archivos y gráficas pedidos, imágenes que se ven y enlaces al código en cada parte.
- Más de cinco commits con mensajes descriptivos.

**Lo que puede mejorar:**
- El informe no trae su nombre completo ni las instrucciones para reproducir los experimentos.
- Quedaron archivos que no deben subirse (`__pycache__` y una carpeta de gráficas de clase dentro del laboratorio).
- La nota final sobre la estructura da una ruta (`laboratorio/...`) que no coincide con la real.

## ¿El código funciona?
Los dos algoritmos ordenan bien. El script de la Parte 4 corre, pero la gráfica solo incluye merge sort. El script de la Parte 3 falla al guardar la primera gráfica, aunque las imágenes publicadas sí existen.

## Para el próximo laboratorio
- Probar los scripts desde cero en una carpeta limpia antes de entregar y usar rutas relativas.
- Incluir su nombre y los comandos para reproducir cada parte en el informe.
- Graficar todas las curvas pedidas y escribir cada parte del enunciado, sin saltarse subsecciones como la 4.2.
- Cumplir PEP 8 y poner type hints y docstrings en todas las funciones; no subir archivos temporales.
- Citar solo datos que se puedan ver en sus gráficas.
