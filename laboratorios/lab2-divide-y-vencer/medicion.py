"""Medicion del tiempo de ambos algoritmos y grafica tiempo vs. n."""
import os
import random
import statistics
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt 

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo  

TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000, 16000]
REPETICIONES = 3
SEMILLA = 36


def medir(tamanos: list[int]) -> tuple[list[float], list[float]]:
    """Mide ambos algoritmos (mediana de varias repeticiones, en ms).

    Args:
        tamanos: tamanos de entrada a medir.

    Returns:
        Dos listas de tiempos en milisegundos: fuerza bruta y divide
        y venceras, en el mismo orden que tamanos.
    """
    rng = random.Random(SEMILLA)
    t_fb: list[float] = []
    t_dv: list[float] = []
    for n in tamanos:
        datos = [rng.randint(-100, 100) for _ in range(n)]
        tiempos_fb = []
        tiempos_dv = []
        for _ in range(REPETICIONES):
            ini = time.perf_counter()
            res_fb = subarreglo_fuerza_bruta(datos)
            tiempos_fb.append((time.perf_counter() - ini) * 1000)

            ini = time.perf_counter()
            res_dv = subarreglo_maximo(datos, 0, n - 1)
            tiempos_dv.append((time.perf_counter() - ini) * 1000)

            assert res_fb[2] == res_dv[2], f"Sumas distintas en n={n}"
        t_fb.append(statistics.median(tiempos_fb))
        t_dv.append(statistics.median(tiempos_dv))
        print(f"n={n:>6}  fuerza bruta={t_fb[-1]} ms  "
              f"divide y venceras={t_dv[-1]} ms", flush=True)
    return t_fb, t_dv


def graficar(tamanos: list[int], t_fb: list[float],
             t_dv: list[float]) -> None:
    """Genera graficas/tiempo_vs_n.png (escala lineal y logaritmica).

    Args:
        tamanos: tamanos de entrada medidos.
        t_fb: tiempos de fuerza bruta en milisegundos.
        t_dv: tiempos de divide y venceras en milisegundos.
    """
    carpeta = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "graficas")
    os.makedirs(carpeta, exist_ok=True)
    fig, ejes = plt.subplots(1, 2, figsize=(13, 5))
    for ax, escala in zip(ejes, ("linear", "log")):
        ax.plot(tamanos, t_fb, "o-", color="tab:red",
                label="Fuerza bruta")
        ax.plot(tamanos, t_dv, "s-", color="tab:blue",
                label="Divide y venceras")
        ax.set_xscale(escala)
        ax.set_yscale(escala)
        ax.set_xlabel("Tamano de entrada n (numero de dias)")
        ax.set_ylabel("Tiempo de ejecucion (ms)")
        ax.grid(True, alpha=0.3)
        ax.legend()
    ejes[0].set_title("Subarreglo maximo: tiempo vs. n (escala lineal)")
    ejes[1].set_title("Subarreglo maximo: tiempo vs. n (escala log-log)")
    fig.tight_layout()
    fig.savefig(os.path.join(carpeta, "tiempo_vs_n.png"), dpi=130)


if __name__ == "__main__":
    fb, dv = medir(TAMANOS)
    graficar(TAMANOS, fb, dv)
    print("Grafica guardada en graficas/tiempo_vs_n.png")