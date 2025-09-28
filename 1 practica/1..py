"""
Datos
"""
nombre = "Angel Pajuelo"
salario = 21000
edad = "17"
compañia = "Mecatronic"

"""
Identificar Variables
"""
print("Tipo de variable para 'nombre' es {}".format(type(nombre)))
print("Tipo de variable para 'salario' es {}".format(type(salario)))
print("Tipo de variable para 'edad' es {}".format(type(edad)))
print("Tipo de variable para 'compañia' es {}".format(type(compañia)))

"""
Identificar si la edad es mayor a 30 y lo voy a convertir profe antes de hacerlo
"""
edad_entero = int(edad)

if edad_entero > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    porcentaje_bono = 0.10

else:
    print("Usted tiene un bono de 5% en el mes de diciembre")
    porcentaje_bono = 0.05

"""
Bono final
"""

bono_final = (salario ** 2) + (salario * porcentaje_bono)

print("El bono final de", nombre, "es:", bono_final)