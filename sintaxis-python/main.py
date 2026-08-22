#n = 1000
#print(type(n))
#tiempo = 0.0034
#print(type(tiempo))
#algoritmo = "algoritmo de ordenamiento"
#print(type(algoritmo))
#ordenado = True 
#print(type(ordenado))
#resultado = None
#print(type(resultado))

'''
if tiempo < 0.001:
    categoria = "rapido"
elif tiempo < 0.001:
    categoria = "moderado"
else: 
    categoria = "lento"

print(categoria)
'''

#Ciclo for

'''
for tamano in range(2, 10, 2):
    print(tamano)
    '''

#Ciclo while

"""
intentos = 0 

while intentos < 3:
    print("Intento", intentos + 1)
    intentos += 1
""" 


#Funciones 
"""
def contar_comparaciones(lista):
    comparaciones = 0
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            comparaciones += 1
    return comparaciones
"""

#Estructuras de datos 

##Listas
"""numeros = [5, 2, 9, 1, 7]
print( numeros[2])
"""
##Tuplas 
"""punto = (1000, 0.34, True)
print(punto[-1])
"""
##Diccionarios 
"""tiempo = {"algoritmo1": 0.0034, "algoritmo2": 0.0056, 1000: 0.0002}
print(tiempo.get("algoritmo1"))
"""
##Conjunto (No admite valores repetidos)
"""conjunto = {1,2,3}
"""

#Para construir una lista de cuadrados

#For clasico
"""tamanios = [100,1000, 10000]"""
"""cuadrados = []
for i in tamanios: 
    cuadrados.append(i**2)
"""
"""cuadrados = [i**2 for i in tamanios] #Primero como se va a procesar los datos y luego el for. 
print(cuadrados)
"""

#Manejo de excepciones 

"""
try: 
    print(1000/2)
    a = 2 
    a.sort()
except ZeroDivisionError : 
    print("No se puede dividir por cero")
except AttributeError:
    print("El método sort solo se puede aplicar en listas")
except:
    print("Ocurrió un error en el programa")

print("El programa se sigue ejecutando")
"""


