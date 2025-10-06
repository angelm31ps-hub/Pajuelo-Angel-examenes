"""- Crear una función que le permitirá almacenar X números aleatorios en
una lista y finalmente los imprimirá por consola al llamar la función. X
solo puede ser entero. No otro tipo de dato. Y también un índice
existente en la lista (usar para esto excepciones)
- Crear una función que le permita almacenar los números no repetidos de
la lista anterior, la función retornará este valor para que pueda ser
impreso por consola.
- Crear una función donde se creará una lista para ordenar de mayor a
menor la lista que se creó en el ítem anterior (número no repetidos) y
otra lista para ordenarlas de menor a mayor, retornar este valor e
imprimirlos por consola.
- Crear una función para indicar cuál es el mayor número par de la lista
(lista de la regla 2), retornar este valor e imprimirlo por consola.
- Crear el archivo main.py, donde solo llamarás las anteriores funciones que
se encontrarán alojadas en un módulo (probarlo para dos casos mínimo)"""

import random

def crear_lista_aleatoria(x):

    try:

        if type(x) != int:
            raise ValueError("X debe ser un número entero")


        lista = []
        for i in range(x):
            numero = random.randint(1, 50)
            lista.append(numero)

        print("Lista creada:", lista)


        indice = int(input("Ingrese un índice para ver su valor: "))
        print("Valor en el índice", indice, "es:", lista[indice])

        return lista

    except ValueError as e:
        print("Error:", e)
    except IndexError:
        print("Error: índice fuera de rango")
    except Exception as e:
        print("Error inesperado:", e)


def obtener_no_repetidos(lista):
    """Devuelve una nueva lista con los números no repetidos"""
    nueva_lista = []
    for n in lista:
        if n not in nueva_lista:
            nueva_lista.append(n)
    print("Lista sin repetidos:", nueva_lista)
    return nueva_lista


def ordenar_listas(lista):
    """Ordena una lista de mayor a menor y de menor a mayor"""
    lista_mayor_a_menor = sorted(lista, reverse=True)
    lista_menor_a_mayor = sorted(lista)
    print("De mayor a menor:", lista_mayor_a_menor)
    print("De menor a mayor:", lista_menor_a_mayor)
    return lista_mayor_a_menor, lista_menor_a_mayor


def mayor_par(lista):
    """Encuentra el mayor número par en la lista"""
    pares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)

    if len(pares) == 0:
        print("No hay números pares")
        return None
    else:
        mayor = max(pares)
        print("El mayor número par es:", mayor)
        return mayor
