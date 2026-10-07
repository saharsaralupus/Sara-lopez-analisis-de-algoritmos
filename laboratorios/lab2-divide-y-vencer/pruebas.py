"""Pruebas del subarreglo maximo."""
import random

from subarreglo import (
    subarreglo_fuerza_bruta,
    subarreglo_maximo,
    suma_cruzada,
)


def dyv(serie):
    return subarreglo_maximo(serie, 0, len(serie) - 1)


def suma_tramo(serie, resultado):
    return sum(serie[resultado[0]:resultado[1] + 1])


# Serie de ocho dias de la situacion problema
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
copia = serie[:]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert dyv(serie)[2] == 17
assert dyv(serie)[:2] == (1, 6)
assert serie == copia

# Un solo elemento
assert subarreglo_fuerza_bruta([7])[2] == 7
assert dyv([7])[2] == 7
assert dyv([-7]) == (0, 0, -7)

# Todos negativos: el mejor tramo es el elemento menos negativo
neg = [-8, -3, -5, -1, -9]
assert subarreglo_fuerza_bruta(neg)[2] == -1
assert dyv(neg)[2] == -1

# Todos positivos: el mejor tramo es toda la serie
pos = [4, 1, 7, 2, 9, 3]
assert subarreglo_fuerza_bruta(pos)[2] == 26
assert dyv(pos)[2] == 26
assert dyv(pos)[:2] == (0, 5)

# Caso cruzado: el mejor tramo (indices 2..5) cruza el punto medio (3|4)
cruz = [-10, -10, 6, 7, 8, 9, -10, -10]
assert suma_cruzada(cruz, 0, 3, 7)[2] == 30
assert dyv(cruz) == (2, 5, 30)
assert subarreglo_fuerza_bruta(cruz)[2] == 30

# Listas aleatorias: ambas funciones deben coincidir en la suma
random.seed(2026)
for _ in range(50):
    n = random.randint(1, 60)
    datos = [random.randint(-100, 100) for _ in range(n)]
    fb = subarreglo_fuerza_bruta(datos)
    dv = dyv(datos)
    assert fb[2] == dv[2], (datos, fb, dv)
    assert suma_tramo(datos, fb) == fb[2]
    assert suma_tramo(datos, dv) == dv[2]

print("Todas las pruebas pasaron.")
