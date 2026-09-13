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

        