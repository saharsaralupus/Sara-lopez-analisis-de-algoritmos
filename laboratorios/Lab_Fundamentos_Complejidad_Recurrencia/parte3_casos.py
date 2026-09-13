import os
import time
import matplotlib.pyplot as plt
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso
from algoritmos import insertion_sort
from typing import Any

# Configurar directorio de salida para gráficas
os.makedirs("graficas", exist_ok=True)

tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

resultados: dict[str, dict[str, list[Any]]] = {
    'A': {'n': [], 'comp': [], 'tiempo': []},
    'B': {'n': [], 'comp': [], 'tiempo': []},
    'C': {'n': [], 'comp': [], 'tiempo': []}
}
for n in tamanos:
    # Escenario A - Aleatorio
    data_A = generar_aleatorio(n)
    t0 = time.perf_counter()
    _, comp_A = insertion_sort(data_A)
    t1 = time.perf_counter()
    resultados['A']['n'].append(n)
    resultados['A']['comp'].append(comp_A)
    resultados['A']['tiempo'].append(t1 - t0)
    
    # Escenario B - Casi ordenado
    data_B = generar_casi_ordenado(n)
    t0 = time.perf_counter()
    _, comp_B = insertion_sort(data_B)
    t1 = time.perf_counter()
    resultados['B']['n'].append(n)
    resultados['B']['comp'].append(comp_B)
    resultados['B']['tiempo'].append(t1 - t0)
    
    # Escenario C - Inverso
    data_C = generar_inverso(n)
    t0 = time.perf_counter()
    _, comp_C = insertion_sort(data_C)
    t1 = time.perf_counter()
    resultados['C']['n'].append(n)
    resultados['C']['comp'].append(comp_C)
    resultados['C']['tiempo'].append(t1 - t0)

# Gráfica 1: Comparaciones vs Tamaño de entrada
plt.figure(figsize=(8, 5))
plt.plot(resultados['A']['n'], resultados['A']['comp'], 'o-', label='Escenario A (Aleatorio)')
plt.plot(resultados['B']['n'], resultados['B']['comp'], 's-', label='Escenario B (Casi Ordenado)')
plt.plot(resultados['C']['n'], resultados['C']['comp'], '^-', label='Escenario C (Orden Inverso)')
plt.title('Comparaciones vs. Tamaño de entrada (Insertion Sort)')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Número de Comparaciones')
plt.grid(True)
plt.legend()
plt.savefig('graficas/parte3_comparaciones.png')
plt.close()

# Gráfica 2: Tiempo vs Tamaño de entrada
plt.figure(figsize=(8, 5))
plt.plot(resultados['A']['n'], resultados['A']['tiempo'], 'o-', label='Escenario A (Aleatorio)')
plt.plot(resultados['B']['n'], resultados['B']['tiempo'], 's-', label='Escenario B (Casi Ordenado)')
plt.plot(resultados['C']['n'], resultados['C']['tiempo'], '^-', label='Escenario C (Orden Inverso)')
plt.title('Tiempo de Ejecución vs. Tamaño de entrada (Insertion Sort)')
plt.xlabel('Tamaño de entrada (n)')
plt.ylabel('Tiempo (segundos)')
plt.grid(True)
plt.legend()
plt.savefig('graficas/parte3_tiempo.png')
plt.close()

print("Experimento completado con éxito. Gráficas guardadas en graficas/")
