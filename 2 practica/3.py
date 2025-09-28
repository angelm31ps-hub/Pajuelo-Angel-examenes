def convertir_precio(texto: str) -> float:
    """
    Crea un programa en Python que implemente una función llamada convertir_precio(texto: str) -> float que:
    - Reciba un string que representa un precio en soles (ejemplo: "123.50","45", "20.99").
    - Intente convertirlo a un número decimal (float).
      Tenga las siguientes excepciones:
    - Si el texto está vacío, debe lanzar un ValueError("El precio no puede estar vacío").
    - Si el texto contiene caracteres inválidos (ejemplo: "abc", "12a3"), debe lanzar un ValueError("Formato de precio inválido").
    - Si el número es negativo, debe lanzar un ValueError("El precio no puede ser negativo").
    """
    if not texto.strip():
        raise ValueError("El precio no puede estar vacío")

    try:
        valor = float(texto)
    except ValueError:
        raise ValueError("Formato de precio inválido")

    if valor < 0:
        raise ValueError("El precio no puede ser negativo")

    return valor


# ejemplo con los valores que dio profe
entradas = ["100.69", "-45", "abc"]
precios = []

for i, texto in enumerate(entradas, start=1):
    try:
        precio = convertir_precio(texto)
        precios.append(precio)
    except ValueError as e:
        print(f"Error: {e}")

if precios:
    promedio = sum(precios) / len(precios)
    print("Precios válidos ingresados:", precios)
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron precios válidos.")
