# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Sara López Cardona · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `2e7305d`

Muy buen trabajo en general: el código es correcto y el informe es completo.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 16 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 16 / 25 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **86 / 100** |
| **Nota (0–5)** | **4.30** |

## 1. Corrección conceptual (16 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar entre n = 10 y n = 50, y explica bien por qué: las llamadas recursivas tienen un costo fijo que pesa con pocos datos.
- La comparación con el máximo de un arreglo es correcta: `T(n) = 2T(n/2) + Θ(1)` da `Θ(n)`, igual que recorrerlo una vez, y explica por qué en el subarreglo máximo sí conviene dividir.
- Recomienda divide y vencerás, declara que es una estimación y no usa regla de tres lineal.

**Lo que puede mejorar:**
- Varias cifras del texto no coinciden con su propia gráfica y su tabla. Por ejemplo, en n = 16.000 la gráfica muestra la fuerza bruta cerca de 7.600 ms, pero el texto usa 8.800 ms. Lo mismo pasa con los valores de n = 10, 50 y 2.000. Con ello la estimación a 1.000.000 de registros parte de datos que no son los publicados.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` explicando de dónde sale cada término, verifica `f(n) = Θ(n^(log_b a))` y aplica correctamente el caso 2.
- Justifica el `Θ(n²)` de la fuerza bruta contando los n(n+1)/2 pares.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias; no se modifica la lista recibida.
- `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- Tiene type hints y docstrings estilo Google en las funciones.


## 4. Calidad del análisis de las gráficas (16 / 25)
**Lo que hizo bien:**
- La gráfica tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, con 9 tamaños y vista lineal y log-log. Se ve bien.
- Calcula factores de crecimiento al duplicar n y los compara con `Θ(n²)` y `Θ(n log n)`.

**Lo que puede mejorar:**
- Los factores se calculan con valores que no están en la gráfica ni en la tabla (616 y 2.592 ms). Con lo publicado, de 4.000 a 8.000 la fuerza bruta pasa de unos 640 a unos 1.930 ms (factor cercano a 3, no 4,2), y de 8.000 a 16.000 el factor es cercano a 4. Las conclusiones deben apoyarse en lo que se lee en su gráfica.
- La curva de divide y vencerás casi no cambia entre 2.000 y 4.000; podría mencionar que es ruido de medición.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Carpeta en la ubicación acordada, informe en el orden pedido, gráfica visible, enlaces al código, instrucciones de reproducción y los tres commits del laboratorio.

**Lo que puede mejorar:**
- Los mensajes de commit ("parte 3 analisis") podrían ser más descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y ambos algoritmos dan la misma suma. La medición está diseñada para generar la gráfica sin problemas.

## Para el próximo laboratorio
- Después de medir, copie al informe los valores exactos de su tabla o gráfica y use solo esos en los cálculos.
- Revise que cada cifra citada en el análisis coincida con lo publicado.
- Escriba mensajes de commit que digan qué cambió.
