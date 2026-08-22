#Antes 

"""
def CalcularPromedio(Lista):
    s=0
    for x in Lista:
     s=s+x
    return s/len(Lista)
 
l=[1,2,3,4,5]
print(CalcularPromedio(l))"""


#Después

def calcular_promedio(numeros: list[float]) -> float:
    """
    Calcula el promedio de una lista de números.

    Args:
        numeros (List[float]): Lista de números.

    Returns:
        float: Promedio de los números.
    """
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    
    suma_total = sum(numeros)
    promedio = suma_total / len(numeros)
    return promedio

def main() -> None:
    """Punto de entrada del script."""
    lista_numeros = [1.0, 2.0, 3.0, 4.0, 5.0]
    promedio = calcular_promedio(lista_numeros)
    print(f"El promedio de {lista_numeros} es: {promedio}")

if __name__ == "__main__":
    main()