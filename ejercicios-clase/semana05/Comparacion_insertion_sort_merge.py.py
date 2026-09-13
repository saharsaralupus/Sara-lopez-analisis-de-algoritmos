import math
import random   
import matplotlib.pyplot as plt
from time import perf_counter

def insertion_sort(arreglo: list, puntos_de_control: set[int]) -> list:
    """
    Ordena una lista de menor a mayor usando el método de insercion  

    Args: 
    arreglo: lista de elementos a ordenar.
    Returns: 
    lista ordenada de menor a mayor.
    """
    for i in range(1, len(arreglo)):
        if i in puntos_de_control:
            assert arreglo[:i] == sorted(arreglo[:i]), f"Error: El arreglo no está ordenado hasta el índice {i}"
        clave = arreglo[i]
        j = i - 1

        while j >= 0 and arreglo[j] > clave:
            arreglo[j + 1] = arreglo[j]
            j -= 1
        arreglo[j + 1] = clave
    return arreglo

if __name__ == "__main__":
    arreglo = [6,5,4,3,2,1, True]
    n = len(arreglo)
    puntos = {2, n//2, n-1}
    arreglo_ordenado = insertion_sort(arreglo, puntos)
    print(arreglo_ordenado)  # Salida: [1, 2, 3, 4, 5, 6]


def medir(algoritmo, tamanio: int, repeticiones: int = 3) -> float:
    """
    Mide el tiempo de ejecución de un algoritmo de ordenamiento

    Args:
        algoritmo: función de ordenamiento a medir
        tamanio: tamaño del arreglo a ordenar

    Returns:
        Tiempo de ejecución en segundos
    """
    tiempo_total = 0.0
    for _ in range(repeticiones):
        datos = [random.randint(0, 10000) for _ in range(tamanio)]
        inicio = perf_counter()
        algoritmo(datos)
        fin = perf_counter()
        tiempo_total += fin - inicio
    return min(tiempos)


if __name__ == "__main__":
    tamanio = [10,50,100,200,400,800,1000,2000,4000,8000]
    tiempos_insertion_sort = []
    tiempos_merge_sort = []

    for n in tamanio:
        tiempo_insertion = medir(insertion_sort, n)
        tiempos_insertion_sort.append(tiempo_insertion)

    for n in tamanio:
        tiempo_merge = medir(merge_sort, n)
        tiempos_merge_sort.append(tiempo_merge)
        