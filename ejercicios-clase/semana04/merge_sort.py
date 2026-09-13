def merge_sort(arreglo: list[int]) -> list[int]:
    """
    Ordena una lista de menor a mayor mediante merge sort (dividir y vencer)
    Arg: 
        arreglo: lista de elementois a ordenar

    Returns: 
        Lista de elementos ordenados
    """

    # Caso base 
    if len(arreglo) <= 1:
        return arreglo

    # Caso recursivo 
    mitad = len(arreglo) // 2
    izquierda = arreglo [:mitad]
    derecha = arreglo [mitad:]

    return merge(izquierda, derecha)


def merge(izquierda: list[int], derecha: list[int]) -> list[int]:
    """
    Combina dos listas ya ordenadas en una lista ordenada 
    
    Args: 
    Izquierda: Lista ordenada de menor a mayor del subarreglo a la izquierda
    Derecha: Lista ordenada de menor a mayor del subarreglo a la derecha 

    Returns: 
    Una lista ordenada con todos los elementos de izquierda y derecha
    """

    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


if __name__ == "__main__":
    arreglo = [38, 27, 43, 3, 9 , 82, 10]
    merge_sort(arreglo)