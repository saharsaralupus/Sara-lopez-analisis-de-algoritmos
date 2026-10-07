# Laboratorio evaluativo 02 - Dividir y vencer

**Autora:** Sara López Cardona

## Cómo reproducir

Desde la raíz del repositorio (PowerShell):

```powershell
venv\Scripts\Activate.ps1
cd laboratorios\lab2-divide-y-vencer
python pruebas.py     # pruebas con assert
python medicion.py    # mediciones y graficas/tiempo_vs_n.png
```

## Parte 1 - Implementar y verificar

Código: [subarreglo.py](subarreglo.py) y [pruebas.py](pruebas.py).

`pruebas.py` usa `assert` y cubre la serie de ocho días (suma 17, tramo días 2 a 7), un solo elemento, todos negativos (gana el menos negativo), todos positivos (gana toda la serie), un caso donde el mejor tramo cruza el punto medio (`[-10,-10,6,7,8,9,-10,-10]`, suma 30), comprobación de que la lista no se modifica y 50 listas aleatorias (semilla fija) donde ambas funciones dan la misma suma, comparando sumas y no índices. Además verifica que la suma del tramo devuelto coincide con la suma reportada.
