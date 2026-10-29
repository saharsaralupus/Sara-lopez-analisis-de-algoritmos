# Laboratorio evaluativo 03 — Estructuras de datos

**Autora:** Sara López Cardona

## Cómo reproducir

Desde la raíz del repositorio en PowerShell:

```powershell
venv\Scripts\Activate.ps1
cd laboratorios\lab3-estructuras-datos
python -B pruebas.py     # verifica ListaEnlazada y TablaHash con assert
python -B medicion.py    # ejecuta los experimentos A y B y genera las gráficas
```

## Parte 1 — Implementar y verificar

Código: [estructuras.py](estructuras.py) y [pruebas.py](pruebas.py).

En `estructuras.py` se implementaron `Nodo`, `ListaEnlazada` (con inserción al inicio en $\Theta(1)$ y búsqueda iterativa con ciclo `while`) y `TablaHash` con encadenamiento y función hash por división ($h(k) = k \bmod m$), reutilizando una `ListaEnlazada` en cada casilla sin recurrir a `dict`, `set` ni `hash()`.

El script `pruebas.py` verifica con `assert`:
1. Casos borde en una lista vacía y una tabla vacía (`tamano == 0`, `factor_carga() == 0.0` y búsqueda que retorna `None`).
2. Búsquedas exitosas e infructuosas sobre las cuatro guías del enunciado (`1000000010`, `1000000024`, `1000000017` y `1000000005`).
3. La colisión forzada con $m = 7$: las guías `10`, `24` y `17` dan `hash(guia) == 3`, se encadenan en `casillas[3]` alcanzando longitud 3, se recuperan sus estados individuales sin pérdida y `factor_carga()` devuelve exactamente `3 / 7`.
4. Veinticinco colecciones aleatorias (semilla fija `2026`, tamaños entre 10 y 150 y distintos $m$ primos) comprobando que `ListaEnlazada` y `TablaHash` coinciden en todas las guías existentes y en 30 guías inexistentes por colección.

