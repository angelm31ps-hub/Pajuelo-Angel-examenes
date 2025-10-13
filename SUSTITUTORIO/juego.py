import random
import datetime




def decorador_mensaje(funcion):
    def envoltura(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        # Contar cuántos parámetros usa la función decorada
        cantidad_parametros = funcion.__code__.co_argcount
        print("La función decorada tiene", cantidad_parametros, "parámetro(s).")
        return resultado

    return envoltura


#obtener numero aleatorio
def obtener_numero_aleatorio():
    numero = random.randint(1, 31)
    return numero


#pedir numero
def pedir_numero():
    while True:
        try:
            valor = int(input("Adivina el día (1 al 31): "))
            if valor < 1 or valor > 31:
                print("Debe estar entre 1 y 31.")
            else:
                return valor
        except ValueError:
            print("Debe ingresar un número entero válido.")


#par ael mes y año
def pedir_mes_y_anio():
    mes = input("Ingresa tu mes de nacimiento (ejemplo: marzo): ")
    anio = input("Ingresa tu año de nacimiento: ")
    return mes, anio


#mostrar el cumple
def mostrar_cumpleanios(dia, mes, anio):
    print(f"\n🎉 Tu cumpleaños completo es: {dia} de {mes} del año {anio}")


#funcion principal
@decorador_mensaje
def adivinaFecha():
    numero_secreto = obtener_numero_aleatorio()

    print("¡Adivina el número del día de cumpleaños!")
    while True:
        intento = pedir_numero()

        if intento < numero_secreto:
            print("El número secreto es MAYOR.")
        elif intento > numero_secreto:
            print("El número secreto es MENOR.")
        else:
            print("\n🎉 ¡Ganaste! 🎉")
            ahora = datetime.datetime.now()
            print("Adivinaste el número el día", ahora.day, "del mes", ahora.month,
                  "a las", ahora.hour, "horas y", ahora.minute, "minutos.")

            # Luego de ganar, pedir mes y año
            mes, anio = pedir_mes_y_anio()
            mostrar_cumpleanios(numero_secreto, mes, anio)
            break
