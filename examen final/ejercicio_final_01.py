""" Clase base Persona
o Atributos: nombre, edad, nacionalidad="peruana", saldo=0.0.
o Métodos para esta clase:
▪ actualizar_nombre(nombre) y actualizar_edad(edad)
(validar edad > 0).
▪ cumplir_anios() (incrementa edad en 1).
▪ mostrar_saldo() (imprime el saldo actual).
▪ transferir(destino, monto) (si no hay fondos
suficientes, imprimir “Saldo insuficiente”; si hay,
basarse en self y acreditar a destino).
• Crear la clase que hereda: Empleado(Persona)
o Atributo adicional: sueldo (float).
o Métodos para esta clase:
▪ aumento_sueldo(porcentaje=0.30) (incrementa el
sueldo en 30% por defecto).
▪ prediccion(anio_objetivo, edad_param=None)
▪ Retorna el mensaje: “En el año XXXX tendrá
XX años”.
▪ Si edad_param se pasa y es menor que
self.edad, imprimir “No es posible realizar la
operación” y no calcular.

• Pruebas mínimas
o Instanciar al menos dos Empleado.
o Aplicar aumento_sueldo 2 veces y mostrar el sueldo
incrementado.
o Realizar una transferencia entre ambos empleados y mostrar
saldos antes y después de ambos

o Probar un caso de saldo insuficiente.
o Usar prediccion(...) con y sin edad_param inválido."""


# Clase base Persona
class Persona:
    def __init__(self, nombre, edad, nacionalidad="peruana", saldo=0.0):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.saldo = saldo

    def actualizar_nombre(self, nuevo_nombre):

        self.nombre = nuevo_nombre

    def actualizar_edad(self, nueva_edad):

        if nueva_edad > 0:
            self.edad = nueva_edad
        else:
            print("La edad debe ser mayor a 0")

    def cumplir_anios(self):

        self.edad = self.edad + 1

    def mostrar_saldo(self):

        print("Saldo actual de", self.nombre, "es:", self.saldo)

    def transferir(self, destino, monto):

        if monto <= 0:
            print("El monto debe ser mayor a 0")
        elif self.saldo < monto:
            print("Saldo insuficiente")
        else:
            self.saldo = self.saldo - monto
            destino.saldo = destino.saldo + monto
            print("Transferencia realizada con éxito de", self.nombre, "a", destino.nombre)




# Clase Empleado que hereda de Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo, nacionalidad="peruana", saldo=0.0):

        Persona.__init__(self, nombre, edad, nacionalidad, saldo)
        self.sueldo = sueldo

    def aumento_sueldo(self, porcentaje=0.30):

        aumento = self.sueldo * porcentaje
        self.sueldo = self.sueldo + aumento

    def prediccion(self, anio_objetivo, edad_param=None):

        anio_actual = 2025

        if edad_param is not None:
            if edad_param < self.edad:
                print("No es posible realizar la operación")
                return
            else:
                edad_base = edad_param
        else:
            edad_base = self.edad

        diferencia = anio_objetivo - anio_actual
        edad_futura = edad_base + diferencia

        print("En el año", anio_objetivo, "tendrá", edad_futura, "años")




#pruebas

#empleados
empleado1 = Empleado("Ana", 25, 1500, saldo=500)
empleado2 = Empleado("Luis", 30, 2000, saldo=300)

#sueldo incial
print("Sueldo inicial de", empleado1.nombre, ":", empleado1.sueldo)
print("Sueldo inicial de", empleado2.nombre, ":", empleado2.sueldo)

#aumento
empleado1.aumento_sueldo()
empleado1.aumento_sueldo()
print("Sueldo después de aumentos de", empleado1.nombre, ":", empleado1.sueldo)

#antes de transferir
print("\nSaldos antes de transferencia:")
empleado1.mostrar_saldo()
empleado2.mostrar_saldo()

#transferencia
empleado1.transferir(empleado2, 200)

#después de transferir
print("\nSaldos después de transferencia:")
empleado1.mostrar_saldo()
empleado2.mostrar_saldo()

#saldo insuficiente
empleado2.transferir(empleado1, 1000)

#predicción válida
print("\nPredicciones:")
empleado1.prediccion(2030)

#predicciín inválida
empleado1.prediccion(2030, edad_param=20)
