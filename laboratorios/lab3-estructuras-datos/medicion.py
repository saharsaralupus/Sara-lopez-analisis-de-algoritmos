"""Medicion experimental de ListaEnlazada y TablaHash."""
import gc
import os
import random
import time

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

# Pares (n, m) donde m es primo cercano a n / 2 (alfa ~ 2)
CONFIG_EXP_A: list[tuple[int, int]] = [
    (100, 53),
    (500, 251),
    (1000, 503),
    (5000, 2503),
    (20000, 10007),
    (50000, 25013),
]

# Con n = 20000 fijo, m primos para variar alfa entre ~0.5 y 10
N_FIJO_EXP_B = 20000
M_VALORES_EXP_B: list[int] = [40009, 20011, 10007, 5003, 2503, 2003]

NUM_BUSQUEDAS = 200
REPETICIONES = 5
SEMILLA_DATOS = 42
ESTADOS = ("en bodega", "en reparto", "entregado", "en transito")


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def generar_coleccion(
    n: int, semilla: int = SEMILLA_DATOS
) -> tuple[list[tuple[int, str]], set[int]]:
    """Genera n pares (guia, estado) unicos de diez digitos con semilla fija.

    Args:
        n: cantidad de guias a generar.
        semilla: semilla del generador aleatorio.

    Returns:
        Una tupla con la lista de pares (guia, estado) y el conjunto de guias.
    """
    azar = random.Random(semilla)
    existentes: set[int] = set()
    pares: list[tuple[int, str]] = []
    while len(pares) < n:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            existentes.add(guia)
            estado = ESTADOS[len(pares) % len(ESTADOS)]
            pares.append((guia, estado))
    return pares, existentes


def experimento_a() -> tuple[list[int], list[float], list[float]]:
    """Ejecuta el Experimento A: lista vs. tabla variando n con alfa ~ 2.

    Returns:
        Tres listas: valores de n, tiempos medios de lista (us) y tiempos
        medios de tabla (us) por busqueda inexistente.
    """
    ns: list[int] = []
    tiempos_lista_us: list[float] = []
    tiempos_tabla_us: list[float] = []

    print("=== Experimento A: Lista vs. Tabla (alfa ~ 2) ===")
    for n, m in CONFIG_EXP_A:
        pares, existentes = generar_coleccion(n, SEMILLA_DATOS + n)
        inexistentes = generar_guias_inexistentes(existentes, NUM_BUSQUEDAS)

        lista = ListaEnlazada()
        tabla = TablaHash(m)
        for guia, estado in pares:
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)

        # Verificacion sobre muestra de guias existentes
        muestra = pares[: min(50, n)]
        for guia, estado in muestra:
            res_l = lista.buscar(guia)
            res_t = tabla.buscar(guia)
            assert res_l == estado and res_t == estado, (
                f"Discrepancia en n={n} para guia {guia}"
            )

        rep_lista: list[float] = []
        rep_tabla: list[float] = []
        gc.collect()
        for _ in range(REPETICIONES):
            gc.disable()
            ini = time.perf_counter()
            for guia in inexistentes:
                res = lista.buscar(guia)
                assert res is None
            fin = time.perf_counter()
            gc.enable()
            rep_lista.append(((fin - ini) / NUM_BUSQUEDAS) * 1e6)

            gc.disable()
            ini = time.perf_counter()
            for guia in inexistentes:
                res = tabla.buscar(guia)
                assert res is None
            fin = time.perf_counter()
            gc.enable()
            rep_tabla.append(((fin - ini) / NUM_BUSQUEDAS) * 1e6)

        t_l = min(rep_lista)
        t_t = min(rep_tabla)
        ns.append(n)
        tiempos_lista_us.append(t_l)
        tiempos_tabla_us.append(t_t)
        print(
            f"n={n:>6} | m={m:>6} | alfa={tabla.factor_carga():.2f} | "
            f"Lista={t_l:>8.3f} us | Tabla={t_t:>6.3f} us",
            flush=True,
        )

    return ns, tiempos_lista_us, tiempos_tabla_us


def experimento_b() -> tuple[list[float], list[float]]:
    """Ejecuta el Experimento B: efecto del factor de carga alfa con n fijo.

    Returns:
        Dos listas: factores de carga alfa y tiempos medios de busqueda (us).
    """
    pares, existentes = generar_coleccion(N_FIJO_EXP_B, SEMILLA_DATOS)
    inexistentes = generar_guias_inexistentes(existentes, NUM_BUSQUEDAS)

    lista_ref = ListaEnlazada()
    for guia, estado in pares[:50]:
        lista_ref.insertar(guia, estado)

    alfas: list[float] = []
    tiempos_us: list[float] = []

    print(f"\n=== Experimento B: Tiempo vs. alfa (n = {N_FIJO_EXP_B}) ===")
    for m in M_VALORES_EXP_B:
        tabla = TablaHash(m)
        for guia, estado in pares:
            tabla.insertar(guia, estado)

        # Verificar muestra de existentes contra la lista de referencia
        for guia, _ in pares[:50]:
            assert tabla.buscar(guia) == lista_ref.buscar(guia)

        rep_tabla: list[float] = []
        gc.collect()
        for _ in range(REPETICIONES):
            gc.disable()
            ini = time.perf_counter()
            for guia in inexistentes:
                res = tabla.buscar(guia)
                assert res is None
            fin = time.perf_counter()
            gc.enable()
            rep_tabla.append(((fin - ini) / NUM_BUSQUEDAS) * 1e6)

        alfa = tabla.factor_carga()
        t_t = min(rep_tabla)
        alfas.append(alfa)
        tiempos_us.append(t_t)
        print(
            f"m={m:>6} | alfa={alfa:>5.2f} | Tabla={t_t:>6.3f} us",
            flush=True,
        )

    return alfas, tiempos_us


def graficar_experimento_a(
    ns: list[int], t_lista: list[float], t_tabla: list[float]
) -> None:
    """Genera graficas/lista_vs_tabla.png en escala lineal y log-log.

    Args:
        ns: valores de n medidos.
        t_lista: tiempos medios por busqueda en ListaEnlazada (us).
        t_tabla: tiempos medios por busqueda en TablaHash (us).
    """
    carpeta = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "graficas"
    )
    os.makedirs(carpeta, exist_ok=True)

    fig, ejes = plt.subplots(1, 2, figsize=(13, 5))
    for ax, escala in zip(ejes, ("linear", "log")):
        ax.plot(
            ns, t_lista, "o-", color="tab:red", label="Lista enlazada Θ(n)"
        )
        ax.plot(
            ns,
            t_tabla,
            "s-",
            color="tab:blue",
            label="Tabla hash (α ≈ 2) Θ(1 + α)",
        )
        ax.set_xscale(escala)
        ax.set_yscale(escala)
        ax.set_xlabel("Número de guías almacenadas n (unidades)")
        ax.set_ylabel("Tiempo medio por búsqueda inexistente (µs)")
        ax.grid(True, alpha=0.3)
        ax.legend()

    ejes[0].set_title("Tiempo de búsqueda vs. n (escala lineal)")
    ejes[1].set_title("Tiempo de búsqueda vs. n (escala log-log)")
    fig.tight_layout()
    fig.savefig(os.path.join(carpeta, "lista_vs_tabla.png"), dpi=130)
    plt.close(fig)


def graficar_experimento_b(
    alfas: list[float], t_tabla: list[float]
) -> None:
    """Genera graficas/tiempo_vs_alfa.png.

    Args:
        alfas: valores del factor de carga (n / m).
        t_tabla: tiempos medios por busqueda inexistente en TablaHash (us).
    """
    carpeta = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "graficas"
    )
    os.makedirs(carpeta, exist_ok=True)

    fig, ax = plt.subplots(figsize=(7.5, 5))
    ax.plot(
        alfas,
        t_tabla,
        "o-",
        color="tab:green",
        linewidth=2,
        label=f"Tabla hash (n = {N_FIJO_EXP_B} fijo)",
    )
    for a, t in zip(alfas, t_tabla):
        ax.annotate(
            f"({a:.2f}, {t:.2f} µs)",
            (a, t),
            textcoords="offset points",
            xytext=(0, 8),
            ha="center",
            fontsize=8,
        )
    ax.set_title("Tiempo medio de búsqueda inexistente vs. factor de carga α")
    ax.set_xlabel("Factor de carga α = n / m (guías por casilla)")
    ax.set_ylabel("Tiempo medio por búsqueda inexistente (µs)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(os.path.join(carpeta, "tiempo_vs_alfa.png"), dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    ns_a, tl_a, tt_a = experimento_a()
    graficar_experimento_a(ns_a, tl_a, tt_a)
    alfas_b, tt_b = experimento_b()
    graficar_experimento_b(alfas_b, tt_b)
    print("\nGraficas guardadas en graficas/lista_vs_tabla.png y "
          "graficas/tiempo_vs_alfa.png")
