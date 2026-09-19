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

            if arr[j] < clave:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = clave
        
    return arr, comparaciones



def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    if len(datos) <= 1:
        return datos.copy(), 0
        
    mid = len(datos) // 2

    izq, comp_izq = merge_sort(datos[:mid])
    der, comp_der = merge_sort(datos[mid:])
    
    mezcla = []

    comparaciones = comp_izq + comp_der
    i = j = 0
    

    while i < len(izq) and j < len(der):
        comparaciones += 1

        if izq[i] >= der[j]:
            mezcla.append(izq[i])
            i += 1
        else:
            mezcla.append(der[j])
            j += 1
            

    mezcla.extend(izq[i:])
    mezcla.extend(der[j:])
    
    return mezcla, comparaciones