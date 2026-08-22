"""Clasificador de años bisiestos.
 
Complete las funciones siguiendo la especificación de cada docstring.
"""
  
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
 
def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    while True:
        lista = input("Ingrese una lista de años separados por comas: ")
        try: 
            anios = [int(anio.strip()) for anio in lista.split(",")]
            if any(anio < 0 for anio in anios):
                print("Por favor, ingrese solo números enteros positivos.")
                continue
            return anios
        except ValueError:
            print("Entrada inválida. Por favor, ingrese solo números enteros separados por comas.")
 

#BONUS

def agrupar_por_decada(anios: list[int]) -> dict[int, list[int]]:
    """Agrupa los años por década.
 
    Args:
        anios: Lista de años como enteros.
 
    Returns:
        Diccionario donde las claves son las décadas (por ejemplo, 1990, 2000)
        y los valores son listas de años que pertenecen a esa década.
    """
    decadas = sorted({anio // 10 * 10 for anio in anios})
    return {decada: [anio for anio in anios if anio // 10 * 10 == decada]
             for decada in decadas
    }


def main() -> None:
    """Punto de entrada del script."""
    anios = leer_anios()
    bisiestos = [anio for anio in anios if es_bisiesto(anio)]
    anios_por_decada = agrupar_por_decada(anios)
    print(f"Años ingresados: {anios}")
    print(f"Años bisiestos: {bisiestos}")
    print(f"Cantidad de años bisiestos: {len(bisiestos)} de {len(anios)}.")
    print(f"Años agrupados por década: {anios_por_decada}")
 
 
if __name__ == "__main__":
    main()