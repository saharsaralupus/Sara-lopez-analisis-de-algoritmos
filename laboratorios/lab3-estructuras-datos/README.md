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
3. La colisión forzada con $m = 7$: las guías `10`, `24` y `17` dan `hash(guia) == 3`, se encadenan en `casillas[3]` alcanzando longitud 3, se recuperan sus estados individules sin pérdida y `factor_carga()` devuelve exactamente `3 / 7`.
4. Veinticinco colecciones aleatorias (semilla fija `2026`, tamaños entre 10 y 150 y distintos $m$ primos) comprobando que `ListaEnlazada` y `TablaHash` coinciden en todas las guías existentes y en 30 guías inexistentes por colección.

## Parte 2 — Medir y graficar

Código: [medicion.py](medicion.py).

### Experimento A: Lista enlazada frente a tabla hash

![Lista vs Tabla](graficas/lista_vs_tabla.png)

| $n$ (guías) | $m$ (casillas) | $\alpha = n/m$ | Lista enlazada (µs) | Tabla hash (µs) |
|---:|---:|---:|---:|---:|
| 100 | 53 | 1,89 | 2,654 | 0,133 |
| 500 | 251 | 1,99 | 15,309 | 0,251 |
| 1.000 | 503 | 1,99 | 34,646 | 0,342 |
| 5.000 | 2.503 | 2,00 | 171,622 | 0,418 |
| 20.000 | 10.007 | 2,00 | 598,321 | 0,382 |
| 50.000 | 25.013 | 2,00 | 1.733,564 | 0,409 |

### Experimento B: Efecto del factor de carga ($\alpha$) con $n = 20.000$ fijo

![Tiempo vs Alfa](graficas/tiempo_vs_alfa.png)

| $m$ (casillas) | $\alpha = n/m$ | Tabla hash (µs) |
|---:|---:|---:|
| 40.009 | 0,50 | 0,103 |
| 20.011 | 1,00 | 0,118 |
| 10.007 | 2,00 | 0,160 |
| 5.003 | 4,00 | 0,206 |
| 2.503 | 7,99 | 0,332 |
| 2.003 | 9,99 | 0,405 |

**Nota metodológica:** Se generaron guías únicas de 10 dígitos con semilla fija (`42`) y 200 guías inexistentes con `generar_guias_inexistentes` (semilla `7`), usando exactamente los mismos datos en ambas estructuras y verificando antes de medir que una muestra de 50 guías existentes devuelve el mismo estado. En el Experimento A se eligió un primo $m \approx n/2$ para mantener $\alpha \approx 2$. Solo se cronometraron las 200 búsquedas con `time.perf_counter()`, repitiendo 5 veces cada prueba con el recolector de basura pausado y tomando el mínimo para filtrar el ruido del sistema operativo.
