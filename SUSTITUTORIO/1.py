import time

#medir el tiempo
def medir_tiempo(funcion):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print("La función tardó", round(fin - inicio, 3), "segundos en ejecutarse.\n")
        return resultado
    return envoltura

#persona
class Persona:
    def __init__(self, nombre, edad, ciudad):

        if type(nombre) != str:
            print("Error: el nombre debe ser texto (string).")
            self.__nombre = "Desconocido"
        else:
            self.__nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    @medir_tiempo
    def imprimir_datos(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.edad)
        print("Ciudad:", self.ciudad)


    def obtener_nombre(self):
        return self.__nombre


#empleado
class Empleado(Persona):
    def __init__(self, nombre, edad, ciudad):
        super().__init__(nombre, edad, ciudad)
        self.sueldo = 0
        self.impuesto_pagar = 0

    @medir_tiempo
    def sueldo_empleado(self):
        try:
            self.sueldo = float(input("Ingrese el sueldo del empleado: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            self.sueldo = 0

    @medir_tiempo
    def impuesto(self):
        if self.sueldo > 5500:
            self.impuesto_pagar = self.sueldo * 0.09
            print("Debe pagar impuesto de:", self.impuesto_pagar)
        else:
            self.impuesto_pagar = 0
            print("No debe pagar impuestos.")

    @medir_tiempo
    def manejoDiccionario(self):
        try:
            diccionario = {
                "nombre": self.obtener_nombre(),
                "edad": self.edad,
                "sueldo": self.sueldo,
                "impuesto": self.impuesto_pagar
            }
            print("\nDiccionario creado con éxito:")
            print(diccionario)
        except Exception as e:
            print("Error al crear diccionario:", e)
        return diccionario


#buscar al empleado en el archivo
def buscar_empleado(nombre_buscar):
    try:
        archivo = open("empleados.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

        for linea in lineas:
            partes = linea.strip().split(",")
            if partes[0] == nombre_buscar:
                print(f"El empleado {partes[0]} tiene una remuneración de {partes[2]} y un impuesto de {partes[3]}")
                return
        print("Empleado no encontrado.")
    except FileNotFoundError:
        print("No se encontró el archivo de empleados.")


#programa principal
def main():
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    ciudad = input("Ingrese la ciudad: ")

    emp = Empleado(nombre, edad, ciudad)
    emp.imprimir_datos()
    emp.sueldo_empleado()
    emp.impuesto()
    datos = emp.manejoDiccionario()

    # Guardar en archivo
    with open("empleados.txt", "a") as f:
        f.write(f"{datos['nombre']},{datos['edad']},{datos['sueldo']},{datos['impuesto']}\n")

    buscar = input("\nIngrese el nombre del empleado a buscar: ")
    buscar_empleado(buscar)

#ejecutar:
main()
