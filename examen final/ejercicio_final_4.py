"""Reglas:
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con m minutos y S segundos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**kwards) para usar más de 6 valores en la función (value_7 = 10,
value_8 = 22, value_9=45) y visualizar los resultados usando el decorador
implementado con un mínimo tres ejemplos."""




from datetime import datetime

def mostrar_hora(funcion):
    def nueva_funcion(**kwargs):
        ahora = datetime.now()
        print(f"\n El decorador está siendo ejecutado a las {ahora.hour} horas, {ahora.minute} minutos y {ahora.second} segundos.")


        suma = 0
        for clave in kwargs:
            suma = suma + kwargs[clave]
        print(" La suma de todos los valores es:", suma)


        resultado = funcion(**kwargs)
        return resultado
    return nueva_funcion



@mostrar_hora
def mostrar_mayor(**kwargs):
    print("Valores recibidos:", kwargs)
    valores = list(kwargs.values())
    mayor = max(valores)
    print("El mayor valor es:", mayor)


#1
mostrar_mayor(a=10, b=25, c=5, d=12, e=7, f=19)

#2
mostrar_mayor(valor1=3, valor2=99, valor3=1, valor4=45)

#3
mostrar_mayor(value_1=11, value_2=20, value_3=30, value_4=40, value_5=15, value_6=60, value_7=10, value_8=22, value_9=45)
