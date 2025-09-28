def normalizar_nombres(nombres):
    """
    Usando el concepto de funciones:
    - Crear una función normalizar_nombres(nombres)
    - El parámetro recibe una lista de string de nombres (6 como mínimo)
    - Este quitará el espacio antes y después si lo hubiera
    - Convierte en tipo título
    - Si hubiera más nombre los debe separar (si debe haber el caso en el input de datos)
    - Devuelve también eliminando duplicados manteniendo el orden de la primera
    - No mutará la lista original
    """
    resultado = []
    vistos = set()

    for item in nombres:
        # Quitar espacios extremos y dividir si hay varios nombres en uno
        partes = item.strip().split()

        for nombre in partes:
            normalizado = nombre.title()  # Convierte a tipo título
            if normalizado not in vistos:
                resultado.append(normalizado)
                vistos.add(normalizado)

    return resultado


# ejmp profe
nombres = [
    "  angel  ",
    "angel gabriel",
    "ana ",
    "PEDRO",
    "maria",
    "juan"
]

resultado = normalizar_nombres(nombres)
print("Lista original:", nombres)
print("Lista normalizada:", resultado)

