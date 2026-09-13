import math 
import matplotlib.pyplot as plt

def trabajo_aproximado_del_algoritmo_a(n: int) -> float:
    """Estima el trabajo del algoritmo A para tamano n de datos. 
    
    Args: 
        n: tamaño de los datos de entrada.
    
    Returns: 
        Trabajo aproximado del algoritmo A (El numero de operaciones que realiza el algoritmo)
    """

    return n ** 2 

def trabajo_aproximado_del_algoritmo_b(n: int) -> float:
    """Estima el trabajo del algoritmo B para tamano n de datos. 
    
    Args: 
        n: tamaño de los datos de entrada.  
    
    Returns:   
        Trabajo aproximado del algoritmo B (El numero de operaciones que realiza el algoritmo)

    """

    return n* math.log(n)

def graticar_y_comprar_algoritmos(tamanos: list[int],  ruta_salida: str) -> None:
    """Grafica y compara el trabajo de los algoritmos A y B para diferentes tamaños de datos. 
    
    Args: 
        tamanos: lista de tamaños de datos para los cuales se desea estimar el trabajo de los algoritmos.
    
    Returns: 
        None
    """
    trabajos_a = [trabajo_aproximado_del_algoritmo_a(n) for n in tamanos]
    trabajos_b = [trabajo_aproximado_del_algoritmo_b(n) for n in tamanos]
    trabajo_a_hardware_rapido = [valor / 2 for valor in trabajos_a]

    plt.figure(figsize=(8, 5))
    plt.plot(tamanos, trabajos_a, label="Algoritmo A (n**2)")
    plt.plot(tamanos, trabajos_b, label= "Algoritmo B (n*log(n))")
    plt.plot(tamanos, trabajo_a_hardware_rapido, label="Algoritmo A (hardware rápido)")
    plt.xlabel("Tamaño de los datos (n)")
    plt.ylabel("Trabajo aproximado del algoritmo")
    plt.title("Comparación del trabajo de los algoritmos A y B")
    plt.grid(True)
    plt.savefig(ruta_salida)

if __name__ == "__main__":
    tamanos = [10, 100, 500, 1000, 5000, 10000, 30000]
    graticar_y_comprar_algoritmos(tamanos, "graficas/clase-1/algotimos_a_vs_b.png")
