def procesar_notas(estudiantes):
    """
    - Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
      un diccionario donde las claves serán los nombres de los estudiantes y sus
      valores serán listas con 3 notas.
    - Calcular el promedio de cada estudiante.
    - Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
    - promedio: que será el promedio de notas
      estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor
    - Mostrar en pantalla el estudiante con mayor promedio
    """
    resultado = {}
    mayor_promedio = -1
    mejor_estudiante = ""

    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        estado = "aprobado" if promedio >= 11 else "desaprobado"

        resultado[nombre] = {
            "promedio": promedio,
            "estado": estado
        }

        if promedio > mayor_promedio:
            mayor_promedio = promedio
            mejor_estudiante = nombre

    print(f"El estudiante con mayor promedio es {mejor_estudiante} con {mayor_promedio:.2f}")
    return resultado


# ejm profe
estudiantes = {
    "Ana": [12, 15, 14],
    "Luis": [8, 10, 9],
    "María": [18, 17, 19]
}

resultado = procesar_notas(estudiantes)
print(resultado)

