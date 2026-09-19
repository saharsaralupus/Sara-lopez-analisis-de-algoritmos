import time
import random
import matplotlib.pyplot as plt
from pathlib import Path
from algoritmos import merge_sort
from algoritmos import insertion_sort 

def generar_escenario_A(tamano: int) -> list[int]:
    """Cargue directo: datos totalmente aleatorios sin orden."""
    return [random.randint(0, 1000) for _ in range(tamano)]

def ejecutar_medicion():

    tamanos = [100, 500, 1000, 2000, 5000, 10000, 15000]
    
    tiempos_merge = []
    tiempos_insertion = []
    
    print("Iniciando medición comparativa...")
    
    for n in tamanos:
        datos = generar_escenario_A(n)
        
     
        t0_merge = time.perf_counter()
        merge_sort(datos)
        t1_merge = time.perf_counter()
        tiempos_merge.append(t1_merge - t0_merge)
        

        t0_ins = time.perf_counter()
        insertion_sort(datos)
        t1_ins = time.perf_counter()
        tiempos_insertion.append(t1_ins - t0_ins)   
        
        print(f"N={n:5d} | Merge: {tiempos_merge[-1]:.5f}s")



    plt.figure(figsize=(10, 6))
    
    plt.plot(tamanos, tiempos_merge, label='Merge Sort', marker='o', linewidth=2)

    
    plt.title('Tiempo de Ejecución vs. Tamaño de Entrada (Escenario A - Aleatorio)')
    plt.xlabel('Tamaño de entrada (cantidad de registros)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    carpeta_actual = Path(__file__).resolve().parent


    ruta_grafica = carpeta_actual / "graficas" / "parte4_tiempo.png"


    plt.savefig(ruta_grafica)

    print(f"Gráfica generada: {ruta_grafica}")
    print("Gráfica generada: parte4_tiempo.png")

if __name__ == "__main__":
    ejecutar_medicion()