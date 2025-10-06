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

import mimodulo

print("=== CASO 1 ===")
lista1 = mimodulo.crear_lista_aleatoria(5)
if lista1:
    no_repetidos1 = mimodulo.obtener_no_repetidos(lista1)
    mimodulo.ordenar_listas(no_repetidos1)
    mimodulo.mayor_par(no_repetidos1)

print("\n=== CASO 2 ===")
lista2 = mimodulo.crear_lista_aleatoria(8)
if lista2:
    no_repetidos2 = mimodulo.obtener_no_repetidos(lista2)
    mimodulo.ordenar_listas(no_repetidos2)
    mimodulo.mayor_par(no_repetidos2)

