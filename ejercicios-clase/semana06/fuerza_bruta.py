import matplotlib.pyplot as plt
from pathlib import Path

def subarreglo_maximo_por_fuerza_bruta(arreglo: list) -> tuple[int, int, float, int]:

    """
    Encuentra el subarreglo de mayor suma en un arreglo original calculando todas las posibles combinaciones

    Args: 
    arreglo: arreglo a procesar para extraer el maximo subarreglo 

    Returns:
    Una tupla con el subarreglo de mayor suma, la suma del subarreglo, el tiempo de ejecución y el número total de comparaciones entre elementos realizadas durante el proceso.
    """

    n = len(arreglo)
    mejor_inicio, mejor_fin = 0, 0
    suma_maxima = float ('-inf')
    operaciones = 0

    for i in range(n):
        operaciones += 1
        for j in range(i, n):
            suma = 0
            operaciones += 1
            for k in range(i, j + 1):
                operaciones += 1
                suma += arreglo[k]
            if suma > suma_maxima:
                suma_maxima = suma
                mejor_inicio = i
                mejor_fin = j

    return mejor_inicio, mejor_fin, suma_maxima, operaciones

def grafdicas_operaciones(tamanios: list[int], resultados: list[int])-> None:
    """
    Genera una gráfica de operaciones vs tamaño de entrada.

    Args:
        tamanios: lista de tamaños de entrada.
        resultados: lista de resultados correspondientes a cada tamaño de entrada.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(tamanios, resultados, marker='o', linestyle='-', color='b')
    plt.title('Número de Operaciones vs Tamaño de Entrada')
    plt.xlabel('Tamaño de Entrada')
    plt.ylabel('Número de Operaciones')
    plt.grid(True)
    plt.tight_layout()
    
    carpeta_actual = Path(__file__).resolve().parent
    ruta_grafica = carpeta_actual / "graficas" / "fuerza_bruta_operaciones.png"
    
    plt.savefig(ruta_grafica)
    print(f"Gráfica generada: {ruta_grafica}")

if __name__ == "__main__":
    arreglo = [-2, 1, -3, 4, -1 ,2, 1, -5, 4]
    inicio, fin, suma, operaciones = subarreglo_maximo_por_fuerza_bruta(arreglo)
    print(f"Subarreglo de mayor suma: {arreglo[inicio:fin + 1]}")
    print(f"Suma del subarreglo: {suma}")
    print( inicio, fin, suma, operaciones)