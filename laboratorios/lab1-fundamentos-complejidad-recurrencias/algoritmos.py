"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arr = list(datos)
    comparaciones = 0
    n = len(arr)
    
    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        
        while j >= 0:
            comparaciones += 1
            # Tamiza requiere ordenar de mayor a menor (orden decreciente)
            if arr[j] < clave:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = clave
        
    return arr, comparaciones
