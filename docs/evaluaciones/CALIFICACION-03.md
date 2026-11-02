# Retroalimentación — Lab 03 Estructuras de datos

**Estudiante:** Sara López Cardona · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `2f56792`

Excelente trabajo: un laboratorio completo, ordenado y bien sustentado con sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **98 / 100** |
| **Nota (0–5)** | **4.90** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y por qué ocurre aunque haya más casillas que guías, usando el ejemplo de 10, 24 y 17 con m = 7.
- Compara encadenamiento y direccionamiento abierto con ventajas y costos claros, e incluso muestra dónde quedaría cada guía con sondeo lineal.
- Justifica bien por qué la tabla no sirve para rangos, y compara el árbol degenerado (altura cercana a 400.000) con el equilibrado (alrededor de 18).
- Recomienda tabla hash más árbol balanceado y declara que la cifra para 5.000.000 es una estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- En la estimación para 5.000.000 de envíos, supone que la tabla seguirá tardando lo mismo que con 50.000, aunque usted misma notó en el informe que la tabla se hace más lenta al crecer por el uso de la memoria caché. No se aclara cuánto podría afectar eso.
  → *Cómo corregirlo:* revise su propia tabla de la Parte 2 (de n = 100 a n = 5.000) y explique si ese efecto pesa más al llegar a millones de guías; dé un rango en lugar de un solo valor.
- No se estima cuántas comparaciones totales harían las 400.000 inserciones ordenadas en el árbol degenerado, solo la búsqueda de una guía.
  → *Cómo corregirlo:* piense cuántos nodos recorre cada inserción nueva y cómo se acumulan.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el Θ(n) de la lista y el Θ(1 + α) de la tabla, nombra el hash uniforme simple y explica que si todas las guías caen en una casilla la tabla se vuelve una lista.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` inserta al inicio en tiempo constante y busca con un ciclo `while`.
- `TablaHash` reutiliza la lista en cada casilla, usa `guia % m` y no usa `dict`, `set` ni `hash()`.
- `pruebas.py` cubre búsquedas exitosas e infructuosas, la colisión forzada con m = 7, `factor_carga() == 3 / 7` y 25 colecciones aleatorias. Todas las pruebas pasan.
- Todas las funciones tienen *docstrings* con `Args` y `Returns`, *type hints* y las líneas en blanco requeridas.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados con unidades y leyenda; la primera cubre seis valores de n con las dos curvas en los mismos ejes y la segunda seis valores de α.
- Calcula factores de crecimiento reales (×4,95 y ×3,49 para la lista, ×0,91 para la tabla) y los contrasta con Θ(n) y Θ(1). Los valores del informe coinciden con los de las gráficas publicadas.
- Interpreta el efecto de α como una base fija más un costo por nodo, coherente con Θ(1 + α).

**Lo que puede mejorar (y cómo corregirlo):**
- Al pasar de n × 4 la lista se multiplica por 3,49, y usted lo da por coincidente con Θ(n) sin comentar la diferencia con el 4 esperado.
  → *Cómo corregirlo:* compare el factor medido con el factor teórico y diga si la diferencia es ruido o efecto de la memoria.
- La explicación del aumento de la tabla entre n = 100 y n = 1.000 ("pesa más en caché") es una hipótesis sin respaldo en sus datos.
  → *Cómo corregirlo:* preséntela como posible causa, o apóyela con una medición.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- El laboratorio está en `laboratorios/lab3-estructuras-datos/`, ubicación válida, con todos los archivos pedidos y las dos gráficas incrustadas con ruta relativa que funciona.
- Incluye su nombre, instrucciones para reproducir, enlaces al código en cada parte y cuatro commits descriptivos.
- Nota: en el repositorio hay archivos `__pycache__` (del laboratorio 1) publicados por error. Se recomienda agregarlos a `.gitignore`; no descuenta puntos.

## ¿El código funciona?
Sí. Las pruebas corren y pasan sin errores, las estructuras responden igual ante los mismos datos y el script de medición está completo y cronometra solo las búsquedas.
