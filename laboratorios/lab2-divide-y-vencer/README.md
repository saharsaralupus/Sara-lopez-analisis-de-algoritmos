# Laboratorio evaluativo 02 - Dividir y vencer

**Autora:** Sara López Cardona

## Cómo reproducir

Desde la raíz del repositorio (PowerShell):

```powershell
venv\Scripts\Activate.ps1
cd laboratorios\lab2-divide-y-vencer
python pruebas.py     # pruebas con assert
python medicion.py    # mediciones y graficas/tiempo_vs_n.png
```

## Parte 1 - Implementar y verificar

Código: [subarreglo.py](subarreglo.py) y [pruebas.py](pruebas.py).

`pruebas.py` usa `assert` y cubre la serie de ocho días (suma 17, tramo días 2 a 7), un solo elemento, todos negativos (gana el menos negativo), todos positivos (gana toda la serie), un caso donde el mejor tramo cruza el punto medio (`[-10,-10,6,7,8,9,-10,-10]`, suma 30), comprobación de que la lista no se modifica y 50 listas aleatorias (semilla fija) donde ambas funciones dan la misma suma, comparando sumas y no índices. Además verifica que la suma del tramo devuelto coincide con la suma reportada.

## Parte 2 - Medir y graficar

Código: [medicion.py](medicion.py).

![Tiempo vs n](graficas/tiempo_vs_n.png)

Medición: datos enteros en [-100, 100] con semilla fija (36), la misma lista para ambos algoritmos en cada tamaño. Solo se cronometra la llamada con `time.perf_counter()`. Cada medición se repitió 3 veces y se grafica la **mediana**. En cada tamaño se verifica que ambas sumas coincidemn. La figura muestra escala lineal (izquierda) y log-log (derecha).

| n | Fuerza bruta (ms) | Divide y vencerás (ms) |
|---:|---:|---:|
| 10 | 0,00489 | 0,00789 |
| 50 | 0,128 | 0,109 |
| 100 | 0,338 | 0,144 |
| 500 | 0,659 | 0,629 |
| 1000 | 35,340 | 1,682 |
| 2000 | 237,89 | 5,784 |
| 4000 | 639,181 | 5,919 |
| 8000 | 1934,41 | 13,280 |
| 16000 | 7605,286 | 25,934 |

## Parte 3 - Análisis

**1. Recurrencia.** `subarreglo_maximo` hace 2 llamadas recursivas, cada una sobre la mitad del rango (n/2), y además `suma_cruzada`, que recorre los n elementos una sola vez (Θ(n)); elegir el mejor de los tres casos cuesta Θ(1). Entonces T(n) = 2T(n/2) + Θ(n), con T(1) = Θ(1). Método maestro: a = 2, b = 2, f(n) = Θ(n); n^(log_b a) = n¹ = n. Como f(n) = Θ(n^(log_b a)) se aplica el caso 2, y T(n) = Θ(n log n). La fuerza bruta tiene un ciclo externo con i de 0 a n-1 y uno interno con j de i a n-1; en total hay n + (n-1) + … + 1 = n(n+1)/2 pares y cada uno cuesta O(1) porque la suma se acumula, así que es Θ(n²).

**2. Medido contra esperado.** En la gráfica lineal la fuerza bruta se dispara en forma de parábola (unos 8.800 ms en n = 16.000), mientras que divide y vencerás casi parece pegada al eje (unos 33 ms), con crecimiento casi lineal. Al duplicar de 4.000 a 8.000: fuerza bruta 616 → 2.592 ms, factor ≈ 4,2; divide y vencerás 7,14 → 16,45 ms, factor ≈ 2,3. De 8.000 a 16.000: factores ≈ 3,4 y ≈ 2,0. Θ(n²) predice ×4, y coincide (con algo de ruido). Θ(n log n) predice un poco más de ×2 (≈ 2,2 entre 4.000 y 8.000), y lo medido (2,3 y 2,0) coincide.

**3. Tamaños pequeños.** Sí hay cruce: con n = 10 la fuerza bruta es más rápida (0,0083 contra 0,0138 ms), pero con n = 50 ya gana divide y vencerás (0,078 contra 0,098 ms). El cruce queda entre 10 y 50. Aparece ahí porque la recursión paga llamadas a funciones, creación de tuplas y el barrido cruzado, costos constantes grandes que el doble ciclo simple no tiene; con pocos datos n² todavía es pequeño y esos costos pesan más. A partir de n = 100 la ventaja ya es de 2,4 veces, y en 16.000 de unas 270.

**4. ¿Cuándo conviene dividir?** Para el máximo de un arreglo, dividir da T(n) = 2T(n/2) + Θ(1) (combinar es comparar dos números). Por el método maestro, n^(log₂2) = n domina a f(n) = Θ(1) (caso 1) y T(n) = Θ(n): igual que recorrer una vez, con el sobrecosto de la recursión. No mejora, en el subarreglo máximo dividir sí ayuda porque el rival no es lineal sino Θ(n²), y combinar cuesta solo Θ(n): se pasa de n² a n log n. Dividir conviene cuando el problema directo cuesta más que el combinar sumado a la división.

**5. Recomendación para la gerente.** Recomiendo divide y vencerás. Para 2.000 días ambos son rápidos (158 ms contra 4 ms), pero con series de sensores la fuerza bruta se vuelve inviable. **Es una estimación**, no una medición. Parto de n = 16.000. Para 1.000.000 el factor es 62,5. Fuerza bruta (cuadrática): 8,8 s × 62,5² ≈ 34.000 s, cerca de 9 horas. Divide y vencerás (n log n): 33 ms × 62,5 × (log 10⁶ / log 16.000 ≈ 1,43) ≈ 3 s. No uso regla de tres lineal porque la fuerza bruta crece con el cuadrado del factor y divide y vencerás lleva el factor logarítmico adicional. Los valores reales variarán con la máquina y la memoria.
