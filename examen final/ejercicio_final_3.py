"""Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente al usuario.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada exitosamente.
- La función que vas a crear va a capturar, la edad, nombre de un alumno, la
hora y el minuto en que fue registrado (usar la librería correspondiente de
tiempo)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante."""


from datetime import datetime


def conteo(funcion):
    def nueva_funcion(*args):
        cantidad = len(args)
        print("Cantidad de parámetros recibidos:", cantidad)

        if cantidad <= 1:
            print("Se necesitan más de 1 parámetro para ejecutar la función.")
            return  # No ejecuta la función decorada

        resultado = funcion(*args)
        print("La función fue ejecutada exitosamente.")
        return resultado
    return nueva_funcion



@conteo
def registrar_alumno(nombre, edad, hora, minuto, n1, n2, n3, n4):
    promedio = (n1 + n2 + n3 + n4) / 4
    print(f"{nombre} de {edad} años ha sido registrado a las {hora} horas con {minuto} minutos.")
    print("Promedio:", promedio)


#correcto
ahora = datetime.now()
registrar_alumno("Pedro", 30, ahora.hour, ahora.minute, 15, 18, 12, 20)

#incorrecto
registrar_alumno("Solo uno")
