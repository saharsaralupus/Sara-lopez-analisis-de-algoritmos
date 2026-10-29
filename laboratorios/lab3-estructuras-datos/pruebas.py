"""Pruebas de ListaEnlazada y TablaHash."""
import random

from estructuras import ListaEnlazada, TablaHash

# 1. Prueba de lista vacia y tabla vacia
lista_vacia = ListaEnlazada()
assert lista_vacia.tamano == 0
assert lista_vacia.buscar(1000000010) is None

tabla_vacia = TablaHash(7)
assert tabla_vacia.tamano == 0
assert tabla_vacia.factor_carga() == 0.0
assert tabla_vacia.buscar(1000000010) is None

# 2. Serie de ejemplo de la situacion problema (busqueda exitosa e infructuosa)
ejemplos = [
    (1000000010, "en bodega"),
    (1000000024, "en reparto"),
    (1000000017, "en bodega"),
    (1000000005, "entregado"),
]
lista = ListaEnlazada()
tabla_ej = TablaHash(7)
for guia, estado in ejemplos:
    lista.insertar(guia, estado)
    tabla_ej.insertar(guia, estado)

assert lista.tamano == 4
assert tabla_ej.tamano == 4
for guia, estado in ejemplos:
    assert lista.buscar(guia) == estado
    assert tabla_ej.buscar(guia) == estado

assert lista.buscar(9999999999) is None
assert tabla_ej.buscar(9999999999) is None

# 3. Colision forzada con m = 7 y guias 10, 24 y 17 en la casilla 3
tabla = TablaHash(7)
estados_colision = {10: "en bodega", 24: "en reparto", 17: "entregado"}
for guia, estado in estados_colision.items():
    assert tabla.hash(guia) == 3
    tabla.insertar(guia, estado)

assert tabla.casillas[3].tamano == 3
assert tabla.factor_carga() == 3 / 7
for guia, estado in estados_colision.items():
    assert tabla.buscar(guia) == estado
assert tabla.buscar(99) is None
assert tabla.buscar(3) is None  # misma casilla 3, pero no insertada

# 4. Colecciones aleatorias (al menos 20): lista y tabla coinciden
azar = random.Random(2026)
estados_posibles = ["en bodega", "en reparto", "entregado", "en transito"]

for _ in range(25):
    n = azar.randint(10, 150)
    m = azar.choice([7, 13, 31, 53, 97])
    lista_rnd = ListaEnlazada()
    tabla_rnd = TablaHash(m)

    guias_vistas: set[int] = set()
    pares: list[tuple[int, str]] = []
    while len(pares) < n:
        g = azar.randint(10**9, 10**10 - 1)
        if g not in guias_vistas:
            guias_vistas.add(g)
            est = azar.choice(estados_posibles)
            pares.append((g, est))
            lista_rnd.insertar(g, est)
            tabla_rnd.insertar(g, est)

    assert lista_rnd.tamano == n
    assert tabla_rnd.tamano == n
    assert abs(tabla_rnd.factor_carga() - (n / m)) < 1e-12

    # Verificar todas las guias existentes
    for g, est in pares:
        res_lista = lista_rnd.buscar(g)
        res_tabla = tabla_rnd.buscar(g)
        assert res_lista == est
        assert res_tabla == res_lista

    # Verificar 30 guias inexistentes por coleccion
    for _ in range(30):
        g_no = azar.randint(10**9, 10**10 - 1)
        if g_no not in guias_vistas:
            assert lista_rnd.buscar(g_no) is None
            assert tabla_rnd.buscar(g_no) is None

print("Todas las pruebas pasaron.")
